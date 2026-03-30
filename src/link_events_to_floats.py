import math
import pandas as pd


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return r * c


def compute_score(distance_km, time_hours, max_distance_km, max_time_hours):
    distance_score = 1 - (distance_km / max_distance_km)
    time_score = 1 - (time_hours / max_time_hours)

    distance_score = max(0, min(1, distance_score))
    time_score = max(0, min(1, time_score))

    final_score = 0.6 * distance_score + 0.4 * time_score
    return round(final_score, 3)


def classify_score(score: float) -> str:
    if score >= 0.75:
        return "HIGH"
    elif score >= 0.5:
        return "MEDIUM"
    else:
        return "LOW"


def link_events_to_floats(
    events_df: pd.DataFrame,
    floats_df: pd.DataFrame,
    max_distance_km: float,
    max_time_hours: float,
) -> pd.DataFrame:
    if events_df.empty or floats_df.empty:
        return pd.DataFrame()

    matches = []

    for _, event in events_df.iterrows():
        event_end_time = pd.to_datetime(event["end_time"], utc=True)

        for _, flt in floats_df.iterrows():
            float_time = pd.to_datetime(flt["timestamp_utc"], utc=True)

            time_diff_hours = (float_time - event_end_time).total_seconds() / 3600

            if time_diff_hours < 0 or time_diff_hours > max_time_hours:
                continue

            distance_km = haversine_km(
                event["centroid_lat"],
                event["centroid_lon"],
                flt["lat"],
                flt["lon"],
            )

            if distance_km > max_distance_km:
                continue

            score = compute_score(
                distance_km,
                time_diff_hours,
                max_distance_km,
                max_time_hours,
            )

            matches.append(
                {
                    "event_start_time": event["start_time"],
                    "event_end_time": event["end_time"],
                    "float_id": flt["float_id"],
                    "distance_km": round(distance_km, 2),
                    "time_diff_hours": round(time_diff_hours, 2),
                    "score": score,
                    "confidence": classify_score(score),
                }
            )

    if not matches:
        return pd.DataFrame()

    result = pd.DataFrame(matches)
    result = result.sort_values("score", ascending=False).reset_index(drop=True)
    return result