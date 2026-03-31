from src.ingest_ais import load_ais_csv
from src.ingest_floats import load_float_csv
from src.select_vessel import select_vessel
from src.detect_events import detect_low_speed_events
from src.link_events_to_floats import link_events_to_floats
from src.config import (
    LOW_SPEED_KNOTS,
    MIN_EVENT_DURATION_MINUTES,
    MAX_GAP_MINUTES,
    MAX_LINK_DISTANCE_KM,
    MAX_LINK_TIME_HOURS,
)


def run_case(
    vessel_id: str,
    ais_path: str,
    float_path: str,
) -> dict:
    df_all = load_ais_csv(ais_path)
    df_vessel = select_vessel(df_all, vessel_id)

    events = detect_low_speed_events(
        df=df_vessel,
        low_speed_knots=LOW_SPEED_KNOTS,
        min_event_duration_minutes=MIN_EVENT_DURATION_MINUTES,
        max_gap_minutes=MAX_GAP_MINUTES,
    )

    floats_df = load_float_csv(float_path)

    links = link_events_to_floats(
        events,
        floats_df,
        max_distance_km=MAX_LINK_DISTANCE_KM,
        max_time_hours=MAX_LINK_TIME_HOURS,
    )

    return {
        "vessel_id": str(vessel_id),
        "ais_point_count": len(df_vessel),
        "event_count": len(events),
        "link_count": len(links),
        "events": events,
        "links": links,
        "vessel_track": df_vessel,
    }