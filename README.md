# 🧬 Inversion of Surface Wave Dispersion Using Evolutionary Algorithms 🧬

This repository contains reproducible material for the study *"Inversion of Surface Wave Dispersion Using Evolutionary Algorithms for the Characterization of Compacted Soil"* by **Marcos Augusto Lima da Luz, Rosana Maria do Nascimento Luz, Diogo Luiz de Oliveira Coelho, and Marcos Alberto Rodrigues Vasconcelos**, submitted to *Computers & Geosciences*.

The provided scripts and notebooks demonstrate the generation and inversion of surface wave dispersion data, enabling the retrieval of the S-wave velocity profile as a function of depth using Evolutionary Algorithms.

## 📦 Required Libraries 📦

The following libraries are used in this project:

- [NumPy](https://numpy.org/): Fundamental package for numerical computing in Python.
- [Pandas](https://pandas.pydata.org/): Data analysis and manipulation tool.
- [Matplotlib](https://matplotlib.org/): Visualization library for creating static, animated, and interactive plots.
- [SciPy](https://scipy.org/): Collection of mathematical algorithms and scientific computing tools.
- [tqdm](https://github.com/tqdm/tqdm): Library for displaying progress bars in loops and scripts.
- [GemPy](https://www.gempy.org/): 3D structural geological modeling library.
- [PyVista](https://pyvista.org/): 3D visualization and mesh analysis library.
- [VTK](https://vtk.org/): Toolkit for 3D computer graphics and visualization.
- [DEAP](https://deap.readthedocs.io/): Evolutionary algorithm framework for optimization tasks.
- [Disba](https://github.com/keurfonluu/disba): Surface wave dispersion analysis.
- [GemGIS](https://github.com/cgre-aachen/gemgis): Geospatial processing library.
- [Verde](https://www.fatiando.org/verde/latest/): Processing and interpolation of spatial data.

## 📀 Installation 📀

To use the provided notebooks, install the required dependencies using pip:

```bash
pip install numpy pandas matplotlib scipy tqdm gempy pyvista vtk deap disba gemgis verde
```

## 🏗️ Project structure 🏗️
This repository is organized as follows:

* 🗃️ **CODES**: These scripts collectively enable the generation, simulation, inversion, and visualization of surface wave dispersion data. 🚀
    * 🗒️ **dispersion_curves.py**: Computes **surface wave dispersion curves** based on velocity profiles, essential for inversion analysis.
    * 🗒️ **evolutionary_algorithm.py**: Implements an **evolutionary algorithm** for inverting dispersion curves and estimating S-wave velocity profiles.  
    * 🗒️ **modeling.py**: Defines **geological models** and manages layer properties used in the inversion process. 
    * 🗒️ **pyvista_create_gif.py**: Uses **PyVista** to generate **3D visualizations** and create animated GIFs of the geological models. 

* 🗃️ **notebooks**: set of jupyter notebooks reproducing the experiments in the paper (see below for more details);

## 📑 Notebooks 📑
The following notebooks are provided:

- 📔 ``creating_model_with_gempy.ipynb``: notebook used to generate the model
- 📔 ``generating_observed_data_via_disba.ipynb``: notebook performing the simulation on synthetic dataset
- 📔 ``inversion_evolutionary_algorithm.ipynb``: notebook to perform inversion using evolutionary algorithms

## 🖱️ Usage 🖱️

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd Agriculture_inversion
   ```
2. Open the Jupyter Notebook environment:
   ```bash
   jupyter-lab
   ```
3. Run the following notebooks to reproduce the results:
   - `creating_model_with_gempy.ipynb`: Generates a 3D geological model.
   - `generating_observed_data_via_disba.ipynb`: Simulates observed data (2D profile).
   - `inversion_evolutionary_algorithm.ipynb`: Performs the inversion using an evolutionary algorithm to retrieve the 2D velocity profile.

## 📺 Model Visualizations 📺

- #### **MWC Model:** *No compaction*

Represents the reference model with normal density variation across layers.

<img src="OUTPUT/MWC/FIGURES/block_soil_model.gif" width="400" align="center">

- #### **MCP1 Model:** *Compaction in the first layer*

Characterized by a higher density in the first layer.

<img src="OUTPUT/MCP1/FIGURES/block_soil_model.gif" width="400" align="center">

- #### **MCP2_1 Model:** *Compaction in the second layer (with lateral variation)*

Features lateral density variations in the second layer.

<img src="OUTPUT/MCP2_1/FIGURES/block_soil_model.gif" width="400" align="center">

- #### **MCP2_2 Model:** *Compaction in the second layer (without lateral variation)*

Uniform density in the second layer with no lateral variation.

<img src="OUTPUT/MCP2_2/FIGURES/block_soil_model.gif" width="400" align="center">

#### These animations illustrate the 3D soil models used in the inversions.

## 📝 License 📝 

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
For further details, refer to the paper associated with this repository.

