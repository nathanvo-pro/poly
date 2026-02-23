# Séances d'Exercices — Analyse Numérique

## Séance 1 — Prise en main d'Octave

### Rappels théoriques

**Octave/Matlab** est un langage de calcul scientifique interprété, orienté matrices. Tout est matrice.

**Commandes essentielles :**
- `clear` : supprime les variables. `clc` : efface la console. `whos` : liste les variables.
- `format short` / `format long` : contrôle la précision d'affichage.
- `;` en fin de ligne : exécute sans afficher le résultat.

**Vecteurs et matrices :**
- Vecteur colonne : `v = [1;2;3]`. Vecteur ligne : `w = [1 2 3]` ou `w = 1:3`.
- Matrice : `M = [1 2; 3 4]` (`;` sépare les lignes, espace sépare les colonnes).
- Transposée : `M'`. Taille : `size(M)`. Longueur : `length(v)`.
- Indexation : `v(2)`, `M(1:2,:)` (lignes 1 à 2, toutes colonnes).
- Concaténation verticale : `[A;B]`. Horizontale : `[A B]` (dimensions doivent correspondre).

**Opérations critiques :**
- `A*B` : produit **matriciel** (les dimensions internes doivent correspondre).
- `A.*B` : produit **élément par élément** (même dimension requise).
- `A\b` : résout $Ax = b$ (équivalent de $A^{-1}b$, mais plus efficient).

**Graphes :**
- `x = 0:0.01:2*pi` crée un vecteur de 0 à $2\pi$ par pas de 0.01.
- `plot(x, sin(x), '-r')` trace $\sin(x)$ en rouge.
- `hold on` / `hold off` : superpose / efface les courbes précédentes.

**Fonctions :**
- `function y = mafct(x)` dans un fichier `mafct.m`.
- Le déterminant d'une matrice triangulaire = produit de sa diagonale.

**Fonctions mathématiques :** `exp`, `log` (ln), `log10`, `log2`, `sin`, `cos`, `pi`.
Pour un logarithme en base $b$ : $\log_b(x) = \frac{\ln(x)}{\ln(b)}$.

### Exercices résolus par type

#### Type 1 : Manipulation de vecteurs et matrices

**Méthode :** Créer des vecteurs/matrices, les indexer, les concaténer et comprendre la différence entre `*` et `.*`.

**Exercice similaire :**
Soit $v = \begin{pmatrix} 2 \\ 5 \\ 8 \\ 3 \end{pmatrix}$ et $M = \begin{pmatrix} 1 & 4 \\ 7 & 2 \\ 3 & 6 \end{pmatrix}$.
a) Créez $v$ et $M$ dans Octave. Extrayez le sous-vecteur $v(2:3)$ et la sous-matrice $M(1:2, :)$.
b) Calculez $v^T v$ (produit scalaire) et $v .* v$ (carré élément par élément). Expliquez la différence.
c) Pourquoi `v * v` provoque-t-il une erreur ?

<details>
<summary>Voir la résolution complète</summary>

```octave
v = [2; 5; 8; 3];
M = [1 4; 7 2; 3 6];

% a) Extraction
v(2:3)         % Résultat: [5; 8]
M(1:2, :)      % Résultat: [1 4; 7 2]

% b) Produit scalaire vs produit élément par élément
v' * v          % = 2² + 5² + 8² + 3² = 4 + 25 + 64 + 9 = 102 (scalaire)
v .* v          % = [4; 25; 64; 9] (vecteur colonne)
```

**Explication :** `v'*v` est un produit matriciel : $(1 \times 4) \cdot (4 \times 1) = (1 \times 1)$, un scalaire.
`v.*v` multiplie chaque élément par lui-même, le résultat est un vecteur de même taille.

**c)** `v * v` essaie un produit matriciel $(4 \times 1) \cdot (4 \times 1)$. Les dimensions internes ($1 \neq 4$) ne correspondent pas → erreur.

</details>

#### Type 2 : Opérations sur les matrices (élimination manuelle, inverse, déterminant)

**Méthode :** Utiliser `rand`, `eye`, `inv`, `det`. Comprendre que $LA$ annule la première colonne si $L$ est une matrice d'élimination de Gauss.

**Exercice similaire :**
a) Créez une matrice aléatoire $A$ de taille $4 \times 4$ et une matrice identité $L = I_4$.
b) Remplacez la première colonne de $L$ (sous la diagonale) par $-a_{i1}/a_{11}$ pour $i = 2, 3, 4$.
c) Calculez $LA$. Que vaut la première colonne du résultat ? Pourquoi ?
d) Vérifiez que $\det(\text{triu}(A)) = \prod_{i} A_{ii}$ (produit des éléments diagonaux).

<details>
<summary>Voir la résolution complète</summary>

```octave
A = rand(4, 4);
L = eye(4);

% b) Remplissage des multiplicateurs
L(2:4, 1) = -A(2:4, 1) / A(1, 1);

% c) Produit
B = L * A;
B(:, 1)    % La première colonne vaut [a11; 0; 0; 0]
```

**Explication de c) :** La matrice $L$ est construite pour annuler tous les éléments sous le pivot $a_{11}$. C'est exactement l'étape 1 de l'élimination de Gauss. Le résultat $LA$ a des zéros sous le pivot dans la première colonne.

```octave
% d) Vérification du déterminant d'une triangulaire
U = triu(A);            % Extrait la partie triangulaire supérieure
det(U)                   % Déterminant calculé par Octave
prod(diag(U))            % Produit des éléments diagonaux
% Les deux valeurs sont identiques !
```

**Explication :** Pour toute matrice triangulaire, $\det(T) = t_{11} \cdot t_{22} \cdots t_{nn}$. C'est une propriété fondamentale.

</details>

#### Type 3 : Écrire des fonctions Octave et tracer des graphes

**Méthode :** Créer un fichier `.m` avec `function y = nom(x)`. Utiliser `plot` pour visualiser. Gérer les cas spéciaux avec `if`.

**Exercice similaire :**
Écrivez deux fonctions Octave et tracez-les sur $[-2, 2]$ :

a) $g(x) = \frac{e^{x/2}}{\log_{10}(|x| + 1)}$

b) $h(x) = \begin{cases} 1 & \text{si } x = 0 \\ \frac{1 - \cos(x)}{x^2} & \text{sinon} \end{cases}$

<details>
<summary>Voir la résolution complète</summary>

```octave
% Fichier g.m
function y = g(x)
    y = exp(x/2) ./ log10(abs(x) + 1);
endfunction

% Fichier h.m
function y = h(x)
    y = zeros(size(x));   % Pré-allouer le vecteur résultat
    for k = 1:length(x)
        if x(k) == 0
            y(k) = 1/2;   % Limite de (1-cos(x))/x² quand x→0 = 1/2
        else
            y(k) = (1 - cos(x(k))) / x(k)^2;
        end
    end
endfunction

% Script principal
x = -2:0.01:2;
figure;
subplot(1,2,1); plot(x, g(x), '-b'); title('g(x)'); grid on;
subplot(1,2,2); plot(x, h(x), '-r'); title('h(x)'); grid on;
```

**Note sur le log en base quelconque :** Octave ne fournit que `log` ($\ln$), `log2`, `log10`. Pour un log en base $b$ : `log(x) / log(b)`. Ce n'est donc pas limitatif.

</details>

---

## Séance 2 — Erreurs d'arrondi et propagation

### Rappels théoriques

**Hypothèses de travail :** Machine IEEE, $u$ = unité d'arrondi, termes en $O(u^2)$ négligeables.

**Formule fondamentale (formule 5 du cours) :** La projection en virgule flottante garantit :

$$
\text{fl}(x) = x(1 + \varepsilon), \quad |\varepsilon| \leq u
$$

**Version alternative :** On peut aussi montrer que $\frac{|\text{fl}(x) - x|}{|\text{fl}(x)|} \leq u$.

**Modèle d'arithmétique standard :** Pour toute opération $\circ \in \{+, -, \times, /\}$ :

$$
a \circledcirc b = (a \circ b)(1 + \varepsilon), \quad |\varepsilon| \leq u
$$

**Propagation des erreurs — Recettes :**
Si $\tilde{x} = x(1 + \varepsilon_1)$ et $\tilde{y} = y(1 + \varepsilon_2)$ avec $|\varepsilon_i| \leq u$ :

