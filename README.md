🚀 Entity Discovery Engine

Spatiotemporal Data Fusion & Maritime Entity Correlation System

🧠 Problem

Maritime intelligence data is fragmented across multiple sources (AIS vessel tracks, environmental sensors, float/buoy data), making it difficult to identify relationships between entities and detect meaningful patterns without significant manual analysis.

This project simulates an analyst-facing data fusion pipeline that automatically surfaces candidate relationships and ranks them using explainable spatial and temporal scoring.

⚙️ What This System Does
Ingests vessel AIS track data
Detects candidate low-speed / loitering events (potential activity of interest)
Ingests float / buoy first-observation data
Links vessel events to downstream entities using spatiotemporal correlation
Ranks associations using explainable distance and time-based scoring
🏗️ System Architecture
AIS Vessel Data        Float / Buoy Data
        ↓                      ↓
   Data Cleaning & Normalization
                ↓
     Event Detection (Loitering)
                ↓
     Spatiotemporal Correlation
                ↓
     Scoring & Ranking Engine
                ↓
      Structured Output + Visualization
📊 Example Use Case

Identify a vessel exhibiting loitering behavior and determine whether nearby downstream observations (e.g., floats or environmental signals) are likely associated.

Supports:

Maritime Domain Awareness (MDA)
ISR workflows
Pattern-of-life analysis
Anomaly detection
📈 Example Output
vessel_id	event_time	event_lat	event_lon	float_id	distance_km	time_delta_hr	confidence
987654321	2026-03-28 12:00	32.71	-117.16	F1023	4.2	1.8	High

(Output simplified for demonstration purposes)

🛠️ Tech Stack
Python
pandas / numpy
matplotlib
🔍 Approach

Ingestion

Load and clean AIS vessel track data
Load and clean float first-observation data

Detection

Identify candidate low-speed / loitering windows

Linkage

Compare event centroids to candidate float observations

Scoring

Rank associations using normalized distance and time features
Generate explainable confidence classifications
📊 Visualization

(Insert screenshot or plot here — REQUIRED for final version)

🎯 Why This Matters

This project demonstrates how disjointed geospatial and time-series data can be transformed into actionable intelligence through structured pipelines.

This type of workflow is directly applicable to:

Defense and intelligence environments
Large-scale data integration problems
Operational decision support systems
▶️ How to Run
python -m src.main

(Ensure data is placed in /data/raw/ directory)

📌 Status

v0.1 — Working local prototype

🔭 Next Steps
Canonical internal schema design
Real-world AIS and buoy ingestion
PostGIS integration for geospatial querying
API layer (FastAPI)
Frontend interface (Next.js)
⚠️ Notes

All data used is synthetic or publicly available. No sensitive or classified information is included.
