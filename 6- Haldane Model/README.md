# Haldane Model: A 2D Chern Insulator on the Honeycomb Lattice

This repository provides a comprehensive computational study of the **Haldane model** – a paradigmatic 2D topological insulator that realizes the quantum anomalous Hall effect without an external magnetic field. The code is organised in two parts, covering static topological properties, Floquet engineering with circularly polarized light, and high‑harmonic generation (HHG) spectroscopy on the honeycomb lattice.

---

## Overview

The Haldane model describes spinless fermions hopping on a honeycomb lattice with:

- **Nearest‑neighbour (NN) hopping** – generates graphene‑like Dirac cones at the \(K\) and \(K'\) valleys.
- **Next‑nearest‑neighbour (NNN) hopping with complex phases** – breaks time‑reversal symmetry without a net magnetic flux through the unit cell.
- **Staggered sublattice potential (mass term)** – breaks inversion symmetry.

The interplay of these terms produces a nontrivial **bulk Chern number**, giving rise to topologically protected chiral edge states via the bulk–boundary correspondence. Key topics covered:

- **Chern number** and its quantized values
- **Valley‑selective gap control** – the \(K\) and \(K'\) valleys respond differently to the NNN hopping phase
- **Floquet engineering** with circularly polarised light
- **Laser‑induced topological phase transitions**
- **High‑harmonic generation** as a probe of topology
- **C₃ symmetry selection rules** in HHG

All numerical implementations are provided in Python, with extensive visualisations and animations.

---

## Theoretical Background

### Haldane Hamiltonian

The tight‑binding Hamiltonian on the honeycomb lattice is

\[
H = -t_1 \sum_{\langle i,j \rangle} \left( c_i^\dagger c_j + \text{h.c.} \right)
    - t_2 \sum_{\langle\!\langle i,j \rangle\!\rangle} \left( e^{i\nu_{ij}\phi} c_i^\dagger c_j + \text{h.c.} \right)
    + M \sum_i \xi_i c_i^\dagger c_i,
\]

where \(t_1\) is the NN hopping, \(t_2 e^{i\phi}\) is the complex NNN hopping, \(M\) is the staggered sublattice potential, and \(\nu_{ij} = \pm 1\) depends on the hopping orientation. In momentum space, the Bloch Hamiltonian takes the form

\[
H(\mathbf{k}) = d_x(\mathbf{k})\,\sigma_x + d_y(\mathbf{k})\,\sigma_y + d_z(\mathbf{k})\,\sigma_z,
\]

with

\[
\begin{aligned}
d_x(\mathbf{k}) &= -t_1 \sum_{j=1}^3 \cos(\mathbf{k}\cdot\mathbf{a}_j), \\
d_y(\mathbf{k}) &= -t_1 \sum_{j=1}^3 \sin(\mathbf{k}\cdot\mathbf{a}_j), \\
d_z(\mathbf{k}) &= M - 2t_2 \sin\phi \sum_{j=1}^3 \sin(\mathbf{k}\cdot\mathbf{b}_j).
\end{aligned}
\]

Here \(\mathbf{a}_j\) are the NN vectors and \(\mathbf{b}_j\) are the NNN vectors.

### Dirac Points and Gap Closing

The honeycomb lattice naturally hosts Dirac cones at the \(K\) and \(K'\) points. At these points, \(d_x = d_y = 0\). The gap closes when

\[
d_z(K) = 0 \quad \Longrightarrow \quad M = 3\sqrt{3}\,t_2\sin\phi,
\]
\[
d_z(K') = 0 \quad \Longrightarrow \quad M = -3\sqrt{3}\,t_2\sin\phi.
\]

The Chern number is

\[
C = 
\begin{cases}
+1, & 0 < M < 3\sqrt{3}t_2\sin\phi, \\
-1, & -3\sqrt{3}t_2\sin\phi < M < 0, \\
0,  & |M| > 3\sqrt{3}t_2|\sin\phi|.
\end{cases}
\]

### Bulk–Boundary Correspondence

If the bulk Chern number \(C\) is nonzero, the system supports **chiral edge states** at open boundaries. The number of edge states equals \(|C|\), and these states are topologically protected against backscattering, realising the anomalous quantum Hall effect without Landau levels.

### Floquet Engineering with Circular Drive

Under a circularly polarised laser field, the Peierls substitution replaces \(\mathbf{k} \to \mathbf{k} + \mathbf{A}(t)\) with

\[
A_x(t) = \frac{F_0}{\omega}\cos(\omega t), \qquad A_y(t) = \frac{F_0}{\omega}\sin(\omega t).
\]

Because the honeycomb lattice has two inequivalent valleys, the circular drive can selectively close the gap at one valley while leaving the other open – enabling **valley‑selective topological transitions** inaccessible with linear polarisation.

### High‑Harmonic Generation

The macroscopic current is

\[
\mathbf{J}(t) = \frac{1}{N_k^2} \sum_{\mathbf{k}} \mathrm{Tr}\!\left[ \hat{\mathbf{j}}(\mathbf{k},t)\, \rho(\mathbf{k},t) \right],
\]

where \(\hat{\mathbf{j}}_\mu = -\partial H/\partial A_\mu\). The HHG spectrum is the Fourier transform of \(\mathbf{J}(t)\). On the honeycomb lattice:

- **C₃ symmetry** suppresses harmonics of order \(3n\).
- **Circular drive** produces distinct selection rules: \(J_+\) carries harmonics \(3n+1\), while \(J_-\) carries \(3n+2\).
- **Even harmonics** appear when inversion symmetry is broken (\(M \neq 0\)).

---

## Code Structure

The project is split into two Jupyter notebooks (or consecutive sections in a single script):

### Part 1 – Haldane Model I (Static Properties)
- Symbolic derivation (SymPy) of Hamiltonian, \(d\)-vector, and dispersion
- 3D band structure and 2D colour maps
- Band dispersion along the \(\Gamma \to K \to M \to K' \to \Gamma\) path
- **Chern number** via the Fukui–Hatsugai–Suzuki method
- Edge‑state dispersion in a ribbon geometry
- Phase diagram \(C(M, \phi)\) with parallel computation
- Spaghetti plots: spectrum vs \(t_1\), \(t_2\), \(M\), and \(\phi\)

### Part 2 – Haldane Model II (Floquet & HHG)
- Symbolic derivation of eigenvectors, Berry connection, and current operators
- **Valley‑selective gap closing** under circular drive
- Dirac cone evolution at \(K\) and \(K'\) as \(|\mathbf{A}|\) increases
- **Floquet propagator** (batched over the BZ) and quasi‑energy spectrum
- **Floquet Chern number** vs drive amplitude \(F_0\)
- Phase diagram \(C_F(M, F_0)\) for circular drive
- Transverse Hall conductance tracking via Berry curvature
- Time‑dependent density‑matrix evolution (k‑space)
- HHG spectra: total, \(J_x\), \(J_y\), and circular components \(J_\pm\)
- Odd/even harmonic decomposition with C₃ selection rules

### Key Functions

| Function | Description |
|----------|-------------|
| `haldane_bloch_2x2(kx, ky, M, t1, t2, phi, Ax, Ay)` | 2×2 Bloch Hamiltonian with Peierls phases |
| `haldane_jx_2x2()`, `haldane_jy_2x2()` | Current operators \(\hat{J}_x, \hat{J}_y\) |
| `haldane_chern_fukui(M, t1, t2, phi, Ax, Ay, Nk)` | Static Chern number via plaquette method |
| `floquet_propagator_H_batch(M, t1, t2, phi, F0, n_steps)` | Batched Floquet propagator \(U_F(\mathbf{k})\) |
| `floquet_chern_H(M, F0, Nk, n_steps)` | Floquet Chern number with adiabatic band tracking |
| `berry_curvature_map(M, Ax, Ay, Nk)` | Berry curvature \(\Omega_z(\mathbf{k})\) via finite differences |
| `time_evolve_H(M, verbose)` | RK4 k‑space density‑matrix evolution; returns \(J_x(t), J_y(t)\) |
| `compute_hhg_H(Jx, Jy)` | FFT of current; total and circular components |

---

## Parameters (Part II Defaults)

| Parameter | Value | Meaning |
|-----------|-------|---------|
| \(t_1\) | 1.0 | Nearest‑neighbour hopping |
| \(t_2\) | 0.3 | Next‑nearest‑neighbour hopping |
| \(M\) (C=+1) | 0.2 | Staggered mass – topological phase |
| \(M\) (trivial) | 4.0 | Staggered mass – trivial phase |
| \(M\) (C=−1) | −0.2 | Staggered mass – opposite topology |
| \(\phi\) | \(\pi/2\) | Haldane phase |
| \(\omega\) | 1.5 | Drive frequency |
| \(F_0\) | 2.5 | Drive amplitude |
| \(n_\text{cyc}\) | 8 | Number of laser cycles |

The gap‑closing critical mass is \(M_{\mathrm{crit}} = 3\sqrt{3}t_2|\sin\phi| = 1.558\) for \(\phi = \pi/2\).

---

## Results and Visualisations

The code produces numerous plots and animated GIFs. A selection of key outputs is listed below.

### Static Properties
- `Haldane_dispersion_cycle.gif` – Band structure along high‑symmetry path as circular \(A(t)\) rotates.
- `Haldane_gap_closing.png` – Valley‑selective gap closing at \(K\) and \(K'\) vs drive phase.
- `Haldane_dirac_cones.png` – 3D Dirac cone evolution at \(K\) and \(K'\) for different \(|A|\).
- `Haldane_bandstructure_vs_A.png` – 2D band maps and path dispersion for different \(|A|\).
- `Haldane_chern_phase_diagram.png` – Static Chern phase diagram \((M/t_2, \phi)\) as \(|\mathbf{A}|\) increases.

### Floquet Analysis
- `Haldane_floquet_spectrum.png` – Quasi‑energy spectrum along high‑symmetry path for several \(F_0\).
- `Haldane_floquet_eigenenergies.gif` – Instantaneous band surface over one laser cycle.
- `Haldane_floquet_chern.png` – Floquet Chern number \(C_F\) vs \(F_0\) for three \(M\) values.
- `Haldane_floquet_phase_diagram.png` – Phase diagram \(C_F(M, F_0)\) with discrete colormap.
- `Haldane_hall_tracking.png` – Transverse Hall conductance tracking during and after the pulse.

### HHG
- `Haldane_HHG_spectrum.png` – HHG spectrum: longitudinal, transverse, and total (topological vs trivial).
- `Haldane_HHG_circular.png` – Circular components \(J_+\) and \(J_-\) with selection rules.
- `Haldane_HHG_odd_even.png` – Odd/even harmonic decomposition with C₃ suppression of \(3n\) harmonics.

---

## Animations

| GIF | Description |
|-----|-------------|
| `Haldane_dispersion_cycle.gif` | Band structure along \(\Gamma \to K \to M \to K' \to \Gamma\) over one cycle. |
| `Haldane_floquet_eigenenergies.gif` | Instantaneous 3D band surface over one laser cycle. |
| `Eigenvectors.gif` | Eigenstates of the static Haldane model (from Part I). |

---

## Dependencies

All code is written in Python 3.8+ and requires the following libraries:

```bash
pip install numpy matplotlib scipy sympy plotly pillow joblib
```

- **NumPy** – numerical arrays and linear algebra
- **Matplotlib** – plotting and animations
- **SciPy** – special functions and linear algebra
- **SymPy** – symbolic derivation
- **Plotly** – optional for interactive 3D plots
- **Pillow** – saving animations as GIFs
- **Joblib** – parallel computation of phase diagrams

---

## Usage

1. Clone or download the repository.
2. Open the Jupyter notebook (or run the Python script) containing the two parts.
3. Execute the cells sequentially to reproduce all figures and animations.
4. Modify parameters (e.g., \(M, F_0, \phi, \omega\)) at the beginning of each section.

All generated figures and GIFs are saved in the working directory.

---

## Key Differences from QWZ Model

| Feature | QWZ Model | Haldane Model |
|---------|-----------|---------------|
| Lattice | Square | **Honeycomb** (two sublattices, C₃ symmetry) |
| Valleys | None | **K and K'** (Dirac points) |
| NNN hopping | None | \(t_2 e^{i\phi}\) – breaks TR without net flux |
| Symmetry | C₄ | **C₃** – different HHG selection rules |
| Drive effect | Uniform BZ shift | **Valley‑selective** gap control |
| Phase diagram | \((t_0, F_0)\) | \((M/t_2, \phi)\) + drive |
| HHG selection | Both (circular drive) | \(3n\) suppressed; \(J_+\): \(3n+1\), \(J_-\): \(3n+2\) |

---

## References

1. Haldane, F. D. M. (1988). *Model for a quantum Hall effect without Landau levels: Condensed-matter realization of the "parity anomaly"*. Physical Review Letters, 61(18), 2015.
2. Fukui, T., Hatsugai, Y., & Suzuki, H. (2005). *Chern numbers in discretized Brillouin zone*. Journal of the Physical Society of Japan, 74(6), 1674‑1677.
3. Oka, T., & Aoki, H. (2009). *Photovoltaic Hall effect in graphene*. Physical Review B, 79(8), 081406.
4. Fregoso, B. M., & Vampa, G. (2019). *High‑harmonic generation in topological materials*. Physical Review B, 100(4), 041402.
