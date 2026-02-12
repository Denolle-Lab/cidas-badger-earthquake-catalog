# CIDAS Badger Earthquake Catalog

Repository for detecting, locating, and characterizing earthquakes using broadband and DAS data in Cook Inlet, Alaska. This workflow combines machine learning phase picking (ELEP, SeisBench), association (PyOcto), and high-precision relative location (HypoDD) to build a comprehensive earthquake catalog.

## Installation

### Using Conda

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)

2. Create the environment:

```bash
conda env create -f environment.yml
```

3. Activate the environment:

```bash
conda activate cidas-badger-catalog
```

### Using Pixi

[Pixi](https://prefix.dev/docs/pixi/overview) is a modern package manager for conda packages.

1. Install pixi:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

2. Install dependencies:

```bash
pixi install
```

3. Run commands in the pixi environment:

```bash
pixi run jupyter
```

Or activate the shell:

```bash
pixi shell
```

## Dependencies

The following Python packages are included:

* **ObsPy**: Seismology library for processing seismic data
* **NumPy**: Numerical computing
* **Matplotlib**: Plotting and visualization
* **Pandas**: Data manipulation and analysis
* **Jupyter**: Interactive notebooks
* **SciPy**: Scientific computing
* **h5py**: HDF5 file format support
* **PyTorch**: Deep learning framework
* **SeisBench**: Seismological machine learning models
* **ELEP**: Earthquake location and phase picking
* **PyOcto**: Octree-based earthquake location
* **usgs-libcomcat**: USGS ComCat data access library

## Workflow

This repository implements a four-stage workflow for earthquake detection, location, and characterization using both DAS and broadband seismic data:

### Stage 1: DAS Phase Picking ([01_das_picking_elep.ipynb](notebooks/01_das_picking_elep.ipynb))
- Read local DAS data files
- Apply ELEP phase picking algorithm
- Clean picks using theoretical travel time constraints
- Output: `outputs/das_picks.csv` (SeisBench-compatible format)

### Stage 2: Broadband Phase Picking ([02_broadband_picking_comparison.ipynb](notebooks/02_broadband_picking_comparison.ipynb))
- Download broadband seismic data via FDSN
- Retrieve existing picks from USGS libcomcat
- Run SeisBench models (PhaseNet, EQTransformer, etc.) or ELEP
- Compare ML picks with catalog picks
- Output: `outputs/broadband_picks.csv`, `outputs/pick_comparison.csv`

### Stage 3: Phase Association ([03_phase_association_pyocto.ipynb](notebooks/03_phase_association_pyocto.ipynb))
- Merge DAS and broadband picks
- Load station metadata
- Run PyOcto associator to identify events
- Output: `outputs/associated_events.csv`, `outputs/associated_picks.csv`

### Stage 4: Relative Location ([04_hypodd_relocation.ipynb](notebooks/04_hypodd_relocation.ipynb))
- Prepare HypoDD input files
- Run double-difference relocation
- Compare locations with/without DAS data
- Quantify DAS contribution to location accuracy
- Output: `outputs/hypodd_relocated_events.csv`, `outputs/location_comparison.csv`

## Usage

Start Jupyter notebook server:

```bash
# With conda
jupyter notebook

# With pixi
pixi run jupyter
```

Then navigate to the `notebooks/` directory and run notebooks in sequence (01 → 04).

## Data Organization

```
cidas-badger-earthquake-catalog/
├── notebooks/          # Jupyter notebooks for each workflow stage
│   ├── 01_das_picking_elep.ipynb
│   ├── 02_broadband_picking_comparison.ipynb
│   ├── 03_phase_association_pyocto.ipynb
│   └── 04_hypodd_relocation.ipynb
├── src/               # Shared Python modules
│   ├── __init__.py
│   └── pick_utils.py  # SeisBench-compatible pick format utilities
├── outputs/           # Processing outputs (created during workflow)
│   ├── das_picks.csv
│   ├── broadband_picks.csv
│   ├── associated_events.csv
│   ├── associated_picks.csv
│   └── hypodd_relocated_events.csv
├── data/              # Input data and metadata (user-provided)
│   ├── das/           # Local DAS data files
│   └── station_metadata.csv
└── environment.yml    # Conda environment specification

```

## Pick Format

All phase picks are stored in SeisBench-compatible CSV format with the following columns:

- `station_id`: Station identifier (NET.STA.LOC.CHA format)
- `phase_time`: Phase arrival time (datetime)
- `phase_label`: Phase type (P, S, etc.)
- `phase_score`: Pick confidence (0-1)
- `phase_index`: Sample index in original trace (optional)
- `event_id`: Associated event ID (added in Stage 3)

This format is compatible with both SeisBench and PyOcto for seamless integration.

## Contributors

This workflow is a collaborative effort. Please add your name and contribution area:

- **Notebook 1 (DAS Picking):** [Names here]
- **Notebook 2 (Broadband Picking):** [Names here]
- **Notebook 3 (Association):** [Names here]
- **Notebook 4 (Relocation):** [Names here]

## References

This workflow is based on methods from:
- [Shi et al. 2023 - DAS denoising](https://github.com/Denolle-Lab/Shi_etal_2023_denoiseDAS)
- SeisBench: Machine learning models for seismology
- PyOcto: Octree-based earthquake location
- HypoDD: Double-difference earthquake relocation

## License

[Add license information]
