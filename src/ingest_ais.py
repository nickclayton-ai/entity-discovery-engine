import pandas as pd


REQUIRED_COLUMNS = ["timestamp", "lat", "lon", "sog"]


def load_ais_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
    df["sog"] = pd.to_numeric(df["sog"], errors="coerce")

    df = df.dropna(subset=["timestamp", "lat", "lon", "sog"]).copy()
    df = df.sort_values("timestamp").reset_index(drop=True)

    return df