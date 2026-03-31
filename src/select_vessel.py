import pandas as pd


def select_vessel(df: pd.DataFrame, vessel_id: str) -> pd.DataFrame:
    """
    Filter canonical AIS dataframe to a single vessel_id
    """
    vessel_df = df[df["vessel_id"].astype(str) == str(vessel_id)].copy()

    if vessel_df.empty:
        available_ids = sorted(df["vessel_id"].astype(str).unique().tolist())
        raise ValueError(
            f"No data found for vessel_id={vessel_id}. "
            f"Available vessel_ids: {available_ids}"
        )

    vessel_df = vessel_df.sort_values("timestamp_utc").reset_index(drop=True)

    return vessel_df