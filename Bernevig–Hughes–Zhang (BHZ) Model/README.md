# Bernevig–Hughes–Zhang (BHZ) Model

This project delves into the **Bernevig–Hughes–Zhang (BHZ) model**, a cornerstone for understanding two-dimensional topological insulators (2D TIs), also known as Quantum Spin Hall (QSH) insulators. It explores the foundational role of Time-Reversal Symmetry (TRS) in classifying and protecting these unique phases of matter.

## Project Structure

The project consists of two Jupyter notebooks:

*   **`TRS.ipynb`**: Provides the theoretical background on Time-Reversal Symmetry.
*   **`BHZ.ipynb`**: Implements and analyzes the Bernevig–Hughes–Zhang model.

---

### `TRS.ipynb`: Time-Reversal Symmetry (TRS)

This notebook lays the theoretical groundwork for understanding time-reversal symmetry in the context of topological phases.

**Purpose**: To introduce the concept of Time-Reversal Symmetry, distinguish it from other symmetries (like those in Chern insulators), and explain its crucial role in the classification of 2D topological insulators.

**Main Logic & Methods**:

1.  **Introduction to TRS**: Defines time reversal ($\mathcal{T}: t \to -t$) and its basic consequences, such as magnetic fields breaking TRS.
2.  **Chern Insulators vs. TR-Invariant Insulators**: Contrasts Chern insulators (which exhibit chiral edge states and broken TRS) with TR-invariant insulators (which host helical edge states and preserve TRS).
3.  **$\mathbb{Z}_2$ Topological Classification**: Introduces the $\mathbb{Z}_2$ invariant, a topological descriptor for 2D TR-invariant insulators, classifying them as either trivial ($\nu=0$) or topological ($\nu=1$) based on the parity of Kramers pairs of edge states.
4.  **TRS in Quantum Mechanics**: Discusses the time-reversal operator, $\mathcal{K}$ (complex conjugation), for spinless particles.
5.  **TRS with Internal Degrees of Freedom ($\mathcal{T}^2 = \pm 1$)**: Generalizes the TR operator to include internal degrees of freedom (like spin) as $\mathcal{T} = U\mathcal{K}$. It demonstrates that $\mathcal{T}^2$ can only be $+1$ (bosonic TR symmetry) or $-1$ (fermionic TR symmetry, relevant for spin-1/2 electrons).
6.  **Kramers' Degeneracy**: Explains the profound consequence of $\mathcal{T}^2 = -1$: every eigenstate is at least twofold degenerate, forming orthogonal Kramers pairs. This degeneracy is robust at Time-Reversal Invariant Momenta (TRIM).
7.  **TRS of a Bulk Hamiltonian**: Derives the condition for TR invariance in momentum space ($U H(-k)^* U^\dagger = H(k)$) and shows its implications for the energy dispersion ($E(k) = E(-k)$) and Kramers' degeneracy at TRIM points.
8.  **Doubling the Hilbert Space**: Introduces a "doubling trick" as a method to construct a generic TR-invariant Hamiltonian from a given Hamiltonian $H$ and its complex conjugate $H^*$. The symmetry of the coupling operator ($C$) between these two copies determines whether the resulting system falls into the $\mathcal{T}^2=+1$ (symmetric $C$) or $\mathcal{T}^2=-1$ (antisymmetric $C$) class.

---

### `BHZ.ipynb`: Bernevig–Hughes–Zhang Model (BHZ)

This notebook applies the theoretical concepts of TRS to construct and analyze the BHZ model, demonstrating its properties as a 2D topological insulator.

**Purpose**: To implement the BHZ model, analyze its band structure and edge states under different coupling conditions, and connect these observations to the underlying time-reversal symmetry and $\mathbb{Z}_2$ topological invariant.

**Main Logic & Methods**:

