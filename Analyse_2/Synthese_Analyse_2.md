# Synthèse — Analyse 2

## Chapitre 14 : Séries de Fourier

> 📚 **Objectif du chapitre :** Apprendre à décomposer n'importe quelle fonction périodique en une somme (potentiellement infinie) de simples sinusoïdes. Ce chapitre est la porte d'entrée vers le traitement du signal, la résolution des EDP (équation de la chaleur), et la compression de données. Nous partons de zéro absolu.

### 1. Introduction et Motivation Physique

#### 1.1. Qu'est-ce qu'un son musical ?

Un son pur (celui d'un diapason) est une simple onde sinusoïdale qui fait vibrer l'air :
$$
y(t) = A \sin(\omega t + \varphi)
$$
Où :
- $A$ est l'**amplitude** (volume sonore),
- $\omega = \frac{2\pi}{T}$ est la **fréquence angulaire** ($T$ = période),
- $\varphi$ est la **phase** (décalage temporel initial).

La **hauteur** du son est déterminée par sa fréquence ($1/T$). Par exemple, le La de référence vibre à $440$ Hz (sa période est $T = 1/440$ sec).

Quand un instrument de musique joue une note, il ne produit pas un son pur ! Il superpose le son fondamental avec plusieurs **harmoniques** (des sons purs dont la fréquence est un multiple entier de la fréquence fondamentale). C'est cette superposition qui crée le **timbre** unique de chaque instrument.

Mathématiquement, cela signifie qu'un son musical est une fonction périodique de la forme :
$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{k} \left( a_n \cos(n\omega t) + b_n \sin(n\omega t) \right)
$$

> 💡 **La Question Fondamentale de Fourier :** Peut-on *toujours* décomposer n'importe quelle fonction périodique en une telle somme de sinus et cosinus ? La réponse (sous certaines conditions) est **OUI**, mais il faut parfois une infinité d'harmoniques. C'est une **série de Fourier**.

#### 1.2. Rappel fondamental : Somme Sinus + Cosinus

**Lemme :** Toute combinaison linéaire $a\cos(\omega t) + b\sin(\omega t)$ peut se réécrire sous la forme d'une **unique** sinusoïde d'amplitude $A$ et de phase $\varphi$ :
$$
a\cos(\omega t) + b\sin(\omega t) = A\sin(\omega t + \varphi)
$$

**Démonstration :**
Développons $A\sin(\omega t + \varphi)$ avec la formule d'addition des arcs :
$$
A\sin(\omega t + \varphi) = A(\sin(\omega t)\cos\varphi + \cos(\omega t)\sin\varphi)
$$
Pour que cela soit égal à $a\cos(\omega t) + b\sin(\omega t)$, il faut identifier :
$$
\begin{cases} a = A\sin\varphi \\ b = A\cos\varphi \end{cases}
$$
En élevant au carré et en sommant : $a^2 + b^2 = A^2\sin^2\varphi + A^2\cos^2\varphi = A^2$.
Donc :
$$
\boxed{A = \sqrt{a^2 + b^2}}
$$
Et la phase se retrouve par $\tan\varphi = a/b$ (en tenant compte du quadrant).

#### 1.3. Pourquoi les Séries de Fourier plutôt que Taylor ?

| Critère | Série de Taylor | Série de Fourier |
| :--- | :--- | :--- |
| **Type d'approximation** | **Locale** (au voisinage d'un point $x_0$) | **Globale** (sur tout un intervalle $[-L, L]$) |
| **Base de fonctions** | Polynômes $\{(x-x_0)^k\}$ | Sinusoïdes $\{1, \cos(n\omega x), \sin(n\omega x)\}$ |
| **Exigence sur $f$** | $f$ doit être $C^{\infty}$ (voire analytique) | $f$ peut être **discontinue** ! |
| **Convergence** | Pas garantie vers $f$ même si $f$ est $C^{\infty}$ | Garantie en moyenne quadratique ($L^2$) |

**Conclusion :** Taylor est utile localement, Fourier est utile pour comprendre le comportement **global** d'une fonction sur un domaine entier.

### 2. Le Produit Scalaire et la Norme $L^2$

#### 2.1. L'espace $L^2$ : Un nouvel univers vectoriel

Avant de parler de Fourier, il faut un cadre mathématique rigoureux. On va traiter les fonctions comme des **vecteurs** dans un espace de dimension infinie.