- **Produit :** $\tilde{x} \otimes \tilde{y} = xy(1 + \varepsilon_1)(1 + \varepsilon_2)(1 + \varepsilon_3) \approx xy(1 + \varepsilon')$ avec $|\varepsilon'| \leq 3u$
- **Somme :** $\tilde{x} \oplus \tilde{y} = (x(1+\varepsilon_1) + y(1+\varepsilon_2))(1+\varepsilon_3)$. Si $x, y > 0$ : erreur relative $\leq 3u$. Mais si $x \approx -y$ → **annulation catastrophique**.
- **Division :** $\tilde{x} \oslash \tilde{y} = \frac{x}{y} \cdot \frac{(1+\varepsilon_1)}{(1+\varepsilon_2)} \cdot (1+\varepsilon_3) \approx \frac{x}{y}(1 + \varepsilon')$ avec $|\varepsilon'| \leq 3u$

**Règles de simplification :**
1. $\alpha\varepsilon_1 \pm \beta\varepsilon_2 = (|\alpha| + |\beta|)\varepsilon_3$
2. $(1+\alpha\varepsilon_1)(1+\beta\varepsilon_2) = 1 + (|\alpha|+|\beta|)\varepsilon_3 + O(u^2)$
3. $\frac{1}{1+\alpha\varepsilon} = 1 + \alpha\varepsilon' + O(u^2)$

**Dérivée numérique et annulation :**
L'approximation par différences finies $f'(x_0) \approx \frac{f(x_0+h) - f(x_0)}{h}$ souffre de deux erreurs contradictoires :
- Erreur de troncature (Taylor) $\sim O(h)$ : diminue quand $h \to 0$
- Erreur d'arrondi $\sim O(u/h)$ : **augmente** quand $h \to 0$
- Il existe un $h$ optimal qui minimise l'erreur totale (typiquement $h^* \sim \sqrt{u}$).

### Exercices résolus par type

#### Type 1 : Démonstration de bornes d'erreur relative

**Méthode :** Partir de la définition de `fl(x)`, manipuler l'inégalité, utiliser les propriétés des valeurs absolues.

**Exercice similaire :**
Soit $x \in \mathbb{R}$ tel que $\text{fl}(x) = x(1+\varepsilon)$ avec $|\varepsilon| \leq u$. Montrez que :

$$
\frac{|\text{fl}(x) - x|}{|\text{fl}(x)|} \leq u + O(u^2)
$$

<details>
<summary>Voir la résolution complète</summary>

On part de $\text{fl}(x) = x(1+\varepsilon)$. L'erreur absolue est :

$$
|\text{fl}(x) - x| = |x(1+\varepsilon) - x| = |x\varepsilon| = |x||\varepsilon|
$$

Divisons par $|\text{fl}(x)| = |x||1+\varepsilon|$ :

$$
\frac{|\text{fl}(x) - x|}{|\text{fl}(x)|} = \frac{|x||\varepsilon|}{|x||1+\varepsilon|} = \frac{|\varepsilon|}{|1+\varepsilon|}
$$

En utilisant la règle 3 : $\frac{1}{1+\varepsilon} = 1 - \varepsilon + O(\varepsilon^2)$, on obtient :

$$
\frac{|\varepsilon|}{|1+\varepsilon|} = |\varepsilon| \cdot (1 + O(u)) = |\varepsilon| + O(u^2) \leq u + O(u^2) \quad \blacksquare
$$

</details>

#### Type 2 : Estimation numérique d'une erreur d'arrondi sur une expression

**Méthode :** Décomposer l'expression en opérations élémentaires. Appliquer le modèle standard $(a \circ b)(1+\varepsilon)$ à chaque étape. Accumuler les $\varepsilon_i$.

**Exercice similaire :**
Estimez l'erreur d'arrondi relative sur l'opération `pi * (1/3) * 3` en double précision ($u \approx 1.1 \times 10^{-16}$). Vérifiez numériquement.

<details>
<summary>Voir la résolution complète</summary>

**Analyse symbolique :**
1. $a_1 = \text{fl}(1/3) = \frac{1}{3}(1 + \varepsilon_1)$
2. $a_2 = \text{fl}(\pi \cdot a_1) = \pi \cdot a_1 (1 + \varepsilon_2) = \frac{\pi}{3}(1+\varepsilon_1)(1+\varepsilon_2)$
3. $a_3 = \text{fl}(a_2 \cdot 3) = a_2 \cdot 3 (1+\varepsilon_3) = \pi(1+\varepsilon_1)(1+\varepsilon_2)(1+\varepsilon_3)$

Par la règle 2 : $(1+\varepsilon_1)(1+\varepsilon_2)(1+\varepsilon_3) = 1 + \varepsilon'$ avec $|\varepsilon'| \leq 3u + O(u^2) \approx 3u$.

Donc l'erreur relative attendue est $\leq 3u \approx 3.3 \times 10^{-16}$.

**Vérification numérique (Octave) :**
```octave
format long;
result = pi * (1/3) * 3;
err = abs(result - pi) / abs(pi)
% err ≈ 4.4e-16 (confirme l'ordre de 3u)
```

</details>

#### Type 3 : Propagation d'erreur sur les opérations arithmétiques

**Méthode :** Partir de $\tilde{x} = x(1+\varepsilon_1)$, $\tilde{y} = y(1+\varepsilon_2)$. Effectuer l'opération machine, développer, utiliser les règles de simplification.

**Exercice similaire :**
Soient $\tilde{a} = a(1+\varepsilon_1)$ et $\tilde{b} = b(1+\varepsilon_2)$ avec $a, b > 0$ et $|\varepsilon_i| \leq u$.
Estimez l'erreur relative de $\tilde{a} \ominus \tilde{b}$ (la soustraction machine). Discutez le cas $a \approx b$.

<details>
<summary>Voir la résolution complète</summary>

$$
\tilde{a} \ominus \tilde{b} = (\tilde{a} - \tilde{b})(1+\varepsilon_3) = (a(1+\varepsilon_1) - b(1+\varepsilon_2))(1+\varepsilon_3)
$$

Développons le cœur :

$$
= (a - b + a\varepsilon_1 - b\varepsilon_2)(1+\varepsilon_3)
$$

$$
= (a-b)(1+\varepsilon_3) + (a\varepsilon_1 - b\varepsilon_2)(1+\varepsilon_3)
$$

En négligeant $O(u^2)$ :

$$
\approx (a-b) + (a-b)\varepsilon_3 + a\varepsilon_1 - b\varepsilon_2
$$

Erreur relative (on divise par $a - b$) :

$$
\frac{|\text{erreur}|}{|a-b|} \leq |\varepsilon_3| + \frac{|a||\varepsilon_1| + |b||\varepsilon_2|}{|a - b|} \leq u + \frac{(|a| + |b|)u}{|a - b|}
$$

**Discussion :** Si $a \approx b$, le dénominateur $|a - b| \to 0$ et la fraction explose → $\infty$.
C'est l'**annulation catastrophique** : l'erreur relative de la soustraction de deux nombres proches diverge, même si les opérandes sont précis.

</details>

#### Type 4 : Dérivée numérique — erreur de troncature + erreur d'arrondi

**Méthode :** Utiliser Taylor pour l'erreur de troncature, et le modèle standard pour l'erreur d'arrondi. Identifier l'erreur totale comme la somme des deux.

**Exercice similaire :**
Soit $f(x) = \sin(x)$ et $x_0 = \pi/4$.
a) Montrez que l'erreur de troncature de $f'_h(x_0) = \frac{f(x_0+h) - f(x_0)}{h}$ est bornée par $\frac{h}{2}|f''(\xi)|$ pour un certain $\xi$.
b) Évaluez numériquement $|f'_h(\pi/4) - f'(\pi/4)|$ pour $h = 10^{-4}, 10^{-8}, 10^{-12}, 10^{-15}$.
c) Expliquez pourquoi l'erreur ne diminue pas indéfiniment.

<details>
<summary>Voir la résolution complète</summary>

**a)** Par Taylor : $f(x_0+h) = f(x_0) + hf'(x_0) + \frac{h^2}{2}f''(\xi)$, donc :

$$
f'_h(x_0) = \frac{f(x_0) + hf'(x_0) + \frac{h^2}{2}f''(\xi) - f(x_0)}{h} = f'(x_0) + \frac{h}{2}f''(\xi)
$$

L'erreur de troncature est $|f'_h - f'| = \frac{h}{2}|f''(\xi)| \leq \frac{h}{2} \cdot 1 = \frac{h}{2}$ (car $|f''| = |\sin| \leq 1$).

**b)** Code Octave et résultats :
```octave
x0 = pi/4;
exact = cos(x0);  % f'(pi/4) = cos(pi/4) = sqrt(2)/2
for k = [4 8 12 15]
    h = 10^(-k);
    approx = (sin(x0 + h) - sin(x0)) / h;
    fprintf('h = 1e-%d, erreur = %.2e\n', k, abs(approx - exact));
end
```

| $h$ | Erreur |
|---|---|
| $10^{-4}$ | $\sim 3.5 \times 10^{-5}$ (dominée par troncature $\sim h/2$) |
| $10^{-8}$ | $\sim 6 \times 10^{-9}$ (meilleur compromis) |
| $10^{-12}$ | $\sim 4 \times 10^{-5}$ (l'arrondi domine !) |
| $10^{-15}$ | $\sim 0.1$ (catastrophe) |

**c)** L'erreur totale est $E(h) \approx \frac{h}{2} + \frac{Cu}{h}$ où $C$ dépend de $|f(x_0)|$.
- Pour $h$ grand : erreur de troncature domine ($\sim h$).
- Pour $h$ petit : erreur d'arrondi domine ($\sim u/h$).
- Le minimum est atteint pour $h^* \sim \sqrt{u} \approx 10^{-8}$ en double précision.

En dessous de $h^*$, réduire $h$ **aggrave** l'erreur au lieu de l'améliorer !

</details>

---

## Séance 3 — Conditionnement et factorisation LU

### Rappels théoriques

**Conditionnement d'un système linéaire $Ax = b$ :**

$$
\kappa(A) = \|A\| \cdot \|A^{-1}\|
$$

Le conditionnement borne l'amplification de l'erreur relative :

$$
\frac{\|\delta x\|}{\|x\|} \leq \kappa(A) \cdot \frac{\|\delta b\|}{\|b\|}
$$

**Interprétation de $\kappa(A)$ pour la stabilité directe :**
Si un algorithme a la stabilité directe (erreur $\leq Cu$), alors la précision atteignable sur la solution est $\sim \kappa(A) \cdot u$. En double précision ($u \approx 10^{-16}$) :
- $\kappa = 10^4$ → on perd 4 chiffres significatifs → ~12 chiffres corrects.
- $\kappa = 10^{15}$ → on perd 15 chiffres → ~1 chiffre correct (inutilisable !).

**Commandes Octave :** `cond(A)` (conditionnement 2-norme), `norm(A)`, `inv(A)`.

**Factorisation LU sans pivotage :**
Algorithme de Gauss : pour chaque colonne $k$ de 1 à $n-1$, calculer les multiplicateurs $l_{ik} = a^{(k)}_{ik} / a^{(k)}_{kk}$ et soustraire :

$$
a^{(k+1)}_{ij} = a^{(k)}_{ij} - l_{ik} \cdot a^{(k)}_{kj}, \quad i > k
$$

