# Synthèse — Analyse Numérique

## Chapitre 1 : Représentation en virgule flottante, stabilité et conditionnement

> 📚 **Objectif du chapitre :** Comprendre comment les ordinateurs représentent les nombres réels de façon finie, quantifier les erreurs inévitables que cela engendre, et analyser la robustesse d'un algorithme (stabilité) vis-à-vis d'un problème donné (conditionnement).

### 1. Motivation : Pourquoi s'en soucier ?

> 💡 **Idée clé :** L'arithmétique des ordinateurs n'est pas l'arithmétique des réels $\mathbb{R}$. Les erreurs numériques s'accumulent et peuvent avoir des conséquences désastreuses.

**Exemples historiques frappants :**
- **Système Patriot (1991) :** Une erreur d'arrondi de 0.34 secondes sur le temps a dérivé en une erreur de position d'un demi-kilomètre pour l'interception, causant la mort de 28 soldats.
- **Fusée Ariane 5 (1996) :** Trente secondes après le décollage, un dépassement de capacité (overflow) sur la vitesse horizontale a poussé la fusée à l'autodestruction. Perte : ~500 millions de dollars.

### 2. Représentation en virgule flottante

L’ensemble $\mathbb{R}$ est infini et continu, or la mémoire de l'ordinateur est finie. On représente donc les réels de manière discrète en utilisant la **virgule flottante**.

#### Définition Mathématique
Un nombre s'écrit sous la forme (notation à gauche, valeur à droite) :

$$
\pm 0.d_1 d_2 \cdots d_t \cdot \beta^e = \pm \beta^e \sum_{i=1}^{t} \frac{d_i}{\beta^i}
$$

| Symbole | Nom | Signification |
| :---: | :--- | :--- |
| $\beta$ | Base | Base $2$ (binaire) ou base $10$ (décimale) |
| $t$ | Chiffres significatifs | Détermine la précision de la représentation |
| $d_i$ | $i$-ème chiffre | $0 \leq d_i \leq \beta - 1$ |
| $0.d_1 \dots d_t$ | Mantisse | L'ensemble des chiffres significatifs |
| $e$ | Exposant | Limité par des bornes $e_{\min} \leq e \leq e_{\max}$ |

#### Représentation normalisée
Certains réels peuvent s'écrire de plusieurs manières (ex: $0.2 \cdot 10^1 = 0.02 \cdot 10^2$).
Pour éviter cette ambiguïté, on ajoute une règle : **le premier chiffre de la mantisse doit être non nul**.

$$
d_1 \neq 0
$$

En base $2$, le seul chiffre non-nul est $1$. Le $1$ initial est donc toujours connu à l'avance et n'a pas besoin d'être stocké en mémoire !

On note $\mathbb{F}$ l'ensemble des réels normalisés :

$$
\mathbb{F} = \{ x \mid x = \pm 0.d_1 d_2 \cdots d_t \cdot \beta^e, \quad e_{\min} \leq e \leq e_{\max}, \quad d_1 \neq 0 \}
$$

> ⚠️ **Propriété essentielle :** Les nombres de $\mathbb{F}$ ne sont **pas uniformément espacés**. Plus on s'éloigne de zéro, plus la distance absolue entre deux nombres représentables est grande.

### 3. Erreurs d'arrondi et Standard IEEE 754

#### L'Unité d'Arrondi ($u$)
Puisque $\mathbb{R}$ n'est pas $\mathbb{F}$, on doit projeter chaque réel vers le plus proche représentant en machine. 
Soit $\text{fl}(x)$ ("float") le réel de $\mathbb{F}$ le plus proche de $x \in \mathbb{R}$.

**Démonstration formelle de la limite d'erreur :**
Soit $x = \pm 0.d_1 d_2 \cdots d_t d_{t+1} \cdots \cdot \beta^e$.
Le flottant le plus proche $\text{fl}(x)$ gardera les $t$ premiers chiffres, et dépendra de la valeur de $d_{t+1}$ pour arrondir au supérieur ou à l'inférieur.
La distance absolue maximale entre $x$ et $\text{fl}(x)$ est physiquement la moitié du poids du dernier chiffre significatif $t$ :
$$
|x - \text{fl}(x)| \leq \frac{1}{2} \beta^{-t} \cdot \beta^e
$$
Pour trouver l'erreur relative maximale, on divise par $|x|$. Or la valeur minimale absolue possible pour $|x|$ avec l'exposant $e$ (vu que $d_1 \geq 1$) est $0.100\dots_ \beta \cdot \beta^e = \beta^{-1} \cdot \beta^e$.
Ainsi, l'erreur relative maximale est bornée par :
$$
\frac{|x - \text{fl}(x)|}{|x|} \leq \frac{\frac{1}{2} \beta^{e-t}}{\beta^{e-1}} = \frac{1}{2}\beta^{1-t}
$$

