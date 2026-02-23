# 🧾 Cheat Sheet — Analyse 2

> ⚡ **Fiche ultra-condensée** — Les formules vitales pour l'examen.

---

## 1. Produit scalaire et Norme $L^2$

$$
\langle f, g \rangle = \int_a^b f(x) \overline{g(x)} \, dx \qquad \|f\|_2 = \sqrt{\int_a^b |f|^2}
$$

---

## 2. Coefficients de Fourier (Série Réelle sur $[-L, L]$)

$$
f(x) \sim \frac{a_0}{2} + \sum_{k=1}^{\infty} \left[ a_k \cos\left(\frac{k\pi x}{L}\right) + b_k \sin\left(\frac{k\pi x}{L}\right) \right]
$$

$$
a_k = \frac{1}{L}\int_{-L}^{L} f(t) \cos\left(\frac{k\pi t}{L}\right) dt \qquad b_k = \frac{1}{L}\int_{-L}^{L} f(t) \sin\left(\frac{k\pi t}{L}\right) dt
$$

**Série sinus seule** ($[0,L]$, prolongement impair) : $b_k = \frac{2}{L}\int_0^{L} f(t)\sin(\frac{k\pi t}{L}) dt$

**Série cosinus seule** ($[0,L]$, prolongement pair) : $a_k = \frac{2}{L}\int_0^{L} f(t)\cos(\frac{k\pi t}{L}) dt$

---

## 3. Série de Fourier Complexe

$$
f(t) \sim \sum_{k=-\infty}^{+\infty} c_k e^{ik\omega_0 t} \qquad c_k = \frac{1}{T}\int_{-T/2}^{T/2} f(t)e^{-ik\omega_0 t} dt \qquad \omega_0 = \frac{2\pi}{T}
$$

Liens : $c_0 = a_0/2$, $c_k = \frac{a_k - ib_k}{2}$, $c_{-k} = \frac{a_k + ib_k}{2}$.

---

## 4. Théorèmes fondamentaux

| Théorème | Énoncé |
| :--- | :--- |
| **Bessel** | $\sum |c_k|^2 \|\varphi_k\|^2 \leq \|f\|_2^2$ |
| **Parseval** | $\sum |c_k|^2 \|\varphi_k\|^2 = \|f\|_2^2$ (si système complet) |
| **Dirichlet** | Si $f, f'$ continues par morceaux, la série converge vers $\tilde{f}(x) = \frac{f(x^-)+f(x^+)}{2}$ |

---

## 5. Opérations

- **Dérivation :** $c_k(f') = ik\omega_0 \cdot c_k(f)$
- **Convolution :** $c_k(f * g) = c_k(f) \cdot c_k(g)$
- **Intégration :** Toujours valide terme à terme !

---

## 6. Équation de la chaleur 1D

$$
\frac{\partial u}{\partial t} = \alpha^2 \frac{\partial^2 u}{\partial x^2}, \quad u(0,t) = u(L,t) = 0, \quad u(x,0) = f(x)
$$

**Solution :**
$$
u(x,t) = \sum_{n=1}^{\infty} b_n \sin\left(\frac{n\pi x}{L}\right) e^{-\alpha^2(n\pi/L)^2 t}
$$
où $b_n = \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right) dx$.
