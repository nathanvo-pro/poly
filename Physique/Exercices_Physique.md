# 📝 Exercices de Physique — PHYSH1002 Vol. I (Électromagnétisme)

> Exercices organisés par difficulté croissante (⭐ à ⭐⭐⭐⭐⭐)  
> Chaque exercice porte un tag de chapitre : `[Ch.X]`

---






## Chapitre 1

### ⭐ Niveau 1 — Compréhension de base

#### Exercice 1.1 — Gradient en 2D `[Ch.1]`

Soit le champ scalaire $f(x, y) = 3x^2 + 2xy - y^2$.

1. Calculez $\vec{\text{grad}}\, f$.
2. Évaluez le gradient au point $P = (1, 2)$.
3. Dans quelle direction la croissance de $f$ est-elle maximale en $P$ ?

<details>
<summary>💡 Solution</summary>

1. $\vec{\text{grad}}\, f = (6x + 2y)\,\vec{1}_x + (2x - 2y)\,\vec{1}_y$
2. En $(1, 2)$ : $\vec{\text{grad}}\, f = 10\,\vec{1}_x - 2\,\vec{1}_y$
3. Direction du gradient : $\vec{u} = (10\,\vec{1}_x - 2\,\vec{1}_y)/\sqrt{104}$. La croissance maximale est dans cette direction.

</details>

---


#### Exercice 1.2 — Dérivée directionnelle `[Ch.1]`

Soit $V(x,y,z) = x^2 + yz$ et la direction $\vec{u} = \frac{1}{\sqrt{3}}(1, 1, 1)$.

Calculez la dérivée directionnelle de $V$ dans la direction $\vec{u}$ au point $(1, 1, 1)$.

<details>
<summary>💡 Solution</summary>

$\vec{\text{grad}}\, V = (2x, z, y)$. En $(1,1,1)$ : $\vec{\text{grad}}\, V = (2, 1, 1)$.

$\frac{\partial V}{\partial \vec{u}} = \vec{\text{grad}}\, V \cdot \vec{u} = \frac{1}{\sqrt{3}}(2 + 1 + 1) = \frac{4}{\sqrt{3}} \approx 2.31$

</details>

---


## Chapitre 2
### ⭐⭐ Niveau 2 — Application directe

#### Exercice 2.1 — Gradient en coordonnées cylindriques `[Ch.1]`

Soit $f(r, \theta, z) = r^2 \cos\theta + z$.

Calculez $\vec{\text{grad}}\, f$ en coordonnées cylindriques.

<details>
<summary>💡 Solution</summary>

$$\vec{\text{grad}}\, f = \frac{\partial f}{\partial r}\vec{1}_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec{1}_\theta + \frac{\partial f}{\partial z}\vec{1}_z$$

$$= 2r\cos\theta\,\vec{1}_r - r\sin\theta\,\vec{1}_\theta + \vec{1}_z$$

</details>

---



### ⭐ Niveau 1 — Compréhension de base

#### Exercice 1.3 — Flux magnétique `[Ch.2]`

Un champ magnétique uniforme $\bar{B} = 0.5\,\vec{1}_z$ T traverse une spire circulaire de rayon $r = 10$ cm placée dans le plan $(x, y)$.

Calculez le flux magnétique à travers la spire.

<details>
<summary>💡 Solution</summary>

$\Phi_B = \bar{B} \cdot \vec{S} = B \times \pi r^2 = 0.5 \times \pi \times 0.01 = 0.0157$ Wb $\approx 15.7$ mWb

</details>

---


### ⭐⭐ Niveau 2 — Application directe

#### Exercice 2.2 — Divergence et rotationnel `[Ch.2]`

Soit $\vec{A} = (xy, yz, zx)$.

1. Calculez $\text{div}\,\vec{A}$.
2. Calculez $\text{rot}\,\vec{A}$.
3. Le champ est-il conservatif ? Solénoïdal ?

<details>
<summary>💡 Solution</summary>

1. $\text{div}\,\vec{A} = y + z + x \neq 0$ → non solénoïdal

2. $\text{rot}\,\vec{A} = \begin{vmatrix} \vec{1}_x & \vec{1}_y & \vec{1}_z \\ \partial_x & \partial_y & \partial_z \\ xy & yz & zx \end{vmatrix} = (0-y)\vec{1}_x + (0-z)\vec{1}_y + (0-x)\vec{1}_z = (-y, -z, -x)$

   $\text{rot}\,\vec{A} \neq \vec{0}$ → non conservatif

