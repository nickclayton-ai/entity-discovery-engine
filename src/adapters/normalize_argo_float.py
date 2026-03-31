from pathlib import Path
import pandas as pd

from src.schema import FLOAT_SCHEMA


COLUMN_CANDIDATES = {
    "float_id": ["float_id", "FLOAT_ID", "platform_number", "PLATFORM_NUMBER", "id", "ID"],
    "timestamp_utc": ["first_timestamp", "FIRST_TIMESTAMP", "timestamp", "TIMESTAMP", "date", "DATE"],
    "lat": ["lat", "LAT", "latitude", "LATITUDE"],
    "lon": ["lon", "LON", "longitude", "LONGITUDE"],
}


REQUIRED_CANONICAL_COLUMNS = [
    "float_id",
    "timestamp_utc",
    "lat",
    "lon",
]


def find_source_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    for col in candidates:
        if col in df.columns:
            return col
    return None


def normalize_argo_float(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    canonical_map = {}

    for canonical_name, candidates in COLUMN_CANDIDATES.items():
        source_col = find_source_column(df, candidates)
        if source_col is not None:
            canonical_map[source_col] = canonical_name

    work = df.rename(columns=canonical_map).copy()

    missing_required = [
        col for col in REQUIRED_CANONICAL_COLUMNS if col not in work.columns
    ]
    if missing_required:
        raise ValueError(
            f"Missing required float columns after mapping: {missing_required}. "
            f"Available source columns: {list(df.columns)}"
        )

    work["timestamp_utc"] = pd.to_datetime(
        work["timestamp_utc"], utc=True, errors="coerce"
    )
    work["lat"] = pd.to_numeric(work["lat"], errors="coerce")
    work["lon"] = pd.to_numeric(work["lon"], errors="coerce")
    work["float_id"] = work["float_id"].astype("string")

    work["source"] = "argo_float"

    work = work.dropna(
        subset=["float_id", "timestamp_utc", "lat", "lon"]
    ).copy()

    work = work[
        (work["lat"] >= -90) & (work["lat"] <= 90) &
        (work["lon"] >= -180) & (work["lon"] <= 180)
    ].copy()

    work = work.sort_values(["float_id", "timestamp_utc"]).reset_index(drop=True)

    for col in FLOAT_SCHEMA:
        if col not in work.columns:
            work[col] = pd.NA

    work = work[FLOAT_SCHEMA]

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    work.to_csv(output_file, index=False)

    return work


if __name__ == "__main__":
    input_path = "data/raw/argo_float_raw_sample.csv"
    output_path = "data/staging/normalized_argo_float.csv"

    normalized_df = normalize_argo_float(input_path, output_path)
    print(f"Normalized {len(normalized_df)} float rows")
    print(f"Saved normalized float data to {output_path}")
    print(normalized_df.head().to_string(index=False))