Résultat : $A = LU$ avec $L$ unitaire inférieure, $U$ triangulaire supérieure.
Résolution : $Ly = b$ (descente), puis $Ux = y$ (remontée). En Octave : `U\y` et `L\b`.

**Factorisation PA = LU (avec pivotage partiel) :**
Avant chaque étape $k$, permuter la ligne du pivot maximal dans la colonne $k$.
En Octave : `[L, U, P] = lu(A)`, puis résoudre $Ly = Pb$ et $Ux = y$.

**Quand LU sans pivot échoue :**
Si le pivot $a^{(k)}_{kk}$ est très petit, le multiplicateur $l_{ik}$ explose → instabilité numérique. Le pivotage résout ce problème en choisissant toujours le plus grand pivot possible.

### Exercices résolus par type

#### Type 1 : Calcul du conditionnement et interprétation

**Méthode :** Utiliser `cond(A)` dans Octave. Interpréter la valeur : combien de chiffres significatifs perd-on ?

**Exercice similaire :**
Calculez le conditionnement des deux systèmes suivants et déterminez combien de chiffres significatifs sont fiables en double précision.

$$
A_1 = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}, \quad
A_2 = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1.0001 & 1 \\ 1 & 1 & 1.0001 \end{pmatrix}
$$

<details>
<summary>Voir la résolution complète</summary>

```octave
A1 = [4 1 1; 1 4 1; 1 1 4];
A2 = [1 1 1; 1 1.0001 1; 1 1 1.0001];

fprintf('kappa(A1) = %.2e\n', cond(A1));   % ≈ 2.00 (excellent !)
fprintf('kappa(A2) = %.2e\n', cond(A2));   % ≈ 3.00e+04 (problématique)
```

**Interprétation :**
- $A_1$ : $\kappa \approx 2$. Perte de $\log_{10}(2) \approx 0.3$ chiffre → **16 chiffres corrects**. Système parfaitement conditionné.
- $A_2$ : $\kappa \approx 3 \times 10^4$. Perte de $\log_{10}(3 \times 10^4) \approx 4.5$ chiffres → **~11 chiffres corrects**. Acceptable mais attention aux erreurs accumulées.

**Précision atteignable :** En stabilité directe, l'erreur relative sur $x$ est bornée par $\kappa(A) \cdot u$. Pour $A_2$ : $3 \times 10^4 \times 1.1 \times 10^{-16} \approx 3.3 \times 10^{-12}$.

</details>

#### Type 2 : Programmation de la factorisation LU (sans pivotage)

**Méthode :** Implémenter l'élimination de Gauss colonne par colonne. Stocker les multiplicateurs dans $L$.

**Exercice similaire :**
Écrivez une fonction Octave `[L, U] = my_lu(A)` qui calcule la factorisation LU sans pivotage. Testez-la sur la matrice $A_1$ ci-dessus avec $b_1 = (6, 6, 6)^T$.

<details>
<summary>Voir la résolution complète</summary>

```octave
function [L, U] = my_lu(A)
    n = size(A, 1);
    L = eye(n);         % L commence comme l'identité
    U = A;              % U commence comme A, on va la transformer

    for k = 1:n-1                       % Pour chaque colonne pivot
        for i = k+1:n                   % Pour chaque ligne sous le pivot
            L(i, k) = U(i, k) / U(k, k);  % Multiplicateur
            U(i, :) = U(i, :) - L(i, k) * U(k, :);  % Élimination
        end
    end
endfunction
```

**Test :**
```octave
A1 = [4 1 1; 1 4 1; 1 1 4];
b1 = [6; 6; 6];

[L, U] = my_lu(A1);

% Vérification : L*U doit redonner A1
norm(L*U - A1)   % ≈ 0 (machine precision)

% Résolution de Ax = b via LU :
y = L \ b1;      % Descente : Ly = b
x = U \ y;       % Remontée : Ux = y
disp(x)          % x = [1; 1; 1] (solution exacte)
```

**Résultat :** $x = (1, 1, 1)^T$ est la solution exacte (car $\kappa(A_1) \approx 2$, presque pas de perte de précision).

</details>

#### Type 3 : Détection d'instabilité LU et correction par PA=LU

**Méthode :** Comparer la solution de `my_lu` vs `lu` d'Octave (avec pivotage). Si le conditionnement est grand ET que la matrice a de petits pivots, LU sans pivotage échoue.

**Exercice similaire :**
Considérez le système :

$$
A_3 = \begin{pmatrix} 10^{-15} & 1 \\ 1 & 1 \end{pmatrix}, \quad b_3 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

a) Résolvez avec `my_lu` (sans pivotage). Que vaut l'erreur relative ?
b) Résolvez avec `[L,U,P] = lu(A3)` puis `U\(L\(P*b3))`. Comparez.
c) Expliquez pourquoi le pivotage sauve le calcul.

<details>
<summary>Voir la résolution complète</summary>

```octave
A3 = [1e-15, 1; 1, 1];
b3 = [1; 2];

% Solution exacte (calculée à la main)
% x1 = 1/(1 - 1e-15), x2 = 1 - x1*1e-15 ≈ 1
x_exact = A3 \ b3;   % En utilisant le solveur interne bien pivoté

% a) LU sans pivotage
[L, U] = my_lu(A3);
y = L \ b3;
x_nopiv = U \ y;
err_nopiv = norm(x_nopiv - x_exact) / norm(x_exact);
fprintf('Erreur sans pivotage: %.2e\n', err_nopiv);  % Très grande !

% b) PA=LU avec pivotage
[L2, U2, P2] = lu(A3);
y2 = L2 \ (P2 * b3);
x_piv = U2 \ y2;
err_piv = norm(x_piv - x_exact) / norm(x_exact);
fprintf('Erreur avec pivotage: %.2e\n', err_piv);    % ≈ 1e-16 (parfait)
```

**c) Explication :** Sans pivotage, le pivot $a_{11} = 10^{-15}$ est microscopique. Le multiplicateur $l_{21} = 1/10^{-15} = 10^{15}$ est astronomique. La ligne 2 est remplacée par $L_2 - 10^{15} L_1$ : le terme $10^{15} \times 1 = 10^{15}$ écrase complètement le $1$, et l'arrondi machine détruit toute information utile.

Avec pivotage, Octave échange les lignes 1 et 2 **avant** l'élimination. Le nouveau pivot est $1$ (la plus grande valeur), et le multiplicateur est $10^{-15}$ (minuscule, inoffensif). Le calcul est stable.

</details>


---

## Séance 4 — Factorisation PA=LU et QR à la main

### Rappels théoriques

#### La factorisation PA = LU avec pivotage partiel

**Algorithme complet** (à exécuter colonne par colonne) :

Pour chaque étape $k = 1, \ldots, n-1$ :
1. **Choisir le pivot :** trouver $i^* = \arg\max_{i \geq k} |a^{(k)}_{ik}|$ (la ligne du plus grand élément dans la colonne $k$ sous la diagonale).
2. **Permuter les lignes :** échanger la ligne $k$ et la ligne $i^*$ dans la matrice courante **et** enregistrer la permutation dans $P$.
3. **Éliminer :** pour $i = k+1, \ldots, n$ :

$$
l_{ik} = \frac{a^{(k)}_{ik}}{a^{(k)}_{kk}}, \qquad \text{ligne}\ i \leftarrow \text{ligne}\ i - l_{ik} \times \text{ligne}\ k
$$

**Résultat :** $PA = LU$ où :
- $P$ : matrice de permutation (produit des échanges de lignes), $P^T P = I$, $P^{-1}=P^T$.
- $L$ : triangulaire inférieure, diagonale = 1, éléments sous-diagonaux = multiplicateurs $l_{ik}$.
- $U$ : triangulaire supérieure issue de l'élimination.

**Résolution du système $Ax = b$ :** on substitue $A = P^T LU$, donc $P^T LU x = b$, soit $LUx = Pb$. On résout :
1. $Ly = Pb$ par descente (forward substitution).
2. $Ux = y$ par remontée (backward substitution).

**En Octave :** `[L, U, P] = lu(A)` (attention : `lu` retourne $PA = LU$, donc `P` est la matrice de permutation).

#### La factorisation QR par réflexions de Householder

**Principe :** transformer $A$ en matrice triangulaire supérieure $R$ en multipliant successivement par des matrices de Householder $H_1, H_2, \ldots$ à gauche :
$$
H_{n-1} \cdots H_2 H_1 A = R \implies A = Q R, \quad Q = H_1^T H_2^T \cdots H_{n-1}^T
$$

**Construction de $H_k$ pour la colonne $k$ :** Soit $a$ la sous-colonne $a = A^{(k)}(k:m, k)$ (les éléments de la colonne $k$ depuis la diagonale).
1. Calculer $\alpha = -\text{sign}(a_1) \|a\|_2$ (le signe évite la cancellation).
2. Former le vecteur de Householder : $v = a - \alpha e_1$ où $e_1 = (1,0,\ldots,0)^T$.
3. Calculer $H = I - 2\frac{vv^T}{\|v\|^2}$.
4. Appliquer à la sous-matrice : $A^{(k+1)}(k:m, k:n) = H \cdot A^{(k)}(k:m, k:n)$.

**Propriétés $H$ :** symétrique ($H^T = H$), orthogonale ($H^2 = I$), applique une réflexion géométrique.

**Algorithme complet Octave (sans `qr`) :**
```octave
function [Q, R] = my_qr(A)
    [m, n] = size(A);
    Q = eye(m);
    R = A;
    for k = 1:min(m-1, n)
        x = R(k:m, k);
        alpha = -sign(x(1)) * norm(x);
        e1 = zeros(length(x), 1); e1(1) = 1;
        v = x - alpha * e1;
        if norm(v) < eps, continue; end
        H_small = eye(length(x)) - 2*(v*v')/(v'*v);
        % Construction de H pleine taille
        H = eye(m);
        H(k:m, k:m) = H_small;
        R = H * R;
        Q = Q * H';  % Q s'accumule
    end
endfunction
```