3. Ni conservatif, ni solénoïdal.

</details>

---


## Chapitre 3
### ⭐⭐⭐ Niveau 3 — Synthèse et raisonnement

#### Exercice 3.1 — Théorème de Stokes `[Ch.2]`

Soit $\vec{A} = (-y, x, 0)$ et $C$ un cercle de rayon $R$ centré à l'origine dans le plan $z = 0$.

1. Calculez la circulation $\oint_C \vec{A} \cdot d\vec{\ell}$ directement.
2. Vérifiez via le théorème de Stokes en calculant $\text{rot}\,\vec{A}$ puis son flux.

<details>
<summary>💡 Solution</summary>

1. Paramétrisation : $\vec{r}(\theta) = R(\cos\theta, \sin\theta, 0)$, $d\vec{\ell} = R(-\sin\theta, \cos\theta, 0)d\theta$.

   $\oint_C = \int_0^{2\pi} R^2(\sin^2\theta + \cos^2\theta)d\theta = 2\pi R^2$

2. $\text{rot}\,\vec{A} = (0, 0, 2)$. Flux = $2 \times \pi R^2 = 2\pi R^2$ ✅

</details>

---



### ⭐⭐ Niveau 2 — Application directe

#### Exercice 2.3 — Force de Lorentz `[Ch.3]`

Un proton ($q = 1.6 \times 10^{-19}$ C) se déplace à $\vec{v} = 10^6\,\vec{1}_x$ m/s dans un champ $\bar{B} = 0.1\,\vec{1}_z$ T.

1. Calculez la force de Lorentz.
2. Quel est le rayon de la trajectoire circulaire ? ($m_p = 1.67 \times 10^{-27}$ kg)

<details>
<summary>💡 Solution</summary>

1. $\vec{F}_L = q\vec{v} \times \bar{B} = 1.6 \times 10^{-19} \times 10^6 \times 0.1 \times (\vec{1}_x \times \vec{1}_z) = -1.6 \times 10^{-14}\,\vec{1}_y$ N

2. $r = \frac{mv}{qB} = \frac{1.67 \times 10^{-27} \times 10^6}{1.6 \times 10^{-19} \times 0.1} = 0.104$ m $\approx 10.4$ cm

</details>

---


#### Exercice 2.4 — Loi de Faraday `[Ch.3]`

Un champ magnétique uniforme $B(t) = 0.2\sin(100\pi t)$ T traverse une spire circulaire de rayon 5 cm.

Calculez l'é.m.f. induite.

<details>
<summary>💡 Solution</summary>

$\Phi_B = B(t) \cdot \pi r^2 = 0.2\sin(100\pi t) \times \pi \times 0.0025$

$\mathcal{E} = -\frac{d\Phi_B}{dt} = -0.2 \times 100\pi \times \cos(100\pi t) \times \pi \times 0.0025$

$\mathcal{E} = -0.157\cos(100\pi t)$ V

Amplitude : $|\mathcal{E}_m| \approx 157$ mV

</details>

---


### ⭐⭐⭐ Niveau 3 — Synthèse et raisonnement

#### Exercice 3.2 — Transformation galiléenne `[Ch.3]`

Un repère $R'$ se déplace à $\vec{u}_0 = 50\,\vec{1}_x$ m/s dans $R$. Le champ magnétique vaut $\bar{B} = 0.3\,\vec{1}_z$ T et $\vec{E} = 100\,\vec{1}_y$ V/m dans $R$.

1. Quel est le champ $\vec{E}'$ dans $R'$ ?
2. La force de Lorentz est-elle différente dans $R'$ ?

<details>
<summary>💡 Solution</summary>

1. $\vec{E}' = \vec{E} + \vec{u}_0 \times \bar{B} = 100\,\vec{1}_y + 50\,\vec{1}_x \times 0.3\,\vec{1}_z = 100\,\vec{1}_y + 50 \times 0.3(-\vec{1}_y) = 85\,\vec{1}_y$ V/m

