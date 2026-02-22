# 📋 CheatSheet — Électromagnétisme PHYSH1002 Vol. I

> Toutes les formules essentielles en un coup d'œil

---

## 1. Opérateurs différentiels

### Gradient (scalaire → vecteur)

| Coord. | $\vec{\text{grad}}\, f$ |
|--------|------------------------|
| Cart. | $\partial_x f\,\hat{x} + \partial_y f\,\hat{y} + \partial_z f\,\hat{z}$ |
| Cyl. | $\partial_r f\,\hat{r} + \frac{1}{r}\partial_\theta f\,\hat{\theta} + \partial_z f\,\hat{z}$ |
| Sph. | $\partial_r f\,\hat{r} + \frac{1}{r}\partial_\theta f\,\hat{\theta} + \frac{1}{r\sin\theta}\partial_\varphi f\,\hat{\varphi}$ |

### Divergence (vecteur → scalaire)

$$\text{div}\,\vec{A} = \partial_x A_x + \partial_y A_y + \partial_z A_z \quad \text{(cart.)}$$

### Rotationnel (vecteur → vecteur)

$$\text{rot}\,\vec{A} = (\partial_y A_z - \partial_z A_y)\hat{x} + (\partial_z A_x - \partial_x A_z)\hat{y} + (\partial_x A_y - \partial_y A_x)\hat{z}$$

### Identités fondamentales

$$\text{rot}(\vec{\text{grad}}\, f) = \vec{0} \qquad \text{div}(\text{rot}\,\vec{A}) = 0$$

---

## 2. Théorèmes intégraux

| Théorème | Formule |
|----------|---------|
| **Stokes** | $\oint_C \vec{A} \cdot d\vec{\ell} = \iint_{S_C} \text{rot}\,\vec{A} \cdot d\vec{S}$ |
| **Divergence (Gauss)** | $\oiint_S \vec{A} \cdot d\vec{S} = \iiint_V \text{div}\,\vec{A}\,dV$ |

---

## 3. Équations de Maxwell

| Loi | Locale | Intégrale |
|-----|--------|-----------|
| **Gauss (E)** | $\text{div}\,\vec{E} = \rho/\varepsilon_0$ | $\oiint \vec{E}\cdot d\vec{S} = Q/\varepsilon_0$ |
| **Gauss (B)** | $\text{div}\,\bar{B} = 0$ | $\oiint \bar{B}\cdot d\vec{S} = 0$ |
| **Faraday** | $\text{rot}\,\vec{E} = -\partial_t\bar{B}$ | $\oint \vec{E}\cdot d\vec{\ell} = -d\Phi_B/dt$ |
| **Ampère-Maxwell** | $\text{rot}\,\bar{B} = \mu_0\vec{J} + \mu_0\varepsilon_0\partial_t\vec{E}$ | $\oint \bar{B}\cdot d\vec{\ell} = \mu_0(I + \varepsilon_0\,d\Phi_E/dt)$ |

---

## 4. Force de Lorentz

$$\boxed{\vec{F}_L = q(\vec{E} + \vec{v} \times \bar{B})}$$

---

## 5. Transformation galiléenne ($u_0 \ll c$)

$$\vec{E}' = \vec{E} + \vec{u}_0 \times \bar{B} \qquad \bar{B}' \approx \bar{B} \qquad \vec{J}' = \vec{J} - \rho\vec{u}_0$$

---

## 6. Potentiels

$$\bar{B} = \text{rot}\,\vec{A} \qquad \vec{E} = -\vec{\text{grad}}\, V - \partial_t\vec{A}$$

Jauge de Lorentz : $\text{div}\,\vec{A} + \frac{1}{c^2}\partial_t V = 0$

---

## 7. Conservation

$$\frac{\partial \rho}{\partial t} + \text{div}\,\vec{J} = 0$$

---

## 8. Inducteur

| Formule | Expression |
|---------|-----------|
| Flux | $\Phi_M = LI$ |
| É.m.f. | $\mathcal{E} = -L\,dI/dt$ |
| Loi V-I | $V_L = L\,dI/dt$ |
| Inductance solénoïde | $L = \mu N^2 S/\ell$ |
| Énergie | $W_L = \frac{1}{2}LI^2$ |
| Densité énergie mag. | $w_B = \frac{1}{2\mu}\|\bar{B}\|^2$ |

---

## 9. Circuit RL

| Phase | $I(t)$ | $\tau$ |
|-------|--------|--------|
| **Charge** | $\frac{V}{R}(1 - e^{-t/\tau})$ | $L/R$ |
| **Décharge** | $I_0\,e^{-t/\tau}$ | $L/R$ |

---

## 10. Transformateur

$$\boxed{V_s = \frac{N_s}{N_p} V_p} \qquad I_s = \frac{N_p}{N_s} I_p$$

---

## 11. Courant alternatif

### Valeurs efficaces

$$I_{\text{eff}} = \frac{I_m}{\sqrt{2}} \qquad V_{\text{eff}} = \frac{V_m}{\sqrt{2}}$$

### Puissance

$$\langle P \rangle = R I_{\text{eff}}^2 = \frac{V_{\text{eff}}^2}{R} = V_{\text{eff}} I_{\text{eff}} \quad \text{(résistance)}$$

$$\langle P \rangle = 0 \quad \text{(inducteur ou condensateur idéal)}$$

### Réactances et déphasage

| Comp. | Réactance/R | $I_m$ | Déphasage | Filtre |
|-------|-------------|-------|-----------|--------|
| **R** | $R$ | $V_m/R$ | $0$ | — |
| **L** | $X_L = \omega L$ | $V_m/(\omega L)$ | $-\pi/2$ | Passe-bas |
| **C** | $X_C = 1/(\omega C)$ | $\omega C V_m$ | $+\pi/2$ | Passe-haut |

---

## 12. Constantes

| Symbole | Valeur |
|---------|--------|
| $\varepsilon_0$ | $8.854 \times 10^{-12}$ F/m |
| $\mu_0$ | $4\pi \times 10^{-7}$ H/m |
| $c = 1/\sqrt{\varepsilon_0\mu_0}$ | $3 \times 10^8$ m/s |
| $e$ | $1.602 \times 10^{-19}$ C |
