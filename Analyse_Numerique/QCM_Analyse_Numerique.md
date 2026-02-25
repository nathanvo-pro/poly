# ✅ Quiz / QCM — Analyse Numérique (MATH-F-2007)

> Quiz avec questions à choix multiples pour réviser chaque chapitre.
> Cliquez sur **💡 Solution** pour vérifier votre réponse et voir l'explication.

---

## Chapitre 1 — Virgule flottante, IEEE 754 & Conditionnement

### Question 1.1 : En représentation IEEE 754 simple précision (32 bits), combien de bits sont alloués à l'exposant ?
- [ ] A) 5 bits
- [ ] B) 8 bits
- [ ] C) 11 bits
- [ ] D) 23 bits

<details>
<summary>💡 Solution</summary>

**Réponse B**. En simple précision (32 bits), on a 1 bit de signe, 8 bits d'exposant (biaisé a 127) et 23 bits de mantisse.
</details>

### Question 1.2 : Qu'est-ce que l'erreur d'arrondi ou "machine epsilon" ($\epsilon_{mach}$) ?
- [ ] A) L'écart maximum entre deux nombres entiers consécutifs
- [ ] B) Le plus petit nombre positif représentable par la machine
- [ ] C) La borne supérieure de l'erreur relative lors de l'arrondi d'un nombre réel à son nombre flottant le plus proche
- [ ] D) L'erreur générée lorsqu'on divise par zéro

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le $\epsilon_{mach}$ limite l'erreur relative maximale d'arrondi : $\frac{|fl(x) - x|}{|x|} \le \epsilon_{mach}$.
</details>

### Question 1.3 : Un problème mathématique est dit "mal conditionné" si :
- [ ] A) L'algorithme utilisé pour le résoudre effectue trop d'opérations.
- [ ] B) De petites perturbations dans les données d'entrée provoquent de petites variations dans la solution.
- [ ] C) De petites perturbations dans les données d'entrée provoquent de grandes variations dans la solution.
- [ ] D) La matrice associée est de taille impaire.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le conditionnement est une propriété intrinsèque du problème. S'il est grand, une infime erreur sur les données (comme l'arrondi) est amplifiée dans le résultat.
</details>

### Question 1.4 : Le phénomène d'« annulation catastrophique » se produit particulièrement dans le cas :
- [ ] A) De la multiplication de deux très grands nombres.
- [ ] B) D'une division par un nombre proche de zéro.
- [ ] C) De la soustraction de deux nombres flottants très proches l'un de l'autre.
- [ ] D) Du calcul du logarithme de 1.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Soustraire deux quantités presque égales fait "perdre" les chiffres significatifs de tête et donne un résultat basé presque entièrement sur l'erreur de représentation, ce qui ruine la précision.
</details>

### Question 1.5 : Laquelle de ces expressions équivalentes mathématiquement est numériquement la plus stable pour évaluer $\sqrt{x^2 + 1} - 1$ quand $x \approx 0$ ?
- [ ] A) $\sqrt{x^2 + 1} - 1$
- [ ] B) $\frac{x^2}{\sqrt{x^2 + 1} + 1}$
- [ ] C) $\frac{1}{\sqrt{x^2 + 1} - 1}$
- [ ] D) $x^2 + 1$

<details>
<summary>💡 Solution</summary>

**Réponse B**. L'expression A subit une annulation (car $\sqrt{1} - 1 = 0$). L'expression B, obtenue en multipliant par le conjugué, évite cette soustraction critique de "presque 1" par "1" et reste donc stable.
</details>

---

## Chapitre 2 — Systèmes Linéaires & Décomposition LU / Cholesky

### Question 2.1 : Quel est le coût algorithmique principal (la complexité) de la méthode d'élimination de Gauss pour une matrice pleine $n \times n$ ?
- [ ] A) $O(n^2)$ opérations
- [ ] B) $\approx \frac{2n^3}{3}$ opérations
- [ ] C) $O(n \log n)$ opérations
- [ ] D) $\approx \frac{n^4}{4}$ opérations

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est un processus en $O(n^3)$. Plus précisément on compte environ $\frac{2n^3}{3}$ opérations flottantes.
</details>

### Question 2.2 : Dans la décomposition LU de Crout ou Doolittle ($A = LU$), quelles propriétés ont L et U ?
- [ ] A) L est triangulaire inférieure, U est orthogonale.
- [ ] B) L est triangulaire inférieure, U est triangulaire supérieure.
- [ ] C) L et U sont toutes deux symétriques.
- [ ] D) L est une matrice de permutation, U est triangulaire.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Lower (Inférieure) et Upper (Supérieure). Cette décomposition permet de résoudre $Ax=b$ en deux substitutions $Ly=b$ et $Ux=y$.
</details>

### Question 2.3 : Quel est le rôle principal de la "stratégie de pivot partiel" dans la résolution de systèmes linéaires ?
- [ ] A) Réduire la complexité temporelle de $O(n^3)$ à $O(n^2)$.
- [ ] B) Permettre d'inverser les matrices singulières.
- [ ] C) Accroître la stabilité numérique en évitant la division par des pivots trop petits (proches de 0).
- [ ] D) Rendre la matrice symétrique définie positive.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Échanger les lignes pour placer le plus grand élément possible en position de pivot minimise l'amplification des erreurs d'arrondi (instabilité).
</details>

