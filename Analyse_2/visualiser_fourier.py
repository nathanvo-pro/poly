import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def fourier_carree(x, N):
    """Série de Fourier de l'onde carrée (-1/2 sur ]-pi, 0[, 1/2 sur ]0, pi[)"""
    y = np.zeros_like(x)
    for n in range(1, 2 * N, 2):  # Seulement les harmoniques impaires (1, 3, 5...)
        y += (2 / (np.pi * n)) * np.sin(n * x)
    return y

def fourier_triangulaire(x, N):
    """Série de Fourier de l'onde triangulaire (|x| sur [-pi, pi])"""
    y = np.full_like(x, np.pi / 2)  # Terme constant a0/2
    for n in range(1, 2 * N, 2):  # Seulement les harmoniques impaires
        y -= (4 / (np.pi * n**2)) * np.cos(n * x)
    return y

def fourier_scie(x, N):
    """Série de Fourier de l'onde en dents de scie (x/2 sur ]-pi, pi[)"""
    y = np.zeros_like(x)
    for n in range(1, N + 1):  # Toutes les harmoniques
        y += ((-1)**(n + 1) / n) * np.sin(n * x)
    return y

# --- Configuration de la Figure ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
fig.canvas.manager.set_window_title("Visualisation des Séries de Fourier")
plt.subplots_adjust(left=0.1, bottom=0.15, hspace=0.4)

x = np.linspace(-3 * np.pi, 3 * np.pi, 2000)
N_init = 3  # Nombre d'harmoniques par défaut

# Tracé des ondes exactes (pour comparaison visuelle abstraite)
onde_carree = np.sign(np.sin(x)) / 2
onde_tri = np.arcsin(np.sin(x - np.pi/2)) * 2 / np.pi * (np.pi/2) + np.pi/2
onde_scie = -np.arctan(np.tan((x+np.pi)/2))

# Initialisation des graphes
line_carree_exact, = ax1.plot(x, onde_carree, 'k--', alpha=0.5, label='Fonction exacte')
line_carree, = ax1.plot(x, fourier_carree(x, N_init), 'b-', label='Série de Fourier')
ax1.set_title("Onde Carrée (Phénomène de Gibbs visible aux sauts)")
ax1.legend(loc="upper right")
ax1.grid(True)

line_tri_exact, = ax2.plot(x, onde_tri, 'k--', alpha=0.5)
line_tri, = ax2.plot(x, fourier_triangulaire(x, N_init), 'r-')
ax2.set_title("Onde Triangulaire (Convergence C.U. rapide en $1/n^2$)")
ax2.grid(True)

line_scie_exact, = ax3.plot(x, onde_scie, 'k--', alpha=0.5)
line_scie, = ax3.plot(x, fourier_scie(x, N_init), 'g-')
ax3.set_title("Onde en Dents de Scie (Convergence simple lente en $1/n$)")
ax3.grid(True)

# Ajout d'un curseur (Slider) pour ajuster N interactivement
ax_slider = plt.axes([0.2, 0.03, 0.6, 0.03])
s_N = Slider(ax_slider, 'Harmoniques (N)', 1, 100, valinit=N_init, valstep=1)

def update(val):
    N = int(s_N.val)
    line_carree.set_ydata(fourier_carree(x, N))
    line_tri.set_ydata(fourier_triangulaire(x, N))
    line_scie.set_ydata(fourier_scie(x, N))
    fig.canvas.draw_idle()

s_N.on_changed(update)

# Ajout d'un texte explicatif
fig.text(0.5, 0.95, 'Visualisation Interactive : Séries de Fourier', ha='center', fontsize=16, fontweight='bold')
fig.text(0.5, 0.08, 'Déplacez le curseur pour ajouter des termes à la somme infinie !', ha='center', fontsize=10, style='italic')

plt.show()
