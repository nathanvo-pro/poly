# Exercices — Analyse Numérique

## Chapitre 1 : Représentation en virgule flottante, stabilité et conditionnement

> 📈 **Difficulté croissante :** Les exercices vont des définitions de base (⭐) aux problèmes de réflexion mathématique (⭐⭐⭐⭐⭐). Pensez à chercher sur papier avant d'ouvrir les solutions !

---

### ⭐ Niveau 1 — Fondamentaux de la virgule flottante

---

**Exercice 1 — Vocabulaire**

Dans l'expression standard $\pm 0.d_1 d_2 \cdots d_t \cdot \beta^e$, à quoi correspondent exactement les lettres $t$, $\beta$, $e$ et $d_i$ ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

- $\beta$ : La base du système (binaire $\beta=2$ ou décimale $\beta=10$)
- $t$ : Le nombre exact de chiffres significatifs (qui dicte la précision)
- $e$ : L'exposant (qui dicte l'ordre de grandeur, encadré par $e_{\min}$ et $e_{\max}$)
- $d_i$ : Le $i$-ème chiffre (encadré par $0 \le d_i \le \beta - 1$)

L'ensemble des chiffres forme ce qu'on appelle la **mantisse**.
</details>

---

**Exercice 2 — Représentation Normalisée**

Qu'est-ce qu'une mantisse normalisée ? Pourquoi est-ce un avantage massif pour les systèmes binaires ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Une représentation est **normalisée** si son tout premier chiffre significatif est non nul ($d_1 \neq 0$). 
Cela permet d'avoir une représentation unique pour chaque nombre (par exemple, on interdit l'ambiguïté entre $2 = 0.2 \cdot 10^1 = 0.02 \cdot 10^2$).

**L'avantage massif en binaire :** Si la base est $2$, les seuls chiffres possibles sont $0$ et $1$. Puisque $d_1$ ne peut pas être $0$, **il est obligatoirement égal à $1$**. Puisqu'on le sait toujours à l'avance, on n'a plus besoin de le stocker en mémoire ! Cela fait gagner $1$ bit de précision gratuitement (le bit implicite).
</details>

---

**Exercice 3 — Démonstration de l'Unité d'arrondi $u$**

Énoncez la formule de l'unité d'arrondi $u$ relative à la virgule flottante. Ensuite, **démontrez mathématiquement** cette borne supérieure à partir de la distance absolue maximale induite par l'arrondi du $(t+1)$-ème chiffre.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

L'unité d'arrondi répond à la formule :
$$
u = \frac{1}{2}\beta^{1-t}
$$

**Démonstration formelle :**
Soit un réel strict $x = \pm 0.d_1 d_2 \cdots d_t d_{t+1} \cdots \cdot \beta^e$.
Son équivalent machine $\text{fl}(x)$ ne garde que $t$ chiffres. L'arrondi ("au plus proche") dépend du chiffre $d_{t+1}$. L'écart absolu maximal entre la vraie valeur et le flottant machine ne dépassera jamais la moitié du poids du dernier chiffre (le $t$-ième chiffre) :
$$
|x - \text{fl}(x)| \leq \frac{1}{2} \beta^{-t} \cdot \beta^e
$$
Ensuite, on cherche l'erreur relative maximale, on divise donc tout par $|x|$.
La plus petite valeur que peut prendre la mantisse de $|x|$ (condition critique) est $1.00\dots \times \beta^{-1}$ (puisque $d_1 \geq 1$).
Donc $|x|_{\min} = \beta^{-1} \cdot \beta^e = \beta^{e-1}$.
Divisons :
$$
\text{Erreur relative max} = \frac{|x - \text{fl}(x)|}{|x|} \leq \frac{\frac{1}{2} \beta^{-t} \beta^e}{\beta^{e-1}} = \frac{1}{2}\beta^{1-t}
$$
Cette borne universelle d'erreur s'appelle $u$.
</details>

---

### ⭐⭐ Niveau 2 — Le Standard IEEE et l'Erreur Relative

---

**Exercice 4 — Erreur absolue vs Erreur relative**