On appelle cette quantité **l'unité d'arrondi $u$** :
$$
\boxed{u = \frac{1}{2}\beta^{1-t}}
$$

Ceci garantit la formule fondamentale :
$$
\text{fl}(x) = x(1 + \varepsilon), \quad \text{avec } |\varepsilon| \leq u
$$

#### Le Standard IEEE 754
Le format en virgule flottante universel a deux déclinaisons majeures en binaire ($\beta = 2$) :

| Format | Bits globaux | Bits mantisse | Bits exposant | Unité d'arrondi $u$ |
| :--- | :---: | :---: | :---: | :--- |
| **Simple (single)** | 32 bits | 23 bits | 8 bits | $\approx 6.0 \times 10^{-8}$ |
| **Double (double)** | 64 bits | 52 bits | 11 bits | $\approx 1.1 \times 10^{-16}$ |

*Note: En Octave/Matlab, la double précision est utilisée par défaut.*

#### Cas marginaux (Overflow, Underflow, NaN)
- **Underflow :** Lorsque $|x| < x_{\min}$, on passe en représentation "dénormalisée" pour tomber gracieusement vers 0. L'erreur relative explose.
- **Overflow :** Lorsque $|x| > x_{\max}$ (ou division par $0$), on obtient la valeur `±Inf` (Infini).
- **NaN (Not a Number) :** Représente une forme indéterminée comme $0/0$ ou $0 \cdot \infty$.

### 4. Modèle standard d'arithmétique

Soit $\circ$ l'opération mathématique exacte (addition, soustraction, multiplication, division) et $\circledcirc$ la même opération exécutée par le processeur. Le résultat d'une opération machine vérifie toujours le modèle suivant :

$$
x \circledcirc y = \text{fl}(x \circ y) = (x \circ y)(1 + \varepsilon), \quad |\varepsilon| \leq u
$$

**Démonstration de propagation (Exemple sur la multiplication) :**
Imaginons qu'on veuille multiplier $x$ et $y$, mais l'ordinateur stocke en réalité $\text{fl}(x)$ et $\text{fl}(y)$, qui possèdent déjà des erreurs inhérentes ($\varepsilon_1, \varepsilon_2$). La machine exécute ensuite sa multiplication $\otimes$, générant une 3ème erreur d'arrondi $\varepsilon_3$.
$$
\text{fl}(x) \otimes \text{fl}(y) = \bigl( x(1+\varepsilon_1) \cdot y(1+\varepsilon_2) \bigr) (1+\varepsilon_3)
$$
$$
= (x \cdot y) (1 + \varepsilon_1)(1 + \varepsilon_2)(1 + \varepsilon_3)
$$
En développant et en ignorant les termes d'ordre supérieur très minuscules $\mathcal{O}(u^2)$, on obtient :
$$
\approx (x \cdot y) (1 + \varepsilon_1 + \varepsilon_2 + \varepsilon_3)
$$
L'opération finale sur la machine produit le résultat mathématique exact, perturbé par l'addition de **trois fois l'unité d'arrondi** !

#### Le phénomène d'Annulation Catastrophique
Si $x$ et $y$ sont des réels très proches ($x \approx y$) mais déjà entachés d'une légère erreur d'arrondi relative due à des calculs précédents, **leur soustraction $x \ominus y$ va amplifier ces erreurs de façon dramatique**. C'est ce qu'on appelle "l'annulation catastrophique" (perte des chiffres significatifs majeurs). 

### 5. Algorithme vs Problème : Stabilité et Conditionnement

L'erreur entre la sortie d'un algorithme informatique ($\hat{y}$) et la fonction mathématique exacte qu'il doit évaluer ($y = f(x)$) s'appelle l'**erreur directe**.

$$
\text{Erreur directe} = \hat{y} - y
$$