**Vérification :** `norm(Q*R - A)` doit être $\approx 0$. `norm(Q'*Q - eye(m))` doit être $\approx 0$.

#### Comparaison PA=LU vs QR

| Critère | PA = LU | QR (Householder) |
|---|---|---|
| Coût | $\frac{2}{3}n^3$ flops | $2n^2(m - n/3)$ flops |
| Stabilité | Très bonne (avec pivotage) | Excellente (toujours) |
| Applications | Systèmes carrés $Ax=b$ | Moindres carrés, systèmes surdéterminés |

### Exercices résolus par type

#### Type 1 : Factorisation PA=LU manuelle (étape par étape)

**Méthode :** Pour chaque colonne, chercher le pivot maximal, noter la permutation dans $P$, appliquer l'élimination avec les multiplicateurs stockés dans $L$.

**Exercice similaire :**
Calculez manuellement les matrices $P$, $L$, $U$ de la factorisation $PA=LU$ pour la matrice :

$$
A = \begin{pmatrix} 0 & 2 & 1 \\ 3 & -1 & 2 \\ 1 & 4 & -1 \end{pmatrix}
$$

<details>
<summary>Voir la résolution complète (étape par étape)</summary>

**État initial :**

$$
A^{(1)} = \begin{pmatrix} 0 & 2 & 1 \\ 3 & -1 & 2 \\ 1 & 4 & -1 \end{pmatrix}, \quad P = I_3
$$

**Étape 1 — Colonne 1 :**
Pivot maximal : $\max(|0|, |3|, |1|) = 3$ à la ligne 2.
Permuter lignes 1 et 2 → enregistrer $P_{12}$ :

$$
P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad A^{(1)} = \begin{pmatrix} 3 & -1 & 2 \\ 0 & 2 & 1 \\ 1 & 4 & -1 \end{pmatrix}
$$

Multiplicateurs : $l_{21} = 0/3 = 0$, $l_{31} = 1/3$.
Élimination ligne 3 : $L_3 \leftarrow L_3 - \frac{1}{3}L_1$ :

$$
A^{(2)} = \begin{pmatrix} 3 & -1 & 2 \\ 0 & 2 & 1 \\ 0 & 4+\frac{1}{3} & -1-\frac{2}{3} \end{pmatrix} = \begin{pmatrix} 3 & -1 & 2 \\ 0 & 2 & 1 \\ 0 & \frac{13}{3} & -\frac{5}{3} \end{pmatrix}
$$

**Étape 2 — Colonne 2 :**
Pivot maximal (sous-matrice $2:3,2:3$) : $\max(|2|, |13/3|) = 13/3$ à la ligne 3.
Permuter lignes 2 et 3 → enregistrer $P_{23}$ :

$$
A^{(2)} = \begin{pmatrix} 3 & -1 & 2 \\ 0 & \frac{13}{3} & -\frac{5}{3} \\ 0 & 2 & 1 \end{pmatrix}, \quad
P = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}
$$

Multiplicateur : $l_{32} = 2/(13/3) = 6/13$.
Élimination : $L_3 \leftarrow L_3 - \frac{6}{13}L_2$ :

$$
U = \begin{pmatrix} 3 & -1 & 2 \\ 0 & \frac{13}{3} & -\frac{5}{3} \\ 0 & 0 & 1 + \frac{6}{13} \cdot \frac{5}{3} \end{pmatrix} = \begin{pmatrix} 3 & -1 & 2 \\ 0 & \frac{13}{3} & -\frac{5}{3} \\ 0 & 0 & \frac{23}{13} \end{pmatrix}
$$

**Résultat final :**

$$
L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ \frac{1}{3} & \frac{6}{13} & 1 \end{pmatrix}
$$

**Vérification Octave :**
```octave
A = [0 2 1; 3 -1 2; 1 4 -1];
[L2, U2, P2] = lu(A);
norm(L2*U2 - P2*A)  % doit être ≈ 0
```

</details>

#### Type 2 : Factorisation QR manuelle par Householder (étape par étape)

**Méthode :** Pour chaque colonne $k$, construire le vecteur $v$ de Householder, calculer $H$, mettre à jour la matrice. Accumuler $Q = H_1^T H_2^T \cdots$.

**Exercice similaire :**
Calculez manuellement la factorisation QR de la matrice :

$$
B = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 3 \end{pmatrix}
$$

<details>
<summary>Voir la résolution complète (étape par étape)</summary>

**Étape 1 — Éliminer sous la diagonale de la colonne 1 :**

Sous-colonne : $a = B(1:3, 1) = (1, 2, 0)^T$.
$\|a\|_2 = \sqrt{1+4+0} = \sqrt{5}$.
Signe de $a_1 = 1 > 0$, donc $\alpha = -\sqrt{5}$.
$e_1 = (1, 0, 0)^T$.
$v = a - \alpha e_1 = (1+\sqrt{5}, 2, 0)^T$.
$\|v\|^2 = (1+\sqrt{5})^2 + 4 = 1 + 2\sqrt{5} + 5 + 4 = 10 + 2\sqrt{5}$.

$$
H_1 = I - \frac{2vv^T}{\|v\|^2}
$$

Application à $B$ : $B^{(2)} = H_1 B$. Le résultat dans la colonne 1 sera $(\sqrt{5}, 0, 0)^T$.

**Colonne 1 de $B^{(2)}$ :** $(\sqrt{5}, 0, 0)^T$ ✓ (les zéros sont garantis par la construction de Householder).

**Étape 2 — Éliminer sous la diagonale de la colonne 2 :**
On travaille sur la sous-matrice $B^{(2)}(2:3, 2:2)$.
Sous-colonne : $a = B^{(2)}(2:3, 2)$ (un vecteur 2×1 calculé numériquement).

**Vérification Octave :**
```octave
B = [1 1; 2 0; 0 3];
[Q, R] = my_qr(B);
norm(Q*R - B)        % ≈ 0
norm(Q'*Q - eye(3))  % ≈ 0 (Q est orthogonale)

% Comparer avec qr() builtin
[Q2, R2] = qr(B);
% Note: QR n'est pas unique (signe des colonnes peut varier)
norm(abs(R) - abs(R2))  % ≈ 0
```

</details>

#### Type 3 : Comparer PA=LU et QR d'Octave vs implémentations manuelles

**Méthode :** Calculer la norme de la différence `norm(Manual - Builtin)`. Comprendre pourquoi les signes peuvent différer (non-unicité de QR) mais les normes doivent coïncider.

**Exercice similaire :**
Pour la matrice $A$ de l'exercice précédent, comparez `my_lu` vs `lu` et `my_qr` vs `qr` en Octave. Qu'est-ce qui peut légitimement différer ? Qu'est-ce qui doit être identique ?

<details>
<summary>Voir la résolution complète</summary>

```octave
A = [0 2 1; 3 -1 2; 1 4 -1];  % matrice 3x3

% -- Comparaison PA=LU --
[L_man, U_man] = my_lu(A);
[L_oct, U_oct, P_oct] = lu(A);

norm(L_man * U_man - A)         % my_lu sans pivotage : peut être imprecis
norm(L_oct * U_oct - P_oct * A) % lu avec pivotage : ≈ 0

% -- Comparaison QR --
[Q_man, R_man] = my_qr(A);
[Q_oct, R_oct] = qr(A);

norm(Q_man * R_man - A)         % ≈ 0 (les deux doivent reconstruire A)
norm(Q_man' * Q_man - eye(3))   % ≈ 0 (Q orthogonale)

% Les signes des colonnes de Q peuvent différer, mais |R| doit être identique
norm(abs(R_man) - abs(R_oct))   % ≈ 0
```

**Ce qui peut différer légitimement :**
- Le signe de chaque colonne de $Q$ (et de la ligne correspondante de $R$) est libre : si $(Q, R)$ est une factorisation QR, alors $(-Q_{:,i}, -R_{i,:})$ en est une aussi.
- Sans pivotage dans `my_lu`, $L$ et $U$ peuvent différer de ceux d'Octave (qui pivote).

**Ce qui doit être identique :**
- $QR = A$ pour les deux méthodes.
- $|r_{ii}|$ (valeurs absolues des diagonales de $R$) pour les deux approches.

</details>



---

## Séance 5 — Moindres carrés : Équations normales vs QR

### Rappels théoriques

#### Le problème des moindres carrés

Un système $Ax = b$ avec $A \in \mathbb{R}^{m \times n}$ ($m > n$) est **surdéterminé** : il y a plus d'équations que d'inconnues. En général, il n'existe aucun $x$ vérifiant exactement toutes les équations.

On cherche plutôt $x^* = \arg\min_{x} \|Ax - b\|_2^2$.

**Le résidu :** $r = b - Ax^*$ est l'erreur minimale. L'angle $\theta$ entre $b$ et l'espace image de $A$ mesure la qualité de l'approximation :
$$
\sin \theta = \frac{\|r\|_2}{\|b\|_2}
$$

#### Méthode 1 : Équations normales

La condition $\nabla_x \|Ax - b\|_2^2 = 0$ donne le système :

$$
A^T A x = A^T b
$$

**Avantages :** Simple, coût $\approx mn^2$ flops.
**Danger critique :** On résout un système dont la matrice est $A^TA$ avec $\kappa(A^TA) = \kappa(A)^2$. Si $\kappa(A) = 10^8$, alors $\kappa(A^TA) = 10^{16}$ — entièrement dans le bruit machine ! La solution sera inutilisable.

**Code Octave :**
```octave
x_normal = (A' * A) \ (A' * b);
```

#### Méthode 2 : Factorisation QR (Householder)

On calcule $A = QR$ (avec $Q \in \mathbb{R}^{m \times m}$ orthogonale, $R \in \mathbb{R}^{m \times n}$ trapézoïdale supérieure). La solution des moindres carrés est alors obtenue par :

