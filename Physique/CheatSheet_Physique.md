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

---

## Chapitre 6 — Oscillateurs harmoniques et amortis

**Oscillateur harmonique :** $\ddot{x} + \omega_0^2 x = 0$, solution $x = A\cos(\omega_0 t + \varphi)$, $\omega_0 = \sqrt{\kappa/m}$

**Énergie :** $E_p = \frac{1}{2}\kappa x^2$, $E_c = \frac{1}{2}m\dot{x}^2$, $E_{\text{tot}} = E_c + E_p = \text{const}$

**Pendule :** $\omega_0 = \sqrt{g/l}$ (indépendant de $m$)

**Circuit LC :** $\omega_0 = 1/\sqrt{LC}$, $W_m = \frac{1}{2}LI^2$, $W_e = \frac{1}{2}CV^2$

**OLA :** $\ddot{x} + 2\alpha\dot{x} + \omega_0^2 x = 0$, $\alpha = \lambda/(2m)$, solution $x = Ae^{-\alpha t}\cos(\omega_a t + \varphi)$, $\omega_a = \sqrt{\omega_0^2 - \alpha^2}$

**RLC :** $\omega_0 = 1/\sqrt{LC}$, $\alpha = R/(2L)$

**Phaseurs :** $x = \text{Re}[\underline{X}e^{i\omega t}]$, $d/dt \to i\omega$

**Universalité :** $\kappa_{\text{eff}} = E_p''(x_0)$ → tout potentiel en U est un OH autour de son minimum

---

## Chapitre 7 — Oscillateur forcé et résonance

**OLAF :** $\ddot{x} + 2\alpha\dot{x} + \omega_0^2 x = a\cos(\omega t)$, phaseur $\underline{X} = \frac{a}{\omega_0^2 - \omega^2 + 2\alpha i\omega}$

**Résonance :** $|\underline{X}|_{\max} = \frac{a}{2\alpha\omega_0}$ quand $\omega = \omega_0$, déphasage $\pi/2$

**Largeur :** $\delta\omega^* = \sqrt{3}\,\alpha$, facteur de qualité $Q = \frac{\omega_0}{2\alpha} = \frac{1}{R}\sqrt{L/C}$

**Impédances :** $Z_R = R$, $Z_L = i\omega L$, $Z_C = \frac{1}{i\omega C}$

**RLC série :** $\underline{Z} = R + i(\omega L - \frac{1}{\omega C})$, résonance quand $\omega_0 = 1/\sqrt{LC}$

**Puissance :** $P_{\text{moy}} = V_{\text{eff}}I_{\text{eff}}\cos\varphi$

---

## Chapitre 8 — Ondes de corde et de compression

**Éq. d'onde :** $\frac{\partial^2 x}{\partial t^2} = v^2\frac{\partial^2 x}{\partial z^2}$

**Corde :** $v = \sqrt{F_T/\mu}$

**Cristal :** $v = d\sqrt{\kappa_c/m}$

**Gaz :** $v = \sqrt{\gamma P/\rho}$

**Solutions :** $x = f(z-vt) + g(z+vt)$ (d'Alembert)

**Superposition :** $ax_1 + bx_2$ est solution si $x_1,x_2$ le sont

---

## Chapitre 9 — Ondes électromagnétiques

**Éq. de l'onde lumineuse :** $\Delta\vec{E} - \frac{1}{c^2} \frac{\partial^2\vec{E}}{\partial t^2} = \vec{0}$, idem pour $\vec{B}$

**Vitesse :** $c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3 \times 10^8\;\text{m/s}$

**Onde harmonique progressive (selon z) :** $\vec{E}(z,t) = \vec{E}_0\cos(kz - \omega t + \varphi)$

**Relations :** $\omega = 2\pi f = \frac{2\pi}{T}$, $k = \frac{2\pi}{\lambda}$, $\lambda = cT = \frac{c}{f}$, $v = \frac{\omega}{k} = c$

**Polarisation :** Direction du vecteur champ électrique $\vec{E}$. Toujours perpendiculaire à la propagation ($\text{div}\vec{E} = 0$).

**Trièdre électromagnétique :** $\vec{E}$, $\vec{B}$, $\vec{k}$ (ou la vitesse) forment un trièdre direct, et $B_0 = E_0/c$.

---

## Chapitre 10 — Ondes stationnaires, battements et Doppler

**Onde stationnaire :** $y(z,t) = 2a\sin(kz)\sin(\omega t + \phi)$ (variables séparées)

**Corde fixée aux extrémités :** $\lambda_n = \frac{2L}{n} \implies f_n = n \frac{v}{2L}$ (modes propres, harmoniques)

**Battement :** $y(t) = 2A\cos\left(\frac{\omega_1-\omega_2}{2}t\right)\cos\left(\frac{\omega_1+\omega_2}{2}t\right)$. Fréquence de l'enveloppe de puissance : $f_b = |f_1 - f_2|$.

**Effet Doppler (général) :** 
$$f' = f \left(\frac{v \pm v_{obs}}{v \mp v_{source}}\right)$$
*Règle :* L'approche mutuelle **augmente** $f'$ (prendre $+$ en haut, $-$ en bas). L'éloignement mutuel **diminue** $f'$ (prendre $-$ en haut, $+$ en bas). Double effet pour un écho sur cible mobile.