### Question 2.4 : À quelle condition stricte peut-on toujours appliquer la décomposition de **Cholesky** ($A = LL^T$) pour une matrice réelle $A$ ?
- [ ] A) $A$ doit être une matrice Diagonale Dominante.
- [ ] B) $A$ doit être tridiagonale.
- [ ] C) $A$ doit être Symétrique et Définie Positive (SDP).
- [ ] D) $A$ doit être de conditionnement nul.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Cholesky est deux fois plus rapide (et plus stable naturellement sans pivotage) mais elle exige mathématiquement que $A = A^T$ et que $x^T A x > 0$ pour tout $x \neq 0$.
</details>

### Question 2.5 : L'indice de conditionnement d'une matrice inversible $A$, noté $\kappa(A)$ en norme quelconque, est calculé comme suit :
- [ ] A) $\kappa(A) = ||A|| + ||A^{-1}||$
- [ ] B) $\kappa(A) = \det(A) \cdot \det(A^{-1})$
- [ ] C) $\kappa(A) = \frac{\lambda_{max}(A)}{\lambda_{min}(A)}$ uniquement
- [ ] D) $\kappa(A) = ||A|| \cdot ||A^{-1}||$

<details>
<summary>💡 Solution</summary>

**Réponse D**. Le conditionnement s'écrit formellement par le produit des normes. S'il est très grand $\kappa(A) \gg 1$, le système $Ax=b$ est mal conditionné et sa solution numérique est instable.
</details>

---

## Chapitre 3 — Équations Non-Linéaires & Recherche de Racines

### Question 3.1 : Quelles sont les exigences sur la fonction $f$ pour appliquer le théorème de Bolzano (base de la méthode de bissection) sur l'intervalle $[a, b]$ ?
- [ ] A) $f$ doit être continue et $f(a) \cdot f(b) < 0$.
- [ ] B) $f$ doit être strictement monotone convexe.
- [ ] C) $f$ doit être dérivable partout.
- [ ] D) L'intervalle doit contenir l'origine zéro.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Si la fonction est continue et change de signe aux bornes ($f(a) \cdot f(b) < 0$), le théorème des valeurs intermédiaires (ou Bolzano) garantit qu'il existe au moins une racine dans $[a, b]$.
</details>

### Question 3.2 : Quelle est la vitesse de convergence (l'ordre) de la méthode de Newton-Raphson lorsque l'on est proche d'une racine **simple** ?
- [ ] A) Convergence Linéaire (Ordre 1)
- [ ] B) Convergence Super-Linéaire (Ordre 1.618)
- [ ] C) Convergence Quadratique (Ordre 2)
- [ ] D) Convergence Cubique (Ordre 3)

<details>
<summary>💡 Solution</summary>

**Réponse C**. La grande force de Newton est sa convergence quadratique. L'erreur à l'étape $n+1$ est approximativement proportionnelle au carré de l'erreur à l'étape $n$.
</details>

### Question 3.3 : Quelle est la formule itérative canonique de la méthode de Newton-Raphson pour trouver la racine de $f(x)=0$ ?
- [ ] A) $x_{k+1} = x_k - \frac{f(x_k)}{2}$
- [ ] B) $x_{k+1} = \frac{x_k + f(x_k)}{f'(x_k)}$
- [ ] C) $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$
- [ ] D) $x_{k+1} = x_k \cdot f(x_k) - f'(x_k)$

<details>
<summary>💡 Solution</summary>

**Réponse C**. Formule de Newton. Elle se base géométriquement sur l'intersection de la tangente à la courbe de $f$ en $x_k$ avec l'axe des abscisses.
</details>

### Question 3.4 : Que se passe-t-il pour la méthode de Newton si la racine $\alpha$ recherchée est *multiple* (par ex. racine double, $f(\alpha)=0$ et $f'(\alpha)=0$) ?
- [ ] A) La méthode n'est pas du tout capable d'évaluer la fonction.
- [ ] B) La méthode de Newton conserve son ordre de convergence quadratique sans problème.
- [ ] C) La méthode de Newton perd sa convergence quadratique et devient seulement linéaire.
- [ ] D) Newton part instantanément vers l'infini.

<details>
<summary>💡 Solution</summary>

**Réponse C**. La racine de la dérivée modifie le profil d'erreur. Si la multiplicité est $>1$, Newton ne converge que de façon linéaire. On peut "modifier" Newton en $x - \frac{m f(x)}{f'(x)}$ pour retrouver un taux quadratique.
</details>

### Question 3.5 : En quoi la méthode de la *Sécante* diffère-t-elle principalement de la méthode de *Newton* ?
- [ ] A) Elle nécessite la dérivée seconde $f''(x)$ pour chaque itération.
- [ ] B) Elle utilise l'intervalle entier, donc elle exige un changement de signe strict $f(a) \cdot f(b) < 0$.
- [ ] C) Elle approxime la dérivée par le quotient différentiel entre les deux derniers points calculés, supprimant le besoin de calculer analytiquement $f'(x)$.
- [ ] D) Elle converge toujours plus vite que Newton.

<details>
<summary>💡 Solution</summary>

**Réponse C**. La Sécante est idéale quand la dérivée $f'(x)$ est trop difficile ou coûteuse à obtenir. Son ordre de convergence est de $1.618$ (nombre d'or), soit un peu moins performant que Newton mais très pratique.
</details>