2. Non ! $\vec{F}_L/q = \vec{E} + \vec{v} \times \bar{B} = \vec{E}' + (\vec{v} - \vec{u}_0) \times \bar{B}'$ → la force est **invariante**.

</details>

---


## Chapitre 4
### ⭐⭐⭐⭐⭐ Niveau 5 — Maîtrise complète

#### Exercice 5.1 — Dynamo de Faraday `[Ch.3]`

Un disque conducteur de rayon $R = 20$ cm tourne à $\omega = 100$ rad/s dans un champ magnétique uniforme $\bar{B} = 0.5$ T perpendiculaire au disque.

1. Montrez que l'é.m.f. entre le centre et le bord vaut $\mathcal{E} = \frac{1}{2}BR^2\omega$.
2. Calculez numériquement cette é.m.f.
3. Si une résistance de $2\,\Omega$ est connectée entre le centre et le bord, calculez le couple résistant dû au freinage EM.

<details>
<summary>💡 Solution</summary>

1. Un élément radial à distance $r$ a une vitesse $v = r\omega$. La force par unité de charge est $v \times B = r\omega B$ (radiale). L'é.m.f. est $\mathcal{E} = \int_0^R r\omega B\,dr = \frac{1}{2}B\omega R^2$.

2. $\mathcal{E} = \frac{1}{2} \times 0.5 \times 100 \times 0.04 = 1$ V

3. $I = \mathcal{E}/R = 0.5$ A. Puissance dissipée $P = \mathcal{E}I = 0.5$ W. Couple résistant $\Gamma = P/\omega = 0.5/100 = 5 \times 10^{-3}$ N·m = 5 mN·m.

</details>

---


#### Exercice 5.3 — Potentiel vecteur et champ EM `[Ch.3]`

