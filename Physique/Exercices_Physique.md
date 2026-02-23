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




## Chapitre 6 — Oscillateurs harmoniques et amortis

### Exercice 6.1 ⭐

Un ressort de constante $\kappa = 200\;\text{N/m}$ supporte une masse $m = 0{,}5\;\text{kg}$. Calculez la pulsation propre $\omega_0$, la période $T$ et la fréquence $f$ des oscillations.

<details>
<summary>Voir la réponse</summary>

$$\omega_0 = \sqrt{\frac{\kappa}{m}} = \sqrt{\frac{200}{0{,}5}} = \sqrt{400} = 20\;\text{rad/s}$$

$$T = \frac{2\pi}{\omega_0} = \frac{2\pi}{20} \approx 0{,}314\;\text{s}$$

$$f = \frac{1}{T} \approx 3{,}18\;\text{Hz}$$

</details>

### Exercice 6.2 ⭐

Un oscillateur harmonique démarre avec $x_0 = 3\;\text{cm}$ et $v_0 = 0$. La pulsation est $\omega_0 = 10\;\text{rad/s}$. Trouvez l'amplitude $A$ et la phase initiale $\varphi$.

<details>
<summary>Voir la réponse</summary>

$$A = \sqrt{x_0^2 + \frac{v_0^2}{\omega_0^2}} = \sqrt{(0{,}03)^2 + 0} = 0{,}03\;\text{m} = 3\;\text{cm}$$

$$\tan\varphi = -\frac{v_0}{\omega_0 x_0} = 0 \implies \varphi = 0$$

La solution est simplement $x(t) = 3\cos(10t)$ cm.

</details>

### Exercice 6.3 ⭐

Un oscillateur harmonique démarre avec $x_0 = 0$ et $v_0 = 2\;\text{m/s}$, et $\omega_0 = 5\;\text{rad/s}$. Trouvez $A$ et $\varphi$.

<details>
<summary>Voir la réponse</summary>

$$A = \sqrt{0 + \frac{4}{25}} = \frac{2}{5} = 0{,}4\;\text{m}$$

$$\tan\varphi = -\frac{v_0}{\omega_0 \cdot 0} \to \pm\infty$$

Comme $v_0 > 0$ et $x_0 = 0$, on a $\varphi = -\pi/2$ (car $x(0) = A\cos\varphi = 0$ et $\dot{x}(0) = -A\omega_0\sin\varphi > 0$).

$$x(t) = 0{,}4\cos(5t - \pi/2) = 0{,}4\sin(5t)$$

</details>

### Exercice 6.4 ⭐⭐

Calculez l'énergie potentielle, cinétique et totale d'un oscillateur harmonique ($\kappa = 100\;\text{N/m}$) à la position $x = 0{,}05\;\text{m}$, sachant que $x_0 = 0{,}1\;\text{m}$.

<details>
<summary>Voir la réponse</summary>

$$E_p = \frac{1}{2}\kappa x^2 = \frac{1}{2}(100)(0{,}05)^2 = 0{,}125\;\text{J}$$

$$E_{\text{tot}} = \frac{1}{2}\kappa x_0^2 = \frac{1}{2}(100)(0{,}1)^2 = 0{,}5\;\text{J}$$

$$E_c = E_{\text{tot}} - E_p = 0{,}5 - 0{,}125 = 0{,}375\;\text{J}$$

</details>

### Exercice 6.5 ⭐⭐

Un pendule simple de longueur $l = 2\;\text{m}$ oscille avec de petites amplitudes. Calculez sa pulsation propre et sa période. La masse est-elle pertinente ?

<details>
<summary>Voir la réponse</summary>

$$\omega_0 = \sqrt{\frac{g}{l}} = \sqrt{\frac{9{,}81}{2}} = \sqrt{4{,}905} \approx 2{,}21\;\text{rad/s}$$

$$T = \frac{2\pi}{\omega_0} \approx \frac{6{,}283}{2{,}21} \approx 2{,}84\;\text{s}$$

La masse n'intervient **pas** dans la pulsation du pendule simple. C'est une conséquence du fait que la force de rappel $f = -\frac{mg}{l}x$ est proportionnelle à $m$, qui se simplifie dans $m\ddot{x} = f$.

</details>

### Exercice 6.6 ⭐⭐

Un circuit LC a une inductance $L = 10\;\text{mH}$ et une capacité $C = 100\;\mu\text{F}$. Calculez la fréquence propre d'oscillation du courant.

<details>
<summary>Voir la réponse</summary>

$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10^{-2} \times 10^{-4}}} = \frac{1}{\sqrt{10^{-6}}} = \frac{1}{10^{-3}} = 1000\;\text{rad/s}$$

$$f = \frac{\omega_0}{2\pi} = \frac{1000}{2\pi} \approx 159\;\text{Hz}$$

</details>

### Exercice 6.7 ⭐⭐

Une masse est plongée dans le potentiel $E_p(x) = -\cos(kx)$. Dans l'approximation des petites oscillations autour de $x = 0$, trouvez la pulsation $\omega_0$.

<details>
<summary>Voir la réponse</summary>

On développe $E_p(x) = -\cos(kx) \approx -1 + \frac{k^2 x^2}{2}$ (Taylor autour de $x = 0$).

Par identification avec $E_p = \text{const} + \frac{1}{2}\kappa_{\text{eff}} x^2$, on obtient $\kappa_{\text{eff}} = k^2$.

Ou directement : $E_p''(0) = k^2\cos(0) = k^2$.

$$\omega_0 = \sqrt{\frac{\kappa_{\text{eff}}}{m}} = \frac{k}{\sqrt{m}}$$

</details>

### Exercice 6.8 ⭐⭐

Pour le potentiel $E_p(x) = a(e^{bx} + e^{-bx})$, calculez la pulsation d'oscillation autour de $x = 0$.

<details>
<summary>Voir la réponse</summary>

$$E_p'(x) = a(be^{bx} - be^{-bx}) \implies E_p'(0) = 0 \quad \checkmark$$

$$E_p''(x) = ab^2(e^{bx} + e^{-bx}) \implies E_p''(0) = 2ab^2$$

$$\kappa_{\text{eff}} = 2ab^2 \implies \omega_0 = \sqrt{\frac{2ab^2}{m}} = b\sqrt{\frac{2a}{m}}$$

</details>

### Exercice 6.9 ⭐⭐⭐

Démontrez que la combinaison d'une force de rappel élastique ($-\kappa x$) et de la gravité ($mg$) donne un oscillateur harmonique. Trouvez la position d'équilibre et la pulsation.

<details>
<summary>Voir la réponse</summary>

Équation de Newton : $m\ddot{x} = mg - \kappa x$.

Position d'équilibre ($\ddot{x} = 0$) : $x_0 = mg/\kappa$.

Changement de variable $x' = x - x_0$ :

$$m\ddot{x}' = mg - \kappa(x' + x_0) = mg - \kappa x' - \kappa x_0 = mg - \kappa x' - mg = -\kappa x'$$

$$\ddot{x}' + \omega_0^2 x' = 0 \quad \text{avec} \quad \omega_0 = \sqrt{\kappa/m}$$

La masse oscille autour de $x_0 = mg/\kappa$ avec la **même pulsation** que sans gravité ! La gravité ne fait que déplacer le centre d'oscillation.

</details>

### Exercice 6.10 ⭐⭐⭐

Dans un circuit LC avec $L = 5\;\text{mH}$, $C = 2\;\mu\text{F}$, le courant initial est $I_0 = 50\;\text{mA}$. Calculez l'énergie totale du circuit et la tension maximale aux bornes du condensateur.

<details>
<summary>Voir la réponse</summary>

Énergie totale ($= W_m$ maximale quand $I = I_0$ et $V = 0$) :

$$W_{\text{tot}} = \frac{1}{2}LI_0^2 = \frac{1}{2}(5\times10^{-3})(50\times10^{-3})^2 = 6{,}25 \times 10^{-6}\;\text{J}$$

