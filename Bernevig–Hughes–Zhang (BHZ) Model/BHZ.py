import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# Pauli matrices
sigma_0 = np.eye(2, dtype=complex)
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

tau_0 = np.eye(2, dtype=complex)
tau_x = np.array([[0, 1], [1, 0]], dtype=complex)
tau_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
tau_z = np.array([[1, 0], [0, -1]], dtype=complex)

# Map names to tau matrices
tau_dict = {
    "tau_0": tau_0,
    "tau_x": tau_x,
    "tau_y": tau_y,
    "tau_z": tau_z
}


# Tensor product helper
def kron(a, b):
    return np.kron(a, b)


# Build stripe Hamiltonian for given kx, C, and t0
def build_H(kx, Cmat, t0, N=10):
    d = 4  # internal dimension per site
    H = np.zeros((N * d, N * d), dtype=complex)

    onsite = kron(sigma_0, (t0 + np.cos(kx)) * tau_z) \
             + kron(sigma_z, np.sin(kx) * tau_x) \
             + kron(sigma_x, Cmat)

    hop_y = kron(sigma_0, 0.5 * tau_z - 0.5j * tau_y)
    hop_y_dag = hop_y.conj().T

    for i in range(N):
        H[i * d:(i + 1) * d, i * d:(i + 1) * d] = onsite + kron(sigma_0, tau_z)
        if i < N - 1:
            H[i * d:(i + 1) * d, (i + 1) * d:(i + 2) * d] = hop_y
            H[(i + 1) * d:(i + 2) * d, i * d:(i + 1) * d] = hop_y_dag
    return H


# Plotting function
def plot_bands(ax1, ax2, C, t0, C_matrix, kx_index=100):
    kxs = np.linspace(-np.pi, np.pi, 201)
    N = 10
    d = 4
    energies = []
    edge_flags = []
    Cmat = C * tau_dict[C_matrix]

    for kx in kxs:
        H = build_H(kx, Cmat, t0, N)
        evals, evecs = np.linalg.eigh(H)

        # Compute edge localization
        edge_mask = []
        for n in range(len(evals)):
            psi = evecs[:, n].reshape(N, d)
            prob_per_site = np.sum(np.abs(psi)**2, axis=1)
            edge_weight = prob_per_site[0] + prob_per_site[-1]
            edge_mask.append(edge_weight > 0.5)
        energies.append(evals)
        edge_flags.append(edge_mask)

    energies = np.array(energies)
    edge_flags = np.array(edge_flags)

    # --- Band structure subplot ---
    ax1.clear()
    for n in range(energies.shape[1]):
        is_edge = edge_flags[:, n]
        ax1.scatter(kxs[~is_edge], energies[~is_edge, n], color="darkblue", s=2)
        ax1.scatter(kxs[is_edge], energies[is_edge, n], color="red", s=5, label="Edge" if n == 0 else "")
    ax1.set_title(f"Band structure: C={C:.2f}, t0={t0:.2f}, C_matrix={C_matrix}")
    ax1.set_xlabel(r"$k_x$")
    ax1.set_ylabel("Energy")
    ax1.set_xlim(-np.pi, np.pi)

    # --- Spectrum at chosen kx (scatter vs index) ---
    ax2.clear()
    evals = energies[kx_index]
    ax2.scatter(range(len(evals)), evals, color="darkblue", s=10)
    ax2.set_title(f"Eigenvalues at kx={kxs[kx_index]:.2f}")
    ax2.set_xlabel("State index")
    ax2.set_ylabel("Energy")

    plt.draw()


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    plt.subplots_adjust(left=0.25, bottom=0.35)

    # Initial parameters
    C0 = 0.5
    t00 = -1.2
    C_matrix0 = "tau_z"
    kx_index0 = 100

    # Initial plot
    plot_bands(ax1, ax2, C0, t00, C_matrix0, kx_index0)

    # Sliders
    ax_C = plt.axes([0.25, 0.25, 0.65, 0.03])
    ax_t0 = plt.axes([0.25, 0.20, 0.65, 0.03])
    ax_kx = plt.axes([0.25, 0.15, 0.65, 0.03])

    slider_C = Slider(ax_C, 'C', -3, 3, valinit=C0, valstep=0.1)
    slider_t0 = Slider(ax_t0, 't0', -3, 3, valinit=t00, valstep=0.1)
    slider_kx = Slider(ax_kx, 'kx index', 0, 200, valinit=kx_index0, valstep=1)

    # Radio buttons for C_matrix
    ax_radio = plt.axes([0.05, 0.5, 0.15, 0.3])
    radio = RadioButtons(ax_radio, ("tau_0", "tau_x", "tau_y", "tau_z"), active=3)

    def update(val):
        plot_bands(ax1, ax2, slider_C.val, slider_t0.val, radio.value_selected, int(slider_kx.val))

    slider_C.on_changed(update)
    slider_t0.on_changed(update)
    slider_kx.on_changed(update)
    radio.on_clicked(update)

    plt.show()


if __name__ == "__main__":
    main()
