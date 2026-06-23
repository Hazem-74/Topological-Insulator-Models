# Rice‑Mele Model: From Static Topology to Floquet‑Driven High Harmonic Generation

This repository provides a comprehensive computational study of the **Rice‑Mele (RM) model** – a one‑dimensional topological insulator that extends the Su‑Schrieffer‑Heeger (SSH) model by adding a **staggered on‑site potential**. The code is organised in two self‑contained notebooks (or consecutive parts) that progressively build from static topological properties to time‑dependent Floquet engineering and high‑harmonic generation (HHG) spectroscopy.

---

## Overview

The RM model describes spinless fermions on a dimerized chain with staggered hopping amplitudes and an alternating on‑site potential. It is a paradigmatic platform for studying:

- **Zak (Berry) phase** as a continuous topological invariant
- **Polarization** via the modern theory of polarization
- **Broken chiral symmetry** – edge states shift away from zero energy
- **Floquet engineering** – laser‑induced changes in the Zak phase
- **High‑harmonic generation** – even harmonics appear due to broken inversion symmetry

All numerical implementations are provided in Python, with extensive visualisations and animations.

---

## Theoretical Background

### Rice‑Mele Hamiltonian

The tight‑binding Hamiltonian for a finite chain of \(N\) unit cells is

\[
H = t_1 \sum_{n} \left( |n_B\rangle\langle n_A| + \text{h.c.} \right)
  + t_2 \sum_{n} \left( |(n+1)_A\rangle\langle n_B| + \text{h.c.} \right)
  + \Delta \sum_{n} \left( |n_A\rangle\langle n_A| - |n_B\rangle\langle n_B| \right),
\]

where \(t_1\) and \(t_2\) are the intra‑cell and inter‑cell hopping amplitudes, and \(\Delta\) is the staggered on‑site potential.  
With periodic boundary conditions, the bulk Bloch Hamiltonian reads

\[
H(k) = \begin{pmatrix} \Delta & t_1 + t_2 e^{-ik} \\ t_1 + t_2 e^{ik} & -\Delta \end{pmatrix}
      = \mathbf{d}(k)\cdot\boldsymbol{\sigma},
\]

with  
\[
d_x(k) = t_1 + t_2 \cos k,\qquad d_y(k) = -t_2 \sin k,\qquad d_z = \Delta.
\]

The energy dispersion is

\[
E_\pm(k) = \pm \sqrt{t_1^2 + t_2^2 + 2t_1t_2\cos k + \Delta^2}.
\]

The **band gap** is  
\[
\Delta_\text{gap} = 2\sqrt{(t_1-t_2)^2 + \Delta^2},
\]
which closes **only** when \(t_1 = t_2\) **and** \(\Delta = 0\) simultaneously.

### Zak Phase and Polarization

The **Zak phase** (Berry phase across the Brillouin zone) for the lower band is

\[
\gamma = i\int_{-\pi}^{\pi} \langle u_-(k)|\partial_k u_-(k)\rangle\,dk.
\]

In the SSH limit (\(\Delta = 0\)), \(\gamma = \pi\) for the topological phase (\(t_2 > t_1\)) and \(0\) for the trivial phase.  
For \(\Delta \neq 0\), \(\gamma\) varies **continuously** between \(0\) and \(\pi\). The macroscopic polarization is

\[
P = \frac{e}{2\pi}\gamma \pmod{e}.
\]

Thus, the Zak phase determines the quantized (or continuous) electronic polarization.

### Chiral Symmetry Breaking

The staggered potential \(\Delta\) breaks the chiral (sublattice) symmetry present in the SSH model. As a result:

- Zero‑energy edge states (when \(t_2 > t_1\)) are **shifted** to energies \(\pm\Delta\).
- The winding number is no longer integer‑quantised; instead, the Zak phase becomes a continuous invariant.
- **Even harmonics** appear in the HHG spectrum, even in the bulk (not only at edges), because inversion symmetry is broken.

### Floquet Engineering

Under a periodic laser field, the vector potential \(A(t) = -\frac{F_0}{\omega}\cos(\omega t)\) is introduced via the Peierls substitution \(k \to k + A(t)\). The one‑cycle Floquet propagator is

\[
U_F(k) = \mathcal{T}\exp\!\left( -i\int_0^{T} H(k, A(t))\,dt \right),
\]

and its eigenvalues define the **Floquet quasi‑energies** \(\varepsilon\). The **Floquet Zak phase** \(\gamma_F\) is the Berry phase of the lower Floquet eigenstate; it can change continuously with \(F_0\), and jumps at gap‑closing points in the Floquet spectrum – these are **laser‑induced topological transitions**.

### High‑Harmonic Generation

The macroscopic current is

