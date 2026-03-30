import pandas as pd


REQUIRED_COLUMNS = ["timestamp", "lat", "lon", "sog"]


def load_ais_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df = df.rename(
        columns={
            "timestamp": "timestamp_utc",
            "sog": "sog_knots",
            "cog": "cog_deg",
        }
    )

    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
    df["sog_knots"] = pd.to_numeric(df["sog_knots"], errors="coerce")

    df["source"] = "synthetic_ais"
    df["vessel_id"] = df.get("mmsi", "unknown")

    df = df.dropna(subset=["timestamp_utc", "lat", "lon", "sog_knots"])
    df = df.sort_values("timestamp_utc").reset_index(drop=True)

    return df