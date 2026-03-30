# Entity Discovery Engine

## Overview
Entity Discovery Engine is a spatiotemporal analytics workflow for identifying relationships and uncovering hidden patterns across large datasets.

The current prototype focuses on maritime-style entity discovery by:
- ingesting vessel AIS track data
- detecting candidate low-speed / loitering events
- ingesting float first-observation data
- linking vessel events to candidate downstream entities
- ranking associations using explainable spatial and temporal scoring

## Problem
Traditional analysis workflows often require significant manual effort to identify related entities across large volumes of time-series and geospatial data.

This project explores how an analyst-facing pipeline can reduce that burden by surfacing candidate relationships automatically and scoring them transparently.

## Current Capabilities (v0.1-engine)
- AIS ingestion and cleaning
- candidate event detection using low-speed clustering
- float ingestion
- event-to-float linkage
- distance and time filtering
- explainable scoring and confidence classification
- basic visualization of vessel track and detected events

## Approach
This project uses a staged workflow:

1. **Ingestion**
   - load and clean vessel AIS data
   - load and clean float first-observation data

2. **Detection**
   - identify candidate low-speed / loitering windows

3. **Linkage**
   - compare event centroids to candidate float first appearances

4. **Scoring**
   - rank likely associations using normalized distance and time features

## Tech Stack
- Python
- pandas
- numpy
- matplotlib

Planned stack expansion:
- scikit-learn
- PostgreSQL / PostGIS
- FastAPI
- Next.js

## Status
v0.1-engine — working local prototype

## Notes
All data used in this project is synthetic or publicly available. No sensitive or classified information is included.

## Next Steps
- design a canonical internal schema
- add real-world AIS ingestion
- add real-world Argo / buoy ingestion
- normalize heterogeneous source formats
- integrate PostGIS for persistent geospatial querying
- build an API and frontend UX
