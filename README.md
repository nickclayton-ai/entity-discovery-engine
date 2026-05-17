# 🚀 Entity Discovery Engine

### Spatiotemporal Data Fusion & Maritime Entity Correlation System

Entity Discovery Engine is a containerized Python analytics pipeline designed to identify potential relationships between vessel AIS behavior and downstream float detections through spatiotemporal correlation and explainable confidence scoring.

---

# 🧠 Problem

Maritime intelligence data is often fragmented across multiple sources, such as AIS vessel tracks, environmental sensors, and float/buoy observations. This fragmentation makes it difficult to identify relationships between entities and detect meaningful operational patterns without significant manual analysis.

This project simulates an analyst-facing data fusion workflow that automatically surfaces candidate relationships and ranks them using explainable spatial and temporal scoring.

---

# ⚙️ What This System Does

- Ingests vessel AIS track data
- Detects candidate low-speed / loitering events
- Ingests float / buoy first-observation data
- Links vessel activity to downstream entities using spatiotemporal correlation
- Ranks associations using explainable distance and time-based scoring
- Generates structured outputs for downstream analysis
- Supports reproducible deployment using Docker containers

---

# 🏗️ System Architecture

```text
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
```

---

# 📂 Project Structure

```text
entity-discovery-engine/
│
├── data/
│   ├── raw/
│   ├── staging/
│   └── processed/
│
├── src/
│   ├── adapters/
│   ├── ingest_ais.py
│   ├── ingest_floats.py
│   ├── detect_events.py
│   ├── link_events_to_floats.py
│   ├── plot_track.py
│   ├── run_case.py
│   └── main.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# 📊 Example Use Case

Identify a vessel exhibiting loitering behavior and determine whether nearby downstream observations (e.g., floats or environmental signals) are likely associated.

Supports:

- Maritime Domain Awareness (MDA)
- ISR workflows
- Pattern-of-life analysis
- Anomaly detection
- Entity resolution workflows

---

# 📈 Example Output

| vessel_id | event_time | event_lat | event_lon | float_id | distance_km | time_delta_hr | confidence |
|---|---|---|---|---|---|---|---|
| 987654321 | 2026-03-28 12:00 | 32.71 | -117.16 | F1023 | 4.2 | 1.8 | High |

(Output simplified for demonstration purposes)

---

# 🛠️ Tech Stack

## Languages & Analytics

- Python
- pandas
- numpy
- scikit-learn
- matplotlib

## Infrastructure & Tooling

- Docker
- Git
- GitHub

---

# 🔍 Pipeline Workflow

## Ingestion

- Load and normalize AIS vessel track data
- Load and normalize float first-observation data

## Detection

- Identify candidate low-speed / loitering windows

## Linkage

- Compare event centroids to candidate float observations

## Scoring

- Rank associations using normalized spatial and temporal features
- Generate explainable confidence classifications

---

# 📊 Visualization

<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/478ac1de-afa7-4daa-ab39-1a629d2aa66c" />

---

# 🎯 Why This Matters

This project demonstrates how disjointed geospatial and time-series data can be transformed into actionable intelligence through structured analytics pipelines.

The workflow mirrors challenges found in:

- Defense and intelligence environments
- Maritime domain awareness operations
- Large-scale data integration problems
- Operational decision support systems
- AI-enabled analytical workflows

---

# ▶️ Local Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python -m src.main
```

Ensure required data is placed in:

```text
/data/
```

---

# 🐳 Run with Docker

Build the container:

```bash
docker build -t entity-discovery-engine .
```

Run the pipeline:

```bash
docker run --rm -v "${PWD}/data:/app/data" entity-discovery-engine
```

Docker support enables reproducible execution across environments without requiring local Python dependency configuration.

---

# 📌 Status

### v0.1 — Working Containerized Prototype

Current capabilities include:

- AIS ingestion and normalization
- Event detection
- Float linkage
- Confidence scoring
- Dockerized execution pipeline

---

# 🔭 Next Steps

- Canonical internal schema design
- Real-world AIS and buoy ingestion
- PostGIS integration for geospatial querying
- FastAPI service layer
- Interactive frontend interface (Next.js / Streamlit)
- CI/CD automation with GitHub Actions
- Multi-source entity enrichment

---

# ⚠️ Notes

All data used is synthetic or publicly available. No sensitive or classified information is included.
