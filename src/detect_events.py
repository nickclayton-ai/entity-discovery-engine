import pandas as pd


def detect_low_speed_events(
    df: pd.DataFrame,
    low_speed_knots: float,
    min_event_duration_minutes: int,
    max_gap_minutes: int,
) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    work = df.copy()
    work["is_low_speed"] = work["sog_knots"] < low_speed_knots
    work["time_diff_min"] = work["timestamp_utc"].diff().dt.total_seconds().div(60)

    event_rows = []
    current_event_points = []

    for _, row in work.iterrows():
        if row["is_low_speed"]:
            if not current_event_points:
                current_event_points = [row]
            else:
                prev_time = current_event_points[-1]["timestamp_utc"]
                gap_min = (row["timestamp_utc"] - prev_time).total_seconds() / 60

                if gap_min <= max_gap_minutes:
                    current_event_points.append(row)
                else:
                    event_rows.append(current_event_points)
                    current_event_points = [row]
        else:
            if current_event_points:
                event_rows.append(current_event_points)
                current_event_points = []

    if current_event_points:
        event_rows.append(current_event_points)

    summaries = []

    for points in event_rows:
        event_df = pd.DataFrame(points)
        start_time = event_df["timestamp_utc"].min()
        end_time = event_df["timestamp_utc"].max()
        duration_min = (end_time - start_time).total_seconds() / 60

        if duration_min >= min_event_duration_minutes:
            summaries.append(
                {
                    "start_time": start_time,
                    "end_time": end_time,
                    "duration_min": round(duration_min, 2),
                    "mean_speed_knots": round(event_df["sog_knots"].mean(), 2),
                    "min_speed_knots": round(event_df["sog_knots"].min(), 2),
                    "max_speed_knots": round(event_df["sog_knots"].max(), 2),
                    "centroid_lat": round(event_df["lat"].mean(), 6),
                    "centroid_lon": round(event_df["lon"].mean(), 6),
                    "point_count": len(event_df),
                }
            )

    return pd.DataFrame(summaries)