# Kane‑Mele Model: A 2D Topological Insulator on the Honeycomb Lattice

This repository provides a comprehensive computational study of the **Kane‑Mele model** – a theoretical framework for realizing a **quantum spin Hall insulator** on a honeycomb lattice (such as graphene). The model describes spin‑1/2 electrons with intrinsic spin‑orbit coupling and predicts the existence of **helical edge states** protected by **time‑reversal symmetry**.

---

## Overview

The Kane‑Mele model is a paradigmatic 2D topological insulator that exhibits the **quantum spin Hall effect** without an external magnetic field. Key features include:

- **Spin‑1/2 fermions** on a honeycomb lattice
- **Nearest‑neighbour hopping** – generates graphene‑like Dirac cones
- **Intrinsic spin‑orbit coupling** – next‑nearest‑neighbour hopping with spin‑dependent complex phases, preserving time‑reversal symmetry
- **Time‑reversal symmetry** – protects **Kramers pairs** and suppresses backscattering
- **Helical edge states** – spin‑momentum locked edge modes with opposite spins propagating in opposite directions

Unlike the Haldane model (which breaks time‑reversal symmetry and has a Chern number), the Kane‑Mele model is characterised by a **ℤ₂ topological invariant** \(\nu \in \{0,1\}\).

All numerical implementations are provided in Python, with extensive visualisations of band structures, edge states, and topological phase diagrams.

---

## Theoretical Background

### Kane‑Mele Hamiltonian

The tight‑binding Hamiltonian is