**Définition :** L'espace $L^2([a,b], \mathbb{K})$ est l'ensemble des fonctions $f$ définies sur $]a,b[$ telles que leur carré est intégrable :
$$
\int_a^b |f(x)|^2 \, dx < +\infty
$$
On dit que $f$ est **de carré sommable** (ou de carré intégrable).

#### 2.2. Le produit scalaire dans $L^2$

Pour comparer deux fonctions $f$ et $g$ dans $L^2([a,b], \mathbb{K})$, on définit le **produit scalaire** :
$$
\boxed{\langle f, g \rangle = \int_a^b f(x) \overline{g(x)} \, dx}
$$
Où $\overline{g}$ est le conjugué complexe de $g$ (si $g$ est réelle, $\overline{g} = g$).

Ce produit scalaire vérifie les mêmes propriétés que le produit scalaire classique de $\mathbb{R}^n$ :
1. **Linéarité à gauche :** $\langle \alpha f + \beta h, g \rangle = \alpha \langle f, g \rangle + \beta \langle h, g \rangle$
2. **Symétrie hermitienne :** $\langle f, g \rangle = \overline{\langle g, f \rangle}$
3. **Positivité :** $\langle f, f \rangle \geq 0$
4. **Définité :** $\langle f, f \rangle = 0 \implies f = 0$ presque partout

#### 2.3. La norme $L^2$ (norme en moyenne quadratique)

La **norme** $L^2$ mesure la « taille » d'une fonction :
$$
\boxed{\|f\|_2 = \sqrt{\langle f, f \rangle} = \left( \int_a^b |f(x)|^2 \, dx \right)^{1/2}}
$$

> 💡 **Analogie visuelle :** Si $f$ est un signal sonore, $\|f\|_2^2$ est proportionnel à l'**énergie totale** du signal. La norme $L^2$ mesure la puissance globale.

**L'inégalité de Cauchy-Schwarz** reste valide dans cet espace :
$$
|\langle f, g \rangle|^2 \leq \langle f, f \rangle \cdot \langle g, g \rangle = \|f\|_2^2 \cdot \|g\|_2^2
$$

#### 2.4. Systèmes orthogonaux et orthonormés

**Définition :** Un ensemble de fonctions $\mathcal{F} = \{\varphi_k\}_{k \in \mathbb{N}}$ dans $L^2([a,b])$ est :
- **Libre** si toute partie finie est linéairement indépendante.
- **Orthogonal** si $\langle \varphi_j, \varphi_k \rangle = 0$ pour tout $j \neq k$.
- **Orthonormé** si de plus $\langle \varphi_k, \varphi_k \rangle = 1$ pour tout $k$ (i.e. $\|\varphi_k\|_2 = 1$).

#### 2.5. Démonstration : Les systèmes trigonométriques classiques sont orthogonaux

**Théorème :** Le système $\mathcal{F} = \{1, \cos(kx), \sin(kx) \mid k \in \mathbb{N}_0\}$ est orthogonal sur $[-\pi, \pi]$.

**Démonstration (par calcul direct des produits scalaires) :**

**(a)** $\langle \cos(jx), \sin(kx) \rangle = \int_{-\pi}^{\pi} \cos(jx)\sin(kx) \, dx = 0$ pour tous $j, k$.
Car $\cos(jx)\sin(kx)$ est une fonction **impaire** (produit d'une paire par une impaire), et l'intégrale d'une fonction impaire sur un intervalle symétrique est toujours nulle.

**(b)** Pour $j \neq k$ : $\langle \cos(jx), \cos(kx) \rangle = \int_{-\pi}^{\pi} \cos(jx)\cos(kx) \, dx$.
On utilise la formule de linéarisation : $\cos(jx)\cos(kx) = \frac{1}{2}[\cos((j-k)x) + \cos((j+k)x)]$.
$$
= \frac{1}{2} \int_{-\pi}^{\pi} \cos((j-k)x) \, dx + \frac{1}{2} \int_{-\pi}^{\pi} \cos((j+k)x) \, dx
$$
Comme $j-k \neq 0$ et $j+k \neq 0$, ces intégrales de cosinus sur une période complète valent **zéro**. Donc $\langle \cos(jx), \cos(kx) \rangle = 0$.

**(c)** De même, $\langle \sin(jx), \sin(kx) \rangle = 0$ pour $j \neq k$.

**(d)** Les normes au carré : Pour $k \geq 1$ :
$$
\|\cos(kx)\|_2^2 = \int_{-\pi}^{\pi} \cos^2(kx) \, dx = \int_{-\pi}^{\pi} \frac{1 + \cos(2kx)}{2} \, dx = \frac{2\pi}{2} + 0 = \pi
$$
De même $\|\sin(kx)\|_2^2 = \pi$. Et $\|1\|_2^2 = 2\pi$.

Le **système orthonormé** correspondant est donc :
$$
\left\{ \frac{1}{\sqrt{2\pi}}, \frac{\cos(kx)}{\sqrt{\pi}}, \frac{\sin(kx)}{\sqrt{\pi}} \; ; \; k \in \mathbb{N}_0 \right\}
$$

**Généralisation sur $[-L, L]$ :** On remplace $x$ par $\frac{\pi x}{L}$. Le système orthonormé devient :
$$
\left\{ \frac{1}{\sqrt{2L}}, \frac{1}{\sqrt{L}}\cos\left(\frac{k\pi x}{L}\right), \frac{1}{\sqrt{L}}\sin\left(\frac{k\pi x}{L}\right) \; ; \; k \in \mathbb{N}_0 \right\}
$$

### 3. Les Coefficients de Fourier et la Meilleure Approximation

#### 3.1. La projection orthogonale : l'idée fondatrice

En algèbre linéaire classique (dans $\mathbb{R}^n$), si on a une base orthonormée $\{e_1, \dots, e_n\}$, tout vecteur $\vec{v}$ se décompose comme :
$$
\vec{v} = \sum_{k=1}^{n} c_k \vec{e}_k \quad \text{où} \quad c_k = \langle \vec{v}, \vec{e}_k \rangle
$$
Les coefficients $c_k$ sont les **projections** de $\vec{v}$ sur chaque axe $\vec{e}_k$.

En Fourier, c'est **exactement la même idée**, mais avec des fonctions à la place des vecteurs, et des intégrales à la place des produits scalaires !

#### 3.2. Définition des Coefficients de Fourier

**Définition :** Soit $\mathcal{F} = \{\varphi_k\}$ un système orthogonal dans $L^2([a,b])$, et $f \in L^2([a,b])$.

Le **coefficient de Fourier** de $f$ relativement à $\varphi_k$ est :
$$
\boxed{c_k = \frac{\langle f, \varphi_k \rangle}{\langle \varphi_k, \varphi_k \rangle} = \frac{\langle f, \varphi_k \rangle}{\|\varphi_k\|_2^2}}
$$

**Démonstration (pourquoi cette formule ?) :**
On cherche le scalaire $c_k$ tel que la projection de $f$ sur la droite engendrée par $\varphi_k$ soit $c_k \varphi_k$. Par définition, le résidu $f - c_k \varphi_k$ doit être orthogonal à $\varphi_k$ :
$$
\langle f - c_k \varphi_k, \varphi_k \rangle = 0
$$
$$
\langle f, \varphi_k \rangle - c_k \langle \varphi_k, \varphi_k \rangle = 0
$$
$$
c_k = \frac{\langle f, \varphi_k \rangle}{\langle \varphi_k, \varphi_k \rangle}
$$

La **série de Fourier** de $f$ relativement au système $\mathcal{F}$ est alors :
$$
f \sim \sum_{k=0}^{\infty} c_k \varphi_k
$$

#### 3.3. Les formules classiques des coefficients (le cas trigonométrique)

Pour le système $\{1/2, \cos(k\pi x/L), \sin(k\pi x/L)\}$ sur $[-L, L]$ :

$$
\boxed{a_k = \frac{1}{L} \int_{-L}^{L} f(t) \cos\left(\frac{k\pi t}{L}\right) dt \qquad b_k = \frac{1}{L} \int_{-L}^{L} f(t) \sin\left(\frac{k\pi t}{L}\right) dt}
$$

Et la série de Fourier s'écrit :
$$
f(x) \sim \frac{a_0}{2} + \sum_{k=1}^{\infty} \left[ a_k \cos\left(\frac{k\pi x}{L}\right) + b_k \sin\left(\frac{k\pi x}{L}\right) \right]
$$

> ⚠️ **Remarque importante :** Le terme $a_0/2$ est la **valeur moyenne** de $f$ sur $[-L, L]$.

#### 3.4. Théorème de la Meilleure Approximation en Moyenne Quadratique

**Théorème :** Parmi toutes les combinaisons linéaires $\sum_{k=0}^{n} \alpha_k \varphi_k$, celle qui **minimise** l'erreur en norme $L^2$ (c'est-à-dire la distance quadratique à $f$) est exactement la somme partielle de Fourier avec $\alpha_k = c_k$.

$$
\text{Minimiser } \left\| f - \sum_{k=0}^{n} \alpha_k \varphi_k \right\|_2 \quad \Longrightarrow \quad \alpha_k = c_k \; \forall k
$$

**Démonstration complète :**
En développant la norme au carré, on utilise l'orthonormalité du système :
$$
\left\| f - \sum_{k=0}^{n} \alpha_k \varphi_k \right\|_2^2 = \langle f, f \rangle - \sum_{k=0}^{n} (\bar{\alpha}_k c_k + \alpha_k \bar{c}_k - |\alpha_k|^2)
$$
En complétant le carré (identique à la technique du $(\alpha_k - c_k)(\bar{\alpha}_k - \bar{c}_k)$) :
$$
= \|f\|_2^2 + \sum_{k=0}^{n} |c_k - \alpha_k|^2 \|\varphi_k\|_2^2 - \sum_{k=0}^{n} |c_k|^2 \|\varphi_k\|_2^2
$$
Le premier et le dernier terme sont **fixes** (ne dépendent pas du choix de $\alpha_k$). Le terme du milieu $\sum |c_k - \alpha_k|^2 \geq 0$ est minimisé (valeur $= 0$) si et seulement si $\alpha_k = c_k$ pour tout $k$.

> 💡 **Interprétation géométrique :** Les coefficients de Fourier réalisent la **projection orthogonale** de $f$ sur le sous-espace engendré par $\{\varphi_0, \dots, \varphi_n\}$. C'est le point le plus proche de $f$ dans ce sous-espace, exactement comme en géométrie euclidienne classique.

### 4. Les Théorèmes de Convergence : Bessel, Parseval, Complétude

#### 4.1. Le Théorème de Pythagore (version $L^2$)

**Théorème (Pythagore dans $L^2$) :** Comme $f - \text{proj}_{E_n} f$ est orthogonal à $\text{proj}_{E_n} f$ :
$$
\boxed{\|f\|_2^2 = \left\| \sum_{k=0}^{n} c_k \varphi_k \right\|_2^2 + \left\| f - \sum_{k=0}^{n} c_k \varphi_k \right\|_2^2}
$$
C'est-à-dire :
$$
\|f\|_2^2 = \sum_{k=0}^{n} |c_k|^2 \|\varphi_k\|_2^2 + R_n^2
$$
Où $R_n = \|f - \sum_{k} c_k \varphi_k\|_2$ est le **reste** (erreur résiduelle d'approximation).

Comme $R_n^2 \geq 0$, on en déduit immédiatement :

#### 4.2. L'Inégalité de Bessel

$$
\boxed{\sum_{k=0}^{\infty} |c_k|^2 \|\varphi_k\|_2^2 \leq \|f\|_2^2}
$$

**Démonstration :** Il suffit de faire tendre $n \to \infty$ dans l'inégalité de Pythagore ($R_n^2 \geq 0 \implies \sum |c_k|^2 \|\varphi_k\|_2^2 \leq \|f\|_2^2$). La limite préserve les inégalités non strictes.

**Conséquence immédiate :** Si le système $\mathcal{F}$ est orthonormé ($\|\varphi_k\|_2 = 1$), alors la série $\sum |c_k|^2$ **converge**, ce qui force les coefficients à tendre vers zéro : $c_k \to 0$ quand $k \to \infty$.

#### 4.3. L'Égalité de Parseval et la Complétude

**Définition :** Convergence en moyenne quadratique ($L^2$) :
$$
\sum_{k=0}^{\infty} c_k \varphi_k \overset{L^2}{=} f \quad \Longleftrightarrow \quad \lim_{n \to \infty} \left\| f - \sum_{k=0}^{n} c_k \varphi_k \right\|_2 = 0
$$

**Théorème (Parseval) :** La série de Fourier converge en $L^2$ vers $f$ **si et seulement si** l'Égalité de Parseval est vérifiée :
$$
\boxed{\sum_{k=0}^{\infty} |c_k|^2 \|\varphi_k\|_2^2 = \|f\|_2^2}
$$

**Démonstration :** Cela découle directement de Pythagore. La convergence $L^2$ signifie $R_n \to 0$, donc $\sum |c_k|^2 \|\varphi_k\|_2^2 = \|f\|_2^2 - \lim R_n^2 = \|f\|_2^2$.

**Définition (Système Complet) :** Un système orthogonal $\mathcal{F}$ est dit **complet** dans $L^2([a,b])$ si pour toute $f \in L^2([a,b])$, la série de Fourier de $f$ converge en $L^2$ vers $f$.

> 🔑 **Fait fondamental:** Les trois systèmes trigonométriques classiques sont **complets** :
> - $\{1, \cos(kx), \sin(kx)\}$ est complet dans $L^2([-\pi, \pi])$
> - $\{\sin(kx)\}$ est complet dans $L^2([0, \pi])$
> - $\{\cos(kx)\}$ est complet dans $L^2([0, \pi])$

#### 4.4. Les trois types de convergence

| Type | Notation | Signification |
| :--- | :--- | :--- |
| **Convergence simple** | $\overset{C.S.}{=}$ | $\forall x$, $\|s_n(x) - f(x)\| \to 0$ |
| **Convergence uniforme** | $\overset{C.U.}{=}$ | $\sup_x \|s_n(x) - f(x)\| \to 0$ |
| **Convergence $L^2$** | $\overset{L^2}{=}$ | $\int |s_n - f|^2 \to 0$ |

Relations entre elles :
$$
\text{C.U.} \Rightarrow \text{C.S.} \quad \text{et} \quad \text{C.U.} \Rightarrow \text{C.}L^2
$$
Mais attention : $\text{C.S.} \not\Rightarrow \text{C.U.}$, $\text{C.S.} \not\Rightarrow \text{C.}L^2$, et $\text{C.}L^2 \not\Rightarrow \text{C.S.}$.

### 5. Les Séries de Fourier Classiques : Formules Pratiques

#### 5.1. Série Sinus + Cosinus sur $[-L, L]$

$$
f(x) \sim \frac{a_0}{2} + \sum_{k=1}^{\infty} \left[ a_k \cos\left(\frac{k\pi x}{L}\right) + b_k \sin\left(\frac{k\pi x}{L}\right) \right]
$$

$$
a_k = \frac{1}{L} \int_{-L}^{L} f(t) \cos\left(\frac{k\pi t}{L}\right) dt \qquad b_k = \frac{1}{L} \int_{-L}^{L} f(t) \sin\left(\frac{k\pi t}{L}\right) dt
$$

#### 5.2. Série Sinus seule sur $[0, L]$ (prolongement impair)

Si on souhaite n'utiliser **que des sinus**, on prolonge $f$ de manière **impaire** et périodique :
$$
f(x) \sim \sum_{k=1}^{\infty} b_k \sin\left(\frac{k\pi x}{L}\right) \qquad \text{où} \quad b_k = \frac{2}{L} \int_0^{L} f(t) \sin\left(\frac{k\pi t}{L}\right) dt
$$

#### 5.3. Série Cosinus seule sur $[0, L]$ (prolongement pair)

$$
f(x) \sim \frac{a_0}{2} + \sum_{k=1}^{\infty} a_k \cos\left(\frac{k\pi x}{L}\right) \qquad \text{où} \quad a_k = \frac{2}{L} \int_0^{L} f(t) \cos\left(\frac{k\pi t}{L}\right) dt
$$

#### 5.4. Série de Fourier Complexe

En utilisant la formule d'Euler $e^{ix} = \cos x + i\sin x$, on peut réécrire la série de Fourier sous forme **complexe**, souvent plus élégante pour les calculs :

**Démonstration du passage réel $\to$ complexe :**
$$
a_k\cos(k\omega_0 t) + b_k\sin(k\omega_0 t) = a_k \frac{e^{ik\omega_0 t} + e^{-ik\omega_0 t}}{2} + b_k \frac{e^{ik\omega_0 t} - e^{-ik\omega_0 t}}{2i}
$$
$$
= \frac{a_k - ib_k}{2} e^{ik\omega_0 t} + \frac{a_k + ib_k}{2} e^{-ik\omega_0 t}
$$

En posant $c_k = \frac{a_k - ib_k}{2}$ et $c_{-k} = \frac{a_k + ib_k}{2}$, et $c_0 = a_0/2$, on obtient :

$$
\boxed{f(t) \sim \sum_{k=-\infty}^{+\infty} c_k e^{ik\omega_0 t} \qquad \text{où} \quad c_k = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-ik\omega_0 t} dt}
$$

Avec $\omega_0 = 2\pi / T$.

**Propriétés pour les fonctions réelles :** Si $f$ est réelle, alors $c_{-k} = \overline{c_k}$ (les coefficients négatifs sont les conjugués des positifs). L'amplitude de la $k$-ième harmonique est $A_k = 2|c_k|$.

### 6. Fonctions Régularisées et Convergence Simple

#### 6.1. Fonctions continues par morceaux

**Définition :** Une fonction $f$ est **continue par morceaux** sur $[a,b]$ s'il existe une subdivision $a = x_0 < x_1 < \dots < x_n = b$ telle que :
- $f$ est continue sur chaque sous-intervalle ouvert $]x_{i-1}, x_i[$
- Les limites à droite $f(x_i^+)$ et à gauche $f(x_i^-)$ existent et sont finies en chaque point de subdivision.

#### 6.2. Fonction régularisée

**Définition :** La **fonction régularisée** $\tilde{f}$ de $f$ est celle qui, à chaque point de discontinuité, prend la **moyenne** des limites à droite et à gauche :
$$
\boxed{\tilde{f}(x) = \frac{f(x^-) + f(x^+)}{2}}
$$
Aux extrémités de l'intervalle $[a,b]$ (en pensant au prolongement périodique) :
$$
\tilde{f}(a) = \tilde{f}(b) = \frac{f(a^+) + f(b^-)}{2}
$$

> 💡 Aux points de **continuité**, $f(x^-) = f(x^+) = f(x)$, donc $\tilde{f}(x) = f(x)$. La régularisation ne change rien aux points où $f$ se comporte bien !

#### 6.3. Dérivées généralisées et écriture simplifiée $C^1_{\text{morc}}$

**Motivation :** Pour le théorème de Dirichlet, on a besoin d'une notion de dérivée adaptée aux fonctions discontinues. On ne peut pas utiliser la dérivée classique en un point de discontinuité.

**Définition (Dérivée généralisée droite/gauche) :** Soit $f \in C^0_{\text{morc}}([a,b])$ et $x \in ]a,b[$. On définit :
$$
\text{DDG}(f)|_x := \lim_{h \to 0^+} \frac{f(x+h) - f(x^+)}{h} \qquad \text{(dérivée à droite généralisée)}
$$
$$
\text{DGG}(f)|_x := \lim_{h \to 0^+} \frac{f(x-h) - f(x^-)}{h} \qquad \text{(dérivée à gauche généralisée)}
$$

> ⚠️ **Remarque cruciale :** La valeur de $f(x)$ elle-même **n'intervient pas** dans le calcul de la dérivée généralisée ! Seules les limites latérales $f(x^+)$ et $f(x^-)$ comptent.

**Proposition :** Si $f \in C^0_{\text{morc}}([a,b])$, que $f$ est dérivable sur $[a,b]$ sauf en un nombre fini de points $c_1, \ldots, c_n$, et que $f'(c_i^+)$ et $f'(c_i^-)$ existent et sont finies en chacun de ces points, alors $f$ admet une dérivée généralisée droite et gauche en tout point de $[a,b]$.

**Convention — Classe $C^1_{\text{morc}}$ :** On écrira $f \in C^1_{\text{morc}}([a,b], \mathbb{R})$ s'il existe une subdivision $a = x_0 < x_1 < \cdots < x_n = b$ telle que :
- $f \in C^1(]x_{i-1}, x_i[, \mathbb{R})$ pour tout $i$,
- Les limites $f(x_i^+)$, $f'(x_i^+)$ et $f(x_i^-)$, $f'(x_i^-)$ existent et sont finies.

> 💡 **Pratiquement :** L'hypothèse du théorème de Dirichlet est que $f \in C^1_{\text{morc}}([-L, L])$, c'est-à-dire que $f$ **et** sa dérivée $f'$ sont toutes deux continues par morceaux. On n'exige **pas** que $f$ soit définie aux points de discontinuité, ni que $f$ soit dérivable en ces points.

#### 6.3. Le Théorème de Dirichlet (Convergence Simple)

C'est **LE** grand théorème de convergence des séries de Fourier :

**Théorème (Dirichlet) :** Soit $f$ une fonction continue par morceaux et $C^1$ par morceaux sur $[-L, L]$ (c'est-à-dire que $f$ ET sa dérivée $f'$ sont continues par morceaux). Alors la série de Fourier de $f$ converge **simplement** (point par point) vers la **fonction régularisée** $\tilde{f}$ :
$$
\boxed{\frac{a_0}{2} + \sum_{k=1}^{\infty} \left[ a_k \cos\left(\frac{k\pi x}{L}\right) + b_k \sin\left(\frac{k\pi x}{L}\right) \right] = \tilde{f}(x) = \frac{f(x^-) + f(x^+)}{2}}
$$

En particulier :
- **Aux points de continuité** : la série converge vers $f(x)$.
- **Aux points de discontinuité** : la série converge vers la moyenne des limites latérales.

#### 6.4. Le Phénomène de Gibbs

Au voisinage d'un point de discontinuité, les sommes partielles de la série de Fourier **oscillent** et dépassent la valeur de $f$ par environ $9\%$ de l'amplitude du saut, même quand $n \to \infty$. Ce dépassement ne disparaît pas : il se concentre au fur et à mesure vers le point de discontinuité, mais l'amplitude fixe du dépassement ($\approx 8.95\%$) ne diminue pas ! C'est le **phénomène de Gibbs**.

### 6 bis. Exemples Canoniques des Séries de Fourier — Trois Ondes Importantes

Ces trois exemples sont fondamentaux et reviennent constamment en pratique.

#### Exemple A — L'Onde Triangulaire ($f(x) = |x|$ sur $[-L, L]$)

$f$ est **continue** et **paire**, donc $b_k = 0$ pour tout $k$. Sa dérivée $f'$ est $C^0_{\text{morc}}$ (elle vaut $\pm 1$), donc le prolongement périodique $f_{\text{pro}}$ est continu et la série converge **uniformément** vers $f$.

$$
f(x) = \frac{L}{2} - \frac{4L}{\pi^2} \sum_{\substack{n=1 \\ n \text{ impair}}}^{\infty} \frac{\cos\left(\frac{n\pi x}{L}\right)}{n^2}
$$

**Conséquence immédiate** (en posant $x = 0$) :
$$
\sum_{n=0}^{\infty} \frac{1}{(2n+1)^2} = 1 + \frac{1}{9} + \frac{1}{25} + \cdots = \frac{\pi^2}{8}
$$
Les coefficients décroissent en $1/n^2$ (typique d'une fonction continue à dérivée discontinue).

#### Exemple B — L'Onde en Dents de Scie ($f(x) = x/2$ sur $[-\pi, \pi]$)

$f$ est **impaire** (à un décalage près), donc $a_k = 0$. Elle est $C^1$ mais son prolongement périodique $f_{\text{pro}}$ est **discontinu** (sauts en $\pm\pi$).

$$
f(x) = \sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} \sin(kx) = \sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \cdots
$$

Les coefficients ne décroissent qu'en $1/k$ (la série $\sum |b_k|$ **diverge**), et la convergence est **simple** (pas uniforme) à cause des discontinuités de $f_{\text{pro}}$. On retrouve par Parseval :
$$
\sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6}
$$