On donne $\vec{A} = \frac{\mu_0 I}{4\pi r}\vec{1}_z$ (potentiel vecteur d'un courant rectiligne fini).

1. Vérifiez que $\text{div}\,\vec{A} = 0$ (jauge de Coulomb).
2. Si $V = 0$ et $\vec{A}$ est statique, montrez que $\vec{E} = \vec{0}$.
3. Comment le champ $\bar{B}$ serait-il modifié si on ajoutait $\vec{\text{grad}}\, f$ à $\vec{A}$ ?

<details>
<summary>💡 Solution</summary>

1. $\text{div}\,\vec{A} = \partial A_z/\partial z = 0$ (car $\vec{A}$ ne dépend que de $r$) ✅

2. $\vec{E} = -\vec{\text{grad}}\, V - \partial\vec{A}/\partial t = 0 - 0 = \vec{0}$ ✅

3. $\bar{B}' = \text{rot}(\vec{A} + \vec{\text{grad}}\, f) = \text{rot}\,\vec{A} + \text{rot}(\vec{\text{grad}}\, f) = \bar{B} + \vec{0} = \bar{B}$.
   Le champ $\bar{B}$ est **invariant** par transformation de jauge → le potentiel vecteur n'est pas unique.

</details>


### ⭐⭐⭐ Niveau 3 — Synthèse et raisonnement

#### Exercice 3.4 — Loi de Lenz et conservation `[Ch.4]`

Un aimant ($\bar{B}_0 = 0.1$ T) est poussé vers une spire conductrice fermée sur une résistance $R = 5\,\Omega$ à vitesse $v = 2$ m/s.

1. Décrivez qualitativement la direction du courant induit (loi de Lenz).
2. Si le flux varie de 0 à $1 \times 10^{-3}$ Wb en 0.1 s, calculez l'é.m.f. et le courant induit moyens.

<details>
<summary>💡 Solution</summary>

1. Le flux augmente → le courant induit crée un $\bar{B}_i$ **opposé** à $\bar{B}_0$ → force **répulsive** sur l'aimant.

2. $\mathcal{E} = -\Delta\Phi/\Delta t = -10^{-3}/0.1 = -10$ mV. $|I_i| = |\mathcal{E}|/R = 10 \times 10^{-3}/5 = 2$ mA.

</details>

---


## Chapitre 5
### ⭐⭐⭐⭐ Niveau 4 — Problèmes approfondis

#### Exercice 4.1 — Courant de déplacement `[Ch.4]`

Un condensateur plan ($S = 10$ cm², $d = 1$ mm) est chargé par un courant constant $I = 2$ A.

1. Calculez $dE/dt$ entre les plaques.
2. Vérifiez que le courant de déplacement $\varepsilon_0 dE/dt \times S$ est bien égal à $I$.

<details>
<summary>💡 Solution</summary>

1. $E = \sigma/\varepsilon_0 = Q/(S\varepsilon_0)$. $dE/dt = I/(S\varepsilon_0) = 2/(10^{-3} \times 8.85 \times 10^{-12}) = 2.26 \times 10^{14}$ V/(m·s)

2. $\varepsilon_0 \times dE/dt \times S = 8.85 \times 10^{-12} \times 2.26 \times 10^{14} \times 10^{-3} = 2.0$ A ✅

</details>

---



### ⭐⭐⭐ Niveau 3 — Synthèse et raisonnement

#### Exercice 3.3 — Circuit RL `[Ch.5]`

Un circuit RL ($R = 10\,\Omega$, $L = 50$ mH) est connecté à une source de 12 V à $t = 0$.

1. Calculez la constante de temps $\tau$.
2. Après combien de temps le courant atteint-il 99% de sa valeur maximale ?
3. Calculez l'énergie stockée dans l'inducteur en régime permanent.

<details>
<summary>💡 Solution</summary>

1. $\tau = L/R = 0.05/10 = 5$ ms

2. $I(t) = 0.99 \times V/R \Rightarrow 1 - e^{-t/\tau} = 0.99 \Rightarrow e^{-t/\tau} = 0.01 \Rightarrow t = \tau\ln(100) = 5 \times 4.605 = 23.0$ ms

3. $I_{\max} = V/R = 1.2$ A. $W_L = \frac{1}{2}LI^2 = \frac{1}{2} \times 0.05 \times 1.44 = 36$ mJ

</details>

---


### ⭐⭐⭐⭐ Niveau 4 — Problèmes approfondis

#### Exercice 4.2 — Transformateur `[Ch.5]`

Un transformateur idéal ($N_p = 500$, $N_s = 50$) est alimenté par le secteur ($V_{\text{eff}} = 230$ V, $f = 50$ Hz).

1. Calculez la tension efficace au secondaire.
2. Si la charge au secondaire consomme 100 W, calculez les courants efficaces au primaire et au secondaire.
3. Calculez le flux magnétique maximal dans le noyau.

<details>
<summary>💡 Solution</summary>

1. $V_s = (N_s/N_p)V_p = (50/500) \times 230 = 23$ V (eff)

2. $I_s = P/V_s = 100/23 = 4.35$ A. $I_p = P/V_p = 100/230 = 0.435$ A.

3. $V_p(t) = V_m\sin(\omega t)$ avec $V_m = 230\sqrt{2} = 325.3$ V. Or $d\Phi/dt = V_p/N_p$, donc $\Phi = -V_m/(N_p\omega)\cos(\omega t)$.
   $\Phi_{\max} = V_m/(N_p\omega) = 325.3/(500 \times 2\pi \times 50) = 2.07 \times 10^{-3}$ Wb $\approx 2.07$ mWb

</details>

---


#### Exercice 4.3 — Impédances et filtrage `[Ch.5]`

Un inducteur ($L = 10$ mH) est alimenté par un signal contenant deux fréquences : $f_1 = 50$ Hz ($V_1 = 10$ V) et $f_2 = 5000$ Hz ($V_2 = 10$ V).

1. Calculez la réactance pour chaque fréquence.
2. Calculez l'amplitude du courant pour chaque composante.
3. Expliquez pourquoi l'inducteur est un filtre passe-bas.

<details>
<summary>💡 Solution</summary>

1. $X_{L1} = \omega_1 L = 2\pi \times 50 \times 0.01 = 3.14\,\Omega$. $X_{L2} = 2\pi \times 5000 \times 0.01 = 314\,\Omega$.

2. $I_{m1} = V_1/X_{L1} = 10/3.14 = 3.18$ A. $I_{m2} = V_2/X_{L2} = 10/314 = 0.032$ A = 32 mA.

3. La réactance $X_L = \omega L$ **augmente** avec $\omega$, donc le courant **diminue** pour les hautes fréquences : c'est un filtre **passe-bas**. Le courant à 5 kHz est 100× plus faible qu'à 50 Hz.

</details>

---


