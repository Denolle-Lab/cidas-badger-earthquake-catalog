# Data Directory

This directory contains input data and metadata for the earthquake catalog workflow.

## Expected Files

### `station_metadata.csv`
Station location information with columns:
- `station_id`: Station identifier (NET.STA.LOC.CHA format)
- `latitude`: Station latitude (decimal degrees)
- `longitude`: Station longitude (decimal degrees)
- `elevation_m`: Station elevation (meters)

This file can be created manually or will be automatically generated from FDSN queries in Notebook 2.

### `das/` subdirectory
Local DAS data files in HDF5 format. Update the path in Notebook 1 configuration to point to your DAS data location.

## Notes

- Station metadata is automatically fetched from FDSN services if not present
- DAS data paths should be configured in [01_das_picking_elep.ipynb](../notebooks/01_das_picking_elep.ipynb)
- Broadband data is downloaded automatically via ObsPy FDSN client
