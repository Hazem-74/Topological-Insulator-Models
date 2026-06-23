# Topological Insulator Models
### Undergraduate Thesis — Numerical Exploration of Topological Phases in Condensed Matter Physics

> **Zewail City of Science and Technology**

This repository contains the complete numerical implementation for my undergraduate thesis, which progressively builds from the foundations of band theory through a series of topological lattice models. Each module is self-contained and combines detailed theoretical derivations with computational simulations, visualisations, and animations — all written in Python.

---

## Project Description

Topological insulators are quantum materials that are insulating in the bulk but host symmetry-protected conducting states at their boundaries. These edge (or surface) states are robust against disorder and imperfections, making them fundamentally different from ordinary band insulators. The classification of these phases relies on topological invariants — integers or binary numbers derived from the global geometry of the electronic wavefunctions across the Brillouin zone.

This project provides a step-by-step computational journey through the key models that shaped our modern understanding of topological matter:

- Starting from the **tight-binding approximation** and Bloch's theorem, we establish how periodic lattices give rise to energy bands.
- The **SSH model** introduces the simplest topological invariant (winding number) and edge states in 1D.
- The **Rice-Mele model** generalises the SSH model with a staggered on-site potential, connecting topology to electronic polarisation via the Zak phase.
- The **QWZ model** extends the concept to 2D, realising a Chern insulator with a quantised Hall response and no external magnetic field.
- The **BHZ model** incorporates spin and time-reversal symmetry, realising the quantum spin Hall effect and the ℤ₂ topological invariant in 2D.
- The **Haldane model** demonstrates that complex next-nearest-neighbour hopping on the honeycomb lattice can produce a Chern insulator with C₃ symmetry.
- The **Kane-Mele model** combines two copies of the Haldane model with spin-orbit coupling to produce a time-reversal-invariant topological insulator on graphene.

For each model beyond the tight-binding foundations, the study extends to **Floquet engineering** (laser-driven topological phase transitions) and **high-harmonic generation (HHG)** spectroscopy as a probe of topological order.

---

## Repository Structure

```
.
├── 1- Tight-Binding Model/
│   ├── Band Structure.ipynb          # Bloch theorem, Dirac comb, band gaps
│   ├── Tight-Binding in 1D.ipynb     # PBC and OBC chains, DOS, Wannier functions
│   ├── Tight-Binding in 3D.ipynb     # Simple cubic, FCC dispersion, Fermi surfaces
│   └── Tight Binding LCOA.ipynb      # First-principles LCAO derivation
│
├── 2- Su-Schrieffer-Heeger (SSH) Model/
│   ├── SSH_I.ipynb                   # Static topology, winding number, edge states
│   ├── SSH_II.ipynb                  # Chiral symmetry, domain walls, localisation
│   └── SSH_III.ipynb                 # Floquet engineering and HHG spectroscopy
│
├── 3- Rice-Mele Model/
│   ├── Rice-Mele_I.ipynb             # Staggered potential, Zak phase, polarisation
│   └── Rice_Mele_II.ipynb            # Floquet Zak phase, HHG with even harmonics
│
├── 4- Qi-Wu-Zhang (QWZ) Model/
│   ├── QWZ_I.ipynb                   # Chern number, edge states, strip geometry
│   ├── QWZ_II.ipynb                  # Floquet Chern number, circular HHG
│   ├── QWZ.py                        # Core model functions
│   └── QWZ_multi.py                  # Parallelised phase diagram computation
│
├── 5- Bernevig–Hughes–Zhang (BHZ) Model/
│   ├── TRS.ipynb                     # Time-reversal symmetry, Kramers degeneracy, ℤ₂
│   └── BHZ.ipynb                     # BHZ Hamiltonian, QSH effect, coupled layers
│
├── 6- Haldane Model/
│   ├── Haldane_I.ipynb               # Honeycomb lattice, Chern number, phase diagram
│   ├── Haldane_II.ipynb              # Floquet phases, valley-selective transitions, HHG
│   └── Haldane Script.py             # Standalone model functions
│
├── 7- Kane-Mele Model/
│   └── Kane-Mele Model.ipynb         # Spin-orbit coupling, helical edges, ℤ₂ invariant
│
└── Writings/
    ├── Thesis.pdf                    # Full undergraduate thesis
    ├── Presentation.pdf              # Defence presentation slides
    ├── Thesis.zip                    # LaTeX source
    └── Beamer.zip                    # Beamer presentation source
```

---

## Models at a Glance

| Module | Dimension | Key Invariant | Physics |
|--------|-----------|---------------|---------|
| Tight-Binding | 1D / 3D | — | Band formation, Fermi surfaces, DOS |
| SSH | 1D | Winding number ℤ | Chiral symmetry, edge states, Floquet HHG |
| Rice-Mele | 1D | Zak phase (continuous) | Polarisation, broken chiral symmetry, even HHG |
| QWZ | 2D | Chern number ℤ | Anomalous Hall effect, chiral edge states |
| BHZ | 2D | ℤ₂ | Quantum spin Hall effect, Kramers pairs |
| Haldane | 2D | Chern number ℤ | Honeycomb, C₃ symmetry, valley-selective Floquet |
| Kane-Mele | 2D | ℤ₂ | Spin-orbit coupling, helical edges, graphene |

