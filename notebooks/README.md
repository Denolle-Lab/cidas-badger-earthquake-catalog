# CIDAS Badger Earthquake Catalog - Notebooks

This directory contains Jupyter notebooks implementing the four-stage earthquake detection and location workflow.

## Workflow Overview

```
DAS Data → [1] → das_picks.csv ──┐
                                 │
Broadband → [2] → broadband_picks.csv ──→ [3] → associated_picks.csv → [4] → relocated_events.csv
            ↓                              ↑
     pick_comparison.csv          associated_events.csv
```

## Notebooks

### [01_das_picking_elep.ipynb](01_das_picking_elep.ipynb)
**Purpose:** Process DAS data with ELEP phase picking

**Inputs:**
- Local DAS data files (HDF5 format)
- Station metadata

**Outputs:**
- `das_picks.csv`: Phase picks in SeisBench format

**Key Steps:**
1. Load DAS data from local files
2. Run ELEP phase picking
3. Apply travel-time based cleanup
4. Export to standardized CSV

---

### [02_broadband_picking_comparison.ipynb](02_broadband_picking_comparison.ipynb)
**Purpose:** Download broadband data and run phase picking with model comparison

**Inputs:**
- Event catalog search parameters
- FDSN data sources

**Outputs:**
- `broadband_picks.csv`: Phase picks from broadband
- `pick_comparison.csv`: Comparison statistics

**Key Steps:**
1. Search USGS ComCat for events
2. Download broadband waveforms
3. Retrieve existing catalog picks
4. Run SeisBench models (PhaseNet/EQTransformer)
5. Compare and merge picks

---

### [03_phase_association_pyocto.ipynb](03_phase_association_pyocto.ipynb)
**Purpose:** Associate picks into events using PyOcto

**Inputs:**
- `das_picks.csv` (from Notebook 1)
- `broadband_picks.csv` (from Notebook 2)
- Station metadata

**Outputs:**
- `associated_events.csv`: Event catalog
- `associated_picks.csv`: Picks with event assignments

**Key Steps:**
1. Merge DAS and broadband picks
2. Load/create station metadata
3. Configure PyOcto associator
4. Run association
5. Format and save results

---

### [04_hypodd_relocation.ipynb](04_hypodd_relocation.ipynb)
**Purpose:** Perform high-precision relative location with HypoDD

**Inputs:**
- `associated_events.csv` (from Notebook 3)
- `associated_picks.csv` (from Notebook 3)
- Velocity model
- HypoDD installation

**Outputs:**
- `hypodd_relocated_events.csv`: Final catalog
- `location_comparison.csv`: DAS contribution analysis

**Key Steps:**
1. Prepare HypoDD input files
2. Run double-difference relocation
3. Compare locations with/without DAS
4. Quantify DAS contribution
5. Visualize results

---

## Running the Workflow

Execute notebooks in order (01 → 04):

```bash
# Start Jupyter
pixi run jupyter

# Or with conda
conda activate cidas-badger-catalog
jupyter notebook
```

Each notebook is self-contained with:
- Configuration section at the top
- Detailed documentation in markdown cells
- Placeholder functions for customization
- Visualization tools

## Configuration

Key parameters to update in each notebook:

**Notebook 1:**
- `DAS_DATA_PATH`: Path to local DAS files
- `ELEP_MODEL_PATH`: ELEP model location
- Travel time parameters

**Notebook 2:**
- Search region bounds (lat/lon)
- Time window
- FDSN client selection
- SeisBench model choice

**Notebook 3:**
- PyOcto parameters (min_picks, tolerance, etc.)
- Velocity model
- Search grid bounds

**Notebook 4:**
- HypoDD executable path
- Velocity model layers
- Relocation parameters

## Shared Utilities

The `src/pick_utils.py` module provides functions used across notebooks:
- `create_picks_dataframe()`: Create standardized pick DataFrame
- `save_picks_csv()` / `load_picks_csv()`: I/O functions
- `merge_picks()`: Combine picks from multiple sources
- `validate_picks_schema()`: Check format compliance

## Contributors

Add your name and contribution area:
- **Notebook 1:** [Names]
- **Notebook 2:** [Names]
- **Notebook 3:** [Names]
- **Notebook 4:** [Names]

## Notes

- All notebooks use SeisBench-compatible pick format for consistency
- DAS stations are identified by `station_id` starting with "DAS"
- Outputs are saved to `../outputs/` directory
- Visualizations are included in each notebook