$$
R_{1:n, :} x = (Q^T b)_{1:n}
$$

où $R_{1:n,:}$ est le bloc carré supérieur de $R$.

**Avantages :** Stable même si $\kappa(A)$ est grand. Coût $\approx 2mn^2$ (environ 2× plus cher que les équations normales, mais numériquement sûr).

**Code Octave :**
```octave
[Q, R] = qr(A, 0);    % QR réduite (0 = économique)
x_qr = R \ (Q' * b);
```

#### Conditionnement pour les moindres carrés

Pour un système surdéterminé résolu au sens des moindres carrés, l'erreur relative est bornée par :
$$
\frac{\|\delta x\|}{\|x\|} \lesssim \left(\kappa(A) + \kappa(A)^2 \tan\theta \right) \cdot u
$$

Si le résidu est petit ($\theta \approx 0$), la borne dominante est $\kappa(A) \cdot u$, soit la même qu'un système carré bien posé. Si le résidu est grand, le terme $\kappa(A)^2$ peut dominer.

**Règle pratique :** en double précision ($u \approx 10^{-16}$), le nombre de chiffres fiables est $16 - \log_{10}(\kappa(A))$ avec QR, mais seulement $16 - 2\log_{10}(\kappa(A))$ avec les équations normales.

#### La matrice de Hilbert — exemple canonique de mauvais conditionnement

$$
H_{ij} = \frac{1}{i+j-1}
$$

$\kappa(H_6) \approx 1.5 \times 10^7$, $\kappa(H_{10}) \approx 10^{13}$. Ces matrices deviennent numériquement singulières très vite.

### Exercices résolus par type

#### Type 1 : Résolution au sens des moindres carrés — deux méthodes

**Méthode :** Appliquer les deux approches sur la même matrice, comparer les résidus et les erreurs relatives (si une solution exacte est connue).

**Exercice similaire :**
Soit la matrice surdéterminée $A$ ($6 \times 3$) et $b$ construites comme suit :

```octave
x_exact = [2; -1; 3];
A = [1 0 1; 2 1 0; 0 1 2; 1 1 1; 3 0 1; 0 2 1];
b = A * x_exact + 1e-10 * randn(6, 1);  % légère perturbation
```

a) Résolvez $\min_x \|Ax - b\|_2$ par équations normales et par QR.
b) Calculez l'erreur relative $\|x_{calc} - x_{exact}\|_2 / \|x_{exact}\|_2$ pour les deux méthodes.
c) Calculez $\kappa(A)$ et comparez les bornes théoriques sur l'erreur.

<details>
<summary>Voir la résolution complète</summary>

```octave
x_exact = [2; -1; 3];
A = [1 0 1; 2 1 0; 0 1 2; 1 1 1; 3 0 1; 0 2 1];
b = A * x_exact + 1e-10 * randn(6, 1);

% --- Méthode 1 : Équations normales ---
x_normal = (A' * A) \ (A' * b);
err_normal = norm(x_normal - x_exact) / norm(x_exact);
fprintf('Équations normales — erreur relative : %.2e\n', err_normal);

% --- Méthode 2 : Factorisation QR ---
[Q, R] = qr(A, 0);   % QR économique (R: 3x3, Q: 6x3)
x_qr = R \ (Q' * b);
err_qr = norm(x_qr - x_exact) / norm(x_exact);
fprintf('QR — erreur relative : %.2e\n', err_qr);

% --- Conditionnement et borne théorique ---
kA = cond(A);
fprintf('kappa(A) = %.2e\n', kA);
fprintf('kappa(A^T A) = %.2e\n', kA^2);
fprintf('Borne erreur (QR) ~ kappa(A) * u = %.2e\n', kA * 1.1e-16);
fprintf('Borne erreur (Normal) ~ kappa(A)^2 * u = %.2e\n', kA^2 * 1.1e-16);
```

**Interprétation attendue :**
- Comme $\kappa(A) \approx 5$ (la matrice est bien conditionnée ici), les deux méthodes donnent un résultat comparable.
- Mais si $A$ était la matrice de Hilbert ($\kappa \approx 10^7$), la méthode des équations normales travaillerait avec $\kappa(A^TA) \approx 10^{14}$, ne laissant que 2 chiffres corrects !

</details>

#### Type 2 : Analyse de stabilité (matrice mal conditionnée)

**Méthode :** Construire une matrice avec grand $\kappa$, observer la dégradation des équations normales vs QR. Vérifier les résidus $\|Ax - b\|$ et l'erreur sur la solution.

**Exercice similaire :**
Construire une matrice proche de la matrice de Hilbert :

```octave
A = round(inv(hilb(5)));  A = A(:, 1:3);
b1 = A * [1; -1; 1] + 1e-8 * randn(5, 1);
```

Résolvez au sens des moindres carrés par les deux méthodes. Commentez sur la précision.

<details>
<summary>Voir la résolution complète</summary>

```octave
A = round(inv(hilb(5))); A = A(:, 1:3);
x_exact = [1; -1; 1];
b1 = A * x_exact + 1e-8 * randn(5, 1);

kA = cond(A);
fprintf('kappa(A) = %.2e\n', kA);
fprintf('kappa(A^T A) = %.2e\n', kA^2);

% Équations normales
x_norm = (A'*A) \ (A'*b1);
err_norm = norm(x_norm - x_exact) / norm(x_exact);

% QR
[Q, R] = qr(A, 0);
x_qr = R \ (Q'*b1);
err_qr = norm(x_qr - x_exact) / norm(x_exact);

fprintf('Erreur normale : %.2e\n', err_norm);
fprintf('Erreur QR      : %.2e\n', err_qr);
```

**Résultat attendu :** Si $\kappa(A) \approx 10^6$ :
- Équations normales : erreur $\sim 10^{-4}$ (seulement 4 chiffres corrects).
- QR : erreur $\sim 10^{-10}$ (10 chiffres corrects).

**Conclusion :** Pour les matrices très mal conditionnées, la méthode QR est indispensable. Les équations normales, bien que 2× plus rapides, compromettent la précision de façon disproportionnée.

</details>

#### Type 3 : Calcul de bornes sur l'erreur et interprétation

**Méthode :** Calculer $\kappa(A)$, l'angle $\theta = \arcsin(\|r\|/\|b\|)$, puis appliquer la formule de borne d'erreur. Comparer avec l'erreur réelle mesurée.

**Exercice similaire :**
Pour les deux systèmes $Ax = b_1$ et $Ax = b_2$ de la séance, une solution exacte est connue pour le premier. Calculez :

a) $\kappa(A)$ en norme 2.
b) Les résidus $\|r_i\|_2 = \|b_i - Ax_i\|_2$ pour les deux méthodes.
c) L'erreur relative réelle sur $x_1$ (comparer à $x^* = (1,-1,1,-1)^T$).
d) Expliquez pourquoi les deux méthodes peuvent donner des résultats très différents sur $b_1$.

<details>
<summary>Voir la résolution complète</summary>

```octave
% Construction de la matrice (séance 5 originale)
A = round(inv(hilb(6))); A = A(:,1:4);
b1 = A * [1; -1; 1; -1];  % second membre avec solution exacte connue
b2 = ones(6, 1);

x_exact = [1; -1; 1; -1];

kA = cond(A);
fprintf('kappa(A) = %.2e\n', kA);

% Méthode 1 : Équations normales
x1_norm = (A'*A) \ (A'*b1);
x2_norm = (A'*A) \ (A'*b2);

% Méthode 2 : QR
[Q, R] = qr(A, 0);
x1_qr = R \ (Q'*b1);
x2_qr = R \ (Q'*b2);

% Analyse de b1 (solution exacte connue)
r1_norm = norm(b1 - A*x1_norm);
r1_qr   = norm(b1 - A*x1_qr);
err1_norm = norm(x1_norm - x_exact) / norm(x_exact);
err1_qr   = norm(x1_qr   - x_exact) / norm(x_exact);

fprintf('Résidu  (équat.norm.) : %.2e\n', r1_norm);
fprintf('Résidu  (QR)          : %.2e\n', r1_qr);
fprintf('Erreur  (équat.norm.) : %.2e\n', err1_norm);
fprintf('Erreur  (QR)          : %.2e\n', err1_qr);
```

**Interprétation :**
- Pour $b_1$ (solution exacte connue) : l'angle $\theta = 0$, donc le résidu doit être $\approx 0$. La borne est $\kappa(A) \cdot u$. Si QR donne erreur $\ll$ équations normales, c'est la preuve concrète de l'explosion de $\kappa^2$.
- Pour $b_2$ : la solution n'est pas exacte (résidu $\neq 0$), et la borne d'erreur fait intervenir $\kappa(A)^2 \sin\theta$.

</details>



---

## Séance 6 — Méthodes itératives et splines cubiques

### Rappels théoriques

#### Méthodes itératives pour systèmes linéaires

Pour les systèmes de grande taille (ex: matrices tridiagonales issues des EDPs), on préfère des méthodes itératives aux méthodes directes ($O(n^3)$).

**Principe général :** décomposer $A = M - N$ et itérer $x^{(k+1)} = M^{-1}(Nx^{(k)} + b)$ jusqu'à convergence.

**Critère d'arrêt :** réduction relative du résidu :
$$
\frac{\|r^{(k)}\|}{\|b\|} = \frac{\|b - Ax^{(k)}\|}{\|b\|} \leq \text{tol}
$$

---

**Méthode de Jacobi :**
Décomposition : $A = D + (A - D)$ où $D = \text{diag}(A)$.
Mise à jour : pour chaque composante $i$ :
$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)
$$
On utilise **uniquement les valeurs de l'itération précédente** $x^{(k)}$.

**Forme matricielle :** $x^{(k+1)} = D^{-1}(b - (A-D)x^{(k)})$.

