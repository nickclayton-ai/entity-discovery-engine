````md
# 🚀 Entity Discovery Engine

### Spatiotemporal Data Fusion & Maritime Entity Correlation System

Entity Discovery Engine is a containerized analytical pipeline designed to identify relationships between vessel behavior and downstream detections through spatiotemporal correlation, machine learning-enabled event analysis, and explainable confidence scoring.

The project simulates a scalable analyst-facing workflow for transforming fragmented maritime data into structured, actionable insight.

---

# 🧠 Problem

Maritime operational data is often fragmented across disconnected sources such as AIS vessel tracks, environmental observations, and downstream detections. This fragmentation creates significant challenges for identifying relationships between entities, detecting meaningful operational patterns, and scaling analysis beyond manual workflows.

Entity Discovery Engine was built to demonstrate how structured analytics pipelines, AI-enabled workflows, and explainable scoring methodologies can improve operational awareness and support scalable decision-making.

---

# ⚙️ Core Capabilities

- Ingests and normalizes vessel AIS track data
- Detects candidate low-speed and loitering events
- Ingests float and downstream observation datasets
- Performs spatiotemporal entity correlation
- Ranks associations using explainable scoring methodologies
- Generates structured outputs for downstream analysis
- Supports reproducible deployment through Docker containerization
- Implements modular architecture for future orchestration scalability

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
````

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

Identify vessels exhibiting anomalous or low-speed behavior and determine whether downstream detections are likely associated through spatial and temporal correlation analysis.

Potential applications include:

* Maritime Domain Awareness (MDA)
* ISR workflow augmentation
* Pattern-of-life analysis
* Activity-based intelligence
* Entity resolution workflows
* Operational anomaly detection
* Multi-source data fusion

---

# 📈 Example Output

| vessel_id | event_time       | event_lat | event_lon | float_id | distance_km | time_delta_hr | confidence |
| --------- | ---------------- | --------- | --------- | -------- | ----------- | ------------- | ---------- |
| 987654321 | 2026-03-28 12:00 | 32.71     | -117.16   | F1023    | 4.2         | 1.8           | High       |

(Output simplified for demonstration purposes)

---

# 🛠️ Technical Focus Areas

* Spatiotemporal entity correlation
* Human-in-the-loop analytical workflows
* Explainable analytical scoring
* Containerized deployment architecture
* Operational AI workflow development
* Modular data-ingestion pipelines
* Scalable analytical system design

---

# 🛠️ Tech Stack

## Languages & Analytics

* Python
* pandas
* numpy
* scikit-learn
* matplotlib

## Infrastructure & Tooling

* Docker
* Git
* GitHub
* Linux/WSL

---

# 🔍 Pipeline Workflow

## Ingestion

* Load and normalize AIS vessel track data
* Load and normalize downstream observation data

## Detection

* Identify candidate low-speed and loitering events

## Correlation

* Compare event centroids against candidate downstream observations

## Scoring

* Rank associations using normalized spatial and temporal features
* Generate explainable confidence classifications

## Output

* Produce structured outputs for downstream analytical workflows
* Support repeatable and reproducible analysis across environments

---

# 📊 Visualization

<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/478ac1de-afa7-4daa-ab39-1a629d2aa66c" />

---

# 🎯 Why This Matters

This project demonstrates how fragmented geospatial and time-series data can be transformed into actionable operational insight through structured analytical pipelines and scalable AI-enabled workflows.

The workflow reflects challenges commonly encountered in:

* Defense and intelligence environments
* Maritime domain awareness operations
* Enterprise data integration initiatives
* Operational decision-support systems
* AI-enabled analytical modernization efforts

The broader goal is to explore how emerging analytical architectures can augment human decision-making in complex operational environments.

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

Containerization enables reproducible execution across environments without requiring local dependency configuration.

---

# 📌 Current Status

### v0.1 — Working Containerized Prototype

Current capabilities include:

* AIS ingestion and normalization
* Event detection workflows
* Spatiotemporal entity linkage
* Explainable confidence scoring
* Dockerized execution pipeline

---

# 🔭 Future Expansion

Planned future enhancements include:

* Canonical internal schema design
* Real-world AIS and buoy ingestion
* PostGIS integration for geospatial querying
* FastAPI service layer
* Interactive frontend interface (Next.js / Streamlit)
* Kubernetes-based orchestration
* Distributed processing workflows
* API-driven ingestion pipelines
* CI/CD automation with GitHub Actions
* Multi-source entity enrichment
* Real-time event-stream processing

---

# ⚠️ Notes

All data used is synthetic or publicly available. No sensitive or classified information is included.

This repository is intended to demonstrate analytical architecture, operational AI workflow design, and scalable data-fusion concepts in a public and unclassified environment.

```
```
