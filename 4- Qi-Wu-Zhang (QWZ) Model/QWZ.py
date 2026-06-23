import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
sigma_I = np.eye(2, dtype=complex)

# --- Helper functions ---
def add_hopping(H, site_i, site_j, matrix):
    """Add hopping (2x2 block) between site_i and site_j in H."""
    si, ei = 2*site_i, 2*(site_i+1)
    sj, ej = 2*site_j, 2*(site_j+1)
    H[si:ei, sj:ej] += matrix
    H[sj:ej, si:ei] += matrix.conj().T  # Hermitian conjugate

def build_Hp(Nx=20, t0=2.0, ky=0.0, mu1=0.0, muN=0.0, h2_1=0.0, h2_N=0.0):
    """Construct Hamiltonian for given parameters"""
    dim = 2 * Nx
    H = np.zeros((dim, dim), dtype=complex)

    # hopping along x
    Mx = (sigma_z + 1j * sigma_x) / 2.0
    for nx in range(Nx - 1):
        add_hopping(H, nx, nx+1, Mx)

    # onsite term
    onsite = np.cos(ky) * sigma_z + np.sin(ky) * sigma_y + t0 * sigma_z
    for nx in range(Nx):
        si, ei = 2*nx, 2*(nx+1)
        H[si:ei, si:ei] += onsite

    # boundary terms
    boundary_left  = (mu1 + h2_1 * np.cos(2*ky)) * sigma_I
    boundary_right = (muN + h2_N * np.cos(2*ky)) * sigma_I
    H[0:2, 0:2] += boundary_left
    last = Nx - 1
    H[2*last:2*(last+1), 2*last:2*(last+1)] += boundary_right
    return H

# --- Band structure calculation ---
def compute_bands(Nx, t0, mu1, muN, h2_1, h2_N, n_ky=100):
    ky_vals = np.linspace(-np.pi, np.pi, n_ky)
    dim = 2 * Nx
    energies = np.zeros((dim, len(ky_vals)))

    for i, ky in enumerate(ky_vals):
        Hp = build_Hp(Nx=Nx, t0=t0, ky=ky, mu1=mu1, muN=muN, h2_1=h2_1, h2_N=h2_N)
        eigvals, _ = np.linalg.eigh(Hp)
        energies[:, i] = np.sort(eigvals)
    return ky_vals, energies

# --- Initial parameters ---
Nx_init = 20
t0_init, mu1_init, muN_init, h2_1_init, h2_N_init = 1.0, 0.0, 0.0, 0.0, 0.0

# Compute initial band structure
ky_vals, energies = compute_bands(Nx_init, t0_init, mu1_init, muN_init, h2_1_init, h2_N_init)

# --- Plot setup ---
fig, ax = plt.subplots(figsize=(8,5))
plt.subplots_adjust(left=0.25, bottom=0.35)

lines = []
for band in range(energies.shape[0]):
    (l,) = ax.plot(ky_vals, energies[band, :], color='darkblue', lw=1)
    lines.append(l)

ax.set_xlabel(r"$k_y$")
ax.set_ylabel("Energy")
ax.set_title(f"QWZ Model Band Structure (Nx={Nx_init})")
ax.grid(True, linestyle=":", alpha=0.6)

# --- Sliders ---
axcolor = 'lightgoldenrodyellow'
ax_t0   = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_mu1  = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
ax_muN  = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_h2_1 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_h2_N = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

s_t0   = Slider(ax_t0,  't0',   -3.0, 3.0, valinit=t0_init)
s_mu1  = Slider(ax_mu1, 'mu1',  -3.0, 3.0, valinit=mu1_init)
s_muN  = Slider(ax_muN, 'muN',  -3.0, 3.0, valinit=muN_init)
s_h2_1 = Slider(ax_h2_1,'h2_1', -3.0, 3.0, valinit=h2_1_init)
s_h2_N = Slider(ax_h2_N,'h2_N', -3.0, 3.0, valinit=h2_N_init)

# --- Update function ---
def update(val):
    t0, mu1, muN, h2_1, h2_N = s_t0.val, s_mu1.val, s_muN.val, s_h2_1.val, s_h2_N.val
    ky_vals, energies = compute_bands(Nx_init, t0, mu1, muN, h2_1, h2_N)

    for band, l in enumerate(lines):
        l.set_ydata(energies[band, :])
    fig.canvas.draw_idle()

# Connect sliders to update function
s_t0.on_changed(update)
s_mu1.on_changed(update)
s_muN.on_changed(update)
s_h2_1.on_changed(update)
s_h2_N.on_changed(update)

plt.show()
