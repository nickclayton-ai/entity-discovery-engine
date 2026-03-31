from src.ingest_ais import load_ais_csv
from src.detect_events import detect_low_speed_events
from src.plot_track import plot_vessel_track
from src.ingest_floats import load_float_csv
from src.link_events_to_floats import link_events_to_floats
from src.config import (
    LOW_SPEED_KNOTS,
    MIN_EVENT_DURATION_MINUTES,
    MAX_GAP_MINUTES,
    MAX_LINK_DISTANCE_KM,
    MAX_LINK_TIME_HOURS,
)


def main() -> None:
    ais_path = "data/staging/normalized_ais_marinecadastre.csv"
    float_path = "data/staging/normalized_argo_float.csv"

    df = load_ais_csv(ais_path)
    print(f"Loaded {len(df)} AIS points")

    events = detect_low_speed_events(
        df=df,
        low_speed_knots=LOW_SPEED_KNOTS,
        min_event_duration_minutes=MIN_EVENT_DURATION_MINUTES,
        max_gap_minutes=MAX_GAP_MINUTES,
    )

    if events.empty:
        print("No candidate low-speed events found.")
    else:
        print("\nCandidate events:")
        print(events.to_string(index=False))

        events_output_path = "data/processed/candidate_events.csv"
        events.to_csv(events_output_path, index=False)
        print(f"\nSaved events to {events_output_path}")

    plot_vessel_track(df, events)

    floats_df = load_float_csv(float_path)
    print(f"\nLoaded {len(floats_df)} float records")

    links = link_events_to_floats(
        events,
        floats_df,
        max_distance_km=MAX_LINK_DISTANCE_KM,
        max_time_hours=MAX_LINK_TIME_HOURS,
    )

    if links.empty:
        print("\nNo event-to-float links found.")
    else:
        print("\nCandidate event-to-float links:")
        print(links.to_string(index=False))

        links_output_path = "data/processed/event_float_links.csv"
        links.to_csv(links_output_path, index=False)
        print(f"\nSaved links to {links_output_path}")


if __name__ == "__main__":
    main()