1.  **BHZ Hamiltonian Construction**: The BHZ model is constructed in momentum space using a four-band representation (two copies, two internal states per copy). It builds upon a modified Qi-Wu-Zhang (QWZ) Chern insulator, applying the "doubling trick" introduced in `TRS.ipynb`.
    *   Pauli matrices $\sigma_{x,y,z}$ operate on the **copy space** (two layers).
    *   Pauli matrices $\tau_{x,y,z}$ operate on the **internal degree of freedom** (e.g., orbital/sublattice) within each copy.
    *   A critical parameter is the coupling operator $C$, which couples the two copies.
2.  **Analysis of Coupling Strength ($C$)**:
    *   **Case $C=0$ (Uncoupled)**: The Hamiltonian block-diagonalizes into two independent QWZ copies with opposite Chern numbers. This results in an overall zero Chern number but features helical edge states (two counterpropagating modes) at each edge. These are protected by two distinct TR symmetries ($\mathcal{T}_1^2=-1$ and $\mathcal{T}_2^2=+1$).
    *   **Case $C \neq 0$ (Coupled Layers)**:
        *   **Symmetric Coupling ($C = C^T$)**: If $C$ is symmetric (e.g., $C \propto \tau_x$), the system preserves only $\mathcal{T}^2=+1$ symmetry. This allows hybridization between edge states from different layers, opening a gap and making the system topologically trivial.
        *   **Antisymmetric Coupling ($C = -C^T$)**: If $C$ is antisymmetric (e.g., $C \propto \tau_y$), the system preserves the $\mathcal{T}^2=-1$ symmetry. This protects the helical edge states, preventing them from gapping out even in the presence of coupling, leading to a 2D topological insulator (Quantum Spin Hall effect).
3.  **Numerical Diagonalization & Visualization**:
    *   The notebook leverages `SymPy` for initial symbolic definition of the Hamiltonian.
    *   `NumPy` is used to construct and numerically diagonalize the Hamiltonian for a finite-width stripe geometry (periodic in $x$, finite in $y$) across various $k_x$ momenta.
    *   `Matplotlib` is used to plot the resulting band structures, visually demonstrating the presence or absence of protected edge states within the bulk gap.
4.  **$\mathbb{Z}_2$ Invariant Calculation**: A Python function `calculate_Z2` is provided to numerically determine the $\mathbb{Z}_2$ invariant by identifying states localized at the edges and counting the number of Kramers pairs.
5.  **Role of Disorder**: Discusses how the $\mathcal{T}^2 = -1$ symmetry provides topological protection against backscattering from TR-symmetric disorder, preserving the robust conductance of the helical edge states.

---

## Getting Started

### Project Requirements

To run these Jupyter notebooks, you will need a Python environment with the following libraries:

*   `Python 3.x`
*   `jupyter`
*   `numpy`
*   `sympy`
*   `matplotlib`

### Installation

1.  **Clone the Repository**:
    First, clone the entire `Topological Insulator Models` repository from GitHub:

    ```bash
    git clone https://github.com/Hazem-74/Topological-Insulator-Models.git
    cd Topological-Insulator-Models/'Bernevig–Hughes–Zhang (BHZ) Model'
    ```

2.  **Install Dependencies**:
    It is recommended to use a virtual environment.

    ```bash
    # (Optional) Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install required packages
    pip install jupyter numpy sympy matplotlib
    ```

### How to Run the Notebooks

1.  **Launch Jupyter Notebook**:
    From the `'Bernevig–Hughes–Zhang (BHZ) Model'` directory, launch Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

2.  **Open Notebooks**:
    Your web browser will open to the Jupyter interface. Navigate to and click on `TRS.ipynb` or `BHZ.ipynb` to open them.

3.  **Execute Cells**:
    You can run each cell sequentially by selecting a cell and pressing `Shift + Enter`, or run all cells using the "Run All" option from the "Cell" menu. Follow the comments and explanations within the notebooks for a guided exploration of the models.