\[
J(t) = \mathrm{Tr}\!\left[ \hat{J}(t)\,\rho(t) \right],
\qquad \hat{J}(t) = -\frac{\partial H(t)}{\partial A}.
\]

The HHG power spectrum is obtained by Fourier transforming \(J(t)\):

\[
S(\Omega) = \left| \int_0^{t_\text{max}} J(t)\,e^{i\Omega t}\,dt \right|^2.
\]

In the RM model, broken inversion symmetry (\(\Delta \neq 0\)) allows **even harmonics** in the bulk, making the even/odd ratio a sensitive probe of the staggered potential and the Zak phase.

---

## Code Structure

The project is split into two Jupyter notebooks (or consecutive sections in a single script):

### Part 1 – Rice‑Mele Model I (Static Properties)
- Construction of the real‑space Hamiltonian with staggered potential
- Energy spectrum and edge‑state localization (with \(\Delta \neq 0\), edge states shift to \(\pm\Delta\))
- Animated eigenstates (probability density) for all eigenstates
- “Spaghetti” plots: spectrum vs \(t_1\), vs \(t_2\), vs \(\Delta\)
- **Polarization calculation** via the Zak phase (Berry phase) for the SSH limit
- \(\mathbf{d}(k)\)‑vector in 3D (since \(d_z = \Delta\))

### Part 2 – Rice‑Mele Model II (Floquet & HHG)
- Symbolic derivation (SymPy) of Hamiltonian, eigenvectors, current operator
- \(\mathbf{d}(k)\)‑loop animation over one laser cycle (2D projection and 3D)
- Dispersion vs staggered potential \(\Delta\) and 2D colormap
- Floquet propagator via 4th‑order Runge–Kutta
- Quasi‑energy spectrum vs drive amplitude \(F_0\)
- **Floquet Zak phase** and polarization vs \(F_0\)
- Phase diagram of \(\gamma_F\) in the \((t_1/t_2, F_0)\) plane
- Time‑dependent current from coherent density‑matrix evolution
- HHG power spectra with gap‑order markers
- Odd/even harmonic decomposition; even/odd ratio vs \(F_0\)

### Key Functions

| Function | Description |
|----------|-------------|
| `build_H_RM(t1, t2, A, Δ)` | Real‑space RM Hamiltonian for a given vector potential \(A\) |
| `build_J_RM(t1, t2, A)` | Current operator \(\hat{J} = -\partial H/\partial A\) |
| `dispersion_RM(t1, t2, A, Δ, k)` | Analytical band \(E_+(k) = \sqrt{t_1^2+t_2^2+2t_1t_2\cos(k+A)+\Delta^2}\) |
| `zak_phase(t1/t2, t2, A, Δ)` | Computes the static Zak phase \(\gamma\) |
| `floquet_propagator_batch_RM()` | One‑cycle Floquet propagator \(U_F(k)\) for all \(k\) |
| `floquet_zak_phase_RM()` | Computes the Floquet Zak phase \(\gamma_F\) |
| `time_evolve_RM()` | RK4 time evolution of the density matrix; returns \(J(t)\) |
| `compute_hhg()` | HHG power spectrum from the time‑dependent current |

---

## Parameters (Notebook II Defaults)

| Parameter | Value | Meaning |
|-----------|-------|---------|
| \(t_1, t_2\) (topological) | 0.6, 1.0 | \(t_2 > t_1\) → topological SSH limit |
| \(t_1, t_2\) (trivial) | 1.0, 0.5 | \(t_1 > t_2\) → trivial SSH limit |
| \(\Delta\) | 0.3 | Staggered on‑site potential |
| \(\omega\) | 1.5 | Drive frequency |
| \(F_0\) | 2.5 | Drive amplitude |
| \(n_\text{cyc}\) | 8 | Number of laser cycles |
| \(N\) | 50 | Number of unit cells |

---

## Results and Visualisations

The code produces a wealth of plots and animated GIFs. Below is a selection of key outputs.

### Static Band Structure and Edge States

- `RM_dvector.png` – \(\mathbf{d}(k)\)‑vector in 2D projection and 3D (lifted by \(\Delta\)); gap vs \(\Delta\).
- Energy spectrum for open chain: edge states appear at \(\pm\Delta\) (not zero).
- `RM_Eigenvectors.gif` – Probability density of all eigenstates, showing edge localisation shifted from zero.
- Spaghetti plots: spectrum vs \(t_1\), \(t_2\), \(\Delta\).

### Polarization and Zak Phase

- Polarization vs \(\Delta t\) for SSH limit (from Berry phase).
- `RM_zak_vs_Delta.png` – Zak phase \(\gamma/\pi\) vs \(\Delta\) for topological and trivial limits.
- `RM_zak_phase_diagram.png` – Full phase diagram of \(\gamma\) in the \((t_1/t_2, \Delta)\) plane.