L'erreur directe dépend de deux composants fondamentaux qui se multiplient entre eux :
1. **La Stabilité (due à l'Algorithme informatique)**
2. **Le Conditionnement (dû au Problème mathématique)**

#### 5.1. La Stabilité (Algorithme)
Un algorithme est "stable" si les erreurs commises à cause de l'arrondi en machine ne sont pas pires que l'effet provoqué s'il y avait eu une minuscule incertitude sur les variables d'entrée. 

Dans cette optique, on a la notion très forte d'**erreur inverse** :
L'erreur inverse consiste à postuler que le résultat numérique obtenu, $\hat{y}$, est mathématiquement la **solution exacte d'un problème aux données légèrement altérées** ($x + \Delta x$).

$$
f(x + \Delta x) = \hat{y}
$$
Un algorithme possède une **stabilité inverse** s'il existe toujours un petit $\Delta x$ tel que :
$$
\frac{\|\Delta x\|}{\|x\|} \leq C u
$$
*(Ce concept donne l'assurance que notre résultat inexact est au moins la réponse parfaite à une question presque identique).*

#### 5.2. Le Conditionnement (Problème Mathématique)
Le **conditionnement** est une valeur absolue propre au problème de base, insensible à l'algorithme choisi. Il mesure à quel point de minuscules erreurs sur les données d'entrée $x$ vont s'amplifier ou se réduire en traversant la fonction $f$.

**Démonstration formelle de la définition de $\kappa(x)$ :**
On cherche le rapport entre l'erreur relative de la sortie et l'erreur relative de l'entrée pour la pire des très petites perturbations $\delta x$.
$$
\kappa(x) = \lim_{\epsilon \to 0} \sup_{\|\delta x\| \leq \epsilon \|x\|} \frac{\frac{\|f(x + \delta x) - f(x)\|}{\|f(x)\|}}{\frac{\|\delta x\|}{\|x\|}}
$$
Si la fonction $f$ est différentiable, on utilise le développement de Taylor de premier ordre : $f(x + \delta x) \approx f(x) + f'(x)\delta x$.
La variation de la fonction $\|f(x + \delta x) - f(x)\|$ devient simplement $\|f'(x)\delta x\|$, ce qui donne $\leq \|f'(x)\| \|\delta x\|$.
En remplaçant cela dans la grande limite supérieure, l'amplificateur du bruit d'entrée $\|\delta x\|$ se simplifie et nous donne la formule explicite magique :
$$
\boxed{\kappa(x) = \frac{\|f'(x)\| \cdot \|x\|}{\|f(x)\|}}
$$

*Interprétation du conditionnement:*
- $\kappa(x) \approx 1$ : Le problème est **bien conditionné**. 
- $\kappa(x) \gg 1$ : Le problème est **mal conditionné** (toute petite variation initiale donnera un résultat chaotique). 

**Démonstration formelle de l'Annulation Catastrophique :**
Étudions le problème de la soustraction de deux nombres $f(x) = x_1 - x_2$.
Le vecteur d'entrée est $x = (x_1, x_2)^T$. La Jacobienne $f'(x) = [1, -1]$.
Sa norme (par exemple avec la norme matricielle 1) est $\|f'(x)\|_1 = 1 + |-1| = 2$.
En appliquant la formule prouvée juste au dessus :
$$
\kappa(\text{soustraction}) = \frac{\| [1, -1] \| \cdot \|x\|}{|x_1 - x_2|} = \frac{2 \cdot \|x\|}{|x_1 - x_2|}
$$
**Analyse mathématique :** Si $x_1$ et $x_2$ ont presque la même valeur ($x_1 \approx x_2$), le dénominateur $|x_1 - x_2|$ tend de force vers $0$. Un dénominateur qui tend vers zéro force la fraction $\kappa \to \infty$. 
Ceci prouve mathématiquement que la soustraction de nombres proches est le problème le plus fondamentalement mal conditionné de l'informatique.

---

## Chapitre 2 : Systèmes d'équations linéaires : méthodes directes

> 📚 **Objectif du chapitre :** Utiliser les ordinateurs pour résoudre efficacement et surtout *de manière stable* de larges systèmes d'équations linéaires sous forme matricielle $Ax = b$.

### 1. Généralités et le Conditionnement d'une Matrice

Un système linéaire peut s'écrire sous forme vectorielle/matricielle compacte :

$$
Ax = b
$$

Avec $A$ une matrice $m \times n$, $x$ le vecteur des inconnues et $b$ le vecteur solution. Les méthodes directes de base (ce chapitre) se focalisent sur les systèmes **carrés (m = n) réguliers, c'est-à-dire inversibles (déterminant non nul)**.

#### Le conditionnement du système linéaire $\kappa(A)$
De la même manière qu'une fonction au Chapitre 1 possède un conditionnement, une **matrice possède un conditionnement** face aux erreurs d'arrondis des données initiales.

**Démonstration de la borne du conditionnement matriciel :**
Si on a une erreur pure numérique $\delta b$ sur le vecteur solution, alors le système résolu par la machine trouve $\hat{x} = x + \delta x$.
$$ A(x + \delta x) = b + \delta b \implies A \delta x = \delta b \implies \delta x = A^{-1} \delta b $$
En prenant les normes vectorielles de l'équation ci-dessus, et en utilisant les propriétés des normes ($\|M v\| \leq \|M\|\|v\|$) :
$$ \|\delta x\| \leq \|A^{-1}\| \|\delta b\| \quad \text{ (Éq. 1)} $$
Et on sait aussi grâce à l'équation nominale $Ax = b$ que $\|b\| \leq \|A\| \|x\|$, ce qui implique que :
$$ \frac{1}{\|x\|} \leq \frac{\|A\|}{\|b\|} \quad \text{ (Éq. 2)} $$
Si on multiplie nos deux inéquations (Éq. 1 et Éq. 2) membre à membre pour former l'erreur relative côté gauche :
$$
\frac{\|\delta x\|}{\|x\|} \leq \left( \|A^{-1}\| \|A\| \right) \frac{\|\delta b\|}{\|b\|}
$$

Cette formule relie le pire cas d'amplification d'erreur au produit de la norme de la matrice par la norme de son inverse. L'amplification fatale des imprécisions des données initiales dépendra donc **exclusivement des propriétés singulières de la matrice $A$**.

On isole cette valeur sous le nom officiel de **Conditionnement d'une matrice** :
$$
\kappa(A) = \|A^{-1}\| \cdot \|A\|
$$

Si $\kappa(A) \approx 1$, le système est **bien conditionné**.
Si $\kappa(A) \gg 1$, le système est **mal conditionné** (exemple: la célèbre matrice de Hilbert).

### 2. Normes Vectorielles et Matricielles

Pour quantifier la "taille" des erreurs ou d'une matrice, on utilise des normes.

#### Normes Vectorielles (sur un vecteur $v$)
- **Norme 1 (Manhattan) :** $\|v\|_1 = \sum_{i=1}^n |v_i|$ *(Somme des valeurs absolues)*
- **Norme 2 (Euclidienne) :** $\|v\|_2 = \sqrt{\sum_{i=1}^n |v_i|^2}$ *(Distance géométrique ordinaire)*
- **Norme infinie (Max) :** $\|v\|_\infty = \max_{i=1 \dots n} |v_i|$ *(La plus grande composante gouverne)*

#### Normes Matricielles Induites
Une norme matricielle $\|A\|$ découle des normes vectorielles, et représente "l'allongement maximum" que la matrice peut faire subir à n'importe quel vecteur de longueur $1$ :

$$
\|A\| = \max_{v \neq 0} \frac{\|Av\|}{\|v\|}
$$

### 3. Les Mauvaises Méthodes Directes
Avant d'étudier la Factorisation LU, tordons le cou à deux très mauvaises idées informatiques :

1. **La méthode de Cramer ($x_i = \det(A_i) / \det(A)$)** : Pour un système à $n$ inconnues, calculer ces déterminants coûte au minimum $\approx n!$ opérations (une complexité factorielle !). Un système $50 \times 50$ prendrait plus que l'âge de l'univers.
2. **L'inversion matricielle brute ($x = A^{-1}b$) :** Calculer rigoureusement toute la matrice inverse $A^{-1}$ avant de multiplier par $b$ est environ $2.3 \times$ plus lent que l'algorithme "d'élimination" qui mène à la solution de façon asymétrique. (L'utilisation de la commande `inv(A)*b` est à proscrire : on utilise la division gauche matricielle `A\b`).

### 4. Résolution de réseaux triangulaires

Résoudre un système dont la matrice est **uniquement construite par un triangle** est rapide, gratuit, et hyper stable.

Par exemple, un système triangulaire inférieur $L$ ("Lower") :

$$
\begin{pmatrix} a_{11} & 0 & 0 \\ a_{21} & a_{22} & 0 \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}
$$

Cette équation se résout "en cascade à l'endroit" (*forward-substitution*) ligne par ligne, avec une complexité d'à peine $n^2$ opérations (flops), et sans aucune instabilité numérique, car on évite les grandes soustractions de masses. De même, une matrice triangulaire supérieure $U$ ("Upper") se résoudra par remontée (*backward-substitution*).

**L'idée de génie de l'Analyse Numérique :** "Transformons tous les systèmes complexes et intriqués (matrices pleines) en cascades de simples triangles."

### 5. L'Élimination de Gauss et la Factorisation LU

**Démonstration Algorithmique et Théorème :**
Prenons la matrice A :
$$
A = \begin{pmatrix} a_{11} & a_{12} & a_{1n} \\ a_{21} & a_{22} & a_{2n} \\ a_{n1} & a_{n2} & a_{nn} \end{pmatrix}
$$

**Étape 1 :** On veut mettre des zéros dans la 1ère colonne en dessous de $a_{11}$.
On multiplie A par une matrice d'élimination $L_1$ :
$$
L_1 = \begin{pmatrix} 1 & 0 & 0 \\ -\frac{a_{21}}{a_{11}} & 1 & 0 \\ -\frac{a_{n1}}{a_{11}} & 0 & 1 \end{pmatrix}
\implies L_1 A = \begin{pmatrix} a_{11} & a_{12} & a_{1n} \\ 0 & a^{(2)}_{22} & a^{(2)}_{2n} \\ 0 & a^{(2)}_{n2} & a^{(2)}_{nn} \end{pmatrix}
$$
(Où chaque fraction $-\frac{a_{i1}}{a_{11}}$ est le multiplicateur de ligne $k$).

**Étape k :** On reproduit cela $(n-1)$ fois avec $L_2, L_3 \dots L_{n-1}$.
À la fin, la partie inférieure est remplie de zéros. Ce qu'il reste est une matrice purement triangulaire supérieure qu'on appelle $U$.
$$
L_{n-1} \dots L_2 L_1 A = U
$$

**Le génie du Théorème :** Si on rassemble tous ces modificateurs en les inversant du côté du U, l'inverse de la matrice $(L_{n-1} \dots L_1)$ donne la prestigieuse matrice $L$.
Miraculeusement, $L$ est triangulaire inférieure ET tous ses coefficients ne sont **rien d'autre que les coefficients multiplicateurs $l_{ik} = \frac{a_{ik}}{a_{kk}}$ bruts, rangés pile à leur place !**
$$
L = (L_{n-1} \dots L_1)^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ \frac{a_{21}}{a_{11}} & 1 & 0 \\ \frac{a_{n1}}{a_{11}} & \frac{a^{(2)}_{n2}}{a^{(2)}_{22}} & 1 \end{pmatrix}
$$

D'où l'incontournable **Théorème de la Factorisation LU** : Toute matrice régulière peut être scindée algorithmiquement en :
$$
\boxed{A = LU}
$$
Où $L$ rassemble l'historique des multiplicateurs avec des $1$ sur la diagonale, et $U$ contient l'état final des pivots.

Cette factorisation demande une puissance de calcul de :

$$
\text{Coût de Factorisation LU} \approx \frac{2}{3}n^3 \text{ flops}
$$

*(C'est une complexité polynomiale $O(n^3)$ ce qui est massivement meilleur que $n!$).*

#### La Révolution algorithmique de la séparation LU
Le véritable intérêt informatique d'imprimer la matrice "$L$" (au lieu d'effectuer le pivot de Gauss et d'oublier toutes les étapes) intervient si notre second membre $b$ change soudainement.

Pour résoudre n'importe qu'elle nouvelle équation $Ax = b'$, sachant qu'on a déjà souffert pour extraire $A = LU$ (la déconstruction qui coûte le $\frac{2}{3}n^3$) :

$$
L \cdot U \cdot x = b'
$$

On s'y prend en deux temps. D'abord on pose la variable interne $(Ux) = y$ :
1. **Étape de descente** : Résoudre $Ly = b'$ (Cascade avant, coûte $n^2$ flops).
2. **Étape de remontée** : Résoudre $Ux = y$ (Cascade arrière, coûte $n^2$ flops).

Grâce à cet enregistrement mémoire, re-résoudre l'équation avec des variables externes alternatives devient ridiculeusement instantané (du $\sim O(n^2)$ !).

### 6. Le problème de l'instabilité et la correction (Factorisation $PA=LU$)

> ⚠️ **Constat d'échec :** La factorisation naïve $A = LU$ n'est **pas stable**.

**Démonstration du crash avec un petit pivot :**
Prenons la matrice :
$$ A = \begin{pmatrix} 10^{-20} & 1 \\ 1 & 1 \end{pmatrix} \quad (Ax=b \text{ avec } b=(1,2)^T) $$
Cette matrice a un $\kappa(A) \approx 2$ (Donc parfaite pour la machine a priori).
Cependant, l'algorithme $LU$ force la division par le pivot $(1, 1)$. Donc le multiplicateur $l_{21} = \frac{1}{10^{-20}} = 10^{20}$.
La matrice $U$ sera :
$$ U = \begin{pmatrix} 10^{-20} & 1 \\ 0 & 1 - 10^{20} \end{pmatrix} = \begin{pmatrix} 10^{-20} & 1 \\ 0 & -10^{20} \end{pmatrix} $$
 *(Car $1 \ominus 10^{20} = -10^{20}$ à cause du nombre limité de bits de la mantisse, le "1" a été détruit et est tombé dans le néant : Annulation catastrophique !)*
L'ordinateur vient de rater lamentablement le calcul en interne.

#### Le Pivotage Partiel
La parade : On choisit la ligne possédant la **valeur absolue maximale** comme pivot en la permutant. 
Pour l'ordinateur, échanger la ligne $1$ et $2$ correspond à pré-multiplier l'équation $Ax=b$ par une matrice identité permutée $P$ :
$$
P(Ax) = P(b) \implies \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 10^{-20} & 1 \\ 1 & 1 \end{pmatrix} x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$
La nouvelle matrice à factoriser devient $\begin{pmatrix} 1 & 1 \\ 10^{-20} & 1 \end{pmatrix}$.
Maintenant, le pivot en $(1,1)$ est $1$. Le multiplicateur est $l_{21} = \frac{10^{-20}}{1} = 10^{-20}$. **Aucune erreur d'arrondi ou gonflement mathématique infernal n'a lieu**. La stabilité est parfaite.

L'algorithme moderne définitif est **Factorisation LU avec Pivotage ($PA = LU$)** :
$$
\boxed{PA = LU}
$$
Où $P$ est une matrice de repérage de lignes. **Le calcul $PA=LU$ est garanti inconditionnellement stable algorithmiquement.**

### 7. Applications annexes de la force LU

Le but de tout système matriciel n'est pas uniquement de trouver le vecteur $x$.
Les facteurs purs $L, U$ et $P$ ont dévoilé tous les secrets structurels profonds de la trame.

#### Calcul d'un Déterminant lourd
Si on se rappelle qu'un déterminant matriciel se multiplie, alors :
$$ \det(P) \det(A) = \det(L) \det(U) $$
Étant donné que $L$ et $U$ sont des matrices "triangulaires", leur déterminant s'élève à la simple... multiplication de toute leur propre diagonale ! Puisque la diagonale de $L$ ne contient que des $1$ (c'est forcé par le design bas niveau de l'informatique), $\det(L) = 1$. Et le déterminant de $P$ est simplement $(-1)^p$ avec $p$ le nombre de lignes interchangées.

Le véritable déterminant d'un monstre abstrait multidimensionnel $A$ est donc :
$$
\det(A) = (-1)^p \cdot u_{11} \cdot u_{22} \cdots u_{nn}
$$
*(En calculant la factorisation de coût raisonnable, la vraie machine à calculer Octave délivre les déterminants de manière infiniment plus élégante et performante que la technique algébrique scolaire usuelle).*

#### Calcul profond de l'Inversion ($A^{-1}$)
L'inverse s'écrit formellement en recherchant la collection des colonnes vectorielles $x_i$ répondant à l'indépendance de la base canonnique : $A x_i = e_i$.
On exécute l'algorithme de factorisation en cascade sur $PA=LU$ pour toutes les colonnes unitaires, coûtant au global un impressionnant total brut de : $\frac{8}{3}n^3$ flops en pur temps machine.
