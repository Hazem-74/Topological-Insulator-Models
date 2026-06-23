# Qi‑Wu‑Zhang (QWZ) Model: A 2D Chern Insulator

This repository provides a comprehensive computational study of the **Qi‑Wu‑Zhang (QWZ) model** – a minimal two‑dimensional Chern insulator that realizes the anomalous quantum Hall effect without an external magnetic field. The code is organised in two parts, covering static topological properties, Floquet engineering with circularly polarized light, and high‑harmonic generation (HHG) spectroscopy.

---

## Overview

The QWZ model (also known as the “half‑BHZ” model) is a paradigmatic lattice model for a 2D topological insulator. It can be obtained by **dimensional extension** of the Rice‑Mele Thouless pump, promoting the cyclic pump parameter to a momentum coordinate. The model exhibits a non‑zero Chern number and hosts chiral edge states.

Key topics covered:

- **Chern number** and its quantised values
- **Edge states** in a strip geometry
- **Floquet engineering** with circularly polarised light
- **Laser‑induced topological phase transitions**
- **High‑harmonic generation** as a probe of topology
- **Circular components** of the HHG spectrum (selection rules)

All numerical implementations are provided in Python, with extensive visualisations and animations.

---

## Theoretical Background

### QWZ Hamiltonian

The bulk momentum‑space Hamiltonian of the QWZ model is

\[
H_{\mathrm{QWZ}}(\mathbf{k}) =
\sin k_x \, \sigma_x + \sin k_y \, \sigma_y
+ \bigl[ t_0 + \cos k_x + \cos k_y \bigr] \sigma_z,
\]

with \(\mathbf{d}(k_x,k_y) = (\sin k_x,\ \sin k_y,\ t_0 + \cos k_x + \cos k_y)\).  
The energy dispersion is

\[
E_\pm(\mathbf{k}) = \pm \sqrt{\sin^2 k_x + \sin^2 k_y + (t_0 + \cos k_x + \cos k_y)^2}.
\]

The **Chern number** \(C\) of the lower band is determined by the winding of \(\mathbf{d}(\mathbf{k})\) around the origin:

\[
C = \frac{1}{4\pi} \int_{\mathrm{BZ}} \mathbf{d} \cdot \left( \frac{\partial \mathbf{d}}{\partial k_x} \times \frac{\partial \mathbf{d}}{\partial k_y} \right) \frac{dk_x dk_y}{|\mathbf{d}|^3}.
\]

For the QWZ model,

\[
C =
\begin{cases}
0, & t_0 < -2 \quad\text{or}\quad t_0 > 2, \\
-1, & -2 < t_0 < 0, \\
+1, & 0 < t_0 < 2.
\end{cases}
\]

Gap closings occur at \(t_0 = \{-2, 0, +2\}\), corresponding to the \(\Gamma\), \(X\), and \(M\) points.

### Edge States

In a strip geometry with open boundary conditions along \(x\) and periodic along \(y\), the Hamiltonian acquires a dependence on \(k_y\). Chiral edge states appear in the bulk gap, with opposite velocities on opposite edges. Their dispersion \(\varepsilon(k_y)\) connects the conduction and valence bands.

### Floquet Engineering with Circular Drive

Under a **circularly polarised** laser field, the Peierls substitution replaces \(k_\mu \to k_\mu + A_\mu(t)\) with

\[
A_x(t) = \frac{F_0}{\omega}\cos(\omega t), \qquad A_y(t) = \frac{F_0}{\omega}\sin(\omega t).
\]

The one‑cycle Floquet propagator \(U_F(\mathbf{k})\) defines the quasi‑energy spectrum. The **Floquet Chern number** \(C_F(F_0)\) can take integer values that differ from the static Chern number, signalling **laser‑induced topological transitions**.

### High‑Harmonic Generation

The macroscopic current is

\[
\mathbf{J}(t) = \frac{1}{N_k^2} \sum_{\mathbf{k}} \mathrm{Tr}\!\left[ \hat{\mathbf{j}}(\mathbf{k},t)\, \rho(\mathbf{k},t) \right],
\]

where \(\hat{\mathbf{j}}_\mu = -\partial H/\partial A_\mu\). The HHG power spectrum is the Fourier transform of \(\mathbf{J}(t)\). With circular drive, **odd harmonics** preserve the lattice symmetry, while **even harmonics** are sensitive to the topological phase.

---

## Code Structure

The project is split into two Jupyter notebooks (or consecutive sections in a single script):

### Part 1 – QWZ Model I (Static Properties)
- Construction of the real‑space Hamiltonian and current operators
- 3D band structure and 2D colour maps
- Band dispersion along high‑symmetry paths
- **Chern number** via the Fukui–Hatsugai–Suzuki method
- Edge‑state dispersion in a strip geometry
- Animation of eigenstates and band structure as \(t_0\) varies

### Part 2 – QWZ Model II (Floquet & HHG)
- Symbolic derivation (SymPy) of Hamiltonian, eigenvectors, current operators
- Instantaneous eigenenergies and dispersion vs vector potential
- **Floquet propagator** (batched over the BZ) and quasi‑energy spectrum
- **Floquet Chern number** vs drive amplitude \(F_0\)
- Phase diagram \(C_F(t_0, F_0)\) for circular drive
- Time‑dependent density‑matrix evolution (k‑space)
- HHG spectra: total, \(J_x\), \(J_y\), and circular components \(J_\pm\)
- Odd/even harmonic decomposition

