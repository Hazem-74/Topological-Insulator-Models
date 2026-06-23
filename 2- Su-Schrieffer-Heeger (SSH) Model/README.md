# Su-Schrieffer-Heeger (SSH) Model: From Static Topology to Floquet-Driven High Harmonic Generation

This repository provides a comprehensive computational study of the **Su-Schrieffer-Heeger (SSH) model**, a paradigmatic one‑dimensional topological insulator. The code is organised in three self‑contained parts that progressively build from static topological properties to time‑dependent Floquet engineering and high‑harmonic generation (HHG) spectroscopy.

---

## Overview

The SSH model describes spinless fermions on a dimerized chain with staggered hopping amplitudes. Its simplicity makes it an ideal platform for illustrating key concepts in topological condensed matter:

- **Bulk topology** and the **winding number**
- **Chiral symmetry** and **edge states**
- **Domain‑wall bound states** and **charge fractionalisation**
- **Floquet engineering**: laser‑induced topological phase transitions
- **High‑harmonic generation** as a probe of topology

All numerical implementations are provided in Python, with extensive visualisations and animations.

---

## Theoretical Background

### SSH Hamiltonian

The tight‑binding Hamiltonian for a finite chain of \(N\) unit cells is

\[
H = t_1 \sum_{n=1}^{N} \left( |n_B\rangle\langle n_A| + \text{h.c.} \right)
    + t_2 \sum_{n=1}^{N-1} \left( |(n+1)_A\rangle\langle n_B| + \text{h.c.} \right),
\]

where \(t_1\) and \(t_2\) are the intra‑cell and inter‑cell hopping amplitudes.  
With periodic boundary conditions, the bulk Bloch Hamiltonian reads

\[
H(k) = \begin{pmatrix} 0 & t_1 + t_2 e^{-ik} \\ t_1 + t_2 e^{ik} & 0 \end{pmatrix}
      = \mathbf{d}(k)\cdot\boldsymbol{\sigma},
\]

with  
\[
d_x(k) = t_1 + t_2 \cos k,\qquad d_y(k) = -t_2 \sin k.
\]

The energy dispersion is

\[
E_\pm(k) = \pm \sqrt{t_1^2 + t_2^2 + 2t_1t_2\cos k}.
\]

The system is **topological** when \(t_2 > t_1\) (winding number \(\nu = 1\)), hosting zero‑energy edge states, and **trivial** when \(t_1 > t_2\) (\(\nu = 0\)).

### Chiral Symmetry

The SSH Hamiltonian obeys **chiral (sublattice) symmetry**:

\[
\Gamma H \Gamma = -H,\qquad \Gamma = \sum_n \left( |n_A\rangle\langle n_A| - |n_B\rangle\langle n_B| \right).
\]

This forces the spectrum to be symmetric about zero energy and guarantees that zero‑energy states are fully polarised on a single sublattice.

### Bulk Winding Number

The winding number of the \(\mathbf{d}(k)\) loop around the origin is

\[
\nu = \frac{1}{2\pi i} \int_{-\pi}^{\pi} dk\;\partial_k \log h(k),
\qquad h(k) = d_x(k) - i d_y(k) = t_1 + t_2 e^{-ik}.
\]

This integer invariant distinguishes the topological and trivial phases.

### Floquet Engineering

Under a periodic laser field, the vector potential \(A(t) = -\frac{F_0}{\omega}\cos(\omega t)\) is introduced via the Peierls substitution \(k \to k + A(t)\). The one‑cycle Floquet propagator is

\[
U_F(k) = \mathcal{T}\exp\!\left( -i\int_0^{T} H(k, A(t))\,dt \right),
\]

and its eigenvalues define the **Floquet quasi‑energies** \(\varepsilon\). The **Floquet winding number** \(\nu_F\) can change even though the instantaneous winding number is fixed, giving rise to **laser‑induced topological phase transitions**.

### High‑Harmonic Generation

The macroscopic current is computed from the density matrix:

\[
J(t) = \mathrm{Tr}\!\left[ \hat{J}(t)\,\rho(t) \right],
\qquad \hat{J}(t) = -\frac{\partial H(t)}{\partial A}.
\]

The HHG power spectrum is obtained by Fourier transforming \(J(t)\):

\[
S(\Omega) = \left| \int_0^{t_\text{max}} J(t)\,e^{i\Omega t}\,dt \right|^2.
\]

In systems with bulk inversion symmetry only **odd harmonics** are allowed; even harmonics can arise from edge‑state contributions, making the even/odd ratio a spectroscopic signature of topology.

---

## Code Structure

The project is split into three Jupyter notebooks (or consecutive sections in a single script), each focusing on a different aspect.

### Part 1 – SSH Model I (Static Topology)
- Construction of the real‑space and momentum‑space Hamiltonians
- Energy dispersion and \(\mathbf{d}(k)\)‑vector plots (static and animated)
- Fully dimerized limits (trivial, topological, general)
- Eigenvalue spectrum for open chains (N=20) and edge‑state localisation
- “Spaghetti” plots: spectrum vs \(t_1\) and vs \(t_2\)

### Part 2 – SSH Model II (Topology & Edge States)
- Chiral symmetry and its consequences
- Numerical computation of the winding number
- Exact and approximate edge‑state amplitudes; localisation length
- Hybridisation and energy splitting in finite chains
- Domain‑wall bound states and their localisation
- Spectrum dependence on all four hopping parameters (2×2 panel)