### Dispersion and \(\mathbf{d}\)-Vector Animations

- `RM_dvector_cycle.gif` – \(\mathbf{d}(k)\) loop over one laser cycle (2D projection).
- `RM_dispersion_vs_Delta.png` – Dispersion \(E_\pm(k)\) for different \(\Delta\) values.
- `RM_dispersion_map.png` – 2D colormap of \(E_+(k,\Delta)\).
- `RM_dispersion_cycle.gif` – Instantaneous dispersion over one laser cycle, showing gap minimum shift.

### Floquet Analysis

- `RM_floquet_spectrum.png` – Quasi‑energy spectrum vs \(F_0\) (navy = topological, red = trivial).
- `RM_floquet_gap.png` – Minimum Floquet gap vs \(F_0\); gap‑closing points indicate transitions.
- `RM_eigenenergy_cycle.gif` – Instantaneous eigenenergy spectrum over one cycle, highlighting shifted edge states.
- `RM_floquet_spectrum_vs_index.gif` – Full quasi‑energy spectrum vs eigenstate index as \(F_0\) ramps.
- `RM_floquet_gap_tracking.gif` – Quasi‑energy bands vs \(k\) as \(F_0\) ramps; gap closings visible.

### Floquet Zak Phase and Phase Diagrams

- `RM_floquet_zak_1d.png` – Floquet Zak phase \(\gamma_F/\pi\) vs \(F_0\).
- `RM_floquet_polarization_1d.png` – Polarization \(P = \gamma_F/(2\pi)\) vs \(F_0\).
- `RM_floquet_zak_phasediagram.png` – Phase diagram of \(\gamma_F\) in the \((t_1/t_2, F_0)\) plane with \(\gamma_F = \pm\pi/2\) contours.

### High‑Harmonic Generation

- `RM_HHG_current.png` – Time‑dependent current for topological and trivial phases.
- `RM_HHG_spectra.png` – HHG power spectra (topological and trivial side‑by‑side) with gap‑order markers.
- `RM_odd_even_spectra.png` – Odd/even harmonic bar charts.
- `RM_even_odd_ratio.png` – Even/odd ratio \(R\) vs \(F_0\), with vertical lines marking Floquet gap‑closing points.

---

## Animations

| GIF | Description |
|-----|-------------|
| `RM_Eigenvectors.gif` | Probability density of eigenstates for RM chain (N=20), showing edge states at \(\pm\Delta\). |
| `RM_dvector_cycle.gif` | \(\mathbf{d}(k)\) loop over one laser cycle (2D projection). |
| `RM_dispersion_cycle.gif` | Instantaneous dispersion \(E_\pm(k, A(t))\) over one cycle. |
| `RM_eigenenergy_cycle.gif` | Real‑space eigenenergy spectrum over one cycle (shifted edge states highlighted). |
| `RM_floquet_gap_tracking.gif` | Quasi‑energy bands vs \(k\) as \(F_0\) ramps, showing gap closings. |
| `RM_floquet_spectrum_vs_index.gif` | Full quasi‑energy spectrum vs eigenstate index as \(F_0\) varies. |

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
2. Open the Jupyter notebook (or run the Python script) containing both parts.
3. Execute the cells sequentially to reproduce all figures and animations.
4. To customise parameters, modify the variables at the top of each section (e.g., \(t_1, t_2, \Delta, F_0, \omega\)).

All generated figures and GIFs are saved in the working directory.

---

## Key Differences from SSH Model

| Feature | SSH Model | Rice‑Mele Model |
|---------|-----------|-----------------|
| Staggered potential | \(\Delta = 0\) | \(\Delta \neq 0\) |
| Chiral symmetry | Present | Broken |
| Edge states | Exactly zero energy | Shifted to \(\pm\Delta\) |
| Topological invariant | Winding number (integer) | Zak phase (continuous) |
| Bulk inversion symmetry | Present | Broken (if \(\Delta \neq 0\)) |
| HHG even harmonics | Only from edges | Present in bulk |
| Gap closing | \(t_1 = t_2\) | \(t_1 = t_2\) **and** \(\Delta = 0\) |

---

## References

1. Rice, M. J., & Mele, E. J. (1982). *Elementary excitations of a linearly conjugated diatomic polymer*. Physical Review Letters, 49(19), 1455.
2. Zak, J. (1989). *Berry's phase for energy bands in solids*. Physical Review Letters, 62(23), 2747.
3. Vanderbilt, D. (2018). *Berry Phases in Electronic Structure Theory*. Cambridge University Press.
4. Fregoso, B. M., & Vampa, G. (2019). *High‑harmonic generation in topological materials*. Physical Review B, 100(4), 041402.
