# ⚡ Synthèse Complète — Physique (PHYSH1002)

> Synthèse regroupant les 5 chapitres du Volume I.

---

##  Chapitre1 Gradient

> **Cours** : PHYSH1002 — Électromagnétisme, Vol. I  

> **Thème** : Physique mésoscopique — Modélisation, courbes de niveau, gradient

---

### 1. Échelle mésoscopique et maillage

#### 1.1 Principe de la physique mésoscopique

La physique mésoscopique travaille à une échelle intermédiaire entre l'échelle microscopique (atomes) et macroscopique (objets). On décompose l'espace en **petits volumes** (éléments de maillage) suffisamment grands pour contenir beaucoup de particules, mais suffisamment petits pour considérer les grandeurs physiques comme uniformes.

#### 1.2 Maillage

- En **2D** : décomposition en **triangles** (chaque sommet porte une valeur de la grandeur physique)

- En **3D** : décomposition en **tétraèdres** (4 sommets)

- On associe à chaque élément une grandeur physique **moyennée** (densité, température, potentiel…)

> 💡 **Pourquoi des triangles/tétraèdres ?** Ils permettent de mailler n'importe quelle géométrie avec précision. C'est la base de la **méthode des éléments finis**.

---

### 2. Courbes de niveau et potentiel

#### 2.1 Courbes de niveau (isolignes)

- Lieux géométriques des points ayant la **même valeur** d'une grandeur scalaire (altitude, température, potentiel…)

- Les courbes de niveau **ne se croisent jamais** (sauf aux cols/points selle)

- Plus les courbes sont **rapprochées**, plus la variation est **rapide**

#### 2.2 Potentiel

Le **potentiel** est une grandeur scalaire associée à chaque point de l'espace :

$$V = V(x, y, z)$$

Les **surfaces équipotentielles** sont les généralisations 3D des courbes de niveau.

---

### 3. Le gradient

#### 3.1 Définition intuitive

Le **gradient** d'une fonction scalaire $f$ est un **vecteur** qui :

- Pointe dans la **direction de la plus grande croissance** de $f$

- A pour **norme** le taux de variation maximal de $f$

- Est **perpendiculaire** aux courbes de niveau

#### 3.2 Définition formelle (coordonnées cartésiennes)

$$\vec{\text{grad}}\, f = \frac{\partial f}{\partial x} \vec{1}_x + \frac{\partial f}{\partial y} \vec{1}_y + \frac{\partial f}{\partial z} \vec{1}_z$$

Notation avec l'opérateur **nabla** :

$$\vec{\nabla} f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$$

#### 3.3 Gradient dans d'autres systèmes de coordonnées

| Système | Expression de $\vec{\text{grad}}\, f$ |

|---------|--------------------------------------|

| **Cartésien** $(x,y,z)$ | $\frac{\partial f}{\partial x}\vec{1}_x + \frac{\partial f}{\partial y}\vec{1}_y + \frac{\partial f}{\partial z}\vec{1}_z$ |

| **Cylindrique** $(r,\theta,z)$ | $\frac{\partial f}{\partial r}\vec{1}_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec{1}_\theta + \frac{\partial f}{\partial z}\vec{1}_z$ |

| **Sphérique** $(r,\theta,\varphi)$ | $\frac{\partial f}{\partial r}\vec{1}_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec{1}_\theta + \frac{1}{r\sin\theta}\frac{\partial f}{\partial \varphi}\vec{1}_\varphi$ |

#### 3.4 Lien gradient–force

En physique, le gradient du potentiel donne la **force** (au signe près) :

$$\vec{F} = -\vec{\text{grad}}\, V$$

C'est le cas pour :

- La **force gravitationnelle** : $\vec{g} = -\vec{\text{grad}}\, V_g$

- La **force électrostatique** : $\vec{E} = -\vec{\text{grad}}\, V_e$

---

### 4. Dérivée directionnelle

La **dérivée directionnelle** de $f$ dans la direction $\vec{u}$ (unitaire) exprime le taux de variation de $f$ dans cette direction :

$$\frac{\partial f}{\partial \vec{u}} = \vec{\text{grad}}\, f \cdot \vec{u}$$

> 🔑 **Cas importants** :

> - Si $\vec{u}$ est parallèle au gradient : dérivée maximale

> - Si $\vec{u}$ est perpendiculaire au gradient : dérivée nulle (on se déplace sur une courbe de niveau)

> - Si $\vec{u}$ est antiparallèle au gradient : dérivée minimale (descente la plus rapide)

---

### 5. Base conjuguée et maillage

#### 5.1 Base conjuguée

Pour un maillage triangulaire, on définit la **base conjuguée** $\{\vec{c}_1, \vec{c}_2\}$ à partir des vecteurs d'arête $\{\vec{a}_1, \vec{a}_2\}$ :

$$\vec{c}_i \cdot \vec{a}_j = \delta_{ij}$$

où $\delta_{ij}$ est le symbole de **Kronecker** (= 1 si $i = j$, = 0 sinon).

#### 5.2 Gradient sur un triangle

Le gradient d'une quantité $f$ répartie sur les sommets d'un triangle se calcule :

$$\vec{\text{grad}}\, f = (f_2 - f_1)\vec{c}_1 + (f_3 - f_1)\vec{c}_2$$

où $f_1, f_2, f_3$ sont les valeurs aux sommets.

> 💡 **Application** : cette formule est à la base des méthodes numériques (éléments finis) pour résoudre les équations de la physique sur des géométries complexes.

---

### 6. Propriétés essentielles du gradient

| Propriété | Formule |

|-----------|---------|

| **Linéarité** | $\vec{\text{grad}}(af + bg) = a\,\vec{\text{grad}}\, f + b\,\vec{\text{grad}}\, g$ |

