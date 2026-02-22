# 🧾 Cheat Sheet — Analyse Numérique (Chapitre 1)

> ⚡ **Fiche ultra-condensée** — Uniquement les formules et concepts vitaux pour l'examen.

---

## 1. Représentation en virgule flottante

La représentation (normalisée si $d_1 \neq 0$) :

$$
x = \pm 0.d_1 d_2 \cdots d_t \cdot \beta^e
$$

### L'Unité d'Arrondi ($u$)

Borne la perte de précision relative maximale lors du passage de $\mathbb{R} \to \mathbb{F}$ (flottants machine).

$$
u = \frac{1}{2}\beta^{1-t}
$$

| Format IEEE 754 | $u$ | Chiffres significatifs |
| :--- | :--- | :--- |
| **Simple Précision** | $\approx 6.0 \times 10^{-8}$ | $\sim 7$ chiffres |
| **Double Précision** | $\approx 1.1 \times 10^{-16}$ | $\sim 16$ chiffres |

---

## 2. Modèle et Propagation des Erreurs

Chaque calcul machine amplifie l'erreur.
Si $\circ$ est l'opération exacte et $\circledcirc$ la version machine :

$$
x \circledcirc y = (x \circ y)(1 + \varepsilon) \quad \text{avec } |\varepsilon| \leq u
$$

### Règles de base d'analyse

Dans l'hypothèse où $|\varepsilon_i| \leq u$ et $\alpha, \beta \in \mathbb{R}$ :

| Règle | Expression simplifiée | Résultat pratique |
| :---: | :--- | :--- |
| **1** | $\alpha\varepsilon_1 \pm \beta\varepsilon_2$ | $(|\alpha| + |\beta|)\varepsilon_3$ |
| **2** | $(1+\alpha\varepsilon_1)(1+\beta\varepsilon_2)$ | $1+(|\alpha|+|\beta|)\varepsilon_3 + O(u^2)$ |
| **3** | $\frac{1}{1+\alpha\varepsilon_4}$ | $1 + \alpha\varepsilon' + O(u^2)$ |

---

## 3. Stabilité et Conditionnement

L'erreur entre notre code et la réalité s'appelle l'**Erreur Directe** ($\hat{y} - y$).

### Règle d'or de la robustesse d'un code
Une seule règle :
$$
\text{Stabilité Inverse} \implies \text{Stabilité Directe}
$$

---

## 5. Systèmes d'équations (Chapitre 2)

Pour analyser la robustesse d'un système matriciel carré $Ax = b$ (*Attention: l'algorithme LU est direct en $\approx O(n^3)$. N'utilisez **JAMAIS** Cramer ou l'inversion naïve $A^{-1}$*).

### Conditionnement du système $\kappa(A)$
Borne la propagation de l'incertitude sur la matrice $A$ vers le résultat final $x$.

$$
\kappa(A) = \|A^{-1}\| \cdot \|A\|
$$
*(Une matrice avec un conditionnement $\approx 10^{16}$ est numériquement instable/singulière).*

### Factorisation LU avec Pivotage
Le théorème affirme que toute matrice régulière $A$ peut être dissociée en 2 matrices idéales pour un ordinateur. **Algorithme d'or : $PA = LU$**

- $P$ : Matrice de Permutations. $\det(P) = \pm 1$
- $L$ : Matrice triangulaire inférieure (Lower), sa diagonale $= 1$ pur. $\det(L) = 1$
- $U$ : Matrice triangulaire supérieure (Upper). 

**Astuce Déterminant** : Après exécution de l'algo $PA=LU$, extraire un déterminant giganteste ou inverse est trivial :
$$
\det(A) = (-1)^p \cdot u_{11} \cdot u_{22} \cdots u_{nn}
$$

- *(La stabilité inverse garantit que notre résultat numérique exact est la réponse stricte à une question très légèrement perturbée : $\hat{y} = f(x + \Delta x)$).*

### Le Conditionnement Absolu $\kappa$

Mesure l'amplification fatale **due au problème mathématique lui-même** :

$$
\kappa(x) = \frac{\|f'(x)\| \cdot \|x\|}{\|f(x)\|}
$$

- $\kappa(x) \approx 1$ : Bien conditionné.
- $\kappa(x) \gg 1$ : Mal conditionné (Danger extrême).

**L'annulation catastrophique** survient sur la fonction $f(x_1, x_2) = x_1 - x_2$ car son dénominateur s'écrase $|x_1 - x_2|$, ce qui envoie $\kappa \to \infty$.

---

## 4. Les Pièges Classiques du Standard

⚠️ **Division par 0 ou Dépassement Capacitaire** $\to$ `±Inf` (Overflow).
⚠️ **Chute sous le niveau minimum** $\to$ Représentation Dénormalisée (Underflow, perte gravissime de précision).
⚠️ **Formes indéterminées** $\to$ `NaN` (Not a Number).
