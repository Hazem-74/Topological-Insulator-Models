# Su-Schrieffer-Heeger (SSH) Model: 1D Topological Insulators

This repository contains a collection of Jupyter notebooks that explore the fundamental concepts of one-dimensional (1D) topological insulators, with a primary focus on the **Su-Schrieffer-Heeger (SSH) model** and its extensions. Through theoretical explanations, mathematical derivations, and numerical simulations using Python, these notebooks aim to provide a comprehensive understanding of bulk-boundary correspondence, chiral symmetry, topological invariants, and electronic polarization in these systems.

## Table of Contents

1.  [About the SSH Model](#about-the-ssh-model)
2.  [Notebooks Overview](#notebooks-overview)
    *   [SSH I.ipynb](#ssh-iipynb)
    *   [SSH II.ipynb](#ssh-iiipynb)
    *   [Rice-Mele Model & Polarization.ipynb](#rice-mele-model--polarizationipynb)
3.  [Project Requirements](#project-requirements)
4.  [Installation](#installation)
5.  [How to Run the Notebooks](#how-to-run-the-notebooks)
6.  [License](#license)

## About the SSH Model

The Su-Schrieffer-Heeger (SSH) model is a seminal 1D tight-binding model that describes spinless fermions on a bipartite lattice with staggered hopping amplitudes. It serves as a paradigmatic example for illustrating key concepts in topological phases of matter, including:

*   **Bulk-Boundary Correspondence**: The deep connection between bulk topological properties (e.g., winding number) and the existence of protected edge states at the system's boundaries.
*   **Chiral Symmetry**: A fundamental symmetry that protects zero-energy edge states and ensures a symmetric energy spectrum.
*   **Topological and Trivial Phases**: How the system's parameters lead to distinct phases characterized by different topological invariants.
*   **Edge States**: Localized states at the boundaries of the system, often robust against perturbations and carrying fractional charges.

These notebooks provide both theoretical background and practical computational exercises to explore these phenomena.

## Notebooks Overview

### SSH I.ipynb

This notebook serves as an introduction to the Su-Schrieffer-Heeger (SSH) model.

*   **Purpose**: To introduce the real-space and momentum-space Hamiltonians of the SSH model, derive its energy dispersion relation, and visualize the key features that distinguish its topological and trivial phases. It also explores the concept of edge states in finite chains.
*   **Methods & Main Logic**:
    *   **Hamiltonian Construction**: Defines the real-space SSH Hamiltonian for a finite chain with open boundary conditions, explicitly showing its matrix representation.
    *   **Momentum-Space Hamiltonian**: Derives the Bloch Hamiltonian $H(k)$ and expresses it in terms of Pauli matrices, defining the $\vec{d}(k)$ vector.
    *   **Energy Dispersion**: Calculates and plots the energy bands $E(k)$ for varying hopping parameters ($t_1, t_2$), demonstrating the band gap opening/closing and the transition between topological ($t_1 < t_2$) and trivial ($t_1 > t_2$) phases.
    *   **d-vector Trajectory**: Visualizes the trajectory of the $\vec{d}(k)$ vector in the $d_x-d_y$ plane, showing how its winding around the origin characterizes the topological phase.
    *   **Finite Chain Analysis**: Numerically diagonalizes the real-space Hamiltonian for a finite chain to compute the energy spectrum and identify zero-energy edge states.
*   **Key Visualizations**:
    *   Animated plots of the dispersion relation and $\vec{d}(k)$ trajectory as hopping parameters vary.
    *   Energy spectrum and probability density of edge states in a finite SSH chain.

### SSH II.ipynb

Building upon the first notebook, `SSH II.ipynb` delves deeper into the theoretical underpinnings and advanced phenomena of the SSH model.

*   **Purpose**: To meticulously examine the role of chiral symmetry, define and calculate the bulk winding number, and provide an exact real-space derivation of edge states. It further explores the hybridization of these states and the emergence of bound states at domain walls.
*   **Methods & Main Logic**:
    *   **Chiral Symmetry**: Rigorously defines chiral symmetry, discusses its conditions (unitarity, locality, robustness), and explains its implications for the energy spectrum (symmetric about zero) and sublattice polarization of eigenstates.
    *   **Bulk Winding Number**: Introduces the winding number as a topological invariant derived from the $\vec{d}(k)$ vector. It visualizes the winding paths in 3D and provides a computational method to calculate the winding number using a complex integral of $h(k) = d_x(k) - i d_y(k)$.
    *   **Exact Edge State Calculation**: Derives recursive formulas for edge state amplitudes in real space, demonstrating their exponential localization and calculating the localization length ($\xi$).
    *   **Hybridization**: Explains how finite system size leads to hybridization between left and right edge states, causing an exponentially small energy splitting ($\Delta E$).
    *   **Domain Walls**: Simulates an SSH chain with a domain wall (transition between topological and trivial regions), showing how localized bound states emerge at the interface, demonstrating charge fractionalization.
*   **Key Visualizations**:
    *   3D plots of $\vec{d}(k)$ trajectories illustrating winding.
    *   Plot of $h(k)$ in the complex plane for winding number verification.
    *   Plots of edge state amplitudes showing exponential decay.
    *   Energy spectrum and animated wavefunction localization for domain wall states.

### Rice-Mele Model & Polarization.ipynb

This notebook extends the understanding of 1D topological insulators by introducing the Rice-Mele model and the concept of electronic polarization as a topological invariant.

*   **Purpose**: To investigate the effects of a staggered on-site potential on the SSH model, leading to the Rice-Mele model, and to introduce the modern theory of electronic polarization as a diagnostic for topological phases.
*   **Methods & Main Logic**:
    *   **Rice-Mele Hamiltonian**: Formulates the Rice-Mele Hamiltonian by adding a staggered on-site potential ($t_0$) to the SSH model. Discusses how $t_0$ breaks chiral symmetry and its implications for the energy spectrum.
    *   **Numerical Diagonalization**: Computes the energy spectrum and eigenstate wavefunctions for a finite Rice-Mele chain, observing how edge states are lifted from zero energy due to $t_0$.
    *   **Parameter Sweeps**: Visualizes the evolution of the energy spectrum as $t_1$, $t_2$, and $t_0$ are varied, highlighting the persistence of the band gap even when chiral symmetry is broken.
    *   **Electronic Polarization**: Explains the modern theory of polarization, relating it to the Berry connection and Berry phase. It demonstrates how polarization quantizes to $0$ or $e/2$ (modulo $e$) in the trivial and topological phases, respectively, even in the absence of chiral symmetry.
*   **Key Visualizations**:
    *   Energy spectrum and animated wavefunction localization for Rice-Mele model.
    *   Energy spectrum plots showing the effect of varying $t_1, t_2,$ and $t_0$.
    *   Plots of electronic polarization as a function of hopping parameter difference ($\Delta t$), showcasing its quantized nature.

## Project Requirements

To run these Jupyter notebooks, you will need the following Python libraries:

*   `numpy`
*   `matplotlib`
*   `plotly` (for interactive 3D plots in `SSH II.ipynb`)
*   `IPython` (for displaying GIFs in notebooks)

## Installation

To get a local copy of this project up and running, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Hazem-74/Topological-Insulator-Models.git
    ```

2.  **Navigate to the Project Directory**:
    The SSH Model notebooks are located within the `Topological Insulator Models/Su-Schrieffer-Heeger (SSH) Model` directory.
    ```bash
    cd Topological-Insulator-Models/Topological Insulator Models/Su-Schrieffer-Heeger (SSH) Model
    ```

3.  **Create a Virtual Environment (Recommended)**:
    ```bash
    python -m venv venv
    ```

4.  **Activate the Virtual Environment**:
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

5.  **Install Dependencies**:
    While activated, install the required libraries:
    ```bash
    pip install numpy matplotlib plotly ipython
    ```
    *(Note: `ipython` is usually installed with Jupyter, but explicitly listed for completeness).*

## How to Run the Notebooks

1.  **Launch Jupyter**:
    Ensure your virtual environment is active, then start Jupyter Lab or Jupyter Notebook from the `Su-Schrieffer-Heeger (SSH) Model` directory:
    ```bash
    jupyter lab
    # or
    jupyter notebook
    ```

2.  **Open the Notebooks**:
    Your web browser will open, displaying the Jupyter interface. Navigate to and open `SSH I.ipynb`, `SSH II.ipynb`, or `Rice-Mele Model & Polarization.ipynb`.

3.  **Execute Cells**:
    You can run the cells sequentially to see the code, derivations, plots, and animations.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.