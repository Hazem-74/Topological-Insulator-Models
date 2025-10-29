#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- Parameters ---
t1_init = 1.0
t2_init = 0.3
t0_init = 0.2
phi_init = np.pi/2
N_x_init = 40

Nk = 100
k_vals = np.linspace(-np.pi, np.pi, Nk)
phi_vals_raw = np.linspace(0, 2, 60)
t0_vals = np.linspace(0.0, 1.0, 50)
t1_vals = np.linspace(0.0, 2.0, 50)
t2_vals = np.linspace(0.0, 0.6, 50)

# --- Build Haldane Ribbon ---
def build_haldane_ribbon(k_y, t1=1.0, t2=0.1, t0=0.3, phi=np.pi/2, N_x=30):
    def index(x, sublattice):
        return 2*x + sublattice  

    N_sites = 2 * N_x
    H = np.zeros((N_sites, N_sites), dtype=complex)

    for x in range(N_x):
        iA = index(x, 0)
        iB = index(x, 1)

        # On-site potential
        H[iA, iA] += t0 / 2
        H[iB, iB] -= t0 / 2

        # NN Hopping
        H[iA, iB] += -t1
        H[iB, iA] += -t1
        if x > 0:
            jB = index(x-1, 1)
            H[iA, jB] += -t1 * np.exp(-1j * k_y)
            H[jB, iA] += -t1 * np.exp(1j * k_y)
            H[iA, jB] += -t1
            H[jB, iA] += -t1

        # NNN Hopping
        if x < N_x-1:
            jA = index(x+1, 0)
            H[iA, jA] += -t2 * np.exp(1j * phi)
            H[jA, iA] += -t2 * np.exp(-1j * phi)
            jB = index(x+1, 1)
            H[iB, jB] += -t2 * np.exp(1j * phi)
            H[jB, iB] += -t2 * np.exp(-1j * phi)
        if x > 0:
            jA = index(x-1, 0)
            H[iA, jA] += -t2 * np.exp(-1j * phi)
            H[jA, iA] += -t2 * np.exp(1j * phi)
            jB = index(x-1, 1)
            H[iB, jB] += -t2 * np.exp(-1j * phi)
            H[jB, iB] += -t2 * np.exp(1j * phi)

    return H


# --- Function to compute bands ---
def compute_bands(param, sweep_vals, sweep_name, k_y=0.0, N_x=N_x_init):
    all_energies = []
    for val in sweep_vals:
        kwargs = dict(t1=t1_init, t2=t2_init, t0=t0_init, phi=phi_init, N_x=N_x)
        kwargs[sweep_name] = val
        H = build_haldane_ribbon(k_y, **kwargs)
        evals = np.linalg.eigvalsh(H)
        all_energies.append(np.sort(evals))
    return np.array(all_energies)


# --- Plot ---
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25, hspace=0.4)

(ax1, ax2, ax3), (ax4, ax5, _) = axes

def update(val):
    t1 = s_t1.val
    t2 = s_t2.val
    t0 = s_t0.val
    phi = s_phi.val
    N_x = int(s_Nx.val)

    # Band structure vs ky
    bands = []
    for ky in k_vals:
        H = build_haldane_ribbon(ky, t1=t1, t2=t2, t0=t0, phi=phi, N_x=N_x)
        eigvals = np.linalg.eigvalsh(H)
        bands.append(eigvals)
    bands = np.array(bands)

    ax1.clear()
    for n in range(bands.shape[1]):
        ax1.plot(k_vals, bands[:, n], 'b-', lw=0.5, alpha=0.8)
    ax1.axhline(0, color='k', linestyle='--', alpha=0.6)
    ax1.set_title(r'$E$ vs $k_y$')
    ax1.set_xlabel(r'$k_y$')
    ax1.set_ylabel(r'$E$')

    # t0 sweep
    all_energies = compute_bands(t0, t0_vals, 't0', N_x=N_x)
    ax2.clear()
    for i in range(all_energies.shape[1]):
        ax2.plot(t0_vals, all_energies[:, i], 'b-', lw=0.5, alpha=0.8)
    ax2.set_title(r'$E$ vs $t_0$')
    ax2.set_xlabel(r'$t_0$')

    # t1 sweep
    all_energies = compute_bands(t1, t1_vals, 't1', N_x=N_x)
    ax3.clear()
    for i in range(all_energies.shape[1]):
        ax3.plot(t1_vals, all_energies[:, i], 'b-', lw=0.5, alpha=0.8)
    ax3.set_title(r'$E$ vs $t_1$')
    ax3.set_xlabel(r'$t_1$')

    # t2 sweep
    all_energies = compute_bands(t2, t2_vals, 't2', N_x=N_x)
    ax4.clear()
    for i in range(all_energies.shape[1]):
        ax4.plot(t2_vals, all_energies[:, i], 'b-', lw=0.5, alpha=0.8)
    ax4.set_title(r'$E$ vs $t_2$')
    ax4.set_xlabel(r'$t_2$')

    # phi sweep
    all_energies = compute_bands(phi, phi_vals_raw*np.pi, 'phi', N_x=N_x)
    ax5.clear()
    for i in range(all_energies.shape[1]):
        ax5.plot(phi_vals_raw, all_energies[:, i], 'b-', lw=0.5, alpha=0.8)
    ax5.set_title(r'$E$ vs $\phi$')
    ax5.set_xlabel(r'$\phi/\pi$')
    ax5.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
    ax5.set_xticklabels([r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])

    fig.canvas.draw_idle()


# --- Sliders ---
axcolor = 'lightgoldenrodyellow'
ax_t1  = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_t2  = plt.axes([0.1, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_t0  = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_phi = plt.axes([0.1, 0.00, 0.65, 0.03], facecolor=axcolor)
ax_Nx  = plt.axes([0.8, 0.05, 0.1, 0.03], facecolor=axcolor)

s_t1  = Slider(ax_t1,  r'$t_1$', 0.0, 2.0, valinit=t1_init)
s_t2  = Slider(ax_t2,  r'$t_2$', 0.0, 0.6, valinit=t2_init)
s_t0  = Slider(ax_t0,  r'$t_0$', 0.0, 1.0, valinit=t0_init)
s_phi = Slider(ax_phi, r'$\phi$', 0, 2*np.pi, valinit=phi_init)
s_Nx  = Slider(ax_Nx,  r'$N_x$', 10, 60, valinit=N_x_init, valstep=1)

for slider in [s_t1, s_t2, s_t0, s_phi, s_Nx]:
    slider.on_changed(update)

update(None)  # Initial plot
plt.show()

