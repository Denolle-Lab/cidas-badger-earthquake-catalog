# cidas-badger-earthquake-catalog
Repository that hosts scripts to detect, locate, characterize earthquakes using broadbands+DAS in Cook Inlet

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

## Usage

Start Jupyter notebook server:

```bash
# With conda
jupyter notebook

# With pixi
pixi run jupyter
```