Tension maximale (quand toute l'énergie est dans le condensateur) :

$$W_{\text{tot}} = \frac{1}{2}CV_{\max}^2 \implies V_{\max} = \sqrt{\frac{2W_{\text{tot}}}{C}} = \sqrt{\frac{2 \times 6{,}25 \times 10^{-6}}{2 \times 10^{-6}}} = \sqrt{6{,}25} = 2{,}5\;\text{V}$$

</details>

### Exercice 6.11 ⭐⭐⭐

Un circuit RLC a $R = 10\;\Omega$, $L = 0{,}1\;\text{H}$, $C = 100\;\mu\text{F}$. Calculez $\omega_0$, $\alpha$, $\omega_a$ et dites si l'amortissement est faible.

<details>
<summary>Voir la réponse</summary>

$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{0{,}1 \times 10^{-4}}} = \frac{1}{\sqrt{10^{-5}}} \approx 316\;\text{rad/s}$$

$$\alpha = \frac{R}{2L} = \frac{10}{0{,}2} = 50\;\text{s}^{-1}$$

Comme $\alpha = 50 < \omega_0 \approx 316$, l'amortissement est **faible**.

$$\omega_a = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{316^2 - 50^2} = \sqrt{99856 - 2500} = \sqrt{97356} \approx 312\;\text{rad/s}$$

La pseudo-période est $T_a = 2\pi/\omega_a \approx 0{,}020\;\text{s}$.

</details>

### Exercice 6.12 ⭐⭐⭐

Expliquez physiquement pourquoi $\omega_a < \omega_0$ dans un OLA. Que se passe-t-il quand $\alpha \to \omega_0$ ?

<details>
<summary>Voir la réponse</summary>

L'amortissement retire de l'énergie au système à chaque oscillation. L'oscillateur met **plus de temps** pour accomplir chaque cycle car il est freiné → la pseudo-période $T_a > T_0$ et donc $\omega_a < \omega_0$.

Quand $\alpha \to \omega_0$ : $\omega_a = \sqrt{\omega_0^2 - \alpha^2} \to 0$, ce qui signifie une pseudo-période $T_a \to \infty$. L'oscillateur ne fait plus qu'un seul demi-cycle avant de s'arrêter → c'est la limite de l'**amortissement critique** ($\alpha = \omega_0$). Au-delà ($\alpha > \omega_0$), il n'y a plus d'oscillation du tout → **régime sur-amorti** (retour apériodique vers l'équilibre).

</details>

### Exercice 6.13 ⭐⭐⭐⭐

En utilisant les phaseurs, résolvez l'équation de l'oscillateur harmonique $\ddot{x} + \omega_0^2 x = 0$. Montrez qu'on retrouve la solution générale $x(t) = A\cos(\omega_0 t + \varphi)$.

<details>
<summary>Voir la réponse</summary>

On pose $x(t) = \text{Re}[\underline{X}e^{i\omega t}]$ avec $\underline{X} \in \mathbb{C}$ et $\omega$ inconnu.

Les dérivées en phaseur : $\dot{x} \leftrightarrow i\omega\underline{X}$, $\ddot{x} \leftrightarrow -\omega^2\underline{X}$.

Substitution dans l'EDO :

$$-\omega^2\underline{X} + \omega_0^2\underline{X} = 0 \implies (\omega_0^2 - \omega^2)\underline{X} = 0$$

Pour $\underline{X} \neq 0$ : $\omega^2 = \omega_0^2$, donc $\omega = \omega_0$.

Le phaseur $\underline{X} = |\underline{X}|e^{i\varphi}$ est libre (arbitraire), ce qui donne bien :

$$x(t) = \text{Re}[|\underline{X}|e^{i\varphi}e^{i\omega_0 t}] = |\underline{X}|\cos(\omega_0 t + \varphi) = A\cos(\omega_0 t + \varphi)$$

avec $A = |\underline{X}|$ et $\varphi = \arg(\underline{X})$ déterminés par les conditions initiales. $\square$

</details>

### Exercice 6.14 ⭐⭐⭐⭐

Un cylindre muni d'un piston de masse $m$ contient de l'air à pression atmosphérique $P_a$. La hauteur du cylindre à l'équilibre est $h_0$. Montrez que le piston oscille harmoniquement et trouvez $\omega_0$. (On suppose une compression adiabatique avec $\gamma = 1{,}4$.)

<details>
<summary>Voir la réponse</summary>

Soit $S$ la section et $x$ le déplacement du piston par rapport à l'équilibre ($h_0$). La nouvelle hauteur est $h = h_0 - x$ et le volume $V = S(h_0 - x)$.

Compression adiabatique : $PV^\gamma = P_a(Sh_0)^\gamma$, donc $P = P_a\left(\frac{h_0}{h_0 - x}\right)^\gamma$.

Force nette : $F = (P - P_a)S = P_aS\left[\left(\frac{h_0}{h_0-x}\right)^\gamma - 1\right]$.

Pour petits déplacements ($x \ll h_0$), développement de Taylor :

$$\left(\frac{h_0}{h_0-x}\right)^\gamma = \left(1 - \frac{x}{h_0}\right)^{-\gamma} \approx 1 + \frac{\gamma x}{h_0}$$

Donc $F \approx P_a S \cdot \frac{\gamma x}{h_0}$, une force de rappel avec $\kappa_{\text{eff}} = \frac{\gamma P_a S}{h_0}$.

$$\omega_0 = \sqrt{\frac{\kappa_{\text{eff}}}{m}} = \sqrt{\frac{\gamma P_a S}{m h_0}}$$

</details>

### Exercice 6.15 ⭐⭐⭐⭐⭐

Un bathyscaphe cylindrique de diamètre $D = 15\;\text{cm}$, hauteur $H = 60\;\text{cm}$ et masse $m = 9\;\text{kg}$ flotte verticalement à la surface de l'eau ($\rho = 1000\;\text{kg/m}^3$). On le pousse légèrement vers le bas et on le relâche. Calculez la fréquence $f$ des oscillations verticales.

<details>
<summary>Voir la réponse</summary>

**Position d'équilibre :** La profondeur immergée $h_0$ est donnée par la poussée d'Archimède : $mg = \rho g S h_0$, donc $h_0 = m/(\rho S)$.

Section : $S = \pi(D/2)^2 = \pi(0{,}075)^2 = 1{,}767 \times 10^{-2}\;\text{m}^2$.

$h_0 = \frac{9}{1000 \times 1{,}767 \times 10^{-2}} = 0{,}509\;\text{m}$ (soit $\approx 51\;\text{cm}$, bien $< H$ donc le cylindre flotte).

**Perturbation :** Si on enfonce le bathyscaphe d'une distance $x$ supplémentaire, la poussée d'Archimède augmente de $\rho g S x$ (force vers le haut), tandis que le poids reste constant.

Force de rappel : $F = -\rho g S x$ (proportionnelle et opposée au déplacement).

$$\omega_0 = \sqrt{\frac{\rho g S}{m}} = \sqrt{\frac{1000 \times 9{,}81 \times 1{,}767 \times 10^{-2}}{9}} = \sqrt{19{,}26} \approx 4{,}39\;\text{rad/s}$$

$$f = \frac{\omega_0}{2\pi} \approx \frac{4{,}39}{6{,}28} \approx 0{,}70\;\text{Hz}$$

</details>


## Chapitre 7 — Oscillateur linéaire amorti forcé et résonance

### Exercice 7.1 ⭐

Un OLAF a $\omega_0 = 100\;\text{rad/s}$, $\alpha = 2\;\text{s}^{-1}$, et $a = 10\;\text{m/s}^2$. Calculez le phaseur $\underline{X}$ et l'amplitude à la résonance ($\omega = \omega_0$).

<details>
<summary>Voir la réponse</summary>

À la résonance ($\omega = \omega_0$) :

$$\underline{X} = \frac{a}{2\alpha i\omega_0} = \frac{10}{2(2)(i)(100)} = \frac{10}{400i} = \frac{-i}{40}$$

$$|\underline{X}|_{\max} = \frac{a}{2\alpha\omega_0} = \frac{10}{2 \times 2 \times 100} = \frac{10}{400} = 0{,}025\;\text{m} = 2{,}5\;\text{cm}$$

Le déphasage est $\varphi = \arg(-i) = -\pi/2$ → le mouvement est $x(t) = 0{,}025\sin(\omega_0 t)$ (en retard de $\pi/2$).