### Key Functions

| Function | Description |
|----------|-------------|
| `build_H_QWZ(Ax, Ay, t0)` | Real‑space Hamiltonian with Peierls phases |
| `build_J_QWZ_x`, `build_J_QWZ_y` | Current operators \(\hat{J}_x, \hat{J}_y\) |
| `qwz_bloch_2x2(kx, ky, t0, Ax, Ay)` | 2×2 Bloch Hamiltonian |
| `chern_number_fukui(t0, Ax, Ay, Nk)` | Static Chern number via plaquette method |
| `floquet_propagator_QWZ(t0, F0, n_steps)` | Batched Floquet propagator \(U_F(\mathbf{k})\) |
| `floquet_chern_QWZ(t0, F0, Nk, n_steps)` | Floquet Chern number with band tracking |
| `time_evolve_QWZ(t0)` | RK4 k‑space density‑matrix evolution; returns \(J_x(t), J_y(t)\) |
| `compute_hhg_2d(Jx, Jy)` | FFT of current; total and circular components |

---

## Parameters (Part II Defaults)

| Parameter | Value | Meaning |
|-----------|-------|---------|
| \(t_0\) (C=+1) | 1.0 | Static Chern number +1 |
| \(t_0\) (trivial) | 3.0 | Static Chern number 0 |
| \(t_0\) (C=−1) | −1.0 | Static Chern number −1 |
| \(\omega\) | 1.5 | Drive frequency |
| \(F_0\) | 2.5 | Drive amplitude |
| \(n_\text{cyc}\) | 8 | Number of laser cycles |
| \(N_x, N_y\) | 10, 10 | Real‑space grid (for visualisation) |
| \(N_k\) (Floquet) | 25–50 | Momentum‑space grid |

---

## Results and Visualisations

The code produces numerous plots and animated GIFs. A selection of key outputs is listed below.

### Static Properties
- `QWZ_dispersion_vs_A.png` – Dispersion \(E_+(\mathbf{k})\) for different \(|A|\).
- `QWZ_eigenenergies_vs_A.gif` – Instantaneous eigenvalues as \(|A|\) sweeps.
- `QWZ_dirac_cones.png` – 3D band surfaces at representative \(|A|\).
- `QWZ_edge_states_vs_A.png` – Edge‑state dispersion in strip geometry.

### Floquet Analysis
- `QWZ_floquet_spectrum.png` – Quasi‑energy spectrum along high‑symmetry path for several \(F_0\).
- `QWZ_floquet_eigenenergies.gif` – Instantaneous band surface over one laser cycle.
- `QWZ_floquet_chern.png` – Floquet Chern number \(C_F\) vs \(F_0\) for three \(t_0\) values.
- `QWZ_phase_diagram.png` – Phase diagram \(C_F(t_0, F_0)\) with discrete colormap.

### HHG
- `QWZ_HHG_spectrum.png` – Total HHG spectrum (topological vs trivial).
- `QWZ_HHG_circular.png` – Circular components \(J_+\) and \(J_-\) (selection rules).
- `QWZ_HHG_odd_even.png` – Odd/even harmonic bar charts for total and circular components.

---

## Animations

| GIF | Description |
|-----|-------------|
| `QWZ_eigenenergies_vs_A.gif` | Real‑space eigenvalues as \(|A|\) is swept. |
| `QWZ_gap_vs_A.gif` | Gap maps \(\Delta(k_x,k_y)\) as circular \(A\) rotates. |
| `QWZ_floquet_eigenenergies.gif` | Instantaneous 3D band surface over one laser cycle. |
| `QWZ_bandstructure.gif` | Strip edge‑state dispersion as \(t_0\) varies. |

---

## Dependencies

All code is written in Python 3.8+ and requires the following libraries:

```bash
pip install numpy matplotlib scipy sympy plotly pillow
```

- **NumPy** – numerical arrays and linear algebra
- **Matplotlib** – plotting and animations
- **SciPy** – special functions and linear algebra (e.g., `eigh`, `expm`)
- **SymPy** – symbolic derivation
- **Plotly** – optional for interactive 3D plots
- **Pillow** – saving animations as GIFs

---

## Usage

1. Clone or download the repository.
2. Open the Jupyter notebook (or run the Python script) containing the two parts.
3. Execute the cells sequentially to reproduce all figures and animations.
4. Modify parameters (e.g., \(t_0, F_0, \omega\)) at the beginning of each section.

All generated figures and GIFs are saved in the working directory.

---

## References

1. Qi, X.-L., Wu, Y.-S., & Zhang, S.-C. (2006). *Topological quantization of the spin Hall effect in two‑dimensional insulating systems*. Physical Review B, 74(8), 085308.
2. Fukui, T., Hatsugai, Y., & Suzuki, H. (2005). *Chern numbers in discretized Brillouin zone*. Journal of the Physical Society of Japan, 74(6), 1674‑1677.
3. Oka, T., & Aoki, H. (2009). *Photovoltaic Hall effect in graphene*. Physical Review B, 79(8), 081406.
4. Fregoso, B. M., & Vampa, G. (2019). *High‑harmonic generation in topological materials*. Physical Review B, 100(4), 041402.
