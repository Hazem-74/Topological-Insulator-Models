# Graphene Models: Topological Insulator Studies

This repository contains Jupyter notebooks that explore fundamental two-dimensional topological insulator models on a honeycomb lattice, specifically focusing on graphene-based systems. These models provide theoretical insights into phenomena like the Quantum Spin Hall Effect and the Quantum Anomalous Hall Effect, showcasing how topology can lead to robust, protected edge states.

The notebooks are located within the directory `Topological Insulator Models/Graphene Models/` in the main repository.

## Models Covered

### 1. Kane-Mele Model (`Kane-Mele Model.ipynb`)

*   **Purpose**: This notebook investigates the Kane-Mele model, a seminal theoretical framework for realizing a **2D Quantum Spin Hall Insulator (QSHI)**. It describes spin-1/2 electrons on a honeycomb lattice with intrinsic spin-orbit coupling, crucially preserving time-reversal symmetry. The model predicts the existence of robust helical edge states at the material's edges.
*   **Methods & Logic**:
    *   The tight-binding Hamiltonian is constructed, incorporating nearest-neighbor hopping and intrinsic spin-orbit coupling (next-nearest-neighbor hopping with spin-dependent complex phases).
    *   The Hamiltonian is transformed into momentum space, where it decouples into effective blocks for spin-up and spin-down electrons.
    *   The bulk band dispersion is numerically calculated and visualized through 3D plots, contour plots, and along high-symmetry paths in the Brillouin Zone, illustrating the opening of a topological gap due to spin-orbit coupling.
    *   The energy spectrum of a finite ribbon geometry (open boundaries in one direction, periodic in another) is computed to demonstrate the presence of **helical edge states** within the bulk band gap, a signature of the QSHI phase.
    *   The notebook outlines the theoretical basis for calculating the $\mathbb{Z}_2$ topological invariant using spin Chern numbers and explores a phase diagram illustrating topological transitions based on key parameters.

### 2. Haldane Model (`Haldane Model.ipynb`)

*   **Purpose**: This notebook explores the Haldane model, a pioneering proposal for a **2D Chern Insulator** that exhibits the **Quantum Anomalous Hall Effect (QAHE)** without requiring an external magnetic field. It describes spinless fermions on a honeycomb lattice.
*   **Methods & Logic**:
    *   The tight-binding Hamiltonian is defined, incorporating nearest-neighbor hopping, a staggered on-site sublattice potential (mass term), and a crucial next-nearest-neighbor complex hopping term that breaks time-reversal symmetry without introducing a net magnetic flux.
    *   The momentum-space Hamiltonian is derived and used to calculate the bulk band dispersion, which is visualized through 3D plots, contour plots, and high-symmetry path diagrams.
    *   The energy spectrum for a finite ribbon geometry is computed, demonstrating the emergence of **chiral edge states** at the boundaries, protected by the bulk topology and providing a pathway for unidirectional electron transport.
    *   The notebook includes a numerical implementation of the Fukui-Hatsugai method to calculate the **bulk Chern number**, a $\mathbb{Z}$-valued topological invariant, and generates a topological phase diagram illustrating transitions between trivial and topological phases based on model parameters.

## Project Requirements

To run these Jupyter notebooks, you'll need the following Python libraries:

*   `numpy`
*   `matplotlib`
*   `sympy`
*   `joblib`
*   `pfapack` (imported for theoretical context in Kane-Mele, though the specific $\mathbb{Z}_2$ calculation uses a spin Chern number approach)
*   `scipy` (often a dependency of `numpy` or `matplotlib`)

## Installation

1.  **Clone the Repository**:
    First, clone the entire `Hazem-74/repository-name` repository (replace `repository-name` with the actual name of the repository) to your local machine using Git:

    ```bash
    git clone https://github.com/Hazem-74/repository-name.git
    cd repository-name
    ```

2.  **Navigate to the Project Directory**:
    The Jupyter notebooks for these models are located in a specific subdirectory:

    ```bash
    cd "Topological Insulator Models/Graphene Models"
    ```

3.  **Install Dependencies**:
    It's recommended to create a virtual environment. Then, install the required Python packages. If a `requirements.txt` file is not present, you can install them manually:

    ```bash
    # (Optional) Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`

    # Install packages
    pip install numpy matplotlib sympy joblib pfapack scipy
    ```

## How to Run the Notebooks

1.  **Start Jupyter**:
    From the `Graphene Models` directory, launch Jupyter Notebook or Jupyter Lab:

    ```bash
    jupyter notebook
    # or
    jupyter lab
    ```

2.  **Open Notebooks**:
    Your web browser will open, displaying the Jupyter interface. Navigate to and open either `Kane-Mele Model.ipynb` or `Haldane Model.ipynb`.

3.  **Execute Cells**:
    You can run the code cells sequentially to reproduce the calculations and visualizations. Use `Shift + Enter` to execute a cell and move to the next.