Si je souhaite stocker la valeur absolue $A = 1000$ et qu'elle devient $\hat{A} = 1000.5$, calculez l'erreur absolue puis l'erreur relative.
Recommencez si je veux stocker la valeur $B = 0.001$ et qu'elle devient $\hat{B} = 0.0015$. Quelle conclusion en tirer ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Pour A ($1000 \to 1000.5$) :**
- Erreur absolue = $|1000.5 - 1000| = 0.5$
- Erreur relative = $0.5 / 1000 = 0.0005$ soit $\approx 0.05\%$

**Pour B ($0.001 \to 0.0015$) :**
- Erreur absolue = $|0.0015 - 0.001| = 0.0005$
- Erreur relative = $0.0005 / 0.001 = 0.5$ soit $\approx 50\%$

**Conclusion :** 
Ici l'erreur absolue sur $B$ est de seulement $0.0005$ (ce qui semble insignifiant), mais proportionnellement à sa petite grandeur, on se trompe de $50\%$ ! L'erreur relative est la seule métrique fiable en analyse numérique pour évaluer l'impact réel d'une imprécision.
</details>

---

**Exercice 5 — Les limites (Overflow, Underflow)**

Que devient l'état du processeur si l'on calcule :
1. $2 \cdot x_{\max}$
2. $x_{\min} / 2$
3. $0.0 / 0.0$

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

1. **Overflow (dépassement supérieur) :** La valeur dépasse le maximum stockable pour l'exposant. Le standard dicte de renvoyer la valeur spéciale `Inf` (Infini).
2. **Underflow (dépassement inférieur) :** La valeur devient plus petite que nos crans d'échelle. Cependant, plutôt que de crasher vers $0$, on passe à une représentation **dénormalisée**, mais en sacrifiant la précision (l'unité $u$ n'est plus garantie).
3. **NaN (Not a Number) :** Forme indéterminée qui ne donne aucun sens mathématique.
</details>

---

### ⭐⭐⭐ Niveau 3 — Propagation et Annulation

---

**Exercice 6 — Le Modèle d'Arithmétique Standard**

Dites comment la machine calcule mathématiquement l'opération abstraite "$\circledcirc$" (qui remplace l'opération mathématique exacte $\circ$) entre deux flottants $A$ et $B$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Selon la spécification IEEE, le processeur exécute l'opération exacte puis s'autorise une imprécision d'arrondi sur ce résultat :

$$
A \circledcirc B = (A \circ B)(1 + \varepsilon), \quad |\varepsilon| \leq u
$$

Cette formule universelle permet de prédire de combien s'amplifiera l'erreur relative après des centaines de multiplications/soustractions.
</details>

---

**Exercice 7 — Démonstration formelle de l'Annulation Catastrophique ($\kappa$)**