\[
H = -t_1 \sum_{\langle i,j \rangle, \sigma} \left( c_{i,\sigma}^\dagger c_{j,\sigma} + \text{h.c.} \right)
    + i \lambda_{\text{SO}} \sum_{\langle\!\langle i,j \rangle\!\rangle, \sigma\sigma'} \nu_{ij} (s_z)_{\sigma\sigma'} c_{i,\sigma}^\dagger c_{j,\sigma'} + \text{h.c.},
\]

where:
- \(t_1\) is the nearest‑neighbour hopping amplitude
- \(\lambda_{\text{SO}}\) is the intrinsic spin‑orbit coupling strength
- \(\nu_{ij} = \pm 1\) is the orientation‑dependent sign for next‑nearest‑neighbour hopping
- \(s_z\) is the Pauli matrix for spin

### Momentum‑Space Representation

In the basis \(\{ |k,A,\uparrow\rangle, |k,B,\uparrow\rangle, |k,A,\downarrow\rangle, |k,B,\downarrow\rangle \}\), the Hamiltonian decouples into two spin blocks:

\[
H(\mathbf{k}) = \begin{pmatrix} H_\uparrow(\mathbf{k}) & 0 \\ 0 & H_\downarrow(\mathbf{k}) \end{pmatrix},
\]

with

\[
H_\sigma(\mathbf{k}) = d_x(\mathbf{k})\sigma_x + d_y(\mathbf{k})\sigma_y + \sigma \cdot d_z^{\text{SO}}(\mathbf{k})\sigma_z,
\]

where \(\sigma = +1\) for \(\uparrow\), \(-1\) for \(\downarrow\), and

\[
\begin{aligned}
d_x(\mathbf{k}) &= -t_1 \sum_{j=1}^3 \cos(\mathbf{k}\cdot\mathbf{a}_j), \\
d_y(\mathbf{k}) &= -t_1 \sum_{j=1}^3 \sin(\mathbf{k}\cdot\mathbf{a}_j), \\
d_z^{\text{SO}}(\mathbf{k}) &= 2\lambda_{\text{SO}} \sum_{j=1}^3 \sin(\mathbf{k}\cdot\mathbf{b}_j).
\end{aligned}
\]

### Bulk Dispersion

The eigenvalues are doubly degenerate (Kramers degeneracy):

\[
E_{\pm,\sigma}(\mathbf{k}) = \pm \sqrt{d_x(\mathbf{k})^2 + d_y(\mathbf{k})^2 + \left(\sigma d_z^{\text{SO}}(\mathbf{k})\right)^2}.
\]

The gap opens at the Dirac points \(K\) and \(K'\) with magnitude

\[
\Delta = 6\sqrt{3}\,|\lambda_{\text{SO}}|.
\]

### ℤ₂ Topological Invariant

The Kane‑Mele model is characterised by a **ℤ₂ invariant** \(\nu \in \{0,1\}\):

- \(\nu = 0\): trivial insulator
- \(\nu = 1\): topological insulator with helical edge states

For \(\lambda_{\text{SO}} > 0\), the system is in the **topological phase** (\(\nu = 1\)) regardless of the sign of \(\lambda_{\text{SO}}\). The gap never closes unless \(\lambda_{\text{SO}} = 0\).

### Helical Edge States

In the topological phase (\(\nu = 1\)):
- **Helical edge states** appear at boundaries
- Spin‑up and spin‑down electrons propagate in **opposite directions**
- Backscattering is **forbidden** by time‑reversal symmetry
- Quantised **spin Hall conductance** \(\sigma_{xy}^s = e/2\pi\)

---

## Code Structure

The project is contained in a single Jupyter notebook with the following sections:

### 1. Symbolic Derivation
- Definition of lattice vectors and Pauli matrices
- Symbolic construction of \(H_\uparrow\) and \(H_\downarrow\)
- Display of the spin‑up block

### 2. Numerical Band Structure
- 3D dispersion plots (conduction and valence bands)
- 2D contour maps of \(E_+\) and \(E_-\)
- Band gap contour map
- Band structure along the \(\Gamma \to K \to M \to \Gamma\) path

### 3. Ribbon Geometry (Edge States)
- Construction of the Kane‑Mele ribbon with open boundary conditions along \(x\) and periodic along \(y\)
- Eigenvalue spectrum as a function of \(k_y\)
- Spaghetti plots: spectrum vs \(\lambda_{\text{SO}}\) and vs \(t_1\)

### 4. ℤ₂ Invariant Computation (Fu‑Kane Method)
- Definition of time‑reversal operator
- Construction of the overlap matrix \(B(\mathbf{k})\)
- Pfaffian evaluation at TRIM points
- Phase diagram \(\nu(t_1, \lambda_{\text{SO}})\)

### Key Functions

| Function | Description |
|----------|-------------|
| `energy_plus_km(kx, ky, t1, λ_SO, a)` | Conduction band energy for a single spin block |
| `energy_minus_km(kx, ky, t1, λ_SO, a)` | Valence band energy |
| `build_kanemele_ribbon(k_y, t1, λ_SO, N_x)` | Ribbon Hamiltonian with open boundary in \(x\) |
| `h_k(kx, ky, t1, λ_SO)` | 2×2 Bloch Hamiltonian for a single spin |
| `compute_chern_number_cell(h_func, nk)` | Chern number via Fukui method (for each spin) |
| `compute_z2(t1, λ_SO, nk)` | ℤ₂ invariant from spin Chern numbers |

---

## Parameters

| Parameter | Default | Meaning |
|-----------|---------|---------|
| \(t_1\) | 1.0 | Nearest‑neighbour hopping |
| \(\lambda_{\text{SO}}\) | 0.3 | Spin‑orbit coupling strength |
| \(a\) | 1.0 | Lattice constant |
| \(N_x\) | 40 | Number of unit cells (ribbon width) |
| \(N_k\) | 200 | Number of \(k\)-points for band structure |

---

## Results and Visualisations

### Static Band Structure
- **3D dispersion**: Shows the spin‑degenerate conduction and valence bands with a gap opened by \(\lambda_{\text{SO}}\)
- **Contour maps**: \(E_+\) and \(E_-\) in the Brillouin zone with the hexagonal BZ boundary
- **Band gap map**: Reveals the gap opening at \(K\) and \(K'\)
- **Path dispersion**: \(\Gamma \to K \to M \to \Gamma\) showing the band gap

### Ribbon Edge States
- **Energy spectrum vs index**: Shows the full eigenvalue spectrum for a fixed \(k_y\)
- **Band structure vs \(k_y\)**: Reveals helical edge states connecting valence and conduction bands
- **Spaghetti plots**: Evolution of the spectrum as \(\lambda_{\text{SO}}\) or \(t_1\) varies

### ℤ₂ Phase Diagram
- **Phase diagram in \((t_1, \lambda_{\text{SO}})\) space**: Shows the topological (\(\nu = 1\)) and trivial (\(\nu = 0\)) regions
- The topological phase exists for \(\lambda_{\text{SO}} \neq 0\) (gap open)
- The trivial phase occurs when \(\lambda_{\text{SO}} = 0\) (gapless Dirac cones)

---

## Animations

*(The notebook currently generates static plots. Animations can be added using `FuncAnimation` similar to the other model notebooks.)*

---

## Dependencies

All code is written in Python 3.8+ and requires the following libraries:

```bash
pip install numpy matplotlib scipy sympy joblib pfapack
```

- **NumPy** – numerical arrays and linear algebra
- **Matplotlib** – plotting and visualisations
- **SciPy** – linear algebra and special functions
- **SymPy** – symbolic derivation
- **Joblib** – parallel computation (optional)
- **pfapack** – Pfaffian computation for the ℤ₂ invariant

---

## Usage

1. Clone or download the repository.
2. Open the Jupyter notebook.
3. Execute the cells sequentially to reproduce all figures.
4. Modify parameters (e.g., \(\lambda_{\text{SO}}, t_1, N_x\)) at the beginning of each section.

---

## Key Differences from Other Models

| Feature | Haldane Model | Kane‑Mele Model | QWZ Model |
|---------|---------------|-----------------|-----------|
| Particles | Spinless fermions | **Spin‑1/2 electrons** | Spinless fermions |
| Time‑reversal | **Broken** | **Preserved** | Broken (Chern insulator) |
| Topological invariant | Chern number \(C \in \mathbb{Z}\) | **ℤ₂** \(\nu \in \{0,1\}\) | Chern number \(C\) |
| Edge states | Chiral (unidirectional) | **Helical** (spin‑locked) | Chiral |
| Symmetry class | A (unitary) | **AII** (symplectic) | A |
| Lattice | Honeycomb | **Honeycomb** | Square |
| Physical realisation | Artificial gauge fields | **Intrinsic SOC** (e.g., graphene, silicene) | Artificial gauge fields |

---

## References

1. Kane, C. L., & Mele, E. J. (2005). *Quantum spin Hall effect in graphene*. Physical Review Letters, 95(22), 226801.
2. Kane, C. L., & Mele, E. J. (2005). *Z₂ topological order and the quantum spin Hall effect*. Physical Review Letters, 95(14), 146802.
3. Fu, L., & Kane, C. L. (2006). *Time reversal polarization and a Z₂ adiabatic spin pump*. Physical Review B, 74(19), 195312.
4. Fukui, T., Hatsugai, Y., & Suzuki, H. (2005). *Chern numbers in discretized Brillouin zone*. Journal of the Physical Society of Japan, 74(6), 1674‑1677.
