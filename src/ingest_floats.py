import pandas as pd


REQUIRED_COLUMNS = ["float_id", "first_timestamp", "lat", "lon"]


def load_float_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["first_timestamp"] = pd.to_datetime(df["first_timestamp"], utc=True, errors="coerce")
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")

    df = df.dropna(subset=["float_id", "first_timestamp", "lat", "lon"]).copy()
    df = df.sort_values("first_timestamp").reset_index(drop=True)

    # ✅ Normalize to canonical schema
    df = df.rename(
        columns={
            "first_timestamp": "timestamp_utc",
        }
    )

    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
    df["source"] = "synthetic_float"

    return df