# Outputs Directory

This directory contains intermediate and final outputs from the earthquake catalog workflow.

## Generated Files

### Stage 1: DAS Phase Picking
- `das_picks.csv`: Phase picks from DAS data using ELEP

### Stage 2: Broadband Phase Picking
- `broadband_picks.csv`: Phase picks from broadband stations
- `pick_comparison.csv`: Comparison between catalog and ML picks

### Stage 3: Phase Association
- `associated_events.csv`: Event catalog with origin times and preliminary locations
- `associated_picks.csv`: Phase picks assigned to events

### Stage 4: Relative Location
- `hypodd/`: HypoDD working directory with input/output files
- `hypodd_relocated_events.csv`: Final relocated event catalog
- `location_comparison.csv`: Analysis of DAS contribution to location accuracy

## File Format

All pick files follow SeisBench-compatible CSV format:
- `station_id`: NET.STA.LOC.CHA
- `phase_time`: ISO datetime
- `phase_label`: P or S
- `phase_score`: Confidence 0-1
- `event_id`: Event identifier (after association)

Event catalogs include:
- `event_id`: Unique identifier
- `origin_time`: Event origin time
- `latitude`, `longitude`, `depth`: Location
- Quality metrics (errors, RMS, number of picks, etc.)