</details>

### Exercice 7.2 ⭐

Donnez l'amplitude statique $|\underline{X}_S|$ pour les mêmes paramètres ($a = 10$, $\omega_0 = 100$). Comparez au cas résonant.

<details>
<summary>Voir la réponse</summary>

$$|\underline{X}_S| = \frac{a}{\omega_0^2} = \frac{10}{10000} = 10^{-3}\;\text{m} = 1\;\text{mm}$$

Facteur d'amplification à la résonance :

$$\frac{|\underline{X}|_{\max}}{|\underline{X}_S|} = \frac{\omega_0}{2\alpha} = \frac{100}{4} = 25$$

La résonance amplifie l'amplitude par un facteur 25 par rapport au cas statique !

</details>

### Exercice 7.3 ⭐⭐

Calculez la demi-largeur de résonance $\delta\omega^*$ et la largeur totale $\Delta\omega$ (à mi-amplitude) pour $\alpha = 5\;\text{s}^{-1}$.

<details>
<summary>Voir la réponse</summary>

$$\delta\omega^* = \sqrt{3}\,\alpha = \sqrt{3} \times 5 \approx 8{,}66\;\text{rad/s}$$

La largeur totale (symétrique) est :

$$\Delta\omega = 2\delta\omega^* = 2\sqrt{3}\,\alpha \approx 17{,}3\;\text{rad/s}$$

</details>

### Exercice 7.4 ⭐⭐

Calculez le facteur de qualité $Q$ d'un circuit RLC avec $L = 10\;\text{mH}$, $C = 1\;\mu\text{F}$, $R = 20\;\Omega$.

<details>
<summary>Voir la réponse</summary>

$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10^{-2} \times 10^{-6}}} = \frac{1}{10^{-4}} = 10^4\;\text{rad/s}$$

$$\alpha = \frac{R}{2L} = \frac{20}{0{,}02} = 1000\;\text{s}^{-1}$$

$$Q = \frac{\omega_0}{2\alpha} = \frac{10^4}{2000} = 5$$

$Q = 5$ indique une résonance moyennement sélective.

</details>

### Exercice 7.5 ⭐⭐

Calculez les réactances $X_L$ et $X_C$ pour $L = 0{,}1\;\text{H}$, $C = 10\;\mu\text{F}$ à $\omega = 500\;\text{rad/s}$. Le circuit est-il en dessous ou au-dessus de la résonance ?

<details>
<summary>Voir la réponse</summary>

$$X_L = \omega L = 500 \times 0{,}1 = 50\;\Omega$$

$$X_C = \frac{1}{\omega C} = \frac{1}{500 \times 10^{-5}} = \frac{1}{5 \times 10^{-3}} = 200\;\Omega$$

Comme $X_C > X_L$, la partie imaginaire de $\underline{Z}$ est $i(50 - 200) = -150i$ : le circuit est **capacitif** (en dessous de la résonance).

Résonance : $\omega_0 = 1/\sqrt{0{,}1 \times 10^{-5}} = 1000\;\text{rad/s} > 500$, confirmé.

</details>

### Exercice 7.6 ⭐⭐

Écrivez l'impédance complexe d'un circuit RLC série avec $R = 100\;\Omega$, $L = 50\;\text{mH}$, $C = 2\;\mu\text{F}$ à la fréquence $f = 500\;\text{Hz}$. Calculez le déphasage tension-courant.

<details>
<summary>Voir la réponse</summary>

$\omega = 2\pi \times 500 = 3142\;\text{rad/s}$

$$X_L = \omega L = 3142 \times 0{,}05 = 157{,}1\;\Omega$$

$$X_C = \frac{1}{\omega C} = \frac{1}{3142 \times 2 \times 10^{-6}} = 159{,}1\;\Omega$$

$$\underline{Z} = 100 + i(157{,}1 - 159{,}1) = 100 - 2i\;\Omega$$

$$\arg(\underline{Z}) = \arctan\!\left(\frac{-2}{100}\right) \approx -0{,}02\;\text{rad} \approx -1{,}1°$$

Le déphasage est quasi nul : on est très proche de la résonance ! (La tension est très légèrement en avance sur le courant en termes de retard capacitif.)

</details>

### Exercice 7.7 ⭐⭐⭐

Démontrez que l'amplitude du courant dans un circuit RLC série est maximale quand $\omega = \omega_0 = 1/\sqrt{LC}$.

<details>
<summary>Voir la réponse</summary>

L'amplitude du courant est :

$$|\underline{I}| = \frac{|\underline{V}|}{|\underline{Z}|} = \frac{V_m}{\sqrt{R^2 + (X_L - X_C)^2}}$$

$|\underline{I}|$ est maximal quand $|\underline{Z}|$ est minimal, soit quand $(X_L - X_C)^2$ est minimal (car $R$ est fixe).

Le minimum de $(X_L - X_C)^2 = (\omega L - 1/(\omega C))^2$ est atteint quand :

$$\omega L - \frac{1}{\omega C} = 0 \implies \omega^2 = \frac{1}{LC} \implies \omega = \frac{1}{\sqrt{LC}} = \omega_0$$

À la résonance : $|\underline{Z}| = R$ et $|\underline{I}|_{\max} = V_m/R$. $\square$

</details>

### Exercice 7.8 ⭐⭐⭐

Un circuit RC série ($R = 900\;\Omega$, $C = 3{,}5\;\mu\text{F}$) est alimenté par $V_e(t) = 220\sin(2\pi \times 50\,t)$ V. Calculez le phaseur de la tension aux bornes du condensateur et le déphasage par rapport à $V_e$.

<details>
<summary>Voir la réponse</summary>

$\omega = 2\pi \times 50 = 314{,}2\;\text{rad/s}$

$X_C = 1/(\omega C) = 1/(314{,}2 \times 3{,}5 \times 10^{-6}) = 909\;\Omega$

Impédance totale : $\underline{Z} = R - iX_C = 900 - 909i\;\Omega$

$|\underline{Z}| = \sqrt{900^2 + 909^2} = \sqrt{810000 + 826281} = \sqrt{1636281} \approx 1279\;\Omega$

Phaseur d'entrée : $\underline{V}_e = -220i$ (car $\sin(\omega t) = \cos(\omega t - \pi/2)$, donc $\underline{V}_e = 220e^{-i\pi/2}$).

Courant : $\underline{I} = \underline{V}_e/\underline{Z} = \frac{-220i}{900 - 909i}$

$\underline{V}_C = -iX_C \cdot \underline{I} = \frac{-iX_C(-220i)}{900 - 909i} = \frac{-220 \times 909}{900 - 909i} = \frac{-199980}{900 - 909i}$

On multiplie haut et bas par le conjugué :

$\underline{V}_C = \frac{-199980(900 + 909i)}{900^2 + 909^2} = \frac{-199980(900 + 909i)}{1636281}$

$\underline{V}_C \approx -109{,}9 - 110{,}9i$

$|\underline{V}_C| \approx \sqrt{109{,}9^2 + 110{,}9^2} \approx 156{,}2\;\text{V}$