#### Exemple C — L'Onde Carrée ($f(x) = \pm 1/2$ sur $[-\pi, \pi]$)

$f$ est **impaire** et discontinue, donc $a_k = 0$ et seuls les $b_k$ des harmoniques impaires sont non nuls :
$$
\tilde{f}_{\text{pro}}(x) = \frac{2}{\pi} \sum_{\substack{k=1 \\ k \text{ impair}}}^{\infty} \frac{\sin(kx)}{k} = \frac{2}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots\right)
$$

Le phénomène de Gibbs est particulièrement visible sur cet exemple : les sommes partielles dépassent $\pm 1/2$ d'environ $9\%$ au voisinage des sauts.

| Onde | Continuité de $f_{\text{pro}}$ | Décroissance des coefs | Convergence |
|:---|:---|:---|:---|
| Triangulaire ($\|x\|$) | Continue | $1/n^2$ | **Uniforme** |
| Dents de scie ($x/2$) | Discontinue | $1/n$ | **Simple** seulement |
| Carrée ($\pm 1/2$) | Discontinue | $1/n$ | **Simple** + Gibbs |

### 7. Convergence Uniforme

#### 7.1. Coefficients de Fourier de la dérivée

**Théorème :** Si $f$ est $C^1$ par morceaux et continue sur $[-L, L]$ (avec $f(-L) = f(L)$), alors les coefficients de Fourier de $f'$ s'obtiennent par simple multiplication :

