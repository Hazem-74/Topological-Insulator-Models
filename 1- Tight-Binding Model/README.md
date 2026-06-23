## Overview

This project provides a comprehensive numerical exploration of electronic band structures in crystalline solids using the tight-binding approximation. The implementation covers both 1D and 3D lattice models, with detailed derivations and visualizations of key concepts in solid-state physics.

## Contents

### 1. Band Structure and Periodic Potential

The project begins by establishing the foundation of band theory, demonstrating how a periodic potential transforms discrete atomic energy levels into continuous energy bands. Key concepts covered include:

- **Bloch's Theorem**: Solutions to the Schrödinger equation in a periodic potential satisfy ψ(x + a) = e^(iqa)ψ(x)
- **Dirac Comb Potential**: A model potential consisting of delta functions at lattice sites, leading to the dispersion relation:
  
  ```
  cos(qa) = cos(ka) + (mα/(ħ²k)) sin(ka)
  ```

- **Energy Bands and Gaps**: The transcendental equation reveals allowed energy bands where |f(z)| ≤ 1, separated by band gaps

![Band Structure Simulation](band_structure_simulation.png)

### 2. Tight-Binding Model in 1D

The tight-binding model discretizes space, restricting electrons to atomic positions with quantum tunneling between neighboring sites.

#### Periodic Boundary Conditions (PBC)

Hamiltonian:
```
H = E₀ Σ|n⟩⟨n| - t Σ(|n⟩⟨n+1| + |n+1⟩⟨n|)
```

Energy dispersion:
```
E(k) = E₀ - 2t cos(ka)
```

The eigenstates are plane waves ψₙ = e^(ikna), with k quantized as k = 2πm/(Na).

#### Open Boundary Conditions (OBC)

For finite chains without wrap-around, eigenstates become standing waves:
```
ψₙ^(m) = √(2/(N+1)) sin(kₘna)
```
where kₘ = mπ/((N+1)a), m = 1, 2, ..., N.

![Tight-Binding 1D Comparison](tb_1d_comparison.png)

### 3. Tight-Binding Model in 3D

Extension to three dimensions reveals richer band structures and Fermi surface topologies.

#### Simple Cubic Lattice

Dispersion relation:
```
E(k) = E₀ - 2t[cos(kₓa) + cos(kᵧa) + cos(k_z a)]
```

**Effective Mass**: Near the band bottom (k ≈ 0):
```
m* = ħ²/(2ta²)
```

#### Key Visualizations

- **3D Energy Surfaces**: Visual representation of the band structure in the Brillouin zone
- **Contour Plots**: Constant-energy contours revealing the symmetry of the lattice
- **Fermi Surface**: The surface in k-space separating occupied from unoccupied states

![3D Dispersion Surface](3d_dispersion.png)

### 4. Density of States (DOS)

The DOS counts the number of electronic states per unit energy interval:
```
D(E) = (1/(2π)ᵈ) ∫_{BZ} dᵈk δ(E - E(k))
```

Two numerical methods are implemented:
- **Histogram Binning**: Direct counting of energy states
- **Kernel Density Estimation (KDE)**: Smooth estimation using Gaussian kernels

![DOS Comparison](dos_comparison.png)

### 5. Linear Combination of Atomic Orbitals (LCAO)

A first-principles derivation of the tight-binding model, starting from atomic orbitals and treating the lattice potential as a perturbation.

**Key Integrals**:
- Overlap integral: α(r) = ∫ φ*(x - r) φ(x) d³x
- Hopping integral: γ(r) = ∫ φ*(x - r) ΔV(x) φ(x) d³x

The resulting dispersion:
```
E(k) = ε + Δε + 2Σₐ cos(k·a)[γ(a) - Δε·α(a)]
```

### 6. FCC Lattice Application

The tight-binding model is applied to the face-centered cubic (FCC) lattice, which has 12 nearest neighbors at positions:
```
R = (a/2)(±1, ±1, 0), (a/2)(±1, 0, ±1), (a/2)(0, ±1, ±1)
```

Dispersion for s-orbitals:
```
ε(k) = Eₛ - β - 4γ[cos(kₓa/2)cos(kᵧa/2) + cos(kᵧa/2)cos(k_za/2) + cos(k_za/2)cos(kₓa/2)]
```

![FCC Fermi Surface](fcc_fermi_surface.png)

### 7. Bloch and Wannier Functions

