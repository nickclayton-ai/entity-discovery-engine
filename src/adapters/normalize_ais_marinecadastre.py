from pathlib import Path
import pandas as pd

from src.schema import VESSEL_SCHEMA


COLUMN_CANDIDATES = {
    "mmsi": ["MMSI", "mmsi"],
    "imo": ["IMO", "imo"],
    "timestamp_utc": ["BaseDateTime", "basedatetime", "timestamp", "Timestamp"],
    "lat": ["LAT", "lat", "Latitude", "latitude"],
    "lon": ["LON", "lon", "Longitude", "longitude"],
    "sog_knots": ["SOG", "sog", "SpeedOverGround"],
    "cog_deg": ["COG", "cog", "CourseOverGround"],
}


REQUIRED_CANONICAL_COLUMNS = [
    "mmsi",
    "timestamp_utc",
    "lat",
    "lon",
    "sog_knots",
]


def find_source_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    for col in candidates:
        if col in df.columns:
            return col
    return None


def normalize_ais_marinecadastre(input_path: str, output_path: str) -> pd.DataFrame:
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
            f"Missing required columns after mapping: {missing_required}. "
            f"Available source columns: {list(df.columns)}"
        )

    if "imo" not in work.columns:
        work["imo"] = pd.NA

    if "cog_deg" not in work.columns:
        work["cog_deg"] = pd.NA

    work["timestamp_utc"] = pd.to_datetime(
        work["timestamp_utc"], utc=True, errors="coerce"
    )
    work["lat"] = pd.to_numeric(work["lat"], errors="coerce")
    work["lon"] = pd.to_numeric(work["lon"], errors="coerce")
    work["sog_knots"] = pd.to_numeric(work["sog_knots"], errors="coerce")
    work["cog_deg"] = pd.to_numeric(work["cog_deg"], errors="coerce")
    work["mmsi"] = work["mmsi"].astype("string")
    work["imo"] = work["imo"].astype("string")

    work["source"] = "marinecadastre_ais"
    work["vessel_id"] = work["mmsi"]

    work = work.dropna(
        subset=["mmsi", "timestamp_utc", "lat", "lon", "sog_knots"]
    ).copy()

    work = work[
        (work["lat"] >= -90) & (work["lat"] <= 90) &
        (work["lon"] >= -180) & (work["lon"] <= 180)
    ].copy()

    work = work.sort_values(["mmsi", "timestamp_utc"]).reset_index(drop=True)

    for col in VESSEL_SCHEMA:
        if col not in work.columns:
            work[col] = pd.NA

    work = work[VESSEL_SCHEMA]

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    work.to_csv(output_file, index=False)

    return work


if __name__ == "__main__":
    input_path = "data/raw/marinecadastre_ais_sample.csv"
    output_path = "data/staging/normalized_ais_marinecadastre.csv"

    normalized_df = normalize_ais_marinecadastre(input_path, output_path)
    print(f"Normalized {len(normalized_df)} AIS rows")
    print(f"Saved normalized AIS to {output_path}")
    print(normalized_df.head().to_string(index=False))