Pour la série complexe : si $c_k$ sont les coefficients de $f$, alors les coefficients de $f'$ sont $ik\omega_0 c_k$.

**Démonstration (par intégration par parties) :**
$$
c_k(f') = \frac{1}{T}\int_{-T/2}^{T/2} f'(t) e^{-ik\omega_0 t} dt = \frac{1}{T}\left[ f(t)e^{-ik\omega_0 t} \right]_{-T/2}^{T/2} + \frac{ik\omega_0}{T}\int_{-T/2}^{T/2} f(t) e^{-ik\omega_0 t} dt
$$
Le terme entre crochets s'annule si $f$ est périodique ($f(-T/2) = f(T/2)$). Il reste :
$$
c_k(f') = ik\omega_0 \cdot c_k(f)
$$

**Cas général (sans hypothèse de continuité du prolongement) :** Si $f \in C^1_{\text{morc}}([-\pi, \pi])$ mais $f(-\pi) \neq f(\pi)$, notons $\delta := f(\pi) - f(-\pi)$ le **saut de discontinuité** du prolongement périodique. Alors :
$$
\boxed{a_k(f') = k b_k(f) + \frac{(-1)^k}{\pi} \delta, \qquad b_k(f') = -k a_k(f)}
$$
Le terme correctif $\frac{(-1)^k \delta}{\pi}$ **ne tend pas vers zéro** : si $f(-\pi) \neq f(\pi)$, la formule de dérivation naïve est **fausse** !

> 💡 **Conséquence pratique :** Si $f$ est très dérivable (« lisse »), ses coefficients de Fourier $c_k$ décroissent **très vite** (comme $1/k^p$ si $f$ est $C^{p-1}$). Plus la fonction est régulière, plus sa série de Fourier converge rapidement.

#### 7.2. Théorème de Convergence Uniforme

**Théorème :** Si $f$ est continue, périodique de période $2L$, et $C^1$ par morceaux (sa dérivée existe et est continue par morceaux), alors la série de Fourier de $f$ converge **uniformément** vers $f$ sur tout $\mathbb{R}$.

#### 7.3. Convergence Uniforme pour les Systèmes Complets

**Théorème (cas général) :** Soit $\mathcal{F} = \{\varphi_k\}$ un système orthogonal **complet** dans $L^2([a,b])$. Si $f \in C^2([a,b])$ et satisfait les **conditions aux limites** appropriées au système, alors :
$$
\sum_{k=0}^{\infty} c_k(f) \varphi_k(x) \overset{C.U.}{=} f(x)
$$
En résumé :
$$
\mathcal{F} \text{ complet} + f \in C^2 + f \text{ satisfait les C.L.} \implies \text{convergence uniforme}
$$

**Application :** Pour les séries classiques sinus/cosinus, les conditions aux limites sont $f(-L) = f(L)$ (prolongement périodique continu). Si cette condition n'est pas satisfaite, on s'expose au **phénomène de Gibbs**, même si $f$ est très régulière sur $]-L, L[$.

#### 7.4. Identification des Coefficients d'une Série Uniformément Convergente

**Proposition :** Si le système $\{\varphi_j\}_{j \in \mathbb{N}}$ est orthogonal et si la série $\sum_{j=0}^{\infty} b_j \varphi_j$ converge **uniformément** vers $f$ sur $[a,b]$, alors les $b_j$ sont les **coefficients de Fourier** de $f$ relativement à ce système :
$$
b_k = \frac{\langle f, \varphi_k \rangle}{\|\varphi_k\|_2^2}
$$

**Démonstration :** Comme la convergence est uniforme, on peut **intervertir somme et intégrale** :
$$
\langle f, \varphi_k \rangle = \int_a^b f(x) \varphi_k^*(x) dx = \int_a^b \left(\sum_{j=0}^{\infty} b_j \varphi_j(x)\right) \varphi_k^*(x) dx = \sum_{j=0}^{\infty} b_j \underbrace{\langle \varphi_j, \varphi_k \rangle}_{= \|\varphi_k\|^2 \delta_{jk}} = b_k \|\varphi_k\|^2
$$

> ⚠️ **Important :** Ce résultat garantit l'**unicité** de la représentation : si deux séries d'un même système orthogonal convergent uniformément vers la même fonction, leurs coefficients sont nécessairement égaux.

### 8. Opérations sur les Séries de Fourier

#### 8.1. Dérivation terme à terme

On peut dériver une série de Fourier terme à terme **si** $f$ est suffisamment régulière (continûment différentiable et périodique).

#### 8.2. Intégration terme à terme

**Théorème :** L'intégration terme à terme d'une série de Fourier est **toujours valide** (même pour des fonctions simplement $L^2$), ce qui est beaucoup plus permissif que pour la dérivation.

$$
\int_a^x f(t) dt = \frac{a_0}{2}(x-a) + \sum_{k=1}^{\infty} \int_a^x \left[ a_k \cos\left(\frac{k\pi t}{L}\right) + b_k \sin\left(\frac{k\pi t}{L}\right) \right] dt
$$

#### 8.3. Produit de séries de Fourier

**Question :** Si $f \sim \sum_k f_k e^{ik\omega x}$ et $g \sim \sum_k g_k e^{ik\omega x}$, quels sont les coefficients de Fourier du **produit** $f \cdot g$ ?

**Réponse :** En multipliant formellement les deux séries, on obtient :
$$
\boxed{c_k(f \cdot g) = \sum_{\ell = -\infty}^{+\infty} f_\ell \cdot g_{k-\ell}}
$$

Cette somme est une **convolution discrète** des deux suites de coefficients $(f_k)_{k \in \mathbb{Z}}$ et $(g_k)_{k \in \mathbb{Z}}$. C'est l'analogue discret du produit de convolution de fonctions.

> ⚠️ **Attention :** À ne pas confondre avec le produit de convolution $f * g$ qui, lui, correspond à une multiplication des coefficients $c_k(f * g) = c_k(f) \cdot c_k(g)$. C'est l'opération **inverse** :
> - Produit $\cdot$ dans le temps $\leftrightarrow$ **convolution discrète** dans les fréquences
> - Convolution $*$ dans le temps $\leftrightarrow$ **produit** dans les fréquences

#### 8.4. Produit de convolution

**Définition :** Le **produit de convolution** de deux fonctions périodiques $f$ et $g$ de période $T$ est :
$$
(f * g)(x) = \frac{1}{T}\int_0^T f(t) g(x-t) dt
$$

**Théorème spectaculaire :** La convolution dans le domaine temporel correspond à une **simple multiplication** dans le domaine fréquentiel (des coefficients de Fourier) :
$$
\boxed{c_k(f * g) = c_k(f) \cdot c_k(g)}
$$

> 💡 C'est l'une des propriétés les plus puissantes de l'analyse de Fourier et la raison fondamentale pour laquelle la transformée de Fourier est omniprésente en traitement du signal.

### 9. Application : L'Équation de la Chaleur (1D)

#### 9.1. Le problème physique

On considère une barre métallique de longueur $L$ dont les deux extrémités sont maintenues à température nulle. On connaît la distribution de température initiale $f(x)$ le long de la barre. On cherche la température $u(x,t)$ en tout point $x$ et à tout instant $t > 0$.

Cela se modélise par :
- **EDP (Équation de la chaleur) :** $\frac{\partial u}{\partial t} = \alpha^2 \frac{\partial^2 u}{\partial x^2}$ pour $0 < x < L$, $t > 0$
- **Conditions aux limites :** $u(0, t) = u(L, t) = 0$ pour tout $t > 0$
- **Condition initiale :** $u(x, 0) = f(x)$

#### 9.2. La Méthode de Séparation des Variables

**Étape 1 :** On cherche une solution de la forme $u(x,t) = X(x) \cdot T(t)$ (la variable d'espace et la variable de temps sont séparées).

En injectant dans l'EDP :
$$
X(x) T'(t) = \alpha^2 X''(x) T(t) \implies \frac{T'(t)}{\alpha^2 T(t)} = \frac{X''(x)}{X(x)} = -\lambda
$$
Chaque côté dépend d'une variable différente, donc les deux doivent être **égaux à une même constante** $-\lambda$.

**Étape 2 :** On résout les deux EDO séparément.

L'équation en $X$ avec les conditions aux limites $X(0) = X(L) = 0$ n'admet de solutions non triviales que pour les valeurs propres :
$$
\lambda_n = \left(\frac{n\pi}{L}\right)^2, \quad X_n(x) = \sin\left(\frac{n\pi x}{L}\right), \quad n = 1, 2, 3, \dots
$$

L'équation en $T$ donne : $T_n(t) = e^{-\alpha^2 \lambda_n t} = e^{-\alpha^2 (n\pi/L)^2 t}$

**Étape 3 :** La solution générale est la **superposition** (somme infinie) :
$$
\boxed{u(x,t) = \sum_{n=1}^{\infty} b_n \sin\left(\frac{n\pi x}{L}\right) e^{-\alpha^2 (n\pi/L)^2 t}}
$$

**Étape 4 :** Les coefficients $b_n$ sont déterminés par la condition initiale $u(x,0) = f(x)$ :
$$
f(x) = \sum_{n=1}^{\infty} b_n \sin\left(\frac{n\pi x}{L}\right)
$$
Ce qui n'est rien d'autre que le **développement en série sinus de $f$ sur $[0, L]$** !
$$
\boxed{b_n = \frac{2}{L} \int_0^L f(x) \sin\left(\frac{n\pi x}{L}\right) dx}
$$

> 💡 **Interprétation physique :** Chaque harmonique $\sin(n\pi x/L)$ décroît exponentiellement avec le temps, et les hautes fréquences (grand $n$) disparaissent bien plus vite que les basses fréquences. La barre « oublie » rapidement sa forme initiale complexe pour ne garder que le mode fondamental $n=1$.

### 10. Démonstration Complète du Théorème de Dirichlet (Le Noyau de Dirichlet)

Cette démonstration est l'un des piliers mathématiques du cours. Elle procède en **4 étapes**.

#### 10.1. Étape 1 — La somme partielle comme convolution avec le noyau de Dirichlet

La somme partielle de la série de Fourier de $f$ peut se réécrire comme une intégrale :
$$
s_n(x) = \frac{1}{2\pi} \int_{-\pi}^{\pi} K_n(x - y) f(y) \, dy
$$
où $K_n$ est le **noyau de Dirichlet** :
$$
\boxed{K_n(\theta) = 1 + 2\sum_{k=1}^{n} \cos(k\theta) = \frac{\sin\left(\left(n + \frac{1}{2}\right)\theta\right)}{\sin\left(\frac{\theta}{2}\right)}}
$$

**Démonstration de la formule fermée :** On utilise la somme géométrique en exponentielles complexes :
$$
K_n(\theta) = \sum_{k=-n}^{n} e^{ik\theta} = e^{-in\theta} \cdot \frac{e^{i(2n+1)\theta} - 1}{e^{i\theta} - 1}
$$
En multipliant numérateur et dénominateur par $e^{-i\theta/2}$ :
$$
= \frac{e^{i(n+1/2)\theta} - e^{-i(n+1/2)\theta}}{e^{i\theta/2} - e^{-i\theta/2}} = \frac{2i\sin\left((n+\frac{1}{2})\theta\right)}{2i\sin(\theta/2)} = \frac{\sin\left((n+\frac{1}{2})\theta\right)}{\sin(\theta/2)}
$$

#### 10.2. Étape 2 — Propriétés du noyau de Dirichlet

Le noyau $K_n$ possède trois propriétés fondamentales :
1. $K_n$ est **périodique** de période $2\pi$.
2. $\int_{-\pi}^{\pi} K_n(\theta) \, d\theta = 2\pi$ (intégrer la somme finie terme à terme).
3. Quand $n$ est grand, $K_n$ se concentre de plus en plus autour de $\theta = 0$ : c'est un « pic » qui isole la valeur locale de $f$.

#### 10.3. Étape 3 — L'erreur de troncature via l'inégalité de Bessel

On écrit l'erreur sous la forme d'un produit scalaire :
$$
s_n(x) - f(x) = \frac{1}{2\pi} \int_{-\pi}^{\pi} \frac{f(x+\theta) - f(x)}{\sin(\theta/2)} \cdot \sin\left(\left(n + \frac{1}{2}\right)\theta\right) d\theta = \frac{1}{2\pi}\langle g, \varphi_n \rangle
$$
où $g(\theta) = \frac{f(x+\theta) - f(x)}{\sin(\theta/2)}$ et $\varphi_n(\theta) = \sin\left((n + \frac{1}{2})\theta\right)$.

Les fonctions $\{\varphi_n\}$ forment un **système orthogonal** sur $[-\pi, \pi]$ avec $\|\varphi_n\|^2 = \pi$. Par l'inégalité de Bessel :
$$
\sum_{n=1}^{\infty} \frac{|\langle g, \varphi_n \rangle|^2}{\|\varphi_n\|^2} \leq \|g\|^2 < +\infty
$$
Si $\|g\| < +\infty$ (ce qui est le point de l'étape 4), alors le terme général tend vers zéro, donc $s_n(x) - f(x) \to 0$.

#### 10.4. Étape 4 — La norme de $g$ est finie

Si $f \in C^1$, alors par la règle de L'Hôpital :
$$
\lim_{\theta \to 0} g(\theta) = \lim_{\theta \to 0} \frac{f(x + \theta) - f(x)}{\theta} \cdot \frac{\theta}{\sin(\theta/2)} = f'(x) \cdot 2
$$
Donc $g$ est prolongeable en une fonction **continue** sur $[-\pi, \pi]$, et sa norme $L^2$ est finie. CQFD.

**Généralisation :** Si $f$ et $f'$ sont seulement $C^0_{\text{morc}}$, on découpe l'intégrale en parties gauche et droite autour des discontinuités, avec deux fonctions $g^+$ et $g^-$, et on applique Bessel séparément sur chaque moitié.

### 11. Quantification du Phénomène de Gibbs

Au voisinage d'un saut de discontinuité d'amplitude $d = |f(x_0^+) - f(x_0^-)|$, le dépassement des sommes partielles est quantifié par :
$$
\lim_{n \to \infty} S_n\left(\frac{\pi}{n + 1/2}\right) = \frac{1}{2\pi} \int_{-\pi}^{\pi} \frac{\sin \theta}{\theta} d\theta \approx 0.5895
$$
Comme $f(x_0^+) = 0.5$ (pour un saut unitaire normalisé), le dépassement est $0.5895 - 0.5 = 0.0895$, soit environ **$9\%$ du saut**.

> ⚠️ Ce dépassement est **irréductible** : il ne diminue pas avec le nombre d'harmoniques. Il se comprime spatialement, mais l'amplitude reste constante. C'est une limitation fondamentale de la reconstruction de Fourier pour les signaux discontinus.

### 12. Prolongements Périodiques et Symétries

#### 12.1. Types de prolongements

Étant donnée une fonction $f$ définie sur $[0, L]$, on peut la prolonger de différentes manières sur $\mathbb{R}$ :

| Prolongement | Symétrie | Série résultante | Formule |
| :--- | :--- | :--- | :--- |
| **Pair** ($f_{\text{pair}}$) | $f(-x) = f(x)$ | Série **cosinus** | $f_{\text{pair}}(-x + 2nL) = f(x)$ |
| **Impair** ($f_{\text{imp}}$) | $f(-x) = -f(x)$ | Série **sinus** | $f_{\text{imp}}(-x + 2nL) = -f(x)$ |
| **Alternatif** | $f(x + L) = -f(x)$ | Série harmoniques **impaires** | Seuls les $a_{2k+1}, b_{2k+1}$ restent |

#### 12.2. Conséquence sur les coefficients

- Si $f$ est **paire** : $b_k = 0$ pour tout $k$ (la partie sinus disparaît).
- Si $f$ est **impaire** : $a_k = 0$ pour tout $k$ (la partie cosinus disparaît).
- Si $f$ est **alternative** (demi-période $L$) : $a_{2k} = b_{2k} = 0$ (les harmoniques paires s'annulent).

> 💡 **Astuce examen :** Avant de calculer quoi que ce soit, **vérifier d'abord la parité** de $f$. Si $f$ est paire ou impaire, la moitié des coefficients est automatiquement nulle, ce qui divise le travail de calcul par deux !

### 13. Démonstration de la Convergence Uniforme

#### 13.1. L'astuce de Cauchy-Schwarz pour la convergence absolue des coefficients

**Théorème :** Si $f$ est continue, $f'$ est $C^0_{\text{morc}}$, et $f(-\pi) = f(\pi)$ (continuité du prolongement périodique), alors les séries $\sum |a_k|$ et $\sum |b_k|$ convergent **absolument**.

**Démonstration :**
On sait (par les coefficients de la dérivée) que $|b_k(f)| = \frac{|a_k(f')|}{k}$.

Par Bessel, $\sum_{k=1}^{\infty} (a_k(f'))^2 \leq \|f'\|_2^2 < +\infty$ (car $f' \in L^2$).

L'astuce est d'utiliser **l'inégalité de Cauchy-Schwarz discrète** :
$$
\left(\sum_{k=1}^{n} |b_k(f)|\right)^2 = \left(\sum_{k=1}^{n} \frac{|a_k(f')|}{k}\right)^2 \leq \underbrace{\left(\sum_{k=1}^{n} (a_k(f'))^2\right)}_{\leq \|f'\|_2^2} \cdot \underbrace{\left(\sum_{k=1}^{n} \frac{1}{k^2}\right)}_{\leq \pi^2/6}
$$
Le produit est borné indépendamment de $n$, donc $\sum |b_k|$ converge.

#### 13.2. De la convergence absolue à la convergence uniforme (critère de Weierstrass)

Comme $|a_k \cos(kx)| \leq |a_k|$ et $|b_k \sin(kx)| \leq |b_k|$, et que $\sum |a_k| + \sum |b_k| < +\infty$, le **critère de Weierstrass** (test $M$) garantit la **convergence uniforme** de la série de Fourier.

### 14. Intégration terme à terme : Démonstration

**Théorème :** Si $f \in C^0_{\text{morc}}([-\pi, \pi])$ et $g(x) := f(x) - a_0/2$ (la version « nivelée » de $f$, de moyenne nulle), alors la primitive $G(x) = \int_{-\pi}^{x} g(t) dt$ admet pour coefficients de Fourier :
$$
\boxed{a_k(G) = -\frac{b_k(f)}{k}, \qquad b_k(G) = \frac{a_k(f)}{k}}
$$

**Démonstration (par intégration par parties) :**
$$
a_k(G) = \frac{1}{\pi}\int_{-\pi}^{\pi} G(t) \cos(kt) \, dt = \frac{1}{k\pi}\left[G(t)\sin(kt)\right]_{-\pi}^{\pi} - \frac{1}{k\pi}\int_{-\pi}^{\pi} g(t)\sin(kt) \, dt
$$
Le crochet vaut $0$ (car $\sin(k\pi) = 0$ toujours). Il reste $a_k(G) = -\frac{1}{k} b_k(f)$.

> 💡 **Règle mnémotechnique :** Intégrer une série de Fourier revient à **diviser les coefficients par $k$** et **permuter** sinus et cosinus. C'est l'opération inverse de la dérivation (qui multiplie par $k$).

### 15. Démonstration du Théorème de Convolution

**Théorème :** Si $f$ et $g$ sont périodiques de période $T$, intégrables et bornées, alors :
$$
c_k(f * g) = c_k(f) \cdot c_k(g)
$$

**Démonstration complète :**
$$
c_k(f * g) = \frac{1}{T}\int_{-T/2}^{T/2} (f * g)(x) \, e^{-ik\omega x} dx = \frac{1}{T}\int_{-T/2}^{T/2} \left(\frac{1}{T}\int_{-T/2}^{T/2} f(y)g(x-y) dy\right) e^{-ik\omega x} dx
$$
On sépare l'exponentielle : $e^{-ik\omega x} = e^{-ik\omega y} \cdot e^{-ik\omega(x-y)}$, puis on échange l'ordre d'intégration :
$$
= \frac{1}{T}\int_{-T/2}^{T/2} f(y) e^{-ik\omega y} \left(\frac{1}{T}\int_{-T/2}^{T/2} g(x-y) e^{-ik\omega(x-y)} dx\right) dy
$$
L'intégrale intérieure est $c_k(g)$ (car $g$ est périodique, le changement de variable $u = x - y$ ne change pas les bornes sur une période) :
$$
= \frac{1}{T}\int_{-T/2}^{T/2} f(y) e^{-ik\omega y} \cdot c_k(g) \, dy = c_k(f) \cdot c_k(g)
$$

> 💡 **Interprétation physique :** La convolution « mélange » les deux signaux dans le temps. L'analyse de Fourier transforme cette opération complexe en une simple multiplication fréquence par fréquence. C'est le fondement des filtres en traitement du signal : un filtre est un produit de convolution, et sa réponse fréquentielle est simplement $c_k(g)$.

### 16. Application : Résolution d'une EDL forcée périodiquement (Résonance)

#### 16.1. Le problème physique

Un système masse-ressort ($m, k$) sans amortissement est soumis à une force extérieure périodique $f(t)$ :
$$
my'' + ky = f(t)
$$
La force $f$ est impaire, de période $2$, et ses coefficients de Fourier sont $f_n = (-1)^{n+1} \frac{2}{n\pi}$.

#### 16.2. Résolution par identification des séries

On cherche $y$ périodique de même période. En écrivant $y(t) \sim \sum b_n \sin(n\pi t)$ et en dérivant deux fois terme à terme :
$$
\sum_{n=1}^{\infty} (-mn^2\pi^2 + k) b_n \sin(n\pi t) = \sum_{n=1}^{\infty} f_n \sin(n\pi t)
$$

Par identification des coefficients (les $\sin(n\pi t)$ sont orthogonaux) :
$$
b_n = \frac{f_n}{k - mn^2\pi^2} = \frac{(-1)^{n+1} \cdot 2}{n\pi(k - mn^2\pi^2)}
$$

#### 16.3. Le phénomène de résonance

Si $\sqrt{k/m}/\pi \in \mathbb{N}_0$ (c'est-à-dire si une fréquence propre du système coïncide avec une harmonique de la force), le dénominateur $k - mn^2\pi^2 = 0$ pour un certain $n$. Le coefficient $b_n$ **diverge** : il n'existe **aucune solution périodique**. C'est la **résonance** !

> ⚠️ **La résonance en physique :** Quand la force extérieure « pousse » exactement à la fréquence propre du système, l'énergie s'accumule sans limite et l'amplitude croît linéairement dans le temps (terme en $t\cos(\omega_0 t)$ au lieu de $\sin(\omega_0 t)$). C'est ce qui peut briser un pont, faire exploser un verre, ou détruire une machine industrielle.