Déphasage de $\underline{V}_C$ par rapport à $\underline{V}_e$ : environ $-\pi/4$ (retard d'un quart de période).

</details>

### Exercice 7.9 ⭐⭐⭐

Trouvez la résistance $R$ pour que la largeur de résonance d'un circuit RLC ($L = 1\;\text{mH}$, $C$ variable) soit de $\Delta f = 100\;\text{Hz}$.

<details>
<summary>Voir la réponse</summary>

Largeur de résonance : $\Omega = R/(2L)$, et $\Delta\omega = 2\Omega$ pour la largeur totale à mi-amplitude en puissance (c'est la convention usuelle).

$\Delta\omega = 2\pi \times \Delta f = 2\pi \times 100 = 628\;\text{rad/s}$

$\Omega = \Delta\omega / 2 = 314\;\text{rad/s}$

$$R = 2L\Omega = 2 \times 10^{-3} \times 314 = 0{,}628\;\Omega$$

</details>

### Exercice 7.10 ⭐⭐⭐

Montrez que le facteur de qualité d'un circuit RLC série vaut $Q = \frac{1}{R}\sqrt{\frac{L}{C}}$.

<details>
<summary>Voir la réponse</summary>

Par définition, $Q = \frac{\omega_0}{2\alpha}$ avec $\omega_0 = 1/\sqrt{LC}$ et $\alpha = R/(2L)$ :

$$Q = \frac{1/\sqrt{LC}}{2 \cdot R/(2L)} = \frac{1/\sqrt{LC}}{R/L} = \frac{L}{R\sqrt{LC}} = \frac{\sqrt{L}}{R\sqrt{C}} = \frac{1}{R}\sqrt{\frac{L}{C}} \quad \square$$

</details>

### Exercice 7.11 ⭐⭐⭐⭐

Un circuit RC série ($R = 1{,}3\;\text{k}\Omega$, $C = 3{,}2\;\mu\text{F}$) est alimenté par une tension efficace de $220\;\text{V}$. Trouvez la fréquence $f$ pour que le courant ait un déphasage de $\pi/4$ sur la tension. Calculez l'amplitude du courant et la puissance moyenne.

<details>
<summary>Voir la réponse</summary>

$\underline{Z} = R - iX_C$ avec $X_C = 1/(\omega C)$.

Déphasage du courant sur la tension = $-\arg(\underline{Z}) = \pi/4$ → $\arg(\underline{Z}) = -\pi/4$.

$$\arctan\!\left(\frac{-X_C}{R}\right) = -\frac{\pi}{4} \implies X_C = R$$

$$\frac{1}{\omega C} = R \implies \omega = \frac{1}{RC} = \frac{1}{1300 \times 3{,}2 \times 10^{-6}} = 240{,}4\;\text{rad/s}$$

$$f = \frac{\omega}{2\pi} \approx 38{,}3\;\text{Hz}$$

Amplitude : $|\underline{Z}| = \sqrt{R^2 + R^2} = R\sqrt{2} = 1300\sqrt{2} \approx 1838\;\Omega$

$V_m = V_{\text{eff}}\sqrt{2} = 220\sqrt{2}\;\text{V}$

$I_m = V_m/|\underline{Z}| = 220\sqrt{2}/(1300\sqrt{2}) = 220/1300 \approx 0{,}169\;\text{A}$

Puissance moyenne : $P_m = I_{\text{eff}}V_{\text{eff}}\cos\varphi = \frac{I_m}{\sqrt{2}}\cdot 220 \cdot \cos(\pi/4) = \frac{0{,}169}{\sqrt{2}} \times 220 \times \frac{1}{\sqrt{2}} = \frac{0{,}169 \times 220}{2} \approx 18{,}6\;\text{W}$

</details>

### Exercice 7.12 ⭐⭐⭐⭐

Un ressort idéal (constante $\kappa$) a une extrémité mobile qui subit le mouvement $x_S(t) = a\cos(\omega t)$. La masse $m$ est à l'autre extrémité. Établissez l'équation du mouvement de $m$ et trouvez la solution harmonique.

<details>
<summary>Voir la réponse</summary>

La force du ressort dépend de l'élongation **relative** : $f = -\kappa(x - x_S)$.

Newton : $m\ddot{x} = -\kappa(x - a\cos\omega t) = -\kappa x + \kappa a\cos\omega t$

$$\ddot{x} + \omega_0^2 x = \omega_0^2 a\cos(\omega t) \quad \text{avec} \quad \omega_0 = \sqrt{\kappa/m}$$

En phaseur ($\underline{x} \to \underline{X}$) :

$$-\omega^2\underline{X} + \omega_0^2\underline{X} = \omega_0^2 a$$

$$\underline{X} = \frac{\omega_0^2 a}{\omega_0^2 - \omega^2}$$

Pour $\omega < \omega_0$ : $\underline{X} > 0$ → en phase avec la force. Pour $\omega > \omega_0$ : $\underline{X} < 0$ → en opposition de phase. Pour $\omega = \omega_0$ : $|\underline{X}| \to \infty$ → résonance non amortie !

Avec frottement ($\lambda\dot{x}$) : le dénominateur devient $\omega_0^2 - \omega^2 + 2\alpha i\omega$ → amplitude finie.

</details>

### Exercice 7.13 ⭐⭐⭐⭐

On alimente un circuit LC idéal ($L$ et $C$) avec $V(t) = V_m\sin(\omega t)$. Montrez qu'il existe une pulsation $\omega_0$ pour laquelle le courant s'annule. Calculez la puissance moyenne délivrée par la source.

<details>
<summary>Voir la réponse</summary>

Impédance : $\underline{Z} = i\omega L + \frac{1}{i\omega C} = i\left(\omega L - \frac{1}{\omega C}\right)$

Courant : $\underline{I} = \underline{V}/\underline{Z}$

Le courant s'annule quand $|\underline{Z}| \to \infty$ : impossible (sauf si $\omega L = 1/(\omega C)$, là $\underline{Z} = 0$).

**Correction :** Dans un circuit LC parallèle, l'impédance est infinie quand $\omega L = 1/(\omega C)$. Pour un circuit LC **série**, c'est l'inverse : l'impédance s'annule à la résonance.

Ici en série : $\underline{Z} = i(\omega L - 1/(\omega C))$ est purement imaginaire.

$|\underline{I}| = V_m/|\omega L - 1/(\omega C)|$.

$I = 0$ quand $|\underline{Z}| \to \infty$, i.e., jamais en série. **Mais** $I \to \infty$ quand $\omega_0 = 1/\sqrt{LC}$.

Il n'y a **pas** de $\omega$ pour laquelle le courant s'annule dans un circuit LC série (sans résistance). Si le circuit est **parallèle**, alors $\underline{Z} = i\omega L / (1 - \omega^2 LC)$ et $|\underline{Z}| \to \infty$ quand $\omega^2 = 1/(LC)$, ce qui fait $I = 0$.

Puissance : $P(t) = V(t) \cdot I(t)$. Comme $\underline{Z}$ est purement imaginaire, $\varphi = \pm\pi/2$, et $\langle P \rangle = V_{\text{eff}}I_{\text{eff}}\cos(\pi/2) = 0$. Un circuit LC idéal ne dissipe **aucune puissance en moyenne**.

</details>

### Exercice 7.14 ⭐⭐⭐⭐⭐

Démontrez que la puissance moyenne fournie par une source alternative à un circuit est $P_m = V_{\text{eff}}I_{\text{eff}}\cos\varphi$, où $\varphi$ est le déphasage courant-tension.

<details>
<summary>Voir la réponse</summary>

Soient $V(t) = V_m\cos(\omega t)$ et $I(t) = I_m\cos(\omega t + \varphi)$.

$$P(t) = V(t) \cdot I(t) = V_m I_m \cos(\omega t)\cos(\omega t + \varphi)$$

Identité trigonométrique : $2\cos(a)\cos(b) = \cos(a-b) + \cos(a+b)$

$$P(t) = \frac{V_m I_m}{2}\left[\cos(\varphi) + \cos(2\omega t + \varphi)\right]$$

Moyenne temporelle : $\langle\cos(2\omega t + \varphi)\rangle = 0$ (oscillation rapide), donc :

$$\langle P \rangle = \frac{V_m I_m}{2}\cos\varphi = \frac{V_m}{\sqrt{2}} \cdot \frac{I_m}{\sqrt{2}} \cdot \cos\varphi = V_{\text{eff}} I_{\text{eff}} \cos\varphi \quad \square$$

Le facteur $\cos\varphi$ s'appelle le **facteur de puissance**. Pour un circuit purement réactif ($\varphi = \pm\pi/2$), la puissance moyenne est **nulle**.

</details>

### Exercice 7.15 ⭐⭐⭐⭐⭐

Un filtre passe-bande RLC ($L = 10\;\text{mH}$, $R$ variable, $C$ variable) doit sélectionner la fréquence $f_0 = 500\;\text{Hz}$ et atténuer $f = 1000\;\text{Hz}$ d'un facteur 2. Calculez $C$ et $R$.

<details>
<summary>Voir la réponse</summary>

**Fréquence de résonance :** $\omega_0 = 2\pi f_0 = 3142\;\text{rad/s}$

$$C = \frac{1}{\omega_0^2 L} = \frac{1}{3142^2 \times 0{,}01} = \frac{1}{98762} \approx 10{,}1\;\mu\text{F}$$

**Atténuation à $2f_0$ :** La tension de sortie (aux bornes de R) est $|\underline{V}_{\text{out}}| = R|\underline{I}| = R \cdot |\underline{V}|/|\underline{Z}|$.

La fonction de transfert est $T(\omega) = R/|\underline{Z}|$. On veut $T(2\omega_0) = 1/2$, soit $|\underline{Z}(2\omega_0)| = 2R$.

À $\omega = 2\omega_0$ : $X_L = 2\omega_0 L = 62{,}8\;\Omega$ et $X_C = 1/(2\omega_0 C) = 1/(6284 \times 10{,}1 \times 10^{-6}) = 15{,}8\;\Omega$.

$X_L - X_C = 62{,}8 - 15{,}8 = 47{,}0\;\Omega$

$|\underline{Z}| = \sqrt{R^2 + 47^2} = 2R \implies 4R^2 = R^2 + 2209 \implies R^2 = 736 \implies R = 27{,}1\;\Omega$

</details>


## Chapitre 8 — Ondes de corde et de compression

### Exercice 8.1 ⭐

Une corde de guitare a une masse linéique $\mu = 3\;\text{g/m}$ et est tendue avec $F_T = 80\;\text{N}$. Calculez la vitesse de propagation.

<details><summary>Voir la réponse</summary>

$$v = \sqrt{\frac{F_T}{\mu}} = \sqrt{\frac{80}{3 \times 10^{-3}}} = \sqrt{26667} \approx 163\;\text{m/s}$$

</details>

### Exercice 8.2 ⭐

Vérifiez que $f(z,t) = A\sin(z - vt)$ est solution de l'équation d'onde $\partial_t^2 f = v^2 \partial_z^2 f$.

<details><summary>Voir la réponse</summary>

$\partial_t f = -vA\cos(z-vt)$, $\partial_t^2 f = -v^2 A\sin(z-vt)$

$\partial_z f = A\cos(z-vt)$, $\partial_z^2 f = -A\sin(z-vt)$

$v^2 \partial_z^2 f = -v^2 A\sin(z-vt) = \partial_t^2 f$ ✓

</details>

### Exercice 8.3 ⭐

La fonction $h(z,t) = e^{-(z-vt)^2}$ est-elle solution de l'équation d'onde ? Interprétez physiquement.

<details><summary>Voir la réponse</summary>

Il suffit de vérifier que c'est une fonction de $u = z - vt$ seul. Comme $h = e^{-u^2}$ avec $u = z - vt$, c'est bien une solution de d'Alembert. C'est un **paquet d'onde** gaussien se propageant à vitesse $v$ vers les $z$ positifs sans déformation.

</details>

### Exercice 8.4 ⭐⭐

Montrez que la vitesse d'onde sur une corde a les dimensions d'une vitesse à partir de $F_T/\mu$.

<details><summary>Voir la réponse</summary>

$[F_T] = \text{N} = \text{kg}\cdot\text{m}/\text{s}^2$, $[\mu] = \text{kg/m}$

$$\left[\frac{F_T}{\mu}\right] = \frac{\text{kg}\cdot\text{m}/\text{s}^2}{\text{kg/m}} = \frac{\text{m}^2}{\text{s}^2} \implies \sqrt{F_T/\mu} \;\text{a les dimensions de m/s} \;\checkmark$$

</details>

### Exercice 8.5 ⭐⭐

On double la tension d'une corde. Par quel facteur la vitesse de propagation change-t-elle ?

<details><summary>Voir la réponse</summary>

$$v' = \sqrt{\frac{2F_T}{\mu}} = \sqrt{2}\,v$$

La vitesse est multipliée par $\sqrt{2} \approx 1{,}41$.

</details>

### Exercice 8.6 ⭐⭐

Si $x_1 = 3\cos(2z - 6t)$ et $x_2 = 5\sin(2z + 6t)$ sont solutions, montrez que $x_1 + x_2$ est aussi solution et identifiez $v$.

<details><summary>Voir la réponse</summary>

$x_1 = f(z - 3t)$ avec $v = 3\;\text{m/s}$ (progressive), $x_2 = g(z + 3t)$ (régressive, même $v$).

Par le principe de superposition (linéarité), $x_1 + x_2$ est solution. $v = \omega/k = 6/2 = 3\;\text{m/s}$.

</details>

### Exercice 8.7 ⭐⭐

Dans un cristal 1D, les atomes ($m = 4 \times 10^{-26}\;\text{kg}$, $d = 3\;\text{Å}$) sont liés par $\kappa_c = 15\;\text{N/m}$. Calculez la vitesse du son.

<details><summary>Voir la réponse</summary>

$$v = d\sqrt{\frac{\kappa_c}{m}} = 3 \times 10^{-10}\sqrt{\frac{15}{4 \times 10^{-26}}} = 3 \times 10^{-10} \times \sqrt{3{,}75 \times 10^{26}}$$

$$= 3 \times 10^{-10} \times 6{,}12 \times 10^{13} \approx 1837\;\text{m/s} \approx 5{,}5\;\text{km/s}$$

Ordre de grandeur typique pour un solide cristallin.

</details>

### Exercice 8.8 ⭐⭐⭐

Calculez la vitesse du son dans l'air à $T = 20°\text{C}$, $P = 1{,}013 \times 10^5\;\text{Pa}$, $\rho = 1{,}2\;\text{kg/m}^3$, $\gamma = 1{,}4$.

<details><summary>Voir la réponse</summary>

$$v = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{1{,}4 \times 1{,}013 \times 10^5}{1{,}2}} = \sqrt{\frac{1{,}418 \times 10^5}{1{,}2}} = \sqrt{1{,}182 \times 10^5} \approx 344\;\text{m/s}$$

</details>

### Exercice 8.9 ⭐⭐⭐

Dérivez l'équation d'onde pour une corde à partir de la loi de Newton appliquée au segment $n$. Montrez que $\ddot{x}_n = \frac{F_T}{\mu\Delta l^2}(x_{n-1} + x_{n+1} - 2x_n)$ tend vers $v^2\partial^2 x/\partial z^2$.

<details><summary>Voir la réponse</summary>

Newton : $m\ddot{x}_n = -F_T(\theta_n + \theta'_n)$ avec $\theta_n = (x_n - x_{n-1})/\Delta l$, $\theta'_n = (x_n - x_{n+1})/\Delta l$.

$$\mu\Delta l\,\ddot{x}_n = \frac{F_T}{\Delta l}(x_{n-1} + x_{n+1} - 2x_n)$$

$$\ddot{x}_n = \frac{F_T}{\mu}\cdot\frac{x_{n-1} + x_{n+1} - 2x_n}{\Delta l^2}$$

Quand $\Delta l \to 0$, le terme de droite est la définition de $\frac{\partial^2 x}{\partial z^2}$ :

$$\frac{\partial^2 x}{\partial t^2} = \frac{F_T}{\mu}\frac{\partial^2 x}{\partial z^2} = v^2\frac{\partial^2 x}{\partial z^2} \quad \square$$

</details>

### Exercice 8.10 ⭐⭐⭐

Interprétez physiquement : pourquoi l'accélération d'un point de la corde est-elle proportionnelle à sa courbure locale ?

<details><summary>Voir la réponse</summary>

Si la corde est rectiligne en un point ($\partial^2 x/\partial z^2 = 0$), les forces de tension de part et d'autre sont alignées et se compensent → force nette nulle → pas d'accélération.

Si la corde est courbée vers le haut ($\partial^2 x/\partial z^2 > 0$), les voisins sont **plus hauts** en moyenne → les forces de tension tirent le point **vers le haut** → accélération positive.

Plus la courbure est forte, plus le déséquilibre est grand → accélération proportionnelle à la courbure. Le facteur $v^2 = F_T/\mu$ traduit : plus de tension = plus de force, plus de masse = plus d'inertie.

</details>

### Exercice 8.11 ⭐⭐⭐

Une impulsion triangulaire $x(z,0) = A(1 - |z|/L)$ pour $|z| < L$ et 0 sinon se propage sur une corde de vitesse $v$. Décrivez son évolution.

<details><summary>Voir la réponse</summary>

Par d'Alembert, si la vitesse initiale est nulle : $x(z,t) = \frac{1}{2}[f(z-vt) + f(z+vt)]$ où $f$ est la forme initiale.

L'impulsion se **sépare** en deux demi-impulsions d'amplitude $A/2$ :
- une progressive $\frac{A}{2}(1-|z-vt|/L)$ se déplaçant vers $z > 0$
- une régressive $\frac{A}{2}(1-|z+vt|/L)$ vers $z < 0$

La forme triangulaire se conserve (pas de dispersion dans l'éq. d'onde standard).

</details>

### Exercice 8.12 ⭐⭐⭐⭐

Montrez que $x(z,t) = A\cos(kz)\cos(\omega t)$ est solution de l'éq. d'onde si $\omega = kv$. Montrez que c'est la superposition de deux ondes contra-propagatives.

<details><summary>Voir la réponse</summary>

$\partial_t^2 x = -A\omega^2\cos(kz)\cos(\omega t)$, $\partial_z^2 x = -Ak^2\cos(kz)\cos(\omega t)$

$v^2\partial_z^2 x = -v^2k^2 A\cos(kz)\cos(\omega t)$. Pour que $= \partial_t^2 x$ : $\omega^2 = v^2k^2 \implies \omega = kv$. ✓

Par Simpson : $\cos(kz)\cos(\omega t) = \frac{1}{2}[\cos(kz - \omega t) + \cos(kz + \omega t)]$

$$x = \frac{A}{2}\cos(kz - \omega t) + \frac{A}{2}\cos(kz + \omega t)$$

C'est bien la somme d'une onde progressive et d'une onde régressive d'amplitude $A/2$. $\square$

</details>

### Exercice 8.13 ⭐⭐⭐⭐

Comparez la vitesse du son dans l'eau ($K = 2{,}2\;\text{GPa}$, $\rho = 1000\;\text{kg/m}^3$) et dans l'acier ($K = 160\;\text{GPa}$, $\rho = 7800\;\text{kg/m}^3$). Pourquoi le son va-t-il plus vite dans les solides ?

<details><summary>Voir la réponse</summary>

Eau : $v = \sqrt{2{,}2 \times 10^9 / 1000} = \sqrt{2{,}2 \times 10^6} \approx 1483\;\text{m/s}$

Acier : $v = \sqrt{160 \times 10^9 / 7800} = \sqrt{2{,}05 \times 10^7} \approx 4530\;\text{m/s}$

Le son est **~3× plus rapide** dans l'acier. La rigidité ($K$) augmente beaucoup plus vite que la densité $\rho$. Les solides sont « plus durs à comprimer » → les perturbations se transmettent plus vite entre atomes voisins.

</details>

### Exercice 8.14 ⭐⭐⭐⭐⭐

Un câble de $L = 10\;\text{m}$ ($\mu = 50\;\text{g/m}$, $F_T = 200\;\text{N}$) est frappé à une extrémité. Combien de temps met le signal pour un aller-retour ?

<details><summary>Voir la réponse</summary>

$v = \sqrt{200/(50 \times 10^{-3})} = \sqrt{4000} \approx 63{,}2\;\text{m/s}$

Aller-retour = $2L/v = 20/63{,}2 \approx 0{,}316\;\text{s}$

</details>

### Exercice 8.15 ⭐⭐⭐⭐⭐

On frappe ses mains dans une pièce de $L = 20\;\text{m}$. Calculez le temps entre l'émission et la réception de l'écho. Est-ce perceptible ? ($v_{\text{son}} = 343\;\text{m/s}$)

<details><summary>Voir la réponse</summary>

Aller-retour : $t = 2L/v = 40/343 \approx 0{,}117\;\text{s} \approx 117\;\text{ms}$

L'oreille humaine distingue deux sons séparés de $\gtrsim 50\;\text{ms}$, donc oui, l'écho est perceptible dans une pièce de 20 m.

Pour un couloir de 8 m : $t = 16/343 \approx 47\;\text{ms}$, à la limite de perception.

</details>


## Chapitre 9 — Ondes électromagnétiques

### Exercice 9.1 ⭐

Calculez la valeur de $c$ à partir de $\mu_0 = 4\pi \times 10^{-7}\;\text{T}\cdot\text{m/A}$ et $\varepsilon_0 = 8{,}854 \times 10^{-12}\;\text{F/m}$.

<details><summary>Voir la réponse</summary>

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = \frac{1}{\sqrt{4\pi \times 10^{-7} \times 8{,}854 \times 10^{-12}}} = \frac{1}{\sqrt{1{,}1126 \times 10^{-17}}} = \frac{1}{\sqrt{11{,}126 \times 10^{-18}}}$$

$$c = \frac{1}{3{,}335 \times 10^{-9}} \approx 2{,}998 \times 10^8 \;\text{m/s}$$

</details>

### Exercice 9.2 ⭐

Une onde radio FM a une fréquence $f = 100\;\text{MHz}$. Quelle est sa longueur d'onde spatiale ?

<details><summary>Voir la réponse</summary>

$$\lambda = \frac{c}{f} = \frac{3 \times 10^8}{100 \times 10^6} = \frac{3 \times 10^8}{10^8} = 3\;\text{m}$$

</details>

### Exercice 9.3 ⭐

Un laser rouge hélium-néon émet à $\lambda = 632{,}8\;\text{nm}$. Calculez sa fréquence et son nombre d'onde $k$.

<details><summary>Voir la réponse</summary>

$$f = \frac{c}{\lambda} = \frac{3 \times 10^8}{632{,}8 \times 10^{-9}} \approx 4{,}74 \times 10^{14}\;\text{Hz} = 474\;\text{THz}$$

$$k = \frac{2\pi}{\lambda} = \frac{2\pi}{632{,}8 \times 10^{-9}} \approx 9{,}93 \times 10^6 \;\text{m}^{-1}$$

</details>

### Exercice 9.4 ⭐⭐

Démontrez l'identité $\text{rot}(\text{rot}\vec{E}) = \vec{\nabla}(\text{div}\vec{E}) - \Delta\vec{E}$ en coordonnées cartésiennes pour un champ $\vec{E} = (E_x, 0, 0)$ dépendant uniquement de $z$.

<details><summary>Voir la réponse</summary>

$\vec{E} = E_x(z)\vec{1}_x$.

$\text{div}\vec{E} = \partial_x E_x = 0$ car $E_x$ ne dépend que de $z$. Donc $\vec{\nabla}(\text{div}\vec{E}) = \vec{0}$.

$\text{rot}\vec{E} = (\partial_y E_z - \partial_z E_y, \partial_z E_x - \partial_x E_z, \partial_x E_y - \partial_y E_x) = (0, \partial_z E_x, 0)$.

$\text{rot}(\text{rot}\vec{E}) = \text{rot}(0, \partial_z E_x, 0) = (-\partial_z(\partial_z E_x), 0, 0) = (-\partial_z^2 E_x, 0, 0)$.

Par ailleurs, $\Delta\vec{E} = (\Delta E_x, \Delta E_y, \Delta E_z) = (\partial_z^2 E_x, 0, 0)$.

Donc $\text{rot}(\text{rot}\vec{E}) = -\Delta\vec{E} = \vec{\nabla}(\text{div}\vec{E}) - \Delta\vec{E}$. L'identité est vérifiée pour ce cas simple.

</details>

### Exercice 9.5 ⭐⭐

On allume brusquement un courant surfacique uniforme sur le plan $z=0$, $J_s(t) = J_0$ pour $t > 0$. Tracez qualitativement $B(z,t)$ pour $z>0$ à un instant $t_0 > 0$.

<details><summary>Voir la réponse</summary>

L'onde est émise en $z=0$ : $B(0,t) = \frac{\mu_0}{2}J_0$ pour $t>0$.

La solution est $B(z,t) = B(0, t - z/c)$.

À $t=t_0$, le front d'onde est arrivé en $z = ct_0$.

Pour $z < ct_0$, $t - z/c > 0 \implies B = \frac{\mu_0}{2}J_0$.

Pour $z > ct_0$, $t - z/c < 0 \implies B = 0$.

Le profil spatial est donc un **créneau spatial** (une « marche ») qui avance à la vitesse $c$.

</details>

### Exercice 9.6 ⭐⭐

Une onde s'écrit $\vec{E}(z,t) = E_0\cos(10^7 z + 3 \times 10^{15} t)\vec{1}_x$. Dans quelle direction et dans quel sens se propage-t-elle ? Calculez sa vitesse.

<details><summary>Voir la réponse</summary>

La phase est $\phi = 10^7 z + 3 \times 10^{15} t = k z + \omega t$.

L'argument est de la forme $z + vt$, donc c'est une onde **régressive** : elle se propage dans la direction de l'axe $z$, dans le sens des **$z$ décroissants** (vers les $z$ négatifs).

La vitesse est $v = \frac{\omega}{k} = \frac{3 \times 10^{15}}{10^7} = 3 \times 10^8 \;\text{m/s} = c$. C'est bien une onde électromagnétique dans le vide.

</details>

### Exercice 9.7 ⭐⭐⭐

Pourquoi considérer la dérivée temporelle dans l'équation d'Ampère (le terme de Maxwell) était-il indispensable pour obtenir des ondes ?

<details><summary>Voir la réponse</summary>

L'équation historique d'Ampère dans le vide était $\text{rot}\vec{B} = \vec{0}$ (sans charges ni courants).

Si on prend le rotationnel de la loi de Faraday : $\text{rot}(\text{rot}\vec{E}) = -\partial_t(\text{rot}\vec{B}) = -\partial_t(\vec{0}) = \vec{0}$.

On aurait $-\Delta\vec{E} = \vec{0}$ au lieu de $-\Delta\vec{E} + \mu_0\varepsilon_0\partial_t^2\vec{E} = \vec{0}$.

Sans le courant de déplacement $\varepsilon_0\partial_t\vec{E}$, la dérivée temporelle seconde n'apparaît pas. Le champ s'ajusterait instantanément dans tout l'espace (vitesse infinie), ce qui est absurde. L'ajout de Maxwell couple de façon dynamique $E$ et $B$ dans les deux sens et donne un terme inertiel à la propagation.

</details>

### Exercice 9.8 ⭐⭐⭐

Montrez qu'une onde plane électromagnétique $\vec{E} = \vec{E}_0 e^{i(kz-\omega t)}$ dans le vide est forcément **transversale** ($\vec{E}_0 \cdot \vec{1}_z = 0$).

<details><summary>Voir la réponse</summary>

On utilise l'équation de Maxwell-Gauss dans le vide : $\text{div}\vec{E} = 0$.

$\vec{E} = (E_{0x}e^{i(kz-\omega t)}, E_{0y}e^{i(kz-\omega t)}, E_{0z}e^{i(kz-\omega t)})$.

$\text{div}\vec{E} = \partial_x E_x + \partial_y E_y + \partial_z E_z = 0 + 0 + \partial_z(E_{0z}e^{i(kz-\omega t)}) = ik E_{0z} e^{i(kz-\omega t)}$.

Pour que $\text{div}\vec{E} = 0$ partout, il faut $E_{0z} = 0$.

Le champ $\vec{E}$ n'a pas de composante longitudinale (selon $z$, sa direction de propagation). Il est purement dans le plan $(x, y)$. Il est **transversal**.

</details>

### Exercice 9.9 ⭐⭐⭐

Un pointeur laser vert ($\lambda = 532\;\text{nm}$) a une puissance de $1\;\text{mW}$. Quel est le nombre de paquets d'onde (longueur de l'onde dans le temps) produits chaque seconde ?

<details><summary>Voir la réponse</summary>

C'est une question piège pour introduire à la structure ondulatoire. On demande en fait la fréquence spatiale. L'onde électromagnétique est continue dans ce modèle très classique (bien qu'un laser émette des photons). Le nombre d'oscillations ("cycles" complets de l'onde) par seconde est la **fréquence** $f$.

$$f = \frac{c}{\lambda} = \frac{3 \times 10^8}{532 \times 10^{-9}} \approx 5{,}64 \times 10^{14}\;\text{Hz}$$

Le laser génère donc environ $\sim 5{,}64 \times 10^{14}$ crêtes d'ondes par seconde.

</details>

### Exercice 9.10 ⭐⭐⭐⭐

Justifiez pourquoi une onde plane, dans sa formulation stricte (d'amplitude uniforme à l'infini dans le plan $(x,y)$), a une énergie infinie, ce qui la rend physiquement impossible comme objet unique, bien qu'elle soit une base mathématique utile.

<details><summary>Voir la réponse</summary>

L'énergie d'une onde EM par unité de volume est proportionnelle à $|\vec{E}|^2$.

Si l'onde est rigoureusement plane, le champ $\vec{E}$ a la même amplitude non nulle sur **tout** le plan $(x,y)$, dont la surface est infinie. L'intégrale de la densité d'énergie sur tout le plan est donc infinie pour chaque tranche $dz$.

Une onde réelle est toujours un **faisceau** d'extension finie (par exemple profil gaussien, comme un laser). L'onde plane est une approximation mathématique valable « au centre » d'un large faisceau, ou elle sert de composante de Fourier pour construire un paquet d'onde fini.

</details>

### Exercice 9.11 ⭐⭐⭐⭐

Sachant que $\text{rot}\vec{E} = -\partial_t\vec{B}$, trouvez la relation entre les amplitudes $\vec{E}_0$ et $\vec{B}_0$ pour une onde plane progressive $\vec{E} = E_0\cos(kz-\omega t)\vec{1}_x$.

<details><summary>Voir la réponse</summary>

$\text{rot}\vec{E} = (0, \partial_z E_x, 0)$ car $\vec{E}$ est selon $x$ et ne dépend que de $z$.

$\partial_z E_x = -k E_0 \sin(kz-\omega t)$. Donc $\text{rot}\vec{E} = (0, -k E_0 \sin(kz-\omega t), 0)$.

Par ailleurs, $-\partial_t\vec{B} = \text{rot}\vec{E}$.

On intègre selon le temps pour trouver $\vec{B}$ (en fixant la constante à 0 pour une onde pure) :

$\vec{B} = \int (0, k E_0 \sin(kz-\omega t), 0) \,dt = (0, \frac{k}{\omega} E_0 \cos(kz-\omega t), 0)$

Comme $k/\omega = 1/c$ :

$$\vec{B} = \frac{E_0}{c}\cos(kz-\omega t)\vec{1}_y = \frac{1}{c}(\vec{1}_z \times \vec{E})$$

On observe : $\vec{B}_0$ et $\vec{E}_0$ sont en phase, orthogonaux (trièdre direct $\vec{E}, \vec{B}, \vec{v}$), et liés par $E_0 = cB_0$.

</details>


## Chapitre 10 — Ondes stationnaires, battements et effet Doppler

### Exercice 10.1 ⭐

Une corde de 2 m fixée à ses 2 extrémités a une onde stationnaire avec 3 ventres. Quelle est la longueur d'onde ?

<details><summary>Voir la réponse</summary>

Mode $n=3$ (3 ventres). $\lambda_n = 2L/n$.

$\lambda_3 = \frac{2 \times 2}{3} = 1{,}33\;\text{m}$.

</details>

### Exercice 10.2 ⭐

On entend deux notes simultanément : 440 Hz et 444 Hz. Quelle est la fréquence du battement perçu ?

<details><summary>Voir la réponse</summary>

$f_B = |f_1 - f_2| = |440 - 444| = 4\;\text{Hz}$. On entend 4 modulations (pulsations sonores) par seconde.

La note entendue oscille à la fréquence moyenne : $(440 + 444)/2 = 442\;\text{Hz}$.

</details>

### Exercice 10.3 ⭐

Une sirène d'ambulance (800 Hz) s'approche d'un piéton immobile à 30 m/s. Le son va à 340 m/s. Quelle est la fréquence perçue ?

<details><summary>Voir la réponse</summary>

L'ambulance s'approche : la fréquence augmente, donc le dénominateur doit être plus petit. $(v_0 = 0, v_S = 30)$.

$$f' = f \left(\frac{v}{v - v_S}\right) = 800 \left(\frac{340}{340 - 30}\right) = 800 \left(\frac{340}{310}\right) \approx 877\;\text{Hz}$$

</details>

### Exercice 10.4 ⭐⭐

L'ambulance de l'exo 10.3 s'éloigne maintenant du piéton à 30 m/s. Quelle est la nouvelle fréquence perçue ?

<details><summary>Voir la réponse</summary>

L'ambulance s'éloigne : la fréquence diminue, le dénominateur doit grandir.

$$f' = f \left(\frac{v}{v + v_S}\right) = 800 \left(\frac{340}{340 + 30}\right) = 800 \left(\frac{340}{370}\right) \approx 735\;\text{Hz}$$

On passe aigu-grave : le fameux "piiinn-paaann" compressé puis étiré.

</details>

### Exercice 10.5 ⭐⭐

Un observateur roule à 20 m/s **vers** une sirène fixe d'usine (500 Hz). $v = 340$ m/s. Fréquence perçue ?

<details><summary>Voir la réponse</summary>

L'observateur s'approche : le son lui arrive "plus vite". Fréquence augmente, on prend le (+) au numérateur. $(v_0 = 20, v_S = 0)$.

$$f' = f \left(\frac{v + v_0}{v}\right) = 500 \left(\frac{340 + 20}{340}\right) = 500 \left(\frac{360}{340}\right) \approx 529\;\text{Hz}$$

</details>

### Exercice 10.6 ⭐⭐

Montrez la distance spatiale entre deux nœuds consécutifs d'une onde stationnaire s'exprime de manière très simple.

<details><summary>Voir la réponse</summary>

Onde stationnaire spatiale : $\sin(kz)$. Nœuds quand $kz = m\pi$.

Position du nœud $m$ : $z_m = m\pi / k$.

Distance entre nœuds voisins : $z_{m+1} - z_m = \pi / k$. Or $k = 2\pi/\lambda$.

Donc $z_{m+1} - z_m = \frac{\pi}{2\pi/\lambda} = \frac{\lambda}{2}$.

Deux nœuds (ou deux ventres) consécutifs sont séparés d'une **demi-longueur d'onde**. $\square$

</details>

### Exercice 10.7 ⭐⭐⭐

Un flûtiste avec un tuyau ouvert aux deux bouts veut jouer un la (440 Hz) comme fondamentale (mode fondamental $n=1$). Quelle doit être la longueur du tuyau ? ($v = 343$ m/s).

<details><summary>Voir la réponse</summary>

Un tuyau ouvert aux deux bouts impose un ventres de déplacement (ou nœud de pression acoustique) à chaque bout. La distance entre deux ventres consécutifs est $\lambda/2$.

Pour le fondamental, la longueur $L = \lambda/2$, donc $\lambda = 2L$.

$f = \frac{v}{\lambda} = \frac{v}{2L} \implies L = \frac{v}{2f}$.

$L = \frac{343}{2 \times 440} = \frac{343}{880} \approx 0{,}39\;\text{m} = 39\;\text{cm}$.

</details>

### Exercice 10.8 ⭐⭐⭐

On superpose $\cos(2z-10t)$ et $\cos(2z+10t)$. Décrivez l'onde résultante (pulsation, k, nœuds, ventres, vitesse de phase spatiale s'il y en a).

<details><summary>Voir la réponse</summary>

On somme une onde progressive et régressive de mêmes paramètres $(A=1, k=2, \omega=10)$. C'est une onde stationnaire.

$\cos(2z-10t) + \cos(2z+10t) = 2\cos(2z)\cos(10t)$ (parité du cos et Simpson).

Pulsation intrinsèque : $\omega = 10\;\text{rad/s}$.

Nombre d'onde spatial : $k = 2\;\text{m}^{-1}$.

Nœuds : $\cos(2z) = 0 \implies 2z = \pi/2 + m\pi \implies z = \frac{\pi}{4} + m\frac{\pi}{2}$.

Ventres : $\cos(2z) = \pm 1 \implies 2z = m\pi \implies z = m\frac{\pi}{2}$.

Vitesse de propagation : $0$ (c'est une onde stationnaire).

</details>

### Exercice 10.9 ⭐⭐⭐

Une chauve-souris s'approche d'un mur à 5 m/s et émet des ultrasons à 40 kHz. Calculez la fréquence de l'écho qu'elle perçoit en vol. ($v = 340$ m/s).

<details><summary>Voir la réponse</summary>

C'est un double effet Doppler.

1) Le mur (observateur fixe) reçoit le son de la chauve-souris s'approchant :
$$f_{mur} = f_0 \frac{v}{v - v_{CS}} = 40 \left(\frac{340}{340 - 5}\right) = 40 \left(\frac{340}{335}\right) \approx 40{,}60\;\text{kHz}$$

2) Le mur agit comme une source fixe émettant à $f_{mur}$. La chauve-souris (observateur en mouvement) s'en approche :
$$f_{écho} = f_{mur} \frac{v + v_{CS}}{v} = f_0 \left(\frac{v}{v - v_{CS}}\right) \left(\frac{v + v_{CS}}{v}\right) = f_0 \frac{v + v_{CS}}{v - v_{CS}}$$
$$f_{écho} = 40 \frac{340 + 5}{340 - 5} = 40 \frac{345}{335} \approx 41{,}19\;\text{kHz}$$

</details>

### Exercice 10.10 ⭐⭐⭐⭐

Deux diapasons, A et B. La fréquence de A est 256 Hz. Lorsqu'on les fait sonner ensemble, on entend 3 battements par seconde. On alourdit légèrement B avec de la cire, la fréquence de son battement avec A chute à 1 Hz. Quelle était la fréquence initiale de B ?

<details><summary>Voir la réponse</summary>

$f_A = 256\;\text{Hz}$. On a $|f_A - f_{B1}| = 3\;\text{Hz}$, donc $f_{B1}$ peut être de 253 Hz ou 259 Hz.

En ajoutant de la cire sur B, on l'alourdit. Un oscillateur plus lourd bat plus lentement : la fréquence $f_B$ doit **diminuer**. $f_{B2} < f_{B1}$.

Nouveau battement : $|f_A - f_{B2}| = 1\;\text{Hz}$. Donc la nouvelle fréquence s'est rapprochée de celle de $A$ (256 Hz).

- Si $f_{B1} = 259$ Hz : la cire fait baisser à $f_{B2} = 257$ Hz. Le battement est bien $|256 - 257| = 1$ Hz. Scénario cohérent.
- Si $f_{B1} = 253$ Hz : la cire fait baisser à $f_{B2} = 251$ Hz par exemple, le battement s'écarterait de $A$ et augmenterait ($|256 - 251| = 5$ Hz au lieu de 1 Hz). Contradiction.

Donc la fréquence initiale de B était bien **259 Hz**.

</details>

### Exercice 10.11 ⭐⭐⭐⭐

On trace la fonction d'onde stationnaire $y(x,t) = 0{,}05\sin(2\pi x)\cos(4\pi t)$. Exprimez cette onde comme la somme d'une onde d'amplitude progressive vers la droite et d'une onde régressive.

<details><summary>Voir la réponse</summary>

On utilise l'identité $\sin A \cos B = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$.

Ici $A = 2\pi x$, $B = 4\pi t$.

$$y(x,t) = \frac{0{,}05}{2} [\sin(2\pi x + 4\pi t) + \sin(2\pi x - 4\pi t)]$$

$$y(x,t) = 0{,}025 \sin(2\pi x - 4\pi t) + 0{,}025 \sin(2\pi x + 4\pi t)$$

Le premier terme est déphasé mais progresse vers la droite (les signes de x et t sont opposés), le second vers la gauche (mêmes signes). Les ondes initiales ont une amplitude de $0{,}025\;\text{m}$, un $k = 2\pi \;\text{m}^{-1}$ ($\lambda = 1\;\text{m}$) et $\omega = 4\pi\;\text{rad/s}$.

</details>
