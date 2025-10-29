import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ==============================
# Pauli matrices
# ==============================
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
sigma_I = np.eye(2, dtype=complex)

# ==============================
# Single-layer QWZ Hamiltonian
# ==============================
def H_layer(kx, ky, t0):
    return (
        np.cos(kx) * sigma_x
        + np.cos(ky) * sigma_y
        + (t0 + np.cos(kx) + np.cos(ky)) * sigma_z
    )

# ==============================
# Multilayer QWZ Hamiltonian
# ==============================
def multilayer_QWZ(D, C, kx, ky, t0):
    dim = 2 * D
    H = np.zeros((dim, dim), dtype=complex)

    for d in range(D):
        # Diagonal block
        H[2*d:2*d+2, 2*d:2*d+2] = H_layer(kx, ky, t0)

        # Coupling to nearest layer
        if d < D - 1:
            H[2*d:2*d+2, 2*(d+1):2*(d+1)+2] = C * sigma_I
            H[2*(d+1):2*(d+1)+2, 2*d:2*d+2] = C * sigma_I
    return H

# ==============================
# Compute band structure along ky (kx=0 fixed)
# ==============================
def compute_bands(D, C, t0, nk=200):
    ky_vals = np.linspace(-np.pi, np.pi, nk)
    bands = []
    for ky in ky_vals:
        H = multilayer_QWZ(D, C, 0.0, ky, t0)  # <-- kx fixed at 0
        eigvals = np.linalg.eigvalsh(H)  # Hermitian eigenvalues
        bands.append(eigvals)
    return ky_vals, np.array(bands)

# ==============================
# Initial parameters
# ==============================
D_init = 3
t0_init = 1.0
C_init = 0.5

ky_vals, bands = compute_bands(D_init, C_init, t0_init)

# ==============================
# Plot setup
# ==============================
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)

lines = []
for i in range(bands.shape[1]):
    line, = ax.plot(ky_vals, bands[:, i], lw=2)
    lines.append(line)

ax.set_xlabel(r"$k_y$")
ax.set_ylabel("Energy")
ax.set_title("Multilayer QWZ Band Structure vs $k_y$")
ax.grid(True)

# ==============================
# Sliders
# ==============================
axcolor = 'lightgoldenrodyellow'
ax_t0 = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_C  = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)

s_t0 = Slider(ax_t0, r"$t_0$", -3.0, 3.0, valinit=t0_init)
s_C  = Slider(ax_C,  "C", -2.0, 2.0, valinit=C_init)

# ==============================
# Update function
# ==============================
def update(val):
    t0 = s_t0.val
    C = s_C.val
    ky_vals, bands = compute_bands(D_init, C, t0)
    for i, line in enumerate(lines):
        line.set_ydata(bands[:, i])
    fig.canvas.draw_idle()

s_t0.on_changed(update)
s_C.on_changed(update)

plt.show()