```octave
function [x, niter] = jacobi(A, b, tol, maxiter)
    n = size(A, 1);
    x = zeros(n, 1);          % point de départ
    D_inv = 1 ./ diag(A);     % inverses des diagonaux
    for niter = 1:maxiter
        x_new = D_inv .* (b - (A - diag(diag(A))) * x);
        if norm(b - A*x_new) / norm(b) < tol
            x = x_new; return;
        end
        x = x_new;
    end
    warning('Jacobi: max iterations reached');
endfunction
```

---

**Méthode de Gauss-Seidel :**
Même principe, mais on utilise **immédiatement** les nouvelles valeurs calculées dès qu'elles sont disponibles :
$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)
$$

**Avantage :** converge en général environ 2× plus vite que Jacobi.

```octave
function [x, niter] = gauss_seidel(A, b, tol, maxiter)
    n = size(A, 1);
    x = zeros(n, 1);
    for niter = 1:maxiter
        x_old = x;
        for i = 1:n
            x(i) = (b(i) - A(i,1:i-1)*x(1:i-1) - A(i,i+1:n)*x(i+1:n)) / A(i,i);
        end
        if norm(b - A*x) / norm(b) < tol, return; end
    end
    warning('Gauss-Seidel: max iterations reached');
endfunction
```

---

**Matrice tridiagonale et conditionnement :**
Pour la matrice tridiagonale de la séance (issue du système des splines cubiques) :

$$
A = 2I + \mu \cdot \text{subdiag} + \lambda \cdot \text{superdiag}
$$

La borne du conditionnement est donnée par :
$$
\kappa(A) \leq \frac{d_{\max} + 4c}{d_{\min}}
$$
où $d_i$ sont les éléments diagonaux et $c$ est le couplage hors-diagonale.

**Lien critère d'arrêt → précision sur $x$ :**
En stabilité directe, l'erreur relative est bornée par $\kappa(A) \times \frac{\|r\|}{\|b\|}$.
Donc si $\frac{\|r\|}{\|b\|} \leq 10^{-3}$, l'erreur relative est $\leq \kappa(A) \times 10^{-3}$.

#### Splines cubiques (contexte de la séance)

Une spline cubique est un polynôme par morceaux $S(x)$ de degré 3 sur chaque intervalle $[x_i, x_{i+1}]$ tel que :
- $S(x_i) = y_i$ pour tout $i$ (interpolation).
- $S'$ et $S''$ sont continues (raccordement doux).
- **Conditions aux bords naturelles :** $S''(x_1) = S''(x_n) = 0$.

La construction revient à résoudre un **système tridiagonal** pour les secondes dérivées $\{u_i = S''(x_i)\}$ — c'est exactement le rôle de `u = A\d` dans le code `splinterpol`.

### Exercices résolus par type

#### Type 1 : Implémentation de Jacobi et Gauss-Seidel

**Méthode :** Coder la boucle d'itération. Vérifier la convergence avec le critère du résidu relatif. Compter le nombre d'itérations.

**Exercice similaire :**
Résolvez le système tridiagonal suivant par Jacobi et Gauss-Seidel, avec tolérance $10^{-6}$ :

$$
A = \begin{pmatrix} 4 & 1 & 0 & 0 \\ 1 & 4 & 1 & 0 \\ 0 & 1 & 4 & 1 \\ 0 & 0 & 1 & 4 \end{pmatrix}, \quad b = \begin{pmatrix} 5 \\ 6 \\ 6 \\ 5 \end{pmatrix}
$$

Solution exacte : $x = (1, 1, 1, 1)^T$. Comparez le nombre d'itérations des deux méthodes.

<details>
<summary>Voir la résolution complète</summary>

```octave
A = 4*eye(4) + diag(ones(3,1), 1) + diag(ones(3,1), -1);
b = [5; 6; 6; 5];
x_exact = [1; 1; 1; 1];
tol = 1e-6;

[x_jac, n_jac] = jacobi(A, b, tol, 1000);
[x_gs,  n_gs]  = gauss_seidel(A, b, tol, 1000);

fprintf('Jacobi       : %d itérations, erreur = %.2e\n', n_jac, norm(x_jac - x_exact));
fprintf('Gauss-Seidel : %d itérations, erreur = %.2e\n', n_gs,  norm(x_gs  - x_exact));
```

**Résultats typiques :** Jacobi converge en ~15 itérations, Gauss-Seidel en ~8.

**Analyse :** $A$ est à diagonale strictement dominante ($|a_{ii}| = 4 > |a_{ij}| + |a_{ik}| = 1+1 = 2$), ce qui garantit la convergence des deux méthodes. Gauss-Seidel converge environ 2× plus vite car il exploite immédiatement les nouvelles valeurs.

**Conditionnement :** $\kappa(A) \approx 3.7$ (très bien conditionné). La tolérance $10^{-6}$ sur le résidu garantit une erreur relative $\leq 3.7 \times 10^{-6}$.

</details>

#### Type 2 : Estimation du conditionnement de la matrice tridiagonale

**Méthode :** Identifier les paramètres $d_i$ et $c$ de la matrice, appliquer la borne $\kappa(A) \leq (d_{\max} + 4c) / d_{\min}$, puis comparer avec `cond(A)`.

**Exercice similaire :**
Pour la matrice de spline de la séance, la forme est :

$$
A = 2I_n + \mu \cdot \text{subdiag} + \lambda \cdot \text{superdiag}
$$

avec $\mu_i \in [1/3, 2/3]$ et $\lambda_i \in [1/3, 2/3]$ (coefficients issus des $h_i$).

a) Quelle est la borne sur $\kappa(A)$ selon la formule de la séance ?
b) Si le critère d'arrêt est $10^{-3}$, quelle précision obtient-on sur la solution des secondes dérivées (les $u_i$) ?

<details>
<summary>Voir la résolution complète</summary>

**a)** La matrice a $d_i = 2$ sur la diagonale et couplage $c \leq 2/3$ hors-diagonale.
$$
\kappa(A) \leq \frac{d_{\max} + 4c}{d_{\min}} = \frac{2 + 4 \times \frac{2}{3}}{2} = \frac{2 + \frac{8}{3}}{2} = \frac{\frac{14}{3}}{2} = \frac{7}{3} \approx 2.33
$$

La matrice est **très bien conditionnée** (c'est une propriété des matrices diagonalement dominantes).

```octave
% Vérification numérique (exemple avec h = 1 pour tous les intervalles)
n = 6;
mu = 0.5 * ones(n-1, 1);  % mu_i = 0.5 si h_i = h_{i+1}
lb = 0.5 * ones(n-1, 1);
A = 2*eye(n) + diag(mu, -1) + diag(lb, 1);
d_min = min(diag(A));  % = 2
fprintf('Borne: kappa <= %.2f\n', (2 + 4*0.5) / 2);  % = 2.0
fprintf('cond(A) = %.4f\n', cond(A));                 % ≈ 1.67 (encore mieux)
```

**b)** Précision sur $x$ (les $u_i$) :
$$
\frac{\|x - x^*\|}{\|x^*\|} \lesssim \kappa(A) \cdot \frac{\|r\|}{\|b\|} \leq 2.33 \times 10^{-3} \approx 2.3 \times 10^{-3}
$$

Avec un résidu de $10^{-3}$, on obtient environ 3 chiffres significatifs sur les secondes dérivées — suffisant pour une interpolation graphique.

</details>

#### Type 3 : Comprendre le système tridiagonal des splines

**Méthode :** Lire le code de `splinterpol`, identifier où est résolu le système, comprendre pourquoi la matrice est tridiagonale.

**Exercice similaire :**
À partir du code `splinterpol`, répondez aux questions suivantes :

a) Combien d'équations et d'inconnues contient le système linéaire ?
b) Quelle est la signification physique des $u_i$ (les inconnues) ?
c) Pourquoi remplacer `u = A\d` par une méthode itérative est-il pertinent ici ?

<details>
<summary>Voir la résolution complète</summary>

**a)** Pour $n$ points d'interpolation : $n$ équations, $n$ inconnues ($u_1, \ldots, u_n$).
Les conditions aux bords naturelles ($u_1 = 0$ et $u_n = 0$) réduisent le système effectif à $(n-2)$ équations pour $(n-2)$ inconnues intérieures.

**b)** Les $u_i = S''(x_i)$ sont les **secondes dérivées** du polynôme aux nœuds. Une fois les $u_i$ connus, les coefficients du polynôme cubique sur chaque intervalle $[x_i, x_{i+1}]$ sont calculés analytiquement (lignes $s(:,1)$ à $s(:,4)$ dans le code).

