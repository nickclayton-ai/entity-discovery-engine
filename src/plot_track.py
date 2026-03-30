import matplotlib.pyplot as plt
import pandas as pd
from config import LOW_SPEED_KNOTS


def plot_vessel_track(df: pd.DataFrame, events: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))

    # Full track
    plt.plot(df["lon"], df["lat"], marker="o", linewidth=1, label="Vessel Track")

    # Low-speed points
    low_speed_df = df[df["sog_knots"] < LOW_SPEED_KNOTS]
    if not low_speed_df.empty:
        plt.scatter(
            low_speed_df["lon"],
            low_speed_df["lat"],
            s=80,
            marker="x",
            label="Low-Speed Points",
        )

    # Event centroids
    if not events.empty:
        plt.scatter(
            events["centroid_lon"],
            events["centroid_lat"],
            s=150,
            marker="D",
            label="Detected Event Centroid",
        )

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Vessel Track with Candidate Low-Speed Event")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()