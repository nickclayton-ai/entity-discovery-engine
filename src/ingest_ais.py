import pandas as pd

from src.schema import VESSEL_SCHEMA


REQUIRED_COLUMNS = [
    "source",
    "vessel_id",
    "mmsi",
    "imo",
    "timestamp_utc",
    "lat",
    "lon",
    "sog_knots",
    "cog_deg",
]


def load_ais_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required canonical AIS columns: {missing}")

    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
    df["sog_knots"] = pd.to_numeric(df["sog_knots"], errors="coerce")
    df["cog_deg"] = pd.to_numeric(df["cog_deg"], errors="coerce")

    df["vessel_id"] = df["vessel_id"].astype(str)
    df["mmsi"] = df["mmsi"].astype(str)
    df["imo"] = df["imo"].astype(str)

    return df[VESSEL_SCHEMA]