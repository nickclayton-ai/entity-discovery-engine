import pandas as pd

from src.schema import FLOAT_SCHEMA


REQUIRED_COLUMNS = [
    "source",
    "float_id",
    "timestamp_utc",
    "lat",
    "lon",
]


def load_float_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required canonical float columns: {missing}")

    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")

    df = df.dropna(subset=["float_id", "timestamp_utc", "lat", "lon"]).copy()
    df = df.sort_values(["float_id", "timestamp_utc"]).reset_index(drop=True)

    return df[FLOAT_SCHEMA]