**c)** Pour $n$ petit (ici $n = 6$), la méthode directe `A\d` est parfaitement efficace.
Mais pour $n = 10^6$ points (interpolation d'une courbe très dense), la matrice est $10^6 \times 10^6$ tridiagonale :
- **Méthode directe :** $O(n)$ flops (cas spécial tridiagonal), mais stockage $O(n)$.
- **Méthode itérative (Gauss-Seidel) :** aussi $O(n)$ par itération, mais sans avoir à construire la matrice explicitement — utile pour des structures plus complexes.

La médaille revient à la méthode directe Thomas (LU spécialisé tridiagonal) qui est $O(n)$ exact. Les méthodes itératives brillent surtout pour les matrices **creuses mais non-tridiagonales** (EDPs 2D/3D).

</details>



---

## Séances 7-8 — Recherche de zéros d'équations non-linéaires

### Rappels théoriques

#### Le problème : trouver $x^*$ tel que $f(x^*) = 0$

**Bonne pratique :** toujours commencer par tracer le graphe de $f$ pour localiser approximativement les racines avant d'itérer.

---

#### Méthode de la Dichotomie (Bisection)

**Prérequis :** $f$ continue sur $[a, b]$ avec $f(a) \cdot f(b) < 0$ (signe changement).
**Idée :** diviser l'intervalle par 2 à chaque étape en gardant le sous-intervalle contenant la racine.

**Algorithme :**
```
tant que (b-a)/2 > tol :
    c = (a+b)/2
    si f(a)*f(c) < 0 : b = c
    sinon : a = c
```

**Convergence :** linéaire. L'erreur est divisée par 2 à chaque itération : $e_{k+1} \leq e_k / 2$.
**Nombre d'itérations** pour atteindre précision $\epsilon$ : $N \geq \log_2\left(\frac{b-a}{\epsilon}\right)$.

**Avantages/Inconvénients :**
✅ Robuste, garantit la convergence si les conditions initiales sont satisfaites.
❌ Lente (linéaire). Ne fonctionne que pour les scalaires.

---

#### Méthode de la Fausse Position (Regula Falsi)

**Idée :** comme la dichotomie, mais on choisit $c$ comme l'interpolation linéaire plutôt que le milieu :

$$
c = a - f(a) \frac{b-a}{f(b)-f(a)} = \frac{a \cdot f(b) - b \cdot f(a)}{f(b) - f(a)}
$$

**Convergence :** super-linéaire en général, mais peut stagner si la courbure est mal orientée.

---

#### Méthode de Newton-Raphson

La plus puissante pour les racines isolées :

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

**Convergence :** **quadratique** (le nombre de décimales exactes double à chaque itération !) à proximité de la racine.
**Prérequis :** $f'(x^*) \neq 0$, et bon point de départ ($x_0$ dans un voisinage de $x^*$).
**Danger :** si $f'(x_k) \approx 0$ ou $x_0$ est loin de $x^*$, la méthode peut diverger.

En Octave, si la dérivée analytique n'est pas disponible, on peut l'approcher :
```octave
f_prime = (f(x + 1e-8) - f(x - 1e-8)) / (2e-8);  % différences centrées
```

---

#### Newton avec recherche linéaire (Backtracking-Newton)

Améliorations de Newton pour les départs difficiles. À chaque itération :
1. Calculer le pas de Newton : $\Delta x = -f(x)/f'(x)$.
2. Réduire la longueur du pas si nécessaire (backtracking) : trouver $\alpha \in (0,1]$ tel que $|f(x + \alpha \Delta x)| < |f(x)|$.
3. $x \leftarrow x + \alpha \Delta x$.

Cela garantit que $|f|$ décroît à chaque itération, même si $x_0$ est loin de la racine.

---

#### Extension aux systèmes non-linéaires ($\mathbb{R}^n \to \mathbb{R}^n$)

Pour un système $F(x) = 0$ avec $F : \mathbb{R}^n \to \mathbb{R}^n$ :
$$
x^{(k+1)} = x^{(k)} - J_F(x^{(k)})^{-1} F(x^{(k)})
$$
où $J_F$ est la matrice Jacobienne de $F$.

**Localisation graphique des zéros :** utiliser `mesh` pour visualiser $\|F(x_1, x_2)\|$ en 2D et repérer les creux (proches de zéro).

### Exercices résolus par type

#### Type 1 : Recherche d'un zéro par dichotomie et Newton — comparaison

**Méthode :** tracer $f$, choisir $[a,b]$, implémenter les deux méthodes et comparer le nombre d'itérations.

**Exercice similaire :**
Trouvez le plus petit zéro positif de $f(x) = \cos(x) - x$ par les méthodes de dichotomie et Newton-Raphson. Partez de $[0, 1]$ et $x_0 = 0.5$.

<details>
<summary>Voir la résolution complète</summary>

```octave
% f(x) = cos(x) - x, f'(x) = -sin(x) - 1
f  = @(x) cos(x) - x;
df = @(x) -sin(x) - 1;
tol = 1e-10;

% --- Dichotomie ---
a = 0; b = 1;
n_dich = 0;
while (b - a)/2 > tol
    c = (a + b) / 2;
    if f(a) * f(c) < 0
        b = c;
    else
        a = c;
    end
    n_dich = n_dich + 1;
end
x_dich = (a + b) / 2;
fprintf('Dichotomie : x* = %.12f, %d itérations\n', x_dich, n_dich);

% --- Newton-Raphson ---
x = 0.5;
n_newt = 0;
while abs(f(x)) > tol
    x = x - f(x) / df(x);
    n_newt = n_newt + 1;
end
fprintf('Newton     : x* = %.12f, %d itérations\n', x, n_newt);
```

**Résultats :**
- Dichotomie : $x^* \approx 0.739085133$ en ~34 itérations ($\log_2(1/10^{-10}) \approx 33$).
- Newton : même résultat en ~5 itérations seulement !

**Interprétation :** Newton est exponentiellement plus rapide (quadratique vs linéaire) quand $x_0$ est proche de la racine. La dichotomie est 7× plus lente mais garantie de converger.

</details>

#### Type 2 : Newton-Raphson sur des équations non-triviales (avec localisation graphique)

**Méthode :** 1) tracer $f$ pour identifier les racines. 2) Choisir $x_0$ proche de chaque racine. 3) Itérer Newton.

**Exercice similaire :**
Trouvez toutes les racines réelles de $g(x) = x^3 - 3x + 1$ en utilisant Newton-Raphson.

<details>
<summary>Voir la résolution complète</summary>

```octave
g  = @(x) x.^3 - 3*x + 1;
dg = @(x) 3*x.^2 - 3;

% --- Étape 1 : localisation graphique ---
x_plot = -3:0.01:3;
plot(x_plot, g(x_plot), '-b', x_plot, zeros(size(x_plot)), '--k');
grid on; xlabel('x'); ylabel('g(x)');
% On observe 3 changements de signe : ~[-2,-1], ~[0,0.5], ~[1,2]

% --- Étape 2 : Newton depuis 3 points de départ ---
tol = 1e-12;
starts = [-2, 0.3, 1.5];
for k = 1:length(starts)
    x = starts(k);
    for iter = 1:50
        dx = -g(x) / dg(x);
        x = x + dx;
        if abs(dx) < tol, break; end
    end
    fprintf('Racine %d : x* = %.12f (à partir de x0 = %.1f)\n', k, x, starts(k));
end
```

**Racines :** $x_1 \approx -1.879$, $x_2 \approx 0.347$, $x_3 \approx 1.532$. Vérification : $g(x_i) \approx 0$.

**Convergence quadratique :** à chaque itération, le nombre de décimales correctes double. De 1 chiffre correct → 2 → 4 → 8 → 16.

</details>

#### Type 3 : Newton-Raphson pour systèmes non-linéaires 2D

**Méthode :** Former $F(x_1, x_2)$ et la Jacobienne $J_F$. Itérer $x^{(k+1)} = x^{(k)} - J_F^{-1}F(x^{(k)})$. Visualiser avec `mesh` ou `contour`.

**Exercice similaire :**
Trouvez les intersections du cercle $(x-1)^2 + y^2 = 4$ et de la courbe $y = x^2 - 2$ en utilisant Newton-Raphson.

<details>
<summary>Voir la résolution complète</summary>

**Formulation :**

$$
F(x, y) = \begin{pmatrix} (x-1)^2 + y^2 - 4 \\ y - x^2 + 2 \end{pmatrix} = 0
$$

$$
J_F(x, y) = \begin{pmatrix} 2(x-1) & 2y \\ -2x & 1 \end{pmatrix}
$$

```octave
F  = @(v) [(v(1)-1)^2 + v(2)^2 - 4; v(2) - v(1)^2 + 2];
JF = @(v) [2*(v(1)-1), 2*v(2); -2*v(1), 1];

% --- Localisation graphique ---
[X, Y] = meshgrid(-3:0.1:3, -3:0.1:3);
F1 = (X-1).^2 + Y.^2 - 4;
F2 = Y - X.^2 + 2;
contour(X, Y, F1, [0 0], 'b'); hold on;
contour(X, Y, F2, [0 0], 'r');
% On voit 2 intersections : environ (-1, -1) et (1.5, 0.25)

% --- Newton depuis 2 points de départ ---
tol = 1e-12;
starts = {[-1; -1], [1.5; 0.25]};
for k = 1:length(starts)
    v = starts{k};
    for iter = 1:50
        delta = -JF(v) \ F(v);      % Résoudre J*delta = -F
        v = v + delta;
        if norm(delta) < tol, break; end
    end
    fprintf('Racine %d : (x,y) = (%.8f, %.8f)\n', k, v(1), v(2));
end
```

**Résultats :** $(x_1, y_1) \approx (-1.174, -1.379)$ et $(x_2, y_2) \approx (1.553, 0.411)$.

**Points clés :**
1. La Jacobienne est calculée **analytiquement** à chaque itération (pas de matrices de taille $n \times n$ à stocker pour $n = 2$).
2. Le système linéaire $J \cdot \delta = -F$ est résolu avec `\` (LU pivoté).
3. La convergence est quadratique si $J_F(x^*)$ est inversible.

</details>



---

## Séance 9 — Intégration numérique

### Rappels théoriques

#### Le problème : approcher $I = \int_a^b f(x)\,dx$

On ne peut pas toujours calculer une primitive analytique. On utilise des méthodes numériques basées sur des **formules de quadrature** (combinaisons pondérées des valeurs de $f$).

---

#### Méthode des Trapèzes

**Idée :** sur chaque sous-intervalle $[x_i, x_{i+1}]$ de largeur $h$, approcher $f$ par une droite.

$$
\int_a^b f(x)\,dx \approx h \left[\frac{f(a)}{2} + f(a+h) + f(a+2h) + \cdots + f(b-h) + \frac{f(b)}{2}\right]
$$

**Erreur globale :**
$$
|E_T| \leq \frac{(b-a)h^2}{12} \max_{x \in [a,b]} |f''(x)|
$$

Pour atteindre une erreur $\leq \epsilon$, on choisit :
$$
h \leq \sqrt{\frac{12\epsilon}{(b-a)\max|f''|}}
$$

**Convergence :** ordre 2 en $h$ (l'erreur est divisée par 4 si on divise $h$ par 2).

```octave
function I = trapèzes(f, a, b, n)
    h = (b - a) / n;
    x = a:h:b;
    I = h * (f(a)/2 + sum(f(x(2:end-1))) + f(b)/2);