| **Produit** | $\vec{\text{grad}}(fg) = f\,\vec{\text{grad}}\, g + g\,\vec{\text{grad}}\, f$ |

| **Composition** | $\vec{\text{grad}}\, g(f) = g'(f) \vec{\text{grad}}\, f$ |

| **Rotationnel d'un gradient** | $\text{rot}(\vec{\text{grad}}\, f) = \vec{0}$ toujours |

---

### 🧠 Points clés à retenir

1. Le **gradient** transforme un champ **scalaire** en champ **vectoriel**

2. Il est toujours **perpendiculaire** aux courbes de niveau / surfaces équipotentielles

3. Il indique la direction de **croissance maximale**

4. Le **rotationnel d'un gradient est toujours nul** → un champ dérivant d'un potentiel est **conservatif**

5. La **base conjuguée** permet de calculer le gradient sur un maillage

---

### ⚠️ Erreurs fréquentes

- Confondre le gradient (vecteur) avec la dérivée partielle (scalaire)

- Oublier les facteurs $1/r$ ou $1/(r\sin\theta)$ dans les systèmes cylindrique/sphérique

- Ne pas vérifier que $\text{rot}(\vec{\text{grad}}\, f) = \vec{0}$ pour identifier un champ conservatif

---

##  Chapitre2 Flux Circulation

> **Cours** : PHYSH1002 — Électromagnétisme, Vol. I  

> **Thème** : Conservation, flux, circulation, divergence, rotationnel, théorèmes intégraux

---

### 1. Circulation d'un champ vectoriel

#### 1.1 Définition

La **circulation** d'un champ vectoriel $\vec{A}$ le long d'un contour $C$ mesure l'**entraînement** du champ le long du chemin :

$$\mathcal{C} = \oint_C \vec{A} \cdot d\vec{\ell}$$

- $d\vec{\ell}$ : élément de chemin orienté

- **Interprétation** : quantité de « travail » que le champ effectue le long du contour

#### 1.2 Exemples physiques

| Grandeur | Champ $\vec{A}$ | Circulation |

|----------|-----------------|-------------|

| **Travail** | Force $\vec{F}$ | $W = \int_C \vec{F} \cdot d\vec{\ell}$ |

| **Électromotance** | Champ électrique $\vec{E}$ | $\mathcal{E} = \oint_C \vec{E} \cdot d\vec{\ell}$ |

| **Circulation magnétique** | Champ magnétique $\bar{B}$ | $\oint_C \bar{B} \cdot d\vec{\ell} = \mu_0 I_{\text{encl}}$ |

#### 1.3 Champ conservatif

Un champ $\vec{A}$ est **conservatif** si sa circulation sur tout contour fermé est nulle :

$$\oint_C \vec{A} \cdot d\vec{\ell} = 0 \quad \Leftrightarrow \quad \vec{A} = -\vec{\text{grad}}\, V$$

> 💡 Un champ conservatif **dérive d'un potentiel** : la pseudo-différence de potentiel entre deux points ne dépend pas du chemin.

---

### 2. Rotationnel (curl)

#### 2.1 Définition intuitive

Le **rotationnel** mesure la **densité de circulation** locale d'un champ vectoriel. C'est la tendance du champ à « tourner » autour d'un point.

#### 2.2 Lien avec la circulation — Théorème de Stokes

$$\oint_C \vec{A} \cdot d\vec{\ell} = \iint_{S_C} \text{rot}\,\vec{A} \cdot d\vec{S}$$

> 🔑 **Théorème de Stokes** : la circulation le long d'un contour fermé = le flux du rotationnel à travers toute surface bordée par ce contour.

#### 2.3 Expression en coordonnées cartésiennes

$$\text{rot}\,\vec{A} = \begin{vmatrix} \vec{1}_x & \vec{1}_y & \vec{1}_z \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ A_x & A_y & A_z \end{vmatrix}$$

Ce qui donne composante par composante :

$$\text{rot}\,\vec{A} = \left(\frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}\right)\vec{1}_x + \left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right)\vec{1}_y + \left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right)\vec{1}_z$$

#### 2.4 Propriétés du rotationnel

| Propriété | Formule |

|-----------|---------|

| **Rot d'un gradient** | $\text{rot}(\vec{\text{grad}}\, f) = \vec{0}$ |

| **Div d'un rot** | $\text{div}(\text{rot}\,\vec{A}) = 0$ |

| **Linéarité** | $\text{rot}(a\vec{A} + b\vec{B}) = a\,\text{rot}\,\vec{A} + b\,\text{rot}\,\vec{B}$ |

---

### 3. Flux d'un champ vectoriel

#### 3.1 Définition

Le **flux** d'un champ $\vec{A}$ à travers une surface $S$ mesure la **quantité qui traverse** cette surface :

$$\Phi = \iint_S \vec{A} \cdot d\vec{S}$$

- $d\vec{S} = \hat{n}\,dS$ : élément de surface orienté (vecteur normal)

- **Interprétation** : « débit » du champ à travers la surface

#### 3.2 Exemples physiques

| Grandeur | Champ | Flux |

|----------|-------|------|

| **Flux magnétique** | $\bar{B}$ | $\Phi_B = \iint \bar{B} \cdot d\vec{S}$ |

| **Flux électrique** | $\vec{E}$ | $\Phi_E = \iint \vec{E} \cdot d\vec{S} = Q_{\text{encl}}/\varepsilon_0$ |

| **Débit massique** | $\rho\vec{v}$ | $\iint \rho\vec{v} \cdot d\vec{S}$ |

---

### 4. Divergence

#### 4.1 Définition intuitive

La **divergence** mesure la **densité de flux** en un point : la tendance d'un champ à « émaner » ou « converger » vers un point.