**Bloch Functions**: Delocalized, momentum-space eigenstates satisfying:
```
ψ_{nk}(r) = e^(ik·r) u_{nk}(r)
```

**Wannier Functions**: Localized, real-space counterparts:
```
wₙ(r - R) = (1/√N) Σ_k e^(-ik·R) ψ_{nk}(r)
```

An animated visualization demonstrates the Fourier duality between these representations.

![Bloch-Wannier Animation](bloch_wannier.gif)

## Code Implementation

### Key Functions

```python
# 1D Tight-Binding Dispersion
def dispersion_1D(k, t=1.0, a=1.0, E0=0.0):
    return E0 - 2 * t * np.cos(k * a)

# 3D Simple Cubic Dispersion
def dispersion_SC(kx, ky, kz, t=1.0, a=1.0, E0=0.0):
    return E0 - 2 * t * (np.cos(kx*a) + np.cos(ky*a) + np.cos(kz*a))

# FCC Dispersion
def fcc_dispersion(kx, ky, kz, a=1.0, gamma=1.0, Es=0.0, beta=0.0):
    term1 = np.cos(kx*a/2) * np.cos(ky*a/2)
    term2 = np.cos(ky*a/2) * np.cos(kz*a/2)
    term3 = np.cos(kz*a/2) * np.cos(kx*a/2)
    return Es - beta - 4 * gamma * (term1 + term2 + term3)
```

### Hamiltonian Construction

**Periodic Boundary Conditions**:
```python
H = np.zeros((N, N), dtype=np.complex128)
for n in range(N):
    H[n, n] = E0
    H[n, (n+1) % N] = -t
    H[(n+1) % N, n] = -t
```

**Open Boundary Conditions**:
```python
H = np.zeros((N, N), dtype=np.complex128)
for n in range(N):
    H[n, n] = E0
    if n < N-1:
        H[n, n+1] = -t
        H[n+1, n] = -t
```

### Fermi Surface Extraction

```python
# Find k-points where energy equals Fermi energy
fermi_tol = 0.06
fermi_mask = np.abs(E_3D - E_fermi) < fermi_tol
kx_fs = KX[fermi_mask]
ky_fs = KY[fermi_mask]
kz_fs = KZ[fermi_mask]
```

### Density of States Calculation

```python
from scipy.stats import gaussian_kde

# Histogram method
E_hist, bins = np.histogram(E_flat, bins=n_bins, density=True)
E_centers = 0.5 * (bins[:-1] + bins[1:])

# KDE method
kde = gaussian_kde(E_flat)
E_kde_range = np.linspace(E_flat.min(), E_flat.max(), 1000)
DOS_kde = kde(E_kde_range)
```

## Visualization Features

1. **2D/3D Dispersion Plots**: Energy surfaces in momentum space
2. **Contour Maps**: Constant-energy contours showing band structure symmetry
3. **Fermi Surface Visualizations**: Interactive 3D scatter plots (Plotly)
4. **Density of States**: Histogram and KDE methods
5. **Bloch-Wannier Animation**: Time-dependent visualization of Fourier duality

## Interactive Features

- **3D Rotatable Fermi Surfaces**: Using Plotly for interactive exploration
- **HTML Export**: Fermi surface plots can be saved as standalone HTML files
- **Animation**: GIF generation showing Bloch function evolution

## Requirements

```
numpy
matplotlib
scipy
plotly
```

## Key Physical Insights

1. **Delocalization**: Even infinitesimal hopping fully delocalizes eigenstates across the lattice
2. **Effective Mass**: Lattice structure gives rise to effective mass m* = ħ²/(2ta²)
3. **Band Formation**: Periodic potential splits discrete levels into continuous bands
4. **Fermi Surface Topology**: Reflects underlying lattice symmetry
5. **Bloch-Wannier Duality**: Momentum localization ↔ spatial delocalization

## References

- Griffiths, D.J. "Introduction to Quantum Mechanics"
- Ashcroft, N.W. & Mermin, N.D. "Solid State Physics"
- The theoretical framework follows standard tight-binding model derivations

## Output Files

The code generates several visual outputs:
- `band_structure_simulation.png`
- `tb_1d_comparison.png`
- `3d_dispersion.png`
- `dos_comparison.png`
- `fcc_fermi_surface.png`
- `bloch_wannier.gif`
- `SC_fermi_surface_interactive.html`
- `FCC_fermi_surface_interactive.html`