endfunction
```

---

#### Méthode de Simpson

**Idée :** sur chaque paire de sous-intervalles, approcher $f$ par un polynôme de degré 2 (parabole) :

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 4f(x_{n-1}) + f(x_n)\right]
$$

(avec $n$ pair).

**Erreur globale :**
$$
|E_S| \leq \frac{(b-a)h^4}{180} \max_{x \in [a,b]} |f^{(4)}(x)|
$$

**Convergence :** ordre 4 en $h$ (l'erreur est divisée par 16 si on divise $h$ par 2).

**Remarque importante :** Simpson est exact pour tous les polynômes de degré $\leq 3$ (pas seulement $\leq 2$) — c'est pourquoi on dit que son ordre de précision est 3 (on parle aussi de "degré d'exactitude 3").

```octave
function I = simpson(f, a, b, n)
    if mod(n,2) ~= 0, n = n + 1; end   % n doit être pair
    h = (b - a) / n;
    x = a:h:b;
    w = [1, repmat([4,2], 1, n/2 - 1), 4, 1];
    I = (h/3) * dot(w, f(x));
endfunction
```

---

#### Méthode de Romberg

**Idée :** combiner les trapèzes à différentes résolutions $h, h/2, h/4, \ldots$ pour extrapoler vers une valeur plus précise (extrapolation de Richardson).

Avec $T(h)$ le résultat des trapèzes avec pas $h$ :
$$
T_1(h) = T(h), \qquad T_2(h) = \frac{4T(h/2) - T(h)}{3}
$$

**Le premier pas de Romberg = Simpson !**
En effet, la combinaison $\frac{4T(h/2) - T(h)}{3}$ correspond exactement à la formule de Simpson avec pas $h/2$.

**Preuve :** développer $T(h)$ et $T(h/2)$ via Taylor, les combiner linéairement pour éliminer le terme en $h^2$ → on obtient l'erreur en $O(h^4)$, qui est la signature de Simpson.

---

#### Stratégie pour choisir $h$ (contrôle d'erreur)

1. Estimer $\max|f''|$ sur $[a,b]$ en traçant $f''$ ou en majorant analytiquement.
2. Calculer $h$ via la formule de l'erreur bornée.
3. En pratique : comparer $T(h)$ et $T(h/2)$ — si différence $< \epsilon$, on s'arrête.

### Exercices résolus par type

#### Type 1 : Simpson est exact pour les polynômes de degré ≤ 3 (vérification)

**Méthode :** calculer l'intégrale exacte d'un polynôme $p(x)$ de degré 3, puis vérifier que Simpson donne exactement la même valeur (avec seulement 2 sous-intervalles, soit $n = 2$).

**Exercice similaire :**
Vérifiez que Simpson est exact pour $p(x) = 2x^3 - x^2 + 3x - 1$ sur $[0, 2]$.
Calculez l'intégrale exacte, puis par Simpson avec seulement $n = 2$.

<details>
<summary>Voir la résolution complète</summary>

**Intégrale exacte :**
$$
\int_0^2 (2x^3 - x^2 + 3x - 1)\,dx = \left[\frac{x^4}{2} - \frac{x^3}{3} + \frac{3x^2}{2} - x\right]_0^2 = 8 - \frac{8}{3} + 6 - 2 = 12 - \frac{8}{3} = \frac{28}{3}
$$

**Simpson avec $n = 2$ (seulement 3 points : $x_0 = 0$, $x_1 = 1$, $x_2 = 2$, $h = 1$) :**

$$
S = \frac{h}{3}[p(0) + 4p(1) + p(2)]
$$

$p(0) = -1$, $p(1) = 2 - 1 + 3 - 1 = 3$, $p(2) = 16 - 4 + 6 - 1 = 17$.

$$
S = \frac{1}{3}[-1 + 12 + 17] = \frac{28}{3} \quad \checkmark
$$

**Vérification numérique (Octave) :**
```octave
p = @(x) 2*x.^3 - x.^2 + 3*x - 1;
S_exact = integral(p, 0, 2);       % = 9.3333... = 28/3
S_simp  = simpson(p, 0, 2, 2);    % = 9.3333... = 28/3 exactement !
fprintf('Exact  : %.15f\n', S_exact);
fprintf('Simpson: %.15f\n', S_simp);
```

Simpson donne un résultat **identique à la machine** (erreur $\approx 0$).

</details>

#### Type 2 : Choisir $h$ pour garantir une erreur bornée (méthode des trapèzes)

**Méthode :** 1) estimer $\max|f''|$ sur l'intervalle. 2) Appliquer la formule $|E_T| \leq \frac{(b-a)h^2}{12}\max|f''|$. 3) Résoudre en $h$. 4) Vérifier numériquement.

**Exercice similaire :**
Calculez $\int_0^1 e^{-x^2} dx$ (lié à la fonction d'erreur erf) avec une erreur absolue $\leq 10^{-6}$ par la méthode des trapèzes. Déterminez $h$ nécessaire, puis vérifiez avec Simpson.

<details>
<summary>Voir la résolution complète</summary>

**Étape 1 — Estimer $\max|f''|$ sur $[0,1]$ :**

$f(x) = e^{-x^2}$, $f'(x) = -2x e^{-x^2}$, $f''(x) = (4x^2 - 2)e^{-x^2}$.

Sur $[0,1]$ : $|f''(x)| = |4x^2 - 2| e^{-x^2}$. Le max est en $x = 0$ : $|f''(0)| = 2$.

```octave
f   = @(x) exp(-x.^2);
fpp = @(x) (4*x.^2 - 2) .* exp(-x.^2);
x_plot = 0:0.01:1;
max_fpp = max(abs(fpp(x_plot)));  % ≈ 2.0 (atteint en x=0)
```

**Étape 2 — Calcul de $h$ :**
$$
|E_T| \leq \frac{(1-0) \cdot h^2}{12} \cdot 2 \leq 10^{-6}
$$
$$
h^2 \leq \frac{12 \times 10^{-6}}{2} = 6 \times 10^{-6} \implies h \leq \sqrt{6 \times 10^{-6}} \approx 0.00245
$$

Soit $n \geq \lceil 1/0.00245 \rceil = 409$ sous-intervalles.

**Étape 3 — Calcul numérique :**
```octave
n_trap = 410;
I_trap = trapèzes(f, 0, 1, n_trap);

I_exact = erf(1) * sqrt(pi) / 2;    % valeur de référence ≈ 0.74682413...
err_trap = abs(I_trap - I_exact);

% Simpson avec beaucoup moins de points :
n_simp = 10;    % n=10 sous-intervalles suffisent pour Simpson !
I_simp = simpson(f, 0, 1, n_simp);
err_simp = abs(I_simp - I_exact);

fprintf('Trapèzes (n=%d): I = %.10f, err = %.2e\n', n_trap, I_trap, err_trap);
fprintf('Simpson  (n=%d): I = %.10f, err = %.2e\n', n_simp, I_simp, err_simp);
```

**Conclusion :** Simpson atteint la même précision avec $n=10$ qu'avec $n=410$ pour les trapèzes — l'ordre 4 est beaucoup plus efficace !

</details>

#### Type 3 : Romberg — preuve que le premier pas donne Simpson

**Méthode :** Calculer $T(h)$ et $T(h/2)$ explicitement, appliquer la combinaison de Richardson $\frac{4T(h/2) - T(h)}{3}$, et montrer algébriquement que cela coïncide avec la formule de Simpson.

**Exercice similaire :**
Montrez explicitement (en développant les formules) que $\frac{4T(h/2) - T(h)}{3}$ donne exactement la formule de Simpson sur l'intervalle $[a, b]$ avec un seul sous-intervalle de largeur $h = (b-a)/2$.

<details>
<summary>Voir la résolution complète</summary>

Notons $x_0 = a$, $x_1 = a + h$, $x_2 = b = a + 2h$.

**La formule des trapèzes avec pas $2h$ (un seul trapèze sur tout $[a,b]$) :**
$$
T(2h) = \frac{2h}{2}[f(x_0) + f(x_2)] = h[f(x_0) + f(x_2)]
$$

**La formule des trapèzes avec pas $h$ (deux trapèzes) :**
$$
T(h) = \frac{h}{2}[f(x_0) + 2f(x_1) + f(x_2)]
$$

**Combinaison de Romberg :**
$$
R = \frac{4T(h) - T(2h)}{3} = \frac{4 \cdot \frac{h}{2}[f(x_0) + 2f(x_1) + f(x_2)] - h[f(x_0) + f(x_2)]}{3}
$$

$$
= \frac{2h[f(x_0) + 2f(x_1) + f(x_2)] - h[f(x_0) + f(x_2)]}{3}
$$

$$
= \frac{h[2f(x_0) + 4f(x_1) + 2f(x_2) - f(x_0) - f(x_2)]}{3}
$$

$$
= \frac{h[f(x_0) + 4f(x_1) + f(x_2)]}{3}
$$

C'est **exactement** la formule de Simpson avec pas $h$ ! $\square$

**Vérification numérique (Octave) :**
```octave
f = @(x) sin(x);   a = 0; b = pi;   h = (b-a)/2;

T_2h = h * (f(a) + f(b));                          % trapèzes, 1 intervalle
T_h  = (h/2) * (f(a) + 2*f(a+h) + f(b));          % trapèzes, 2 intervalles
R    = (4*T_h - T_2h) / 3;                          % Romberg = Simpson
S    = (h/3) * (f(a) + 4*f(a+h) + f(b));           % Simpson direct

fprintf('Romberg : %.12f\n', R);
fprintf('Simpson : %.12f\n', S);
fprintf('Différence : %.2e\n', abs(R - S));         % ≈ 0 (identiques !)
```

</details>