- $\text{div}\,\vec{A} > 0$ : **source** (le champ diverge)

- $\text{div}\,\vec{A} < 0$ : **puits** (le champ converge)

- $\text{div}\,\vec{A} = 0$ : champ **sans source** (solénoïdal)

#### 4.2 Lien avec le flux — Théorème de Gauss (divergence)

$$\oiint_S \vec{A} \cdot d\vec{S} = \iiint_V \text{div}\,\vec{A}\, dV$$

> 🔑 **Théorème de la divergence** : le flux à travers une surface fermée = l'intégrale volumique de la divergence à l'intérieur.

#### 4.3 Expression en coordonnées cartésiennes

$$\text{div}\,\vec{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$

---

### 5. Conservation et équation de continuité

#### 5.1 Principe de conservation

Si une grandeur extensive $G$ est conservée, sa variation dans un volume est due uniquement au flux à travers les bords :

$$\frac{dG}{dt} + \oiint_S \vec{J}_G \cdot d\vec{S} = 0$$

#### 5.2 Forme locale (équation de continuité)

$$\frac{\partial g}{\partial t} + \text{div}\,\vec{J}_G = 0$$

où $g$ est la densité volumique de $G$ et $\vec{J}_G$ le courant de $G$.

> 💡 **Application fondamentale** — Conservation de la charge :

> $$\frac{\partial \rho}{\partial t} + \text{div}\,\vec{J} = 0$$

---

### 6. Pseudo-différence de potentiel et champ non conservatif

#### 6.1 Décomposition du champ électrique

Le champ électrique peut avoir une composante **conservative** (issue du potentiel) et une composante **non conservative** (issue de l'induction) :

$$\vec{E} = -\vec{\text{grad}}\, V + \vec{E}_i$$

où $\vec{E}_i$ est le champ induit (non conservatif, avec $\text{rot}\,\vec{E}_i \neq \vec{0}$).

#### 6.2 Pseudo-différence de potentiel

Dans un circuit, on peut définir un potentiel « presque partout », sauf aux points où agissent des forces non conservatives (sources d'é.m.f.).

---

### 7. Équations de Maxwell — Première apparition

| Équation | Forme locale | Forme intégrale |

|----------|-------------|----------------|

| **Gauss (électrique)** | $\text{div}\,\vec{E} = \rho/\varepsilon_0$ | $\oiint \vec{E}\cdot d\vec{S} = Q/\varepsilon_0$ |

| **Gauss (magnétique)** | $\text{div}\,\bar{B} = 0$ | $\oiint \bar{B}\cdot d\vec{S} = 0$ |

| **Faraday** | $\text{rot}\,\vec{E} = -\partial\bar{B}/\partial t$ | $\oint \vec{E}\cdot d\vec{\ell} = -d\Phi_B/dt$ |

| **Ampère-Maxwell** | $\text{rot}\,\bar{B} = \mu_0\vec{J} + \mu_0\varepsilon_0\partial\vec{E}/\partial t$ | $\oint \bar{B}\cdot d\vec{\ell} = \mu_0(I + \varepsilon_0 d\Phi_E/dt)$ |

---

### 8. Résumé des opérateurs différentiels

```

           grad              rot              div

scalaire ────────→ vecteur ────────→ vecteur ────────→ scalaire

  rot(grad f) = 0  toujours     div(rot A) = 0  toujours

```

| Opérateur | Entrée | Sortie | Mesure |

|-----------|--------|--------|--------|

| **grad** | scalaire | vecteur | direction de croissance max |

| **rot** | vecteur | vecteur | densité de circulation locale |

| **div** | vecteur | scalaire | densité de flux (source/puits) |

---

### 🧠 Points clés à retenir

1. **Circulation** = intégrale de ligne → lié au **rotationnel** (Stokes)

2. **Flux** = intégrale de surface → lié à la **divergence** (Gauss)

3. $\text{rot}(\vec{\text{grad}}) = \vec{0}$ : tout gradient est irrotationnel

4. $\text{div}(\text{rot}) = 0$ : tout rotationnel est solénoïdal

5. L'**équation de continuité** exprime la conservation locale

6. Les **4 équations de Maxwell** relient $\vec{E}$ et $\bar{B}$ aux sources $\rho$ et $\vec{J}$

---

### ⚠️ Erreurs fréquentes

- Confondre **flux** (intégrale de surface) et **circulation** (intégrale de ligne)

- Oublier l'orientation ($d\vec{S}$ et $d\vec{\ell}$ doivent respecter la règle de la main droite)

- Appliquer la loi de Gauss avec une surface non fermée

- Oublier que $\text{div}\,\bar{B} = 0$ signifie qu'il n'existe **pas de monopôles magnétiques**

---

##  Chapitre3 Loi de Faraday

> **Cours** : PHYSH1002 — Électromagnétisme, Vol. I  

> **Thème** : Électromotance, induction, force de Lorentz, transformation galiléenne, potentiel vecteur

---

### 1. Électromotance (é.m.f.)

#### 1.1 Définition

L'**électromotance** (é.m.f.) est la circulation d'une force par unité de charge sur un contour fermé :

$$\mathcal{E} = \oint_C \frac{\vec{F}}{q} \cdot d\vec{\ell} = \oint_C \vec{E}_{\text{total}} \cdot d\vec{\ell}$$

#### 1.2 Forces conservatives vs non conservatives

| Type | Caractéristique | Circulation sur $C$ fermé | Exemple |

|------|----------------|--------------------------|---------|

| **Conservative** | Dérive d'un potentiel | $= 0$ | Force électrostatique $\vec{E} = -\vec{\text{grad}}\, V$ |

| **Non conservative** | Rotationnel non nul | $\neq 0$ | Champ induit, pile |

> 💡 L'é.m.f. ne capte que la **partie non conservative** du champ, car la contribution conservative s'annule sur un contour fermé.

#### 1.3 Sources d'électromotance

- **Électrochimique** : pile, batterie (tension de source indépendante du circuit)

- **Électromagnétique** : induction (dépend de la géométrie et du mouvement)

---

### 2. Force de Lorentz

#### 2.1 Expression

La force subie par une charge $q$ se déplaçant à vitesse $\vec{v}$ dans un champ électromagnétique :

$$\boxed{\vec{F}_L = q(\vec{E} + \vec{v} \times \bar{B})}$$

| Composante | Expression | Travail ? |

|------------|-----------|-----------|

| **Électrique** | $q\vec{E}$ | Oui (peut accélérer/ralentir) |

| **Magnétique** | $q\vec{v} \times \bar{B}$ | Non ($\vec{F}_m \perp \vec{v}$ toujours) |

#### 2.2 Interprétation

- La composante magnétique est toujours **perpendiculaire** à la vitesse → elle **ne fournit pas de travail**

- Elle dévie les charges mais ne change pas leur énergie cinétique

- C'est la composante électrique (y compris induite) qui effectue le travail

---

### 3. Induction électromagnétique

#### 3.1 Expérience fondamentale : tige en mouvement

Une tige conductrice se déplaçant à vitesse $\vec{v}$ dans un champ magnétique $\bar{B}$ subit une force de Lorentz qui sépare les charges. Cela crée :

- Une **électromotance** $\mathcal{E} = \oint (\vec{v} \times \bar{B}) \cdot d\vec{\ell}$

- Un **champ électrique induit** $\vec{E}_i = \vec{v} \times \bar{B}$ (dans le repère de la tige)

- Un **équilibre** quand la force électrostatique compense la force magnétique

#### 3.2 Loi de Faraday (forme simple)

$$\boxed{\mathcal{E} = -\frac{d\Phi_B}{dt}}$$

- $\mathcal{E}$ : électromotance (é.m.f.)

- $\Phi_B = \iint_{S_C} \bar{B} \cdot d\vec{S}$ : flux magnétique à travers la surface bordée par le contour

- Le signe $-$ traduit la **loi de Lenz** (opposition à la variation)

#### 3.3 Loi de Faraday (forme locale — équation de Maxwell)

$$\boxed{\text{rot}\,\vec{E} + \frac{\partial \bar{B}}{\partial t} = \vec{0}}$$

> 🔑 Cette équation est **exacte et générale**. Elle relie spatialement $\vec{E}$ et temporellement $\bar{B}$ de manière **non causale** (corrélation, pas causalité).

---

### 4. Transformation galiléenne du champ EM

#### 4.1 Contexte

Quand on passe d'un repère $R$ à un repère $R'$ se déplaçant à $\vec{u}_0$ (avec $u_0 \ll c$), les grandeurs se transforment :

#### 4.2 Formules de transformation (approximation galiléenne)

$$\boxed{\begin{aligned}

\vec{E}' &= \vec{E} + \vec{u}_0 \times \bar{B} \\

\bar{B}' &= \bar{B} \\

\vec{J}' &= \vec{J} - \rho\vec{u}_0

\end{aligned}}$$

> ⚠️ Valable uniquement pour $u_0 \ll c$. En relativité, $\bar{B}$ se transforme aussi.

#### 4.3 Champ électrique induit par le mouvement

$$\vec{E}_i = \vec{E}' - \vec{E} = \vec{u}_0 \times \bar{B}$$

Ce champ induit est nul si $u_0 = 0$ ou $B = 0$.

#### 4.4 Invariance de la force de Lorentz

La force de Lorentz est **invariante** par changement de repère galiléen :

$$\vec{F}_L/q = \vec{E} + \vec{v} \times \bar{B} = \vec{E}' + (\vec{v} - \vec{u}_0) \times \bar{B}'$$

---

### 5. Travail et freinage électromagnétique

#### 5.1 Origine de l'énergie d'induction

Quand une tige se déplace dans $\bar{B}$, la séparation des charges crée un courant de dérive $\vec{v}_d$. Ce courant combiné à $\bar{B}$ produit une force **qui s'oppose au mouvement** :

$$\vec{F}_{Ld} = -\mu q^2 B^2 \vec{v}$$

#### 5.2 Applications

- **Freinage électromagnétique** (ex : Dalton Terror à Walibi)

- **Dynamo de Faraday** : disque conducteur en rotation dans $\bar{B}$ → é.m.f. entre centre et périphérie

- L'énergie mécanique fournit l'énergie aux charges (conservation de l'énergie)

---

### 6. Potentiel vecteur $\vec{A}$

#### 6.1 Définition

$$\text{rot}\,\vec{A} = \bar{B}$$

Cette définition satisfait automatiquement $\text{div}\,\bar{B} = 0$ (car $\text{div}(\text{rot}) = 0$).

#### 6.2 Décomposition du champ électrique

$$\boxed{\vec{E} = -\vec{\text{grad}}\, V - \frac{\partial \vec{A}}{\partial t}}$$

| Composante | Expression | Nature |

|------------|-----------|--------|

| **Conservative** | $-\vec{\text{grad}}\, V$ | Électrostatique |

| **Non conservative** | $-\partial \vec{A}/\partial t$ | Inductive, liée à la variation de $\bar{B}$ |

#### 6.3 Jauge de Lorentz

Condition complémentaire pour fixer $\vec{A}$ de manière unique :

$$\text{div}\,\vec{A} + \frac{1}{c^2}\frac{\partial V}{\partial t} = 0$$

#### 6.4 Équations d'onde pour les potentiels

Sous la jauge de Lorentz, les potentiels satisfont des **équations d'onde** :

$$\frac{1}{c^2}\frac{\partial^2 \vec{A}}{\partial t^2} - \vec{\Delta}\vec{A} = \mu_0 \vec{J}$$

$$\frac{1}{c^2}\frac{\partial^2 V}{\partial t^2} - \Delta V = \frac{\rho}{\varepsilon_0}$$

> 💡 La description en potentiels ne comporte que **4 composantes** (1 scalaire + 1 vecteur), contre 6 pour $(\vec{E}, \bar{B})$.

---

### 7. Loi de Faraday — Cas particuliers

#### 7.1 Deux formes de la loi de Faraday

1. **Forme locale** (eq. de Maxwell) : $\text{rot}\,\vec{E} = -\partial \bar{B}/\partial t$

2. **Forme intégrale** (pour circuits) : $\mathcal{E} = -d\Phi_B/dt$

#### 7.2 Contour fixe dans $\bar{B}$ variable

L'é.m.f. est due au champ induit $\vec{E}_i$ avec $\text{rot}\,\vec{E}_i = -\partial\bar{B}/\partial t$.

#### 7.3 Contour mobile dans $\bar{B}$ constant

L'é.m.f. est due au mouvement : $\vec{E}'_i = \vec{u} \times \bar{B}$.

---

### 🧠 Points clés à retenir

1. $\vec{F}_L = q(\vec{E} + \vec{v} \times \bar{B})$ — la force magnétique ne travaille pas

2. $\mathcal{E} = -d\Phi_B/dt$ — loi de Faraday globale

3. $\text{rot}\,\vec{E} = -\partial\bar{B}/\partial t$ — loi de Faraday locale (Maxwell)

4. Le champ EM est **une seule entité** : $\vec{E}$ et $\bar{B}$ dépendent du repère

5. $\vec{E}' = \vec{E} + \vec{u}_0 \times \bar{B}$ — transformation galiléenne

6. $\vec{E} = -\vec{\text{grad}}\, V - \partial\vec{A}/\partial t$ — potentiel vecteur

---

### ⚠️ Erreurs fréquentes

- Croire que $\bar{B}$ « cause » $\vec{E}$ : c'est une **corrélation**, pas une causalité

- Oublier que la force magnétique ne fournit **jamais** de travail directement

- Confondre é.m.f. avec tension : l'é.m.f. dépend du contour choisi

- Ne pas distinguer le repère de mesure et le repère de calcul dans les transformations

---

##  Chapitre4 Ampere Maxwell Lenz

> **Cours** : PHYSH1002 — Électromagnétisme, Vol. I  

> **Thème** : Loi d'Ampère-Maxwell, courant de déplacement, loi de Lenz, diamagnétisme, applications

---

### 1. Problème de la loi d'Ampère classique

#### 1.1 Ambiguïté de la surface

La loi d'Ampère classique $\oint_C \bar{B} \cdot d\vec{\ell} = \mu_0 I_{\text{encl}}$ pose un problème : le **courant** traversant la surface bordée par $C$ dépend du **choix de la surface**.

**Exemple du condensateur en charge** :

- Surface $S_{C1}$ traversée par le fil → $I_{\text{encl}} = I$

- Surface $S_{C2}$ passant entre les plaques → $I_{\text{encl}} = 0$ (pas de courant matériel entre les plaques)

> ⚠️ Les deux surfaces sont bordées par le même contour $C$, mais donnent des résultats différents → **contradiction** !

#### 1.2 Conservation de la charge

La source du problème est que la divergence de $\vec{J}$ n'est pas nulle lors de la charge d'un condensateur : $\text{div}\,\vec{J} \neq 0$ car il y a accumulation de charges.

---

### 2. Courant de déplacement de Maxwell

#### 2.1 Solution de Maxwell

Maxwell a résolu le problème en ajoutant un terme à la loi d'Ampère :

$$\boxed{\text{rot}\,\bar{B} = \mu_0\vec{J} + \mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}}$$

Le terme $\varepsilon_0 \partial\vec{E}/\partial t$ est appelé **courant de déplacement** (ou densité de courant de déplacement).

#### 2.2 Vérification de la cohérence

En prenant la divergence des deux membres :

$$\text{div}(\text{rot}\,\bar{B}) = 0 = \mu_0\text{div}\,\vec{J} + \mu_0\varepsilon_0\frac{\partial}{\partial t}\text{div}\,\vec{E}$$

En utilisant $\text{div}\,\vec{E} = \rho/\varepsilon_0$ (loi de Gauss) :

$$0 = \mu_0\text{div}\,\vec{J} + \mu_0\frac{\partial\rho}{\partial t}$$

On retrouve bien l'**équation de continuité** $\frac{\partial\rho}{\partial t} + \text{div}\,\vec{J} = 0$ → conservation de la charge ✅

#### 2.3 Interprétation physique — Condensateur

Dans le condensateur, la variation de $\vec{E}$ entre les plaques joue le rôle d'un courant. Le terme $\varepsilon_0 \partial\vec{E}/\partial t$ assure la **continuité** du champ $\bar{B}$ entre la zone des fils et la zone entre les plaques.

$$\iint_{S_{C2}} \varepsilon_0 \frac{\partial\vec{E}}{\partial t} \cdot d\vec{S} = \varepsilon_0 \frac{I}{S\varepsilon_0} S = I = \iint_{S_{C1}} \vec{J} \cdot d\vec{S}$$

---

### 3. Symétrie Faraday–Ampère

En l'absence de courant de conduction ($\vec{J} = 0$), les équations de Faraday et Ampère-Maxwell présentent une **symétrie** :

$$\mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t} = \text{rot}\,\bar{B} \qquad \text{(Ampère-Maxwell)}$$

$$\frac{\partial\bar{B}}{\partial t} = -\text{rot}\,\vec{E} \qquad \text{(Faraday)}$$

> 💡 Cette symétrie montre que $\vec{E}$ et $\bar{B}$ peuvent « engendrer » l'un l'autre → base des **ondes électromagnétiques**.

---

### 4. Les quatre équations de Maxwell (microscopiques, dans le vide)

| # | Nom | Forme locale | Forme intégrale | Signification |

|---|-----|-------------|-----------------|---------------|

| 1 | **Gauss électrique** | $\text{div}\,\vec{E} = \rho/\varepsilon_0$ | $\oiint \vec{E} \cdot d\vec{S} = Q/\varepsilon_0$ | Charges = sources de $\vec{E}$ |

| 2 | **Gauss magnétique** | $\text{div}\,\bar{B} = 0$ | $\oiint \bar{B} \cdot d\vec{S} = 0$ | Pas de monopôles magnétiques |

| 3 | **Faraday** | $\text{rot}\,\vec{E} = -\partial\bar{B}/\partial t$ | $\oint \vec{E} \cdot d\vec{\ell} = -d\Phi_B/dt$ | Corrélation $\vec{E}$–$\bar{B}$ (non causal) |

| 4 | **Ampère-Maxwell** | $\text{rot}\,\bar{B} = \mu_0\vec{J} + \mu_0\varepsilon_0\partial\vec{E}/\partial t$ | $\oint \bar{B} \cdot d\vec{\ell} = \mu_0(I + \varepsilon_0 d\Phi_E/dt)$ | Courants et $\partial\vec{E}/\partial t$ créent $\bar{B}$ |

---

### 5. Loi de Lenz

#### 5.1 Énoncé

> **Le courant induit s'oppose toujours à la variation de flux qui lui a donné naissance.**

Plus précisément : le champ magnétique $\bar{B}_i$ créé par le courant induit $I_i$ est **opposé** à la variation $\partial\bar{B}/\partial t$ du champ extérieur.

#### 5.2 Règle pratique

- Si $\Phi_B$ **augmente** → le courant induit crée un $\bar{B}_i$ **opposé** à $\bar{B}$

- Si $\Phi_B$ **diminue** → le courant induit crée un $\bar{B}_i$ **dans le même sens** que $\bar{B}$

- Mnémonique : la main **gauche** avec le pouce dans le sens de $\partial\bar{B}/\partial t$, les doigts indiquent le sens de $\vec{E}_i$

#### 5.3 Interprétation en termes de forces

| Situation | Sens de $\bar{B}_i$ | Force $\vec{F}_M$ | Effet |

|-----------|---------------------|-------------------|-------|

| Aimant s'approche ($\bar{B}$ â†‘) | Opposé à $\bar{B}$ | **Répulsive** | Freine l'approche |

| Aimant s'éloigne ($\bar{B}$ â†“) | Même sens que $\bar{B}$ | **Attractive** | Freine l'éloignement |

#### 5.4 Conservation de l'énergie

La loi de Lenz est le **reflet de la conservation de l'énergie** :

- Pour créer un courant dans la spire, il faut dépenser de l'énergie mécanique

- La puissance mécanique = puissance dissipée (effet Joule) :

$$P = RI_i^2 = \frac{\mathcal{E}^2}{R} = -\vec{F}_M \cdot \vec{v}$$

> 💡 Loi de Lenz ↔ Loi de Le Chatelier en chimie : un système s'oppose aux changements qui lui sont imposés.

---

### 6. Diamagnétisme

#### 6.1 Mécanisme

1. Un champ $\bar{B}_0$ externe **augmente** au voisinage d'un matériau

2. Par induction (Lenz), les **orbites électroniques** sont modifiées

3. Un électron est **accéléré**, l'autre (apparié) est **décéléré**

4. Il en résulte un **courant net induit** opposé aux courants de l'aimant

5. Le champ induit $\bar{B}_i$ s'oppose à $\bar{B}_0$ → $\bar{B} = \bar{B}_0 + \bar{B}_i < \bar{B}_0$

#### 6.2 Propriétés

- Présent dans **tous** les matériaux (mais observable surtout si pas ferro/paramagnétique)

- Matériaux à **électrons appariés** (moment magnétique atomique nul)

- Perméabilité relative : $\mu_r < 1$ (mais très proche de 1, ex: eau $\mu_r = 1 - 0.88 \times 10^{-5}$)

- **Persistant** : les courants orbitaux persistent tant que $\bar{B}_0$ est maintenu (pas de dissipation orbitale)

- Force **toujours répulsive** entre aimant et matériau diamagnétique

---

### 7. Applications de l'induction

| Application | Principe |

|-------------|----------|

| **Microphone** | Membrane solidaire d'un solénoïde vibrant dans $\bar{B}$ d'un aimant → é.m.f. âˆ signal acoustique |

| **Haut-parleur** | Inverse du micro : courant variable dans la bobine → force sur membrane |

| **Tête de lecture** | Bande magnétique en mouvement → variation de $\Phi_B$ → é.m.f. |

| **Courants de Foucault** | Courants parasites dans un conducteur massif exposé à $\bar{B}$ variable → dissipation |

| **Freinage EM** | Dalton Terror : plaques conductrices dans $\bar{B}$ → force de freinage |

---

### 🧠 Points clés à retenir

1. Maxwell a complété Ampère avec le **courant de déplacement** $\varepsilon_0\partial\vec{E}/\partial t$

2. Ce terme assure la **conservation de la charge** et résout l'ambiguïté de surface

3. Les **4 équations de Maxwell** forment le cadre complet de l'EM classique

4. **Lenz** : le courant induit crée un $\bar{B}_i$ opposé à $\partial\bar{B}/\partial t$ → conservation de l'énergie

5. Le **diamagnétisme** est l'induction EM à l'échelle atomique

---

### ⚠️ Erreurs fréquentes

- Confondre le « courant de déplacement » avec un vrai courant de charges en mouvement

- Dire que $\bar{B}$ variable **cause** $\vec{E}$ : c'est une **corrélation locale** (seuls les mouvements de charges créent les champs)

- Oublier que Lenz n'apporte rien de nouveau théoriquement : c'est juste le signe $-$ dans la loi de Faraday

- Croire que le diamagnétisme disparaît quand l'aimant s'arrête (les courants orbitaux persistent !)

---

##  Chapitre5 Dynamique Circuits

> **Cours** : PHYSH1002 — Électromagnétisme, Vol. I  

> **Thème** : Auto-induction, inductance, circuit RL, transformateur, courants alternatifs, impédances

---

### 1. Auto-induction et inductance

#### 1.1 Phénomène d'auto-induction

Quand le courant $I$ varie dans un inducteur (solénoïde, bobine), le champ $\bar{B}$ qu'il crée varie aussi. Ce changement de flux à travers ses propres spires induit une é.m.f. **qui s'oppose à la variation du courant** (loi de Lenz).

#### 1.2 Inductance $L$

La **proportionnalité** entre le flux magnétique total intercepté par l'inducteur et le courant définit l'inductance :

$$\boxed{\Phi_M = LI}$$

- $L$ : inductance (en Henry, H)

- $\Phi_M$ : flux magnétique total intercepté

#### 1.3 Électromotance d'auto-induction

$$\mathcal{E} = -\frac{d\Phi_M}{dt} = -L\frac{dI}{dt}$$

#### 1.4 Inductance d'un solénoïde

Pour un solénoïde de $N$ spires, longueur $\ell$, section $S$, avec noyau de perméabilité $\mu$ :

$$\boxed{L = \mu \frac{N^2 S}{\ell}}$$

> 💡 Le facteur $N^2$ vient du fait que les $N$ spires captent chacune le flux, et que le flux est $N$ fois plus grand qu'avec une seule spire.

---

### 2. Loi courant-tension de l'inducteur

#### 2.1 Inducteur idéal (résistance nulle)

$$\boxed{V_L = L\frac{dI}{dt}}$$

Convention : $V_L$ est orienté en **opposition** au courant (comme pour une résistance).

#### 2.2 Analogie condensateur–inducteur

| Propriété | Condensateur | Inducteur |

|-----------|-------------|-----------|

| Grandeur stockée | $Q = CV$ | $\Phi_M = LI$ |

| Loi courant-tension | $I = C\frac{dV}{dt}$ | $V = L\frac{dI}{dt}$ |

| Énergie | $W_C = \frac{1}{2}CV^2$ | $W_L = \frac{1}{2}LI^2$ |

| Énergie dans le champ | Électrique | Magnétique |

---

### 3. Circuit RL

#### 3.1 Charge (connexion à une source $V$)

À $t = 0$, on connecte un inducteur $L$ en série avec une résistance $R$ à une tension $V$ :

$$V = RI + L\frac{dI}{dt}$$

**Solution** :

$$\boxed{I(t) = \frac{V}{R}\left(1 - e^{-t/\tau}\right)} \qquad \tau = \frac{L}{R}$$

| Instant | Courant | Tension sur $L$ | Tension sur $R$ |

|---------|---------|-----------------|-----------------|

| $t = 0$ | $0$ | $V$ | $0$ |

| $t = \tau$ | $0.63 \times V/R$ | $0.37 V$ | $0.63 V$ |

| $t \to \infty$ | $V/R$ | $0$ | $V$ |

#### 3.2 Décharge (court-circuit)

$$I(t) = I_0 \, e^{-t/\tau} \qquad \tau = \frac{L}{R}$$

#### 3.3 Interprétation physique

- L'inducteur crée une **inertie** du courant (le courant ne peut pas changer instantanément)

- La constante de temps $\tau = L/R$ caractérise la rapidité de réponse

- Pendant la charge : l'énergie de la source est partagée entre dissipation Joule et stockage magnétique

- En régime permanent : toute l'énergie de la source est dissipée dans $R$

---

### 4. Énergie dans l'inducteur

#### 4.1 Énergie stockée

$$\boxed{W_L = \frac{1}{2}LI^2}$$

#### 4.2 Bilan énergétique du circuit RL

Sur toute la durée de la charge :

$$W_{\text{source}} = W_{\text{Joule}} + W_L$$

$$V \cdot I_0 \cdot t_{\infty} = \frac{1}{2}LI_0^2 + \frac{1}{2}LI_0^2$$

> 💡 Exactement **la moitié** de l'énergie fournie par la source est dissipée dans $R$, l'autre moitié est stockée dans $L$.

#### 4.3 Densité d'énergie magnétique

$$\boxed{w_B = \frac{1}{2\mu}\|\bar{B}\|^2 = \frac{1}{2}\mu_0\|\bar{H}\|^2}$$

Analogue à la densité d'énergie électrique :

$$w_E = \frac{1}{2}\varepsilon_0\|\vec{E}\|^2$$

---

### 5. Le transformateur

#### 5.1 Principe

Un transformateur est constitué de deux solénoïdes (primaire et secondaire) partageant le **même flux magnétique** $\Phi_M$ grâce à un noyau ferromagnétique.

#### 5.2 Fonctionnement (inducteur idéal)

La tension primaire impose la variation de flux :

$$\frac{d\Phi_M}{dt} = \frac{V_p}{N_p}$$

Le secondaire capte ce flux $N_s$ fois :

$$\boxed{V_s = \frac{N_s}{N_p} V_p}$$

| Grandeur | Rapport |

|----------|---------|

| **Tension** | $V_s/V_p = N_s/N_p$ |

| **Courant** | $I_s/I_p = N_p/N_s$ (conservation de la puissance) |

| **Puissance** | $P_s = P_p$ (transformateur idéal) |

#### 5.3 Importance pratique

Le transformateur permet le **transport de l'électricité à haute tension** pour minimiser les pertes Joule dans les câbles :

$$\eta_t = 1 - \frac{2R_t I^2}{P} \quad \Rightarrow \quad \text{plus } V \text{ est grand, plus } I \text{ est petit, plus } \eta_t \to 1$$

---

### 6. Courants alternatifs

#### 6.1 Grandeurs fondamentales

| Grandeur | Notation | Relation |

|----------|----------|----------|

| **Pulsation** | $\omega$ | $\omega = 2\pi f$ |

| **Période** | $T$ | $T = 2\pi/\omega = 1/f$ |

| **Fréquence** | $f$ | $f = 1/T$ |

| **Valeur efficace** | $I_{\text{eff}}, V_{\text{eff}}$ | $I_{\text{eff}} = I_m/\sqrt{2}$, $V_{\text{eff}} = V_m/\sqrt{2}$ |

#### 6.2 Puissance moyenne

En valeurs efficaces, les formules classiques sont conservées :

$$\boxed{\langle P \rangle = R I_{\text{eff}}^2 = \frac{V_{\text{eff}}^2}{R} = V_{\text{eff}} I_{\text{eff}}}$$

---

### 7. Comportement des composants en courant alternatif

#### 7.1 Résistance

$$V = RI \quad \Rightarrow \quad I(t) = \frac{V_m}{R}\sin(\omega t)$$

- Courant **en phase** avec la tension ($\Delta\varphi = 0$)

- Puissance dissipée : $\langle P \rangle = RI_{\text{eff}}^2 \neq 0$

#### 7.2 Inducteur

$$V = L\frac{dI}{dt} \quad \Rightarrow \quad I(t) = \frac{V_m}{\omega L}\sin\left(\omega t - \frac{\pi}{2}\right)$$

- Courant en **retard de $\pi/2$** sur la tension (quadrature)

- **Réactance** : $X_L = \omega L$

- Puissance moyenne : $\langle P \rangle = 0$ (pas de dissipation !)

- **Filtre passe-bas** : laisse passer les basses fréquences ($I_m \propto 1/\omega$)

#### 7.3 Condensateur

$$I = C\frac{dV}{dt} \quad \Rightarrow \quad I(t) = \omega C V_m \sin\left(\omega t + \frac{\pi}{2}\right)$$

- Courant en **avance de $\pi/2$** sur la tension (quadrature)

- **Réactance** : $X_C = 1/(\omega C)$

- Puissance moyenne : $\langle P \rangle = 0$ (pas de dissipation !)

- **Filtre passe-haut** : laisse passer les hautes fréquences ($I_m \propto \omega$)

#### 7.4 Tableau comparatif

| Composant | Loi V–I | Réactance/Résistance | Déphasage $\Delta\varphi$ | $\langle P \rangle$ | Filtre |

|-----------|---------|---------------------|--------------------------|---------------------|--------|

| **R** | $V = RI$ | $R$ | $0$ | $RI_{\text{eff}}^2$ | — |

| **L** | $V = L\frac{dI}{dt}$ | $X_L = \omega L$ | $-\pi/2$ (retard) | $0$ | Passe-bas |

| **C** | $I = C\frac{dV}{dt}$ | $X_C = \frac{1}{\omega C}$ | $+\pi/2$ (avance) | $0$ | Passe-haut |

---

### 8. Déphasage et représentation

#### 8.1 Notation

- **Phase** de $V$ : $\varphi_V = \omega t$

- **Phase** de $I$ : $\varphi_I = \omega t + \Delta\varphi$

- **Retard temporel** : $\Delta t = \Delta\varphi / \omega$

#### 8.2 Interprétation énergétique

- Si $\Delta\varphi = 0$ (résistance) : toute l'énergie est **dissipée** (chaleur)

- Si $\Delta\varphi = \pm\pi/2$ (L ou C) : l'énergie **oscille** entre source et composant, puissance moyenne nulle

- Si $0 < |\Delta\varphi| < \pi/2$ (circuits mixtes) : une partie est dissipée, une partie oscille

---

### 🧠 Points clés à retenir

1. $\Phi_M = LI$ et $V_L = L\,dI/dt$ — lois fondamentales de l'inducteur

2. $\tau = L/R$ — constante de temps du circuit RL

3. $W_L = \frac{1}{2}LI^2$ — énergie magnétique stockée

4. $V_s/V_p = N_s/N_p$ — rapport de transformation

5. Le courant est en **retard** dans $L$ et en **avance** dans $C$ (par rapport à $V$)

6. $X_L = \omega L$ et $X_C = 1/(\omega C)$ — réactances

7. Les composants réactifs ($L, C$) ne **dissipent pas** d'énergie en moyenne

---

### ⚠️ Erreurs fréquentes

- Oublier la convention de signe : $V_L = +L\,dI/dt$ (pas $-L\,dI/dt$, car on inclut le signe dans l'é.m.f.)

- Confondre le temps caractéristique $\tau = L/R$ avec $\tau = RC$ (circuit RC)

- Croire qu'un inducteur en AC dissipe de l'énergie (puissance moyenne = 0 !)

- Oublier que retard = phase **négative** ($I$ retardé → $\Delta\varphi < 0$)

- Ne pas utiliser les valeurs **efficaces** pour les calculs pratiques

