# Entity Discovery Engine (v0.1)

## Overview
This project implements a spatiotemporal entity discovery engine that:

- Ingests vessel AIS data
- Detects candidate behavioral events (low-speed / loitering)
- Ingests float/buoy first-observation data
- Links vessel events to candidate downstream entities
- Ranks associations using distance and temporal proximity

## Current Capabilities (v0.1)
- AIS ingestion and cleaning
- Event detection (low-speed clustering)
- Float ingestion
- Event-to-float linkage
- Distance + time filtering
- Explainable scoring and confidence classification
- Basic visualization of vessel track and detected events

## Architecture
Pipeline stages:

1. **Ingestion**
   - AIS vessel tracks
   - Float first observations

2. **Detection**
   - Low-speed event detection

3. **Linkage**
   - Spatial + temporal correlation

4. **Scoring**
   - Normalized scoring (distance + time)
   - Confidence classification (HIGH / MEDIUM / LOW)

## Example Use Case
Given a vessel track:
- Detect potential deployment window
- Identify floats appearing nearby in space/time
- Rank likely associations

## Tech Stack
- Python
- pandas / numpy
- matplotlib

## Next Steps
- Add real-world data ingestion (AIS + Argo)
- Introduce canonical data schema
- Integrate PostGIS for geospatial querying
- Build API (FastAPI)
- Develop frontend visualization (Next.js)

## Status
v0.1 — Working prototype (local pipeline)