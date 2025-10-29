# Qi-Wu-Zhang (QWZ) Model: 2D Topological Insulator

This project explores the **Qi-Wu-Zhang (QWZ) model**, a foundational two-dimensional (2D) model for realizing a Chern insulator. It demonstrates the Anomalous Quantum Hall Effect without an external magnetic field, exhibiting a non-vanishing bulk Chern number. The QWZ model serves as a minimalist building block for more complex topological insulators like the Bernevig–Hughes–Zhang (BHZ) model, often referred to as the "half BHZ" model.

## Project Overview

The QWZ model is constructed through a process called **dimensional extension**, transforming a 1D time-periodic system (specifically, the Rice–Mele (RM) model) into a 2D static system. This project provides a comprehensive analysis of the QWZ model, covering its theoretical derivation, bulk properties, topological invariants (Chern number), real-space representation, and the emergence of robust edge states.

The `QWZ.ipynb` Jupyter notebook guides users through:

1.  **Theoretical Foundations**: Derivation of the momentum-space Hamiltonian from a Thouless pump.
2.  **Bulk Dispersion Relation**: Calculation and visualization of the energy bands and identification of gap-closing conditions (Dirac points).
3.  **Chern Number Calculation**: Analysis of how the mass term (`t0`) dictates the topological phase and the bulk Chern number.
4.  **Real-Space Hamiltonian**: Construction of the Hamiltonian in real space for finite systems and numerical diagonalization to find eigenvalues and eigenstates.
5.  **Edge States**: Investigation of edge states in a strip geometry (periodic along y, open along x) by analyzing the $k_y$-dependent band structure and group velocity.
6.  **Edge Perturbations**: Demonstration of the robustness of topological edge states against local perturbations.
7.  **Higher Chern Numbers**: Introduction to constructing models with higher Chern numbers by coupling multiple QWZ layers.

## Getting Started

Follow these instructions to set up the project and run the Jupyter notebooks.

### Prerequisites

Ensure you have Python 3.8+ installed. The project relies on several common scientific computing libraries.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Hazem-74/Topological-Insulator-Models.git
    cd Topological-Insulator-Models/Qi-Wu-Zhang (QWZ) Model
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install numpy sympy matplotlib plotly pillow jupyter
    ```

### How to Run the Notebook

1.  **Activate your virtual environment** (if you haven't already):
    ```bash
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

2.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
    This will open a new tab in your web browser.

3.  **Navigate and open `QWZ.ipynb`:**
    In the Jupyter file browser, navigate to the `Qi-Wu-Zhang (QWZ) Model` directory and click on `QWZ.ipynb`.

4.  **Execute the cells:**
    You can run the notebook cells sequentially to reproduce all the calculations, visualizations, and animations presented in the project.

## File Summary

-   **`QWZ.ipynb`**: The main Jupyter notebook containing the full analysis of the Qi-Wu-Zhang model.
    -   **Purpose**: To derive, analyze, and visualize the fundamental properties of the 2D QWZ Chern insulator.
    -   **Methods**:
        -   **Symbolic Mathematics**: Utilizes `sympy` for defining Hamiltonians, Pauli matrices, and performing algebraic manipulations, especially for initial conceptual derivations and real-space Hamiltonian construction.
        -   **Numerical Computation**: Employs `numpy` for efficient array operations, diagonalization (`numpy.linalg.eigh`), and numerical gradients (`numpy.gradient`).
        -   **Visualization**: Leverages `matplotlib` for 2D and 3D plots of band structures, energy maps, Chern number, and group velocity. `plotly` is used for interactive 3D plotting, and `FuncAnimation` from `matplotlib.animation` is used to create GIFs illustrating dynamic behaviors.
    -   **Main Logic**:
        -   Starts with the momentum-space QWZ Hamiltonian derived from the Rice-Mele model.
        -   Calculates bulk energy bands and identifies gap-closing points (`t0 = -2, 0, 2`).
        -   Demonstrates the piecewise nature of the Chern number as a function of `t0`.
        -   Constructs the real-space Hamiltonian for finite lattices to study bulk eigenvalues and eigenstate probability densities.
        -   Transitions to a strip geometry (periodic in `y`, open in `x`) to analyze the `k_y`-dependent Hamiltonian.
        -   Numerically diagonalizes `H(k_y)` to reveal the emergence of topological edge states within the bulk gap.
        -   Computes and visualizes the group velocity of these edge states, highlighting their unidirectional propagation.
        -   Investigates the impact of edge perturbations on the band structure, reinforcing the robustness of topological protection.
        -   Explores how coupling multiple QWZ layers can lead to higher Chern numbers.

## Animations

The notebook generates several GIF animations to visualize dynamic properties and parameter dependencies:

-   `Eigenvectors.gif`: Shows the probability density `|ψ|^2` for different eigenstates in a small real-space lattice.
-   `QWZ_eigenvalues.gif`: Illustrates how the eigenvalues of the real-space Hamiltonian change as the `t0` parameter is varied, demonstrating gap opening and closing.
-   `QWZ_bandstructure.gif`: Displays the evolution of the `k_y`-dependent band structure as `t0` is swept, clearly showing the emergence and disappearance of edge states.
-   `QWZ_group_velocity.gif`: Visualizes the group velocity of the energy bands as `t0` changes, highlighting the unidirectional propagation of edge states.

## Contributions

Feel free to open issues or submit pull requests if you have suggestions or improvements!

---

**Hazem-74** | [GitHub Profile](https://github.com/Hazem-74)