### Part 3 – SSH Model III (Floquet & HHG)
- Symbolic derivation (SymPy) of Hamiltonian, eigenvectors, current operator
- \(\mathbf{d}(k)\)‑loop animation over one laser cycle
- Floquet propagator via 4th‑order Runge–Kutta
- Quasi‑energy spectrum vs drive amplitude \(F_0\)
- Floquet winding number and phase diagram in the \((t_1/t_2, F_0)\) plane
- Time‑dependent current from coherent density‑matrix evolution
- HHG power spectra with gap‑order and phase‑transition markers
- Odd/even harmonic decomposition; ratio \(R\) vs \(F_0\)

### Key Functions

| Function | Description |
|----------|-------------|
| `build_H(t1, t2, A)` | Real‑space Hamiltonian for a given vector potential \(A\) |
| `build_J(t1, t2, A)` | Current operator \(\hat{J} = -\partial H/\partial A\) |
| `dispersion(t1, t2, A, k)` | Analytical band \(E_+(k) = \sqrt{t_1^2+t_2^2+2t_1t_2\cos(k+A)}\) |
| `floquet_propagator_batch()` | One‑cycle Floquet propagator \(U_F(k)\) for all \(k\) |
| `floquet_winding_number()` | Computes \(\nu_F\) from the off‑diagonal element of \(U_F\) |
| `time_evolve()` | RK4 time evolution of the density matrix; returns \(J(t)\) |
| `compute_hhg()` | HHG power spectrum from the time‑dependent current |

---

## Parameters (Notebook III Defaults)

| Parameter | Value | Meaning |
|-----------|-------|---------|
| \(t_1, t_2\) (topological) | 0.6, 1.0 | \(t_2 > t_1\) → \(\nu=1\) |
| \(t_1, t_2\) (trivial) | 1.0, 0.8 | \(t_1 > t_2\) → \(\nu=0\) |
| \(\omega\) | 1.5 | Drive frequency |
| \(F_0\) | 2.5 | Drive amplitude |
| \(n_\text{cyc}\) | 8 | Number of laser cycles |
| \(N\) | 50 | Number of unit cells |

---

## Results and Visualisations

The code produces a wealth of plots and animated GIFs. Below is a selection of key outputs.

### Static Band Structure and d‑Vector

- `dvector_ellipse.png` – \(\mathbf{d}(k)\) loops for topological and trivial phases, with markers for different vector potentials.
- Animated dispersion and \(\mathbf{d}(k)\) loops as \(t_1\) or \(t_2\) vary (`SSH_Dispersion_intracell.gif`, `SSH_Dispersion_intercell.gif`).

### Edge States and Domain Walls

- `Eigenvectors.gif` – Probability density of eigenstates for a topological chain, showing edge localisation.
- `Eigenvectors_Domain_Walls.gif` – Eigenstates of a chain with a domain wall, revealing the bound state at the interface.
- Spectrum vs all four hopping parameters (2×2 panel).

### Floquet Analysis

- `floquet_spectrum.png` – Quasi‑energy spectrum vs \(F_0\) (navy = topological, red = trivial).
- `floquet_phasediagram_blue.png` – Phase diagram in the \((t_1/t_2, F_0)\) plane using a discrete blue colormap.
- `floquet_gap_tracking.gif` – Quasi‑energy bands as \(F_0\) ramps, highlighting gap closings.
- `floquet_spectrum_vs_index.gif` – Full quasi‑energy spectrum vs eigenstate index as \(F_0\) varies.

### High‑Harmonic Generation

- `HHG_topo.png` / `HHG_triv.png` – HHG power spectra with gap‑order and phase‑transition markers.
- `odd_even_topo.png` / `odd_even_triv.png` – Odd/even harmonic bar charts.
- `even_odd_ratio.png` – Even/odd ratio \(R\) vs \(F_0\), with vertical lines marking Floquet transitions.

### Animations of Laser‑Driven Dynamics

- `dvector_cycle.gif` – \(\mathbf{d}(k)\) loop over one laser cycle.
- `dispersion_cycle.gif` – Instantaneous dispersion \(E_\pm(k, A(t))\) over one cycle.
- `floquet_eigenenergy_cycle.gif` – Real‑space eigenenergy spectrum over one cycle.

---

## Dependencies

All code is written in Python 3.8+ and requires the following libraries:

```bash
pip install numpy matplotlib scipy sympy plotly pillow
```

- **NumPy** – numerical arrays and linear algebra
- **Matplotlib** – plotting and animations
- **SciPy** – special functions and linear algebra (e.g., `eigh`, `expm`)
- **SymPy** – symbolic derivation of Hamiltonian and current operator
- **Plotly** – interactive 3D plots (optional)
- **Pillow** – saving animations as GIFs

---

## Usage

1. Clone or download the repository.
2. Open the Jupyter notebook (or run the Python script) containing all three parts.
3. Execute the cells sequentially to reproduce all figures and animations.
4. To customise parameters, modify the corresponding variables at the top of each section (e.g., \(t_1, t_2, F_0, \omega\)).

All generated figures and GIFs are saved in the working directory.

---

## References

1. Su, W. P., Schrieffer, J. R., & Heeger, A. J. (1979). *Solitons in polyacetylene*. Physical Review Letters, 42(25), 1698.
2. Asbóth, J. K., Oroszlány, L., & Pályi, A. (2016). *A short course on topological insulators*. Lecture Notes in Physics, 919.
3. Oka, T., & Aoki, H. (2009). *Photovoltaic Hall effect in graphene*. Physical Review B, 79(8), 081406.
4. Fregoso, B. M., & Vampa, G. (2019). *High‑harmonic generation in topological materials*. Physical Review B, 100(4), 041402.