Montrez un exemple chiffré basique où la soustraction de nombres anéantit la précision $u$.
Ensuite, utilisez la formule du Conditionnement d'un sous-problème différentiable $\kappa(x)$ pour **prouver mathématiquement** que la soustraction de deux nombres extrêmement proches provoque une explosion exponentielle des erreurs initiales vers l'infini.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1. L'Exemple chiffré (Le massacre de la mantisse) :**
Imaginons un système qui ne garde que $6$ chiffres significatifs exacts (comme la simple précision $\approx$ 7 chiffres).
Soit $x = 1.000000$ et $y = 0.999999$. Les deux sont très précis.
Soustrayons :
$$
x - y = 0.000001
$$
Le résultat $\hat{y}$ est normalisé par la machine (puisqu'une mantisse ne peut pas commencer par des zéros). Elle le décale comme $1.00000 \cdot 10^{-6}$. Cependant, à cause de l'exposant négatif, la machine **comble le vide de derrière avec du bruit numérique aléatoire latent** (car la soustraction a détruit les seuls chiffres rigoureusement connus). 

**2. La Preuve mathématique par le conditionnement :**
Posons la fonction $f(x) = x_1 - x_2$.
Son vecteur de dérivées partielles est $f'(x) = [1, -1]$. On prend la norme euclidienne $\|f'(x)\|_2 = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.

Insérons dans la formule jacobienne de $\kappa$ locale :
$$
\kappa(\text{soustraction}) = \frac{\|f'(x)\| \cdot \|x\|}{|f(x)|} = \frac{\sqrt{2} \cdot \sqrt{x_1^2 + x_2^2}}{|x_1 - x_2|}
$$

**Conclusion finale :** Si nos valeurs sont proches ($x_1 \approx x_2$), le dénominateur de la fraction tend furieusement vers $0$, tandis que le numérateur reste hautement positif (les carrés).
Conséquence indiscutable de l'algèbre : $\kappa \to \infty$. 
Le conditionnement du problème devient dramatique, la moindre imprécision machine d'entrée explosera d'un facteur immense dans la sortie finale de la soustraction.
</details>

---

### ⭐⭐⭐⭐ Niveau 4 — Stabilité et Conditionnement

---

**Exercice 8 — Stabilité algorihtmique (Directe et Inverse)**

Décrivez avec des mots simples (et la formule de base avec $C$) la différence entre un algorithme qui bénéficie de la *stabilité directe* par rapport à la *stabilité inverse*. Lequel implique directement l'autre ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

- **Stabilité Directe :** Mon algorithme se trompe légèrement ($\hat{y} - y$ est petit). Mais rassurons-nous : sa marge d'erreur directe n'est *pas pire* que si j'avais donné des données minusculement perturbées à une fonction parfaite.
- **Stabilité Inverse :** C'est un concept encore plus solide. Il dit : Mon résultat inexact et imparfait ($\hat{y}$) N'EST PAS juste "proche", il **EST** LA réponse parfaite et mathématique à un problème ($\Delta x$) qui frôle le mien de très près ($\leq u$).

$$
\text{Stabilité Inverse} : \quad f(x + \Delta x) = \hat{y} \quad \text{avec } \frac{\|\Delta x\|}{\|x\|} \leq C \cdot u
$$

**Conclusion :** La stabilité inverse est beaucoup plus robuste. C'est elle qui **implique et entraîne automatiquement** la stabilité directe.
</details>

---

**Exercice 9 — Calcul du Conditionnement $\kappa(x)$**

Quelle est la formule officielle pour mesurer le conditionnement d'un problème avec une fonction différentiable ? Prouvez que le calcul de la racine carrée $f(x) = \sqrt{x}$ est extrêmement bien conditionné numériquement, sans lien avec l'algorithme choisi.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

La formule utilisant la Jacobienne / dérivée est :

$$
\kappa(x) = \frac{\|f'(x)\| \cdot \|x\|}{\|f(x)\|}
$$

Appliqué à notre racine carrée $f(x) = x^{1/2}$ et donc $f'(x) = \frac{1}{2\sqrt{x}}$ :

$$
\kappa(x) = \frac{\frac{1}{2\sqrt{x}} \cdot x}{\sqrt{x}} = \frac{\frac{x}{2\sqrt{x}}}{\sqrt{x}} = \frac{1}{2}
$$

Ici $\kappa(x) = 1/2$. Étant donné que le conditionnement est aux alentours de $1$ (et encore mieux : il pondère/réduit l'erreur), ce problème physique tolère excessivement bien l'imprécision et ne causera aucun comportement chaotique ! C'est remarquablement bien conditionné.
</details>

---

### ⭐⭐⭐⭐⭐ Niveau 5 — Problèmes Numériques Complexes

---

**Exercice 10 — Le Piège de la Soustraction Analysé via $\kappa(x)$**

En utilisant la formule du conditionnement $\kappa(x)$ ci-dessus, prouvez mathématiquement pourquoi la fonction de soustraction $f(x_1, x_2) = x_1 - x_2$ devient dramatiquement instable (Conditionnement vers l'infini) dès que $x_1$ et $x_2$ se rapprochent très fort. 

(Utilisez la norme vectorielle euclidienne $\|x\| = \sqrt{x_1^2 + x_2^2}$).

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Notre fonction à deux variables est $f(x_1, x_2) = x_1 - x_2$.
Le gradient (la dérivée) par rapport aux composantes donne le vecteur $f'(x) = (1, -1)$.
La norme de ce gradient est $\|(1, -1)\| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.

Appliquons la formule du conditionnement pour multivariables :

$$
\kappa(x_1, x_2) = \frac{\|f'(x)\| \cdot \|(x_1, x_2)\|}{\|f(x_1, x_2)\|}
$$

En insérant la norme du gradient ($\sqrt{2}$), la norme des entrées ($\sqrt{x_1^2 + x_2^2}$) et la valeur absolue formelle de la fonction au dénominateur :

$$
\kappa(x_1, x_2) = \frac{\sqrt{2} \cdot \sqrt{x_1^2 + x_2^2}}{|x_1 - x_2|}
$$

**Que se passe-t-il lorsque $x_1 \approx x_2$ ?**
Le numérateur reste strictement positif (car les carrés s'additionnent et valent en gros $2 \cdot x_1^2$).
Mais le dénominateur $|x_1 - x_2|$ **tend farouchement vers zéro** !
Un nombre positif divisé par presque-zéro explose vers l'infini. 
Donc : **$\kappa(x_1 \approx x_2) \to \infty$**. 

Le petit $\Delta x$ d'incertitude dans l'ordinateur se verra multiplié par un million ou un milliard en franchissant cette opération. Le problème est horriblement **mal conditionné** !
</details>

---

## Chapitre 2 : Systèmes d'équations linéaires : méthodes directes

> 📈 **Difficulté croissante :** De la compréhension des normes (⭐) à la manipulation matricielle experte sur la factorisation PA=LU (⭐⭐⭐⭐⭐). Pensez à l'algèbre linéaire !

---

### ⭐ Niveau 1 — Fondamentaux du Conditionnement $\kappa(A)$

---

**Exercice 11 — La formule de $\kappa(A)$**

Donnez la définition mathématique du conditionnement d'une matrice $A$ régulière, noté $\kappa(A)$. Que signifie physiquement un conditionnement de $1$ ? Et un conditionnement de $10^{15}$ ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

La définition officielle du conditionnement matriciel est :

$$
\kappa(A) = \|A^{-1}\| \cdot \|A\|
$$

- Si $\kappa(A) \approx 1$ : Le système est excellemment bien conditionné. Une petite erreur dans les données (le vecteur $b$) entraînera une erreur de la même taille dans le résultat (le vecteur $x$).
- Si $\kappa(A) \approx 10^{15}$ : Le système est catastrophiquement mal conditionné. La moindre décimale fausse dans l'équation de base sera amplifiée $10^{15}$ fois dans le résultat final ! C'est généralement le cas de matrices presque singulières.
</details>

---

**Exercice 12 — Preuve du théorème d'amplification d'erreur**

Supposons le système exact $Ax = b$. À cause de légères dérives matérielles, l'ordinateur résout en réalité le système perturbé $(A+\delta A)(x+\delta x) = (b + \delta b)$. Pour simplifier, assumons qu'il n'y a un bruit d'incertitude que sur le second membre analytique $b$ (donc $\delta A = 0$).

**Démontrez mathématiquement** (en utilisant les propriétés de l'inverse $A^{-1}$ et des normes $\leq$) le théorème d'amplification d'erreur qui prouve que l'erreur relative de la solution calculée dépend d'un multiplicateur purement matriciel. Identifier le nom de ce modificateur.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Preuve étape par étape :**
Soit l'équation du système perturbé uniquement en $b$ :
$$ A(x + \delta x) = b + \delta b $$
En distribuant, on a $Ax + A\delta x = b + \delta b$.
Or, on sait fondamentalement que la réponse idéale est $Ax = b$. Ces termes purs s'annulent de chaque côté :
$$ A \delta x = \delta b $$

L'ordinateur trouve son erreur réelle $\delta x$ (le parasite injecté) en inversant la dépendance :
$$ \delta x = A^{-1} \delta b $$

On applique ensuite les normes. La propriété des normes induites donne $\|M v\| \leq \|M\| \|v\|$ :
$$ \|\delta x\| \leq \|A^{-1}\| \|\delta b\| \quad \text{(Éq. 1)} $$

Pour exprimer l'amplification *relative*, on doit diviser par la norme pure de la vraie solution $x$.
On sait que $Ax = b \implies \|b\| \leq \|A\| \|x\|$.
Inversons magiquement de bord cette inéquation rigoureuse :
$$ \frac{1}{\|x\|} \leq \frac{\|A\|}{\|b\|} \quad \text{(Éq. 2)} $$

Multiplions intelligemment la partie gauche de l'Éq.1 par la partie gauche de l'Éq.2 :
$$
\frac{\|\delta x\|}{\|x\|} \leq \|A^{-1}\| \|\delta b\| \cdot \frac{\|A\|}{\|b\|}
$$

On réordonne l'inéquation en isolant le bloc pur des erreurs quantifiées :
$$
\frac{\|\delta x\|}{\|x\|} \le \bigl( \|A^{-1}\| \cdot \|A\| \bigr) \frac{\|\delta b\|}{\|b\|}
$$

**Conclusion :** 
L'amplification de l'erreur ne dépend **absolument que de la matrice de base**, peu importe l'algorithme informatique utilisé.
Ce rapport s'appelle le Conditionnement de la Matrice $\kappa(A) = \|A^{-1}\| \cdot \|A\|$.
</details>

---

### ⭐⭐ Niveau 2 — Algorithmique des Matrices

---

**Exercice 13 — Normes Vectorielles ($L_1, L_2, L_\infty$)**

Soit le vecteur $v = \begin{pmatrix} -3 \\ 1 \\ 4 \end{pmatrix}$. 
Calculez manuellement ses trois normes principales : $\|v\|_1$, $\|v\|_2$, et $\|v\|_\infty$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

- **Norme 1 (Somme des valeurs absolues) :** 
  $\|v\|_1 = |-3| + |1| + |4| = 3 + 1 + 4 = 8$
- **Norme 2 (Euclidienne, racine de la somme des carrés) :** 
  $\|v\|_2 = \sqrt{(-3)^2 + 1^2 + 4^2} = \sqrt{9 + 1 + 16} = \sqrt{26} \approx 5.1$
- **Norme infini (Le max absolu) :** 
  $\|v\|_\infty = \max(|-3|, |1|, |4|) = 4$
</details>

---

**Exercice 14 — Les mauvaises pratiques ($n!$ vs $O(n^3)$)**

Pourquoi, pour résoudre informatiquement $Ax = b$, est-il rigoureusement interdit d'utiliser la **méthode de Cramer** (calcul des déterminants successifs) ou de **calculer formellement l'inverse $A^{-1}$** ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

- La méthode de Cramer exige un grand nombre de déterminants lourds. Résoudre un système de taille $n$ prendrait $\approx n!$ opérations. (*Ex : Une matrice $100 \times 100$ prendrait des milliards d'années à l'ordinateur le plus puissant du monde !*).
- Calculer explicitement l'inverse $A^{-1}$ avant de multiplier par $b$ implique de faire $3$ fois trop de calculs inutiles pour rien. L'inversion matricielle prend au minimum $\approx \frac{8}{3}n^3$ flops, alors qu'une méthode directe et asymétrique asymétrique (comme LU) ne prend que $\approx \frac{2}{3}n^3$ flops. L'inverse prend **$2.3 \times$ plus de temps** à un processeur moderne sans aucun gain en précision.
</details>

---

### ⭐⭐⭐ Niveau 3 — Méthode de Gauss et Systèmes Triangulaires

---

**Exercice 15 — La bénédiction des Matrices Triangulaires**

Pourquoi l'analyse numérique réduit-elle systématiquement ses grilles à des **matrices triangulaires** (Inférieures $L$ ou Supérieures $U$) ? Quelle est la complexité algorithmique pour résoudre $Ux = y$ ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Un système triangulaire comme $Ux = y$ a la délicieuse propriété d'avoir déjà sa dernière ligne complètement résolue ! (ex: $a_{nn}x_n = y_n \implies x_n = y_n/a_{nn}$).
Il suffit d'isoler $x_n$ puis d'injecter la réponse dans la ligne au dessus, en remontant (C'est la méthode de *Substitution arrière* / *Backward substitution*).

Ce processus est :
1. Extrêmement rapide : Seulement $n^2$ flops (Opérations polynomiales de degré $2$, donc trivial pour un ordinateur).
2. Toujours mathématiquement rigoureux et stable, car aucune annulation catastrophique massive n'a lieu.
</details>

---

**Exercice 16 — Transformation de Gauss en Matrice**

L'élimination classique de Gauss consiste à soustraire multiple d'une ligne d'une autre (ex: $L_2 = L_2 - (\frac{a_{21}}{a_{11}})L_1$). 
En Analyse Numérique, comment modélise-t-on cela sous le spectre de l'Algèbre ? Que devient le système $A$ à la fin de la procédure ? 

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

On modélise chaque annulation de Gauss non pas comme une manipulation externe, mais intrinsèquement comme la multiplication de $A$ par une matrice élémentaire Inférieure $L_1, L_2, \dots$

Après avoir injecté plusieurs matrices $L_i$ (qui écrasent la moitié bas-gauche pour y mettre des $0$), la matrice complète d'origine **fusionne en un gigantesque triangle supérieur**. On l'appelle $U$.

$$
(L_{n-1} \dots L_2 \cdot L_1) \cdot A = U
$$
</details>

---

### ⭐⭐⭐⭐ Niveau 4 — La Factorisation LU

---

**Exercice 17 — Exécution algorithmique de la Factorisation $A = LU$**

Démontrez la puissance de Gauss algorithmique. Décomposez manuellement la matrice $A$ ci-dessous en ses facteurs $L$ et $U$ en détaillant impérativement les étapes intermédiaires (les duplicateurs $l_{ik}$).
$$
A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 1 & 0 \\ -2 & 2 & 1 \end{pmatrix}
$$

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Étape 1 : Zéros sous le premier pivot ($a_{11} = 2$)**
Multiplicateur ligne 2 : $l_{21} = \frac{4}{2} = 2$
Multiplicateur ligne 3 : $l_{31} = \frac{-2}{2} = -1$

On applique $L_2 = L_2 - 2 L_1$ et $L_3 = L_3 - (-1) L_1$ :
$$
A^{(2)} = \begin{pmatrix} 2 & 1 & 1 \\ 0 & -1 & -2 \\ 0 & 3 & 2 \end{pmatrix}
$$
*Note : On range déjà nos multiplicateurs ($2$ et $-1$) dans la 1ère colonne de notre future matrice $L$ !*

**Étape 2 : Zéro sous le deuxième pivot ($a^{(2)}_{22} = -1$)**
Multiplicateur ligne 3 : $l_{32} = \frac{3}{-1} = -3$

On applique $L_3 = L_3 - (-3) L_2$ :
$$
A^{(3)} = \begin{pmatrix} 2 & 1 & 1 \\ 0 & -1 & -2 \\ 0 & 0 & -4 \end{pmatrix}
$$

**Finalisation Théorique :**
La matrice résultante $A^{(3)}$ est désormais parfaitement triangulaire supérieure. C'est notre $U$.
$$
U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & -1 & -2 \\ 0 & 0 & -4 \end{pmatrix}
$$
La matrice $L$ est la matrice triangulaire inférieure formée d'une diagonale de $1$ et des trois multiplicateurs calculés aux étapes précédentes ($l_{21}=2$, $l_{31}=-1$, $l_{32}=-3$) posés exactement à leur position d'action :
$$
L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{pmatrix}
$$
Vous pouvez vérifier sur papier que $L \cdot U = A$ !
</details>

---

**Exercice 18 — Résolution en 2 Temps avec $LU$**

Maintenant que le dur travail est fait ($A$ a été factorisé en $L \cdot U$ en perdant $\frac{2}{3}n^3$ flops CPU), comment l'ordinateur résout l'équation complexe $Ax = b$ de manière éclair ? Rédigez le processus informatisé en 2 temps de $\sim O(n^2)$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

On substitue dans l'équation :
$$ L \cdot U \cdot x = b $$

L'ordinateur définit astucieusement un vecteur intermédiaire in-memory $y$ et procède en deus temps :
1. **Descente (Forward substitution) :** Il résout $L \cdot y = b$ (coût $n^2$).
2. **Remontée (Backward substitution) :** Il résout la partie de droite $U \cdot x = y$ pour trouver enfin $x$ brut (coût $n^2$).

C'est ça la gloire de LU ! Si l'utilisateur me donne un nouveau vecteur $b'$, je n'ai plus besoin de refaire l'énorme factorisation $A$, je n'exécute que mes 2 descentes ultra-rapides.
</details>

---

### ⭐⭐⭐⭐⭐ Niveau 5 — Le Pivotage et Cas Extrêmes

---

**Exercice 19 — La Ruine Totale de $LU$ et la Matrice de Permutation**

La factorisation $LU$ standard sans modification **tombe en ruine absolue** sur le système trivial suivant :
$$
\begin{pmatrix} 10^{-20} & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$
Expliquez pourquoi le calcul machine crashe, et présentez la méthode absolue requise (impliquant une Matrice $P$) : **Le Pivotage**.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Pourquoi ça crache en $LU$ pur :**
La matrice choisit impérativement la coordonnée $(1, 1)$ comme pivot pour écraser la ligne 2.
Le multiplicateur exigé sera donc $\frac{\text{Ligne 2}}{\text{Ligne 1}} = \frac{1}{10^{-20}} = 10^{20} !$. 
En opérant sur l'ordinateur la ligne $2$ :
$$ L_2 = L_2 - 10^{20} L_1 \implies (1) - 10^{20}(1) = \text{Catastrophe d'arrondi totale} $$
Le $1$ est détruit, l'erreur relative propulse et tout le logiciel explose.

**Le Sauveur (Pivotage Partiel $PA = LU$) :**
L'algorithme moderne ne fonce pas tête baissée. À chaque colonne de travail, il regarde vers le bas toutes les lignes, sélectionne **la plus grande valeur absolue**, et échange géométriquement l'ordre de TOUTE la ligne de la matrice. L'ordinateur mémorise cet échange dans une matrice de permutation unitaire modifiée $P$.

L'algorithme parfait et inconditionnellement stable de l'Analyse Numérique n'est donc pas $A=LU$, mais **$PA = LU$**.
</details>

---

**Exercice 20 — L'Astuce de $\det(A)$**

En vous appuyant du théorème des déterminants $\det(AB) = \det(A)\det(B)$, et de la spécificité de la diagonale de $L, U$ et $P$; démontrez pourquoi Octave/Matlab peut calculer le déterminant d'une matrice gigantesque instantanément dès que $PA = LU$ est terminé.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Prenons la base : $PA = LU$
$$
\det(PA) = \det(LU) \implies \det(P)\det(A) = \det(L)\det(U)
$$

Regardons les propriétés incroyables des actants :
- **$P$** : C'est une matrice d'Identité où les lignes ont été interchangées $p$ fois. Donc $\det(P) = (-1)^p$.
- **$L$** : Matrice triangulaire. Son déterminant est produit de sa diagonale. Son principe d'existence exige des $1$ absolus sur sa diagonale. Donc $\det(L) = 1$.
- **$U$** : Matrice triangulaire. Son déterminant est aussi le produit de sa diagonale (les pivots ultimes : $u_{11}, u_{22}, \dots, u_{nn}$).

Injectons tout ça dans l'équation :
$$
(-1)^p \cdot \det(A) = 1 \cdot \prod u_{ii} \implies \det(A) = (-1)^p \cdot (u_{11} \cdot u_{22} \cdots u_{nn})
$$

**Conclusion magique :** Dès que Gauss a exécuté son $PA = LU$ (qui de toutes façons est nécessaire pour plein d'autres choses), le déterminant complet du système originel se révèle par simple multiplication de l'ossature diagonale de $U$ !
</details>