---

## Key Themes

### Topological Invariants
Each model is characterised by a topological invariant that cannot change without closing the bulk energy gap:
- **Winding number** (SSH): counts how many times the **d**(*k*) vector winds around the origin as *k* traverses the Brillouin zone.
- **Chern number** (QWZ, Haldane): the integral of Berry curvature over the 2D Brillouin zone; governs the quantised Hall conductance.
- **Zak phase** (Rice-Mele): the 1D Berry phase; determines electronic polarisation.
- **ℤ₂ invariant** (BHZ, Kane-Mele): a parity invariant protected by time-reversal symmetry; classifies quantum spin Hall insulators.

### Bulk-Boundary Correspondence
All topological models exhibit a direct link between the bulk invariant and the number of protected boundary modes: chiral edge states for broken time-reversal (Chern insulators), or helical edge states for time-reversal-invariant insulators (QSH).

### Floquet Engineering
Applying a periodic laser field (via the Peierls substitution **k** → **k** + **A**(*t*)) can drive the system through topological phase transitions not accessible in equilibrium. The Floquet quasi-energy spectrum and Floquet topological invariants are computed for SSH, Rice-Mele, QWZ, and Haldane models.

### High-Harmonic Generation (HHG) as a Topological Probe
The macroscopic current is computed from coherent density-matrix evolution under the laser field. Its Fourier spectrum (the HHG spectrum) encodes topological information:
- **Odd harmonics only** → bulk inversion symmetry present (SSH).
- **Even harmonics appear** → inversion broken (Rice-Mele, Haldane with *M* ≠ 0).
- **Circular components** *J*± → C₃ selection rules (Haldane, QWZ with circular drive).
- **Even/odd ratio vs F₀** → tracks Floquet topological transitions.

---

## Installation

All code is written in **Python 3.8+**. Install dependencies with:

```bash
pip install numpy matplotlib scipy sympy plotly pillow joblib pfapack
```

| Library | Purpose |
|---------|---------|
| `numpy` | Arrays and linear algebra |
| `matplotlib` | Plotting and GIF animations |
| `scipy` | `eigh`, `expm`, KDE, special functions |
| `sympy` | Symbolic Hamiltonian and current operator derivation |
| `plotly` | Interactive 3D Fermi surface plots |
| `pillow` | Saving animations as GIFs |
| `joblib` | Parallel phase diagram computation |
| `pfapack` | Pfaffian for Kane-Mele ℤ₂ invariant |

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Hazem-74/Topological-Insulator-Models.git
   cd Topological-Insulator-Models
   ```

2. Navigate into any module directory and launch Jupyter:
   ```bash
   cd "2- Su-Schrieffer-Heeger (SSH) Model"
   jupyter notebook
   ```

3. Run notebooks sequentially (Parts I → II → III where applicable). Parameters are defined at the top of each section for easy customisation.

4. All generated figures and GIF animations are saved to the working directory.

---

## Writings

The `Writings/` folder contains the full thesis and defence presentation. The thesis covers the theoretical background for all seven models, the numerical methods employed, and a discussion of results — including band structures, topological phase diagrams, Floquet quasi-energy spectra, and HHG signatures of topology.

---

## References

1. Griffiths, D. J. *Introduction to Quantum Mechanics*. Cambridge University Press.
2. Ashcroft, N. W. & Mermin, N. D. *Solid State Physics*. Holt, Rinehart and Winston.
3. Asbóth, J. K., Oroszlány, L. & Pályi, A. *A Short Course on Topological Insulators*. Lecture Notes in Physics, 919 (2016).
4. Su, W. P., Schrieffer, J. R. & Heeger, A. J. *Solitons in polyacetylene*. Phys. Rev. Lett. **42**, 1698 (1979).
5. Rice, M. J. & Mele, E. J. *Elementary excitations of a linearly conjugated diatomic polymer*. Phys. Rev. Lett. **49**, 1455 (1982).
6. Qi, X.-L., Wu, Y.-S. & Zhang, S.-C. *Topological quantization of the spin Hall effect in two-dimensional insulating systems*. Phys. Rev. B **74**, 085308 (2006).
7. Haldane, F. D. M. *Model for a quantum Hall effect without Landau levels*. Phys. Rev. Lett. **61**, 2015 (1988).
8. Kane, C. L. & Mele, E. J. *Quantum spin Hall effect in graphene*. Phys. Rev. Lett. **95**, 226801 (2005).
9. Oka, T. & Aoki, H. *Photovoltaic Hall effect in graphene*. Phys. Rev. B **79**, 081406 (2009).
10. Fukui, T., Hatsugai, Y. & Suzuki, H. *Chern numbers in discretized Brillouin zone*. J. Phys. Soc. Jpn. **74**, 1674 (2005).
11. Vanderbilt, D. *Berry Phases in Electronic Structure Theory*. Cambridge University Press (2018).
```
