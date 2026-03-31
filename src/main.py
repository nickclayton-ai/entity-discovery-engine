from src.plot_track import plot_vessel_track
from src.run_case import run_case


def main() -> None:
    ais_path = "data/staging/normalized_ais_marinecadastre.csv"
    float_path = "data/staging/normalized_argo_float.csv"
    target_vessel_id = "123456789"

    result = run_case(
        vessel_id=target_vessel_id,
        ais_path=ais_path,
        float_path=float_path,
    )

    print(f"Selected vessel {result['vessel_id']}")
    print(f"Loaded {result['ais_point_count']} AIS points for selected vessel")

    events = result["events"]
    links = result["links"]
    vessel_track = result["vessel_track"]

    if events.empty:
        print("No candidate low-speed events found.")
    else:
        print("\nCandidate events:")
        print(events.to_string(index=False))

        events_output_path = "data/processed/candidate_events.csv"
        events.to_csv(events_output_path, index=False)
        print(f"\nSaved events to {events_output_path}")

    plot_vessel_track(vessel_track, events)

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