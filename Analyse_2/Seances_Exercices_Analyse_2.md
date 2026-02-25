# Séances d'Exercices — Analyse 2

---

## Séance 1 — Séries de Fourier (première partie)

> **Source :** MATH-H-2000 : Analyse II — Séance 1

### Rappels théoriques

Le développement de Fourier d'une fonction approxime celle-ci de façon globale sur un intervalle (ou sur $\mathbb{R}$ pour une fonction périodique). On travaille dans l'espace $L^2$ des fonctions de carré intégrable.

#### 🔑 Système classique / trigonométrique
Le développement pour une fonction de période $T$ est :
$$ S(x) = \frac{a_0}{2} + \sum_{k=1}^{\infty} \left( a_k \cos\left(\frac{2k\pi x}{T}\right) + b_k \sin\left(\frac{2k\pi x}{T}\right) \right) $$

Avec les coefficients :
$$ a_0 = \frac{2}{T} \int_0^T f(x)\, dx $$
$$ a_k = \frac{2}{T} \int_0^T f(x)\cos\left(\frac{2k\pi x}{T}\right)\, dx, \quad b_k = \frac{2}{T} \int_0^T f(x)\sin\left(\frac{2k\pi x}{T}\right)\, dx $$

#### 🔑 Parité et Simplifications
- **Fonction Paire** : $f(-x) = f(x) \implies b_k = 0$. Série de cosinus.
- **Fonction Impaire** : $f(-x) = -f(x) \implies a_k = 0$ (y compris $a_0 = 0$). Série de sinus.

#### 🔑 Convergence
- **Convergence Simple (Dirichlet)** : Si $f \in C^1_{pm}$, la série converge vers la régularisée $\tilde{f}(x) = \frac{f(x^+) + f(x^-)}{2}$.
- **Convergence Uniforme** : Si $f$ est continue, $f \in C^1_{pm}$, et $f(a) = f(b)$.
- **Convergence $L^2$ (Parseval)** : $\frac{1}{T} \int_0^T |f|^2 = \frac{a_0^2}{4} + \frac{1}{2} \sum (a_k^2 + b_k^2)$.

### Exercices résolus par type

---

#### Type 1 : Propriétés d'intégrales et Parité (Exercice 1)

**Méthode :** Utiliser le changement de variable $u = -x$ pour démontrer les propriétés de réduction d'intervalle.

**Exercice similaire :** 
Soit $g : \mathbb{R} \to \mathbb{R}$ et $L \in \mathbb{R}^*_0$.
a) Prouver que si $g$ est paire alors $\int_{-L}^L g(t)\, dt = 2 \int_0^L g(t)\, dt$.
b) Prouver que si $g$ est impaire alors $\int_{-L}^L g(t)\, dt = 0$.

<details>
<summary>Voir la résolution complète</summary>

$$ \int_{-L}^L g(t)\, dt = \int_{-L}^0 g(t)\, dt + \int_0^L g(t)\, dt $$
Dans la première intégrale, posons $t = -u \implies dt = -du$. Les bornes $-L$ et $0$ deviennent $L$ et $0$.
$$ \int_{-L}^0 g(t)\, dt = \int_L^0 g(-u)(-du) = \int_0^L g(-u)\, du $$

**a) Cas pair ($g(-u) = g(u)$) :**
$$ \int_{-L}^0 g(t)\, dt = \int_0^L g(u)\, du $$
D'où l'intégrale totale devient : $\int_0^L g + \int_0^L g = 2 \int_0^L g(t)\, dt$.

**b) Cas impair ($g(-u) = -g(u)$) :**
$$ \int_{-L}^0 g(t)\, dt = \int_0^L -g(u)\, du = -\int_0^L g(u)\, du $$
D'où l'intégrale totale s'annule : $-\int_0^L g + \int_0^L g = 0$.

</details>

---

#### Type 2 : Calcul avec période $T = \pi$ (Exercice 2)

**Méthode :** Adapter les pulsations au système $\{ \cos(2kx), \sin(2kx) \}$. Période $T=\pi$, donc on divise par $\pi/2$ (qui est $T/2$) et on intègre de $-\pi/2$ à $\pi/2$.

**Exercice similaire :** 
Soit $f(x) = x^3$ sur $[-\pi/2, \pi/2]$, prolongée par $\pi$-périodicité.  
a) Calculer sa série de Fourier classique.  
b) En déduire sa série de Fourier complexe.

<details>
<summary>Voir la résolution complète</summary>

**a) Système trigonométrique**
La fonction est **impaire**, donc $a_k = 0$ pour tout $k \ge 0$.
Le domaine est symétrique, la fonction $x^3 \sin(2kx)$ est paire (impaire $\times$ impaire = paire).
$$ b_k = \frac{2}{\pi/2} \int_0^{\pi/2} x^3 \sin(2kx)\, dx = \frac{4}{\pi} \int_0^{\pi/2} x^3 \sin(2kx)\, dx $$

Par IPP successives (Tableau) :
| Dériver | Intégrer |
|---|---|
| $x^3$ | $\sin(2kx)$ |
| $3x^2$ | $-\frac{1}{2k}\cos(2kx)$ |
| $6x$ | $-\frac{1}{4k^2}\sin(2kx)$ |
| $6$ | $\frac{1}{8k^3}\cos(2kx)$ |
| $0$ | $\frac{1}{16k^4}\sin(2kx)$ |

$$ = \frac{4}{\pi} \left[ -\frac{x^3}{2k}\cos(2kx) + \frac{3x^2}{4k^2}\sin(2kx) + \frac{6x}{8k^3}\cos(2kx) - \frac{6}{16k^4}\sin(2kx) \right]_0^{\pi/2} $$
En $0$, tout s'annule. En $\pi/2$, les termes en sinus s'annulent ($\sin(k\pi)=0$).
$$ = \frac{4}{\pi} \left( -\frac{\pi^3/8}{2k}(-1)^k + \frac{3\pi}{8k^3}(-1)^k \right) = \frac{4}{\pi} (-1)^k \left( -\frac{\pi^3}{16k} + \frac{3\pi}{8k^3} \right) $$

$$ \boxed{b_k = (-1)^k \left( -\frac{\pi^2}{4k} + \frac{3}{2k^3} \right)} $$

**b) Système complexe**
À partir d'Euler : $\sin(2kx) = \frac{e^{i2kx} - e^{-i2kx}}{2i}$.
En distribuant et en réindexant, on obtient la relation : $c_k = \frac{b_k}{2i} = -i \frac{b_k}{2}$.
$$ \boxed{c_k = -i \frac{(-1)^k}{2} \left( -\frac{\pi^2}{4k} + \frac{3}{2k^3} \right)} $$

</details>

---

#### Type 3 : Fonction valeur absolue et points de brisure (Exercice 3)

**Méthode :** Intégrer par parties sur le demi-domaine où $|x| = x$ grâce à la parité.

**Exercice similaire :** 
Soit $f(x) = |x|$ sur $]-\pi, \pi]$, $2\pi$-périodique. Calculer ses coefficients de Fourier trigonométriques, puis complexes.

<details>
<summary>Voir la résolution complète</summary>

**Système trigonométrique**
La fonction est **paire**, donc la série ne contient que des cosinus : $b_k = 0$.
Calcul du terme constant :
$$ a_0 = \frac{1}{\pi} \int_{-\pi}^\pi |x|\, dx = \frac{2}{\pi} \int_0^\pi x\, dx = \frac{2}{\pi} \left[\frac{x^2}{2}\right]_0^\pi = \pi $$
Calcul des $a_k$ (pour $k \ge 1$) :
$$ a_k = \frac{2}{\pi} \int_0^\pi x \cos(kx)\, dx $$
Par IPP ($u=x$, $v'=\cos(kx)$) :
$$ a_k = \frac{2}{\pi} \left( \left[x \frac{\sin(kx)}{k}\right]_0^\pi - \int_0^\pi \frac{\sin(kx)}{k}\, dx \right) $$
Le premier terme disparaît.
$$ a_k = \frac{2}{\pi} \left[ \frac{\cos(kx)}{k^2} \right]_0^\pi = \frac{2}{\pi} \frac{\cos(k\pi) - 1}{k^2} = \frac{2}{\pi} \frac{(-1)^k - 1}{k^2} $$
- Si $k$ est **pair**, $(-1)^k - 1 = 0 \implies a_{2m} = 0$.
- Si $k$ est **impair**, $(-1)^k - 1 = -2 \implies a_{2m+1} = -\frac{4}{\pi (2m+1)^2}$.

**Système complexe**
On sait que $a_k = c_k + c_{-k}$ et $b_k = i(c_k - c_{-k})$.
Ici, la fonction est paire donc réélle, $\implies c_k = c_{-k} = \frac{a_k}{2}$. Et $c_0 = \frac{a_0}{2}$.
$$ c_k = \frac{(-1)^k - 1}{\pi k^2} \quad (k \neq 0), \quad c_0 = \frac{\pi}{2} $$

</details>

---

#### Type 4 : Série complexe et passage au système trigonométrique (Exercice 4)

**Méthode :** Calculer directement $c_k$ et revenir aux coefficients $a_k$ et $b_k$.

**Exercice similaire :** 
Soit $f(x) = e^x$ sur $[-\pi, \pi[$, $2\pi$-périodique.

<details>
<summary>Voir la résolution complète</summary>

**Calcul des $c_k$**
$$ c_k = \frac{1}{2\pi} \int_{-\pi}^\pi e^x e^{-ikx}\, dx = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(1-ik)x}\, dx $$
$$ = \frac{1}{2\pi (1-ik)} \left[ e^{(1-ik)x} \right]_{-\pi}^\pi = \frac{1}{2\pi (1-ik)} \left( e^\pi e^{-ik\pi} - e^{-\pi} e^{ik\pi} \right) $$
Puisque $e^{ik\pi} = e^{-ik\pi} = (-1)^k$ :
$$ c_k = \frac{(-1)^k}{2\pi (1-ik)} (e^\pi - e^{-\pi}) = \frac{(-1)^k \sinh \pi}{\pi (1-ik)} $$
On multiplie par le conjugué pour obtenir la forme standard $a+ib$ :
$$ \boxed{c_k = \frac{(-1)^k \sinh \pi}{\pi} \frac{1+ik}{1+k^2}} $$

**Passage au trigonométrique**
- $a_k = c_k + c_{-k} = 2 \text{Re}(c_k) = \boxed{\frac{2(-1)^k \sinh \pi}{\pi(1+k^2)}}$
- $b_k = i(c_k - c_{-k}) = -2 \text{Im}(c_k) = \boxed{\frac{-2k(-1)^k \sinh \pi}{\pi(1+k^2)}}$

</details>

---


## Séance 2 — Séries de Fourier (seconde partie)

> **Source :** MATH-H-2000 : Analyse II — Séance 2, Titulaire : J. Roland

### Rappels théoriques

Cette séance s'attaque aux **questions de convergence** et à l'**extraction de sommes de séries numériques** à partir de séries de Fourier. C'est l'aboutissement opérationnel de toute la théorie.

---

#### 🔑 Formules de calcul des coefficients de Fourier

Pour $f$ une fonction $2\pi$-périodique et intégrable sur $[-\pi, \pi]$, son développement en série de Fourier est :

$$
f(x) \sim \frac{a_0}{2} + \sum_{k=1}^{\infty} \left( a_k \cos(kx) + b_k \sin(kx) \right)
$$

Avec les **coefficients de Fourier** :

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\, dx, \quad a_k = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\cos(kx)\, dx, \quad b_k = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\sin(kx)\, dx
$$

**Astuce parité :** Si $f$ est **paire**, $b_k = 0$ pour tout $k$. Si $f$ est **impaire**, $a_k = 0$ pour tout $k$.

---

#### 🔑 Théorème de Dirichlet — Convergence simple (pointwise)

Soit $f$ **continue par morceaux** (c.p.m.) et **de classe $C^1$ par morceaux** ($C^1_{pm}$) sur $[-\pi, \pi]$. Alors, pour tout $x$ :

$$
\boxed{S(x) = \frac{f(x^+) + f(x^-)}{2}}
$$

- Aux points de **continuité** : $S(x) = f(x)$.
- Aux points de **saut** (discontinuités) : $S(x) = $ moyenne des deux limites.
- En $x = \pi$ ou $x = -\pi$ (bords) : $S(\pi) = S(-\pi) = \frac{f(\pi^-) + f(-\pi^+)}{2}$.

---

#### 🔑 Convergence en moyenne quadratique (CMQ) et Égalité de Parseval

La série de Fourier converge **toujours** en $L^2$ pour toute fonction de carré intégrable. L'égalité de Parseval donne :

$$
\boxed{\frac{1}{\pi} \int_{-\pi}^{\pi} |f(x)|^2\, dx = \frac{a_0^2}{2} + \sum_{k=1}^{\infty} (a_k^2 + b_k^2)}
$$

**Utilisation :** En calculant $\int |f|^2$ d'un côté et la somme des carrés des coefficients de l'autre, on obtient des **sommes de séries numériques difficiles** (ex: $\sum 1/k^4$) gratuitement !

---

#### 🔑 Convergence uniforme (CU)

**Condition suffisante :** Si $f$ est continue sur $\mathbb{R}$ (en particulier, $f(-\pi) = f(\pi)$ pour que la fonction périodisée reste continue), et si $f$ est $C^1_{pm}$, alors la série de Fourier converge **uniformément** vers $f$.

$$
\text{CU} \implies \text{CS} \quad \text{et} \quad \text{CU} \implies \text{CMQ}
$$

Vitesse de convergence : les coefficients décroissent d'autant plus vite que $f$ est régulière.
- $f$ continue, $C^1$ par morceaux : $|a_k|, |b_k| = O(1/k)$ → CU.
- $f$ de classe $C^p$ par morceaux : $|a_k|, |b_k| = O(1/k^p)$.

---

#### 🔑 Intégration par parties (IBP) — formule standard

Pour calculer $\int x^n \cos(kx)\, dx$ (ou $\sin$), utiliser les IBP successives. La formule tableaux-croisés est très efficace :

| Dériver | Intégrer |
|---|---|
| $x^2$ | $\cos(kx)$ |
| $2x$ | $\frac{1}{k}\sin(kx)$ |
| $2$ | $-\frac{1}{k^2}\cos(kx)$ |
| $0$ | $-\frac{1}{k^3}\sin(kx)$ |

Donc : $\int x^2 \cos(kx)\,dx = \frac{x^2}{k}\sin(kx) + \frac{2x}{k^2}\cos(kx) - \frac{2}{k^3}\sin(kx) + C$.

**La formule clé :** $\int_{-\pi}^{\pi} x^2 \cos(kx)\, dx = \left[\frac{x^2}{k}\sin(kx) + \frac{2x}{k^2}\cos(kx) - \frac{2}{k^3}\sin(kx)\right]_{-\pi}^{\pi}$.

Comme $\sin(k\pi) = \sin(-k\pi) = 0$, il reste uniquement les termes en $\cos(k\pi) = (-1)^k$ :
$$= \frac{2\pi}{k^2}(-1)^k - \frac{(-2\pi)}{k^2}(-1)^k = \frac{4\pi(-1)^k}{k^2}$$

---

### Exercices résolus par type

---

#### Type 1 : Calcul des coefficients de Fourier et évaluation de séries numériques (Exercice 1)

**Méthode :** Calculer $a_k$ et $b_k$ par intégration par parties. Utiliser Dirichlet pour évaluer la série en des points stratégiques ($x=0$, $x=\pi$) pour en déduire des sommes comme $\sum (-1)^k/k^2$ ou $\sum 1/k^2$.

**Exercice similaire :**
Soit $g : \mathbb{R} \to \mathbb{R}$ la fonction $2\pi$-périodique telle que $g(x) = x^2$ pour $x \in [-\pi, \pi[$.

a) Calculer le développement en série de Fourier classique de $g$.  
b) Étudier la convergence simple.  
c) En évaluant en $x = 0$ et $x = \pi$, calculer $\displaystyle\sum_{k=1}^{\infty} \frac{(-1)^k}{k^2}$ et $\displaystyle\sum_{k=1}^{\infty} \frac{1}{k^2}$.  
d) Utiliser Parseval pour calculer $\displaystyle\sum_{k=1}^{\infty} \frac{1}{k^4}$.

<details>
<summary>Voir la résolution complète</summary>

##### Étape 1 : Calcul des coefficients

**Calcul de $a_0$ :**
$$a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} x^2\, dx = \frac{1}{\pi} \cdot \frac{2\pi^3}{3} = \frac{2\pi^2}{3}$$

**Calcul de $a_k$ ($k \ge 1$) :**

$g(x) = x^2$ est une fonction **paire**, donc $b_k = 0$ pour tout $k$.

Pour $a_k$, on utilise les intégrations par parties en tableau :

$$a_k = \frac{1}{\pi}\int_{-\pi}^{\pi} x^2 \cos(kx)\, dx = \frac{2}{\pi}\int_{0}^{\pi} x^2 \cos(kx)\, dx \quad \text{(parité de } x^2\cos(kx)\text{)}$$

IBP croisée :

$$\int_0^{\pi} x^2 \cos(kx)\, dx = \left[\frac{x^2 \sin(kx)}{k}\right]_0^{\pi} - \frac{2}{k}\int_0^{\pi} x\sin(kx)\, dx$$

Le premier terme vaut $0$ car $\sin(k\pi)=0$. Pour le second :

$$\int_0^{\pi} x\sin(kx)\, dx = \left[-\frac{x\cos(kx)}{k}\right]_0^{\pi} + \frac{1}{k}\int_0^{\pi}\cos(kx)\, dx = -\frac{\pi(-1)^k}{k} + \frac{[\sin(kx)]_0^{\pi}}{k^2} = \frac{-\pi(-1)^k}{k}$$

Donc :
$$\int_0^{\pi} x^2 \cos(kx)\, dx = -\frac{2}{k} \cdot \frac{-\pi(-1)^k}{k} = \frac{2\pi(-1)^k}{k^2}$$

Et finalement :
$$\boxed{a_k = \frac{2}{\pi} \cdot \frac{2\pi(-1)^k}{k^2} = \frac{4(-1)^k}{k^2}}$$

**Série de Fourier :**
$$g(x) \sim \frac{\pi^2}{3} + \sum_{k=1}^{\infty} \frac{4(-1)^k}{k^2} \cos(kx)$$

---

##### Étape 2 : Convergence simple

$g(x) = x^2$ est continue sur $\mathbb{R}$ ? Attention : $g$ est $2\pi$-périodique, et $g(-\pi) = \pi^2$, $g(\pi^-) = \pi^2$. La périodisation est **continue** (pas de saut).

De plus, $g$ est $C^1$ par morceaux. Par Dirichlet, la série converge **simplement** vers $g(x)$ pour **tout** $x \in \mathbb{R}$ :

$$\forall x \in \mathbb{R}: \quad \frac{\pi^2}{3} + \sum_{k=1}^{\infty} \frac{4(-1)^k}{k^2} \cos(kx) = x^2 \quad \text{cf. ci-dessous}$$

---

##### Étape 3 : Évaluation de séries numériques

**En $x = \pi$ :** $\cos(k\pi) = (-1)^k$, donc :
$$\frac{\pi^2}{3} + \sum_{k=1}^{\infty} \frac{4(-1)^k}{k^2}(-1)^k = \pi^2$$
$$\frac{\pi^2}{3} + 4\sum_{k=1}^{\infty} \frac{1}{k^2} = \pi^2$$
$$\sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2 - \pi^2/3}{4} = \boxed{\frac{\pi^2}{6}}$$

**En $x = 0$ :** $\cos(0) = 1$, $g(0) = 0$ :
$$\frac{\pi^2}{3} + \sum_{k=1}^{\infty} \frac{4(-1)^k}{k^2} = 0$$
$$\sum_{k=1}^{\infty} \frac{(-1)^k}{k^2} = \boxed{-\frac{\pi^2}{12}}$$

---

##### Étape 4 : Parseval pour $\sum 1/k^4$

On calcule les deux membres de l'égalité de Parseval :

**Membre gauche :**
$$\frac{1}{\pi}\int_{-\pi}^{\pi} x^4\, dx = \frac{1}{\pi} \cdot \frac{2\pi^5}{5} = \frac{2\pi^4}{5}$$

**Membre droit :**
$$\frac{a_0^2}{2} + \sum_{k=1}^{\infty} a_k^2 = \frac{(2\pi^2/3)^2}{2} + \sum_{k=1}^{\infty} \frac{16}{k^4} = \frac{2\pi^4}{9} + 16\sum_{k=1}^{\infty} \frac{1}{k^4}$$

En égalant :
$$\frac{2\pi^4}{5} = \frac{2\pi^4}{9} + 16\sum_{k=1}^{\infty} \frac{1}{k^4}$$
$$16\sum_{k=1}^{\infty} \frac{1}{k^4} = 2\pi^4\left(\frac{1}{5} - \frac{1}{9}\right) = 2\pi^4 \cdot \frac{4}{45} = \frac{8\pi^4}{45}$$
$$\boxed{\sum_{k=1}^{\infty} \frac{1}{k^4} = \frac{\pi^4}{90}}$$

</details>

---

#### Type 2 : Série de Fourier d'une exponentielle et exploitation aux points de discontinuité (Exercice 2)

**Méthode :** Calculer $a_k$ et $b_k$ par IPP pour $f(x) = e^x$. Identifier les points de discontinuité de la périodisation (à $x = 0$ et $x = 2\pi$). Utiliser Dirichlet pour les évaluations en des points stratégiques.

**Exercice similaire :**
Soit $h : \mathbb{R} \to \mathbb{R}$ la fonction $2\pi$-périodique définie par $h(x) = e^x$ pour $x \in [0, 2\pi[$.

a) Développer $h$ en série de Fourier dans le système trigonométrique (form. $\frac{a_0}{2} + \sum a_k\cos + b_k\sin$).  
b) Étudier la convergence simple (attention aux points de discontinuité !).  
c) Calculer $\displaystyle\sum_{k=1}^{\infty} \frac{(-1)^k}{1+k^2}$ et $\displaystyle\sum_{k=1}^{\infty} \frac{1}{1+k^2}$.  
d) Étudier la convergence uniforme.

<details>
<summary>Voir la résolution complète</summary>

##### Étape 1 : Calcul des coefficients

$h$ est définie sur $[0, 2\pi[$, donc on intègre sur cet intervalle (et non $[-\pi, \pi]$). La formule reste valable grâce à la $2\pi$-périodicité.

**Calcul de $a_0$ :**
$$a_0 = \frac{1}{\pi}\int_0^{2\pi} e^x\, dx = \frac{1}{\pi}\left[e^x\right]_0^{2\pi} = \frac{e^{2\pi} - 1}{\pi}$$

**Calcul de $a_k$ ($k \ge 1$) :**

On utilise l'IPP (ou la formule complexe pour aller plus vite) :
$$a_k = \frac{1}{\pi}\int_0^{2\pi} e^x\cos(kx)\, dx$$

On utilise : $\text{Re}\left(\int_0^{2\pi} e^x e^{ikx}\, dx\right) = \text{Re}\left(\int_0^{2\pi} e^{(1+ik)x}\, dx\right)$

$$\int_0^{2\pi} e^{(1+ik)x}\, dx = \left[\frac{e^{(1+ik)x}}{1+ik}\right]_0^{2\pi} = \frac{e^{2\pi(1+ik)} - 1}{1+ik} = \frac{e^{2\pi}e^{2\pi ik} - 1}{1+ik}$$

Or $e^{2\pi ik} = \cos(2\pi k) + i\sin(2\pi k) = 1$ pour $k \in \mathbb{Z}$. Donc :

$$\int_0^{2\pi} e^{(1+ik)x}\, dx = \frac{e^{2\pi} - 1}{1+ik} = \frac{(e^{2\pi}-1)(1-ik)}{1+k^2}$$

En prenant partie réelle et imaginaire :

$$a_k = \frac{1}{\pi}\text{Re}\left(\frac{(e^{2\pi}-1)(1-ik)}{1+k^2}\right) = \boxed{\frac{e^{2\pi}-1}{\pi(1+k^2)}}$$

$$b_k = \frac{1}{\pi}\text{Im}\left(\frac{(e^{2\pi}-1)(1-ik)}{1+k^2}\right) \cdot (-1) = \frac{1}{\pi} \cdot \frac{(e^{2\pi}-1) \cdot k}{1+k^2}$$

Attention au signe : Im$\left(\frac{e^{2\pi}-1}{1+ik}\right) = \text{Im}\left(\frac{(e^{2\pi}-1)(1-ik)}{1+k^2}\right) = \frac{-k(e^{2\pi}-1)}{1+k^2}$

Et comme $\int e^x \sin(kx) = \text{Im}(\int e^{(1+ik)x})$, il faut prendre la partie imaginaire de l'intégrale :

$$b_k = \frac{1}{\pi} \cdot \frac{-k(e^{2\pi}-1)}{1+k^2} \quad \Longrightarrow \quad \boxed{b_k = \frac{-(e^{2\pi}-1)k}{\pi(1+k^2)}}$$

**Série de Fourier :**
$$h(x) \sim \frac{e^{2\pi}-1}{2\pi} + \sum_{k=1}^{\infty} \frac{e^{2\pi}-1}{\pi(1+k^2)}\left(\cos(kx) - k\sin(kx)\right)$$

---

##### Étape 2 : Convergence simple

La fonction $h(x) = e^x$ sur $[0, 2\pi[$ est continue et de classe $C^1$ sur l'intervalle ouvert. Mais la **périodisation** crée une discontinuité : 

- $h(0^+) = e^0 = 1$
- $h(0^-) = h(2\pi - 0^+) = e^{2\pi}$ (limite à gauche de $0$ dans la période précédente)

Il y a donc un **saut** en $x = 0$ (et ses translatés $x = 2k\pi$).

Par le théorème de Dirichlet :
- En $x \neq 2k\pi$ : $S(x) = h(x) = e^x$.
- En $x = 0$ (point de saut) : $S(0) = \dfrac{h(0^+) + h(0^-)}{2} = \dfrac{1 + e^{2\pi}}{2}$.

---

##### Étape 3 : Évaluation de séries numériques

**En $x = 0$ (point de discontinuité — la série converge vers la moyenne) :**

$$S(0) = \frac{1+e^{2\pi}}{2} = \frac{e^{2\pi}-1}{2\pi} + \sum_{k=1}^{\infty} \frac{e^{2\pi}-1}{\pi(1+k^2)}\left(\cos(0) - k\sin(0)\right)$$

$$\frac{1+e^{2\pi}}{2} = \frac{e^{2\pi}-1}{2\pi} + \frac{e^{2\pi}-1}{\pi}\sum_{k=1}^{\infty} \frac{1}{1+k^2}$$

On isole la somme :
$$\sum_{k=1}^{\infty} \frac{1}{1+k^2} = \frac{\pi}{e^{2\pi}-1}\left(\frac{1+e^{2\pi}}{2} - \frac{e^{2\pi}-1}{2\pi}\right)$$

$$= \frac{\pi}{e^{2\pi}-1} \cdot \frac{\pi(1+e^{2\pi}) - (e^{2\pi}-1)}{2\pi}$$

$$= \frac{1}{2(e^{2\pi}-1)}\left[\pi(1+e^{2\pi}) - (e^{2\pi}-1)\right]$$

$$\boxed{\sum_{k=1}^{\infty} \frac{1}{1+k^2} = \frac{\pi(e^{2\pi}+1) - (e^{2\pi}-1)}{2(e^{2\pi}-1)} = \frac{\pi \coth(\pi) - 1}{2}}$$

**En $x = \pi$ (point de continuité) :**

$h(\pi) = e^{\pi}$, $\cos(k\pi) = (-1)^k$, $\sin(k\pi) = 0$ :

$$e^{\pi} = \frac{e^{2\pi}-1}{2\pi} + \frac{e^{2\pi}-1}{\pi}\sum_{k=1}^{\infty} \frac{(-1)^k}{1+k^2}$$

On isole :
$$\sum_{k=1}^{\infty} \frac{(-1)^k}{1+k^2} = \frac{\pi e^{\pi}}{e^{2\pi}-1} - \frac{1}{2} = \frac{\pi}{e^{\pi}-e^{-\pi}} - \frac{1}{2} = \boxed{\frac{\pi}{2\sinh(\pi)} - \frac{1}{2}}$$

---

##### Étape 4 : Convergence uniforme

La périodisation de $h$ est **discontinue** en $x = 2k\pi$ (saut de $e^{2\pi} - 1$). Une condition **nécessaire** pour la convergence uniforme est que la série converge vers une fonction continue. La somme $S(x)$ est discontinue en $2k\pi$ donc :

$$\boxed{\text{La série de Fourier de } h \text{ ne converge pas uniformément.}}$$

De plus, on observe le phénomène de Gibbs à ces discontinuités ($\approx 9\%$ de dépassement irréductible).

</details>

---

#### Type 3 : Implication CU ⟹ CMQ — démonstration formelle (Exercice 3)

**Méthode :** Exploiter la définition de la convergence uniforme pour contrôler l'intégrale $L^2$ (norme quadratique). L'idée est de majorer l'intégrale par le sup, qui tend vers 0 par CU.

**Exercice similaire :**
Soit $f$ définie sur $[a,b]$ avec $a, b \in \mathbb{R}^*$ et $a < b$. Montrer que si la série de Fourier $S(x)$ converge uniformément vers $f(x)$, alors $S(x)$ converge aussi en moyenne quadratique vers $f$.

<details>
<summary>Voir la résolution complète</summary>

**Définitions rappelées :**

- **Convergence uniforme** : $S_N(x) \xrightarrow[N\to\infty]{C.U.} f(x)$ signifie que :
$$\sup_{x \in [a,b]} |S_N(x) - f(x)| \xrightarrow{N \to \infty} 0$$

On note $M_N = \sup_{x \in [a,b]} |S_N(x) - f(x)|$, donc $M_N \to 0$.

- **Convergence en moyenne quadratique** : On doit montrer que :
$$\|S_N - f\|_{L^2}^2 = \int_a^b |S_N(x) - f(x)|^2\, dx \xrightarrow{N \to \infty} 0$$

**Démonstration :**

On majore l'intégrale $L^2$ en utilisant la borne uniforme $M_N$ :

$$\int_a^b |S_N(x) - f(x)|^2\, dx \leq \int_a^b \sup_{t \in [a,b]}|S_N(t) - f(t)|^2\, dx$$

$$= \int_a^b M_N^2\, dx = M_N^2 \cdot (b-a)$$

Donc :
$$0 \leq \|S_N - f\|_{L^2}^2 \leq M_N^2 \cdot (b-a)$$

Or la convergence uniforme implique $M_N \to 0$, donc $M_N^2 \cdot (b-a) \to 0$.

Par le **théorème des gendarmes** :

$$\boxed{\|S_N - f\|_{L^2}^2 \to 0 \quad \text{i.e., } S_N \xrightarrow{L^2} f \quad \square}$$

**Remarque importante :** La réciproque est **fausse**. La CMQ n'implique pas la CU. Un exemple classique : les fonctions $f_n(x) = x^n$ sur $[0,1]$ convergent en $L^2$ vers $0$, mais pas uniformément (car $f_n(1) = 1$ pour tout $n$).

**Interprétation géométrique :** La CU dit que toutes les erreurs $|S_N(x) - f(x)|$ sont petites simultanément (inégalité uniforme). La norme $L^2$ mesure une énergie globale. Si l'erreur est partout petite (petite uniforme), l'énergie totale est aussi petite — mais pas forcément si l'erreur n'est grande que sur un petit ensemble (ce que permet la CMQ).

</details>

---

---


---

## Séance 3 — Séries de Fourier généralisées (Gram-Schmidt, Legendre, Tchebychev)

> **Source :** MATH-H-2000 : Analyse II — Séance 3, Titulaire : J. Roland

### Rappels théoriques

#### 🔑 Espace préhilbertien — Rappels fondamentaux

Un **espace préhilbertien** est un espace vectoriel $E$ muni d'un produit scalaire $\langle \cdot, \cdot \rangle_E$.

| Notion | Définition |
|---|---|
| **Norme** | $\|\vec{x}\|_E = \sqrt{\langle \vec{x}, \vec{x} \rangle_E}$ |
| **Orthogonalité** | $\vec{x} \perp \vec{y} \iff \langle \vec{x}, \vec{y} \rangle_E = 0$ |
| **Système complet** | $\sum c_k \vec{e}_k \overset{E}{=} \vec{x}$ avec $c_k = \frac{\langle \vec{e}_k, \vec{x} \rangle}{\|\vec{e}_k\|^2}$ |
| **Projection orthogonale** | $\text{proj}_V(\vec{x}) = \sum_{k} \frac{\langle \vec{e}_k, \vec{x} \rangle}{\|\vec{e}_k\|^2} \vec{e}_k$ |

---

#### 🔑 Algorithme de Gram-Schmidt

À partir d'une base quelconque $(s_0, s_1, \ldots, s_n)$, on construit une base **orthonormée** $(e_0, e_1, \ldots, e_n)$ :

1. $e_0 = \frac{s_0}{\|s_0\|}$

2. Pour $k \geq 1$ :

$$v_k = s_k - \sum_{j=0}^{k-1} \langle s_k, e_j \rangle\, e_j$$

$$e_k = \frac{v_k}{\|v_k\|}$$

**Principe :** On retire de $s_k$ la composante déjà couverte par les vecteurs orthogonalisés précédents.

---

#### 🔑 Polynômes de Legendre sur $L^2([-1,1])$

Produit scalaire : $\langle f, g \rangle = \int_{-1}^1 f(x)g(x)\,dx$

$$P_0 = 1,\quad P_1 = x,\quad P_2 = \tfrac{1}{2}(3x^2-1),\quad P_3 = \tfrac{1}{2}(5x^3-3x)$$

Orthogonalité : $\langle P_k, P_j \rangle = \frac{2}{2k+1}\delta_{kj}$

Meilleure approximation $L^2$ de $f$ par un polynôme de degré $\leq n$ :

$$P^* = \sum_{k=0}^n \frac{\langle f, P_k \rangle}{\|P_k\|^2} P_k$$

---

#### 🔑 Polynômes de Tchebychev — produit scalaire pondéré

Produit scalaire : $\langle f, g \rangle_p = \int_{-1}^1 \dfrac{f(x)g(x)}{\sqrt{1-x^2}}\,dx$

$$T_n(x) = \cos(n \arccos x),\quad T_0=1,\; T_1=x,\; T_2=2x^2-1,\; T_3=4x^3-3x$$

**Changement de variable clé :** $x = \cos\theta \Rightarrow \langle T_m, T_n \rangle_p = \int_0^\pi \cos(m\theta)\cos(n\theta)\,d\theta$

Orthogonalité : $\|T_0\|_p^2 = \pi$, $\|T_k\|_p^2 = \pi/2$ pour $k \geq 1$.

---

### Exercices résolus par type

---

#### Type 1 : Gram-Schmidt avec produit scalaire classique $L^2([-1,1])$ (Exercice 1 & 2)

**Méthode :** Calculer $\langle s_i, s_j \rangle = \int_{-1}^1 x^{i+j}\,dx$. Appliquer Gram-Schmidt étape par étape.

**Exercice similaire :**
Appliquer Gram-Schmidt à $(s_0, s_1, s_2) = (1, x, x^2)$ dans $L^2([-1,1])$ et reconnaître les polynômes de Legendre.

<details>
<summary>Voir la résolution complète</summary>

**Étape $e_0$ à partir de $s_0 = 1$ :**

$\|1\|^2 = \int_{-1}^1 1\,dx = 2$, donc $e_0 = \dfrac{1}{\sqrt{2}}$.

**Étape $e_1$ à partir de $s_1 = x$ :**

$\langle x, e_0\rangle = \int_{-1}^1 \dfrac{x}{\sqrt{2}}\,dx = 0$ (intégrale d'une impaire sur $[-1,1]$).

$v_1 = x$. $\|x\|^2 = \int_{-1}^1 x^2\,dx = \dfrac{2}{3}$, donc $e_1 = \sqrt{\dfrac{3}{2}}\,x$.

**Étape $e_2$ à partir de $s_2 = x^2$ :**

$\langle x^2, e_0\rangle = \dfrac{1}{\sqrt{2}}\cdot\dfrac{2}{3} = \dfrac{\sqrt{2}}{3}$ ; $\langle x^2, e_1\rangle = \sqrt{\dfrac{3}{2}}\int_{-1}^1 x^3\,dx = 0$ (impaire).

$v_2 = x^2 - \dfrac{\sqrt{2}}{3}\cdot\dfrac{1}{\sqrt{2}} = x^2 - \dfrac{1}{3}$

$\|v_2\|^2 = \int_{-1}^1 \left(x^2-\dfrac{1}{3}\right)^2 dx = \dfrac{2}{5}-\dfrac{4}{9}+\dfrac{2}{9} = \dfrac{8}{45}$

$e_2 = \sqrt{\dfrac{45}{8}}\left(x^2-\dfrac{1}{3}\right) = \sqrt{\dfrac{5}{2}}\cdot\dfrac{3x^2-1}{2} = \sqrt{\dfrac{5}{2}}\,P_2(x)$

On retrouve bien $P_2$ (normalisé) à facteur près d'accord avec $\|P_2\|^2 = 2/5$.

</details>

---

#### Type 2 : Meilleure approximation $L^2$ par Legendre (Exercice 2c)

**Méthode :** Calculer les projections de $f(x) = |x|$ sur chaque $P_k$. Utiliser la parité pour éliminer les termes impairs.

**Exercice similaire :**
Trouver le polynôme de degré $\leq 3$ minimisant $\|\,|x| - P\|_2$ sur $[-1,1]$ par projection sur les $P_k$.

<details>
<summary>Voir la résolution complète</summary>

$|x|$ est **paire** $\Rightarrow$ projections sur $P_1, P_3$ (impairs) nulles : $c_1 = c_3 = 0$.

**$c_0$ :** $\langle |x|, P_0\rangle = \int_{-1}^1|x|\,dx = 1$. $\|P_0\|^2 = 2 \Rightarrow c_0 = \tfrac{1}{2}$.

**$c_2$ :** $\langle |x|, P_2\rangle = \int_{-1}^1 |x|\,\tfrac{3x^2-1}{2}\,dx = \int_0^1(3x^3-x)\,dx = \tfrac{3}{4}-\tfrac{1}{2} = \tfrac{1}{4}$.

$\|P_2\|^2 = \tfrac{2}{5} \Rightarrow c_2 = \tfrac{5}{8}$.

**Résultat :**

$$P^*(x) = \frac{1}{2} + \frac{5}{8}\cdot\frac{3x^2-1}{2} = \frac{3}{16} + \frac{15x^2}{16}$$

</details>

---

#### Type 3 : Gram-Schmidt avec poids Tchebychev (Exercice 4)

**Méthode :** Substitution $x = \cos\theta$ pour transformer les intégrales en intégrales trigonométriques. Reconnaître les $T_n(\cos\theta) = \cos(n\theta)$.

**Exercice similaire :**
Calculer $\langle s_i, s_j\rangle_p$ avec $s_k(x)=x^k$. En déduire que les $T_n$ forment une base orthogonale dans $L^2_p([-1,1])$ et approcher $|x|$ par une combinaison de $T_0, T_1, T_2, T_3$.

<details>
<summary>Voir la résolution complète</summary>

**Intégrales avec $x = \cos\theta$ :**

$\langle s_i, s_j\rangle_p = \int_0^\pi \cos^{i+j}\theta\,d\theta$

Pour $i+j$ impair : $= 0$ (cosinus impair intégré sur $[0,\pi]$).

Pour $i+j$ pair : formule donnée avec les binomiaux.

**Orthogonalité des $T_n$ :** $\langle T_m, T_n\rangle_p = \int_0^\pi \cos(m\theta)\cos(n\theta)\,d\theta = \begin{cases} \pi & m=n=0 \\ \pi/2 & m=n\geq 1 \\ 0 & m\neq n \end{cases}$

**Approximation de $|x|$ :**

$b_0 = \tfrac{1}{\pi}\cdot 2\int_0^{\pi/2}\cos\theta\,d\theta = \tfrac{2}{\pi}$

$b_1 = \tfrac{2}{\pi}\int_{-1}^1\frac{x|x|}{\sqrt{1-x^2}}\,dx = 0$ (impaire)

$b_2 = \tfrac{2}{\pi}\int_0^\pi |\cos\theta|\cos(2\theta)\,d\theta = \tfrac{4}{\pi}\int_0^{\pi/2}\cos\theta(2\cos^2\theta-1)\,d\theta = \tfrac{4}{\pi}\cdot\tfrac{\pi}{8} = \tfrac{1}{2}$

$b_3 = 0$ (impaire)

$$Q^*(x) = \frac{2}{\pi} + \frac{1}{2}(2x^2-1) = x^2 + \frac{2}{\pi} - \frac{1}{2}$$

</details>

---

## Séance 4 — Problèmes aux limites

> **Source :** MATH-H-2000 : Analyse II — Séance 4, Titulaire : J. Roland

### Rappels théoriques

#### 🔑 Définition — Problème aux limites (PAL)

Un **problème aux limites** (PAL) d'ordre $n$ sur $[a,b]$ est de la forme :

$$
\begin{cases} Ly = f \\ \text{cl}_1(y) = c_1 \\ \vdots \\ \text{cl}_n(y) = c_n \end{cases}
$$

où $L$ est un opérateur différentiel linéaire d'ordre $n$, et les **conditions aux limites** $\text{cl}_i(y)$ sont des combinaisons linéaires des valeurs de $y, y', \ldots, y^{(n-1)}$ aux bords $a$ et $b$ :

$$
\text{cl}_i(y) = \alpha_{i0} y(a) + \cdots + \alpha_{i(n-1)} y^{(n-1)}(a) + \beta_{i0} y(b) + \cdots + \beta_{i(n-1)} y^{(n-1)}(b)
$$

> ⚠️ **Différence cruciale avec le problème de Cauchy :** Dans un Cauchy, toutes les conditions sont en $x_0$ (instant initial) → solution unique garantie. Dans un PAL, les conditions sont réparties sur deux bords → peut avoir 0, 1 ou ∞ solutions.

---

#### 🔑 Théorème de l'alternative (critère d'unicité)

> Un PAL non-homogène ($Ly = f$) est **bien posé** (= admet une unique solution) **si et seulement si** le PAL homogène associé ($Ly = 0$, mêmes conditions aux limites) n'admet que la **solution triviale** $y = 0$.

**Stratégie pour résoudre un PAL :**
1. Résoudre l'EDO $Ly = f$ pour trouver la **solution générale** $y = y_h + y_p$ (homogène + particulière).
2. Appliquer les conditions aux limites au système linéaire obtenu sur les constantes $C_1, C_2, \ldots$ de la solution générale.
3. Étudier si ce système a : une solution unique (bien posé), aucune solution (incompatible), ou infinité de solutions (mal posé).

---

#### 🔑 Valeurs propres et fonctions propres d'un PAL

Pour un PAL **homogène** dépendant d'un paramètre $\lambda$ :

$$
\begin{cases} Ly = \lambda y \\ \text{cl}_i(y) = 0,\quad i = 1,\ldots,n \end{cases}
$$

- **Valeur propre** $\lambda$ : valeur pour laquelle le PAL admet une solution non triviale.
- **Fonction propre** $y$ : solution non triviale associée à $\lambda$.

**Méthode :** Chercher la solution générale de $Ly = \lambda y$ (3 cas selon le signe de $\lambda$), puis appliquer les CL et chercher quelles valeurs de $\lambda$ permettent une solution non nulle (déterminant du système = 0).

---

#### 🔑 Équations de Cauchy-Euler ($x^n y^{(n)} + \ldots$)

Pour des EDO du type $x^2 y'' + bxy' + cy = f(x)$, utiliser le changement de variable $x = e^t$ (ou $t = \ln x$). L'équation devient une EDO à coefficients constants en $t$.

---

### Exercices résolus par type

---

#### Type 1 : Résolution d'un PAL avec EDO d'ordre 2 à seconds membres (Exercice 1a)

**Méthode :** Résolution complète en 3 étapes : (1) solution homogène, (2) solution particulière (variation de paramètre ou identification), (3) système linéaire pour les constantes via les CL.

**Exercice similaire d'après (1a) :**
$$
\begin{cases} y'' + y = -3\sin 2x \\ y(0) = 1 \\ y'(\pi) = 1 \end{cases}
$$

<details>
<summary>Voir la résolution complète</summary>

**Étape 1 : Solution homogène de $y'' + y = 0$**

Équation caractéristique : $r^2 + 1 = 0 \Rightarrow r = \pm i$.

$$y_h = C_1 \cos x + C_2 \sin x$$

**Étape 2 : Solution particulière de $y'' + y = -3\sin 2x$**

On essaie $y_p = A\cos 2x + B\sin 2x$. Alors :
$$y_p'' = -4A\cos 2x - 4B\sin 2x$$
$$y_p'' + y_p = (-4A+A)\cos 2x + (-4B+B)\sin 2x = -3A\cos 2x - 3B\sin 2x = -3\sin 2x$$

Identification : $-3A = 0 \Rightarrow A = 0$, $-3B = -3 \Rightarrow B = 1$.

$$y_p = \sin 2x$$

**Solution générale :**
$$y = C_1\cos x + C_2\sin x + \sin 2x$$

**Étape 3 : Application des conditions aux limites**

$y(0) = 1$ : $C_1 \cdot 1 + C_2 \cdot 0 + 0 = 1 \Rightarrow \boxed{C_1 = 1}$

$y'(x) = -C_1\sin x + C_2\cos x + 2\cos 2x$

$y'(\pi) = 1$ : $-C_1 \cdot 0 + C_2(-1) + 2\cos 2\pi = 1 \Rightarrow -C_2 + 2 = 1 \Rightarrow \boxed{C_2 = 1}$

**Solution :**
$$\boxed{y(x) = \cos x + \sin x + \sin 2x}$$

</details>

---

#### Type 2 : PAL bien posé ou mal posé — analyse d'unicité (Exercice 3)

**Méthode :** Appliquer le théorème de l'alternative : résoudre le PAL homogène associé. Si la seule solution est $y = 0$ → bien posé. Sinon → mal posé (0 ou ∞ solutions selon la compatibilité du second membre).

**Exercice similaire d'après (3a/3b) :**
Les problèmes suivants sont-ils bien posés ?

$$
(a)\; \begin{cases} 4y'' + y = e^{x^2} \\ y(\pi) + 2y'(0) = 0 \\ y(0) - 2y'(0) = 1 \end{cases} \qquad (b)\; \begin{cases} 4y'' + y = e^{x^2} \\ y(\pi) - 2y'(0) = 0 \\ y(0) + 2y'(0) = 1 \end{cases}
$$

<details>
<summary>Voir la résolution complète</summary>

On étudie le PAL homogène de $4y'' + y = 0\,$, i.e., $y'' + \frac{1}{4}y = 0$.

Coefficients caractéristiques : $r^2 + \frac{1}{4} = 0 \Rightarrow r = \pm \frac{i}{2}$.

$$y_h = C_1\cos\frac{x}{2} + C_2\sin\frac{x}{2}$$

**Cas (a) — CL homogènes :** $y(\pi) + 2y'(0) = 0$ et $y(0) - 2y'(0) = 0$.

$y(0) = C_1$, $y'(x) = -\frac{C_1}{2}\sin\frac{x}{2} + \frac{C_2}{2}\cos\frac{x}{2}$, donc $y'(0) = \frac{C_2}{2}$.

$y(\pi) = C_1\cos\frac{\pi}{2} + C_2\sin\frac{\pi}{2} = C_2$.

CL 1 : $C_2 + 2 \cdot \frac{C_2}{2} = C_2 + C_2 = 2C_2 = 0 \Rightarrow C_2 = 0$

CL 2 : $C_1 - 2 \cdot \frac{C_2}{2} = C_1 - C_2 = C_1 = 0 \Rightarrow C_1 = 0$

Seule solution : $y = 0$. **Problème (a) est bien posé.** ✅

**Cas (b) — CL homogènes :** $y(\pi) - 2y'(0) = 0$ et $y(0) + 2y'(0) = 0$.

CL 1 : $C_2 - 2\frac{C_2}{2} = C_2 - C_2 = 0$ — satisfait pour tout $C_2$.

CL 2 : $C_1 + 2\frac{C_2}{2} = C_1 + C_2 = 0 \Rightarrow C_1 = -C_2$.

Le PAL homogène admet une infinité de solutions : $y = C_2(-\cos\frac{x}{2} + \sin\frac{x}{2})$ pour tout $C_2 \in \mathbb{R}$. **Problème (b) est mal posé.** ❌

</details>

---

#### Type 3 : Recherche des valeurs propres d'un PAL (Exercice 2a)

**Méthode :** Écrire la solution générale de $Ly = \lambda y$ (3 formes selon $\lambda > 0$, $\lambda = 0$, $\lambda < 0$). Appliquer les CL et déterminer les $\lambda$ pour lesquels le système admet une solution non triviale.

**Exercice similaire d'après (2a) :**
$$
\begin{cases} -y'' - 2y' - y = \lambda y \\ y(0) = y(\pi) = 0 \end{cases}
$$
Trouver toutes les valeurs propres et les fonctions propres.

<details>
<summary>Voir la résolution complète</summary>

L'EDO se réécrit :
$$y'' + 2y' + (1 + \lambda)y = 0$$

Équation caractéristique : $r^2 + 2r + (1+\lambda) = 0$, discriminant $\Delta = 4 - 4(1+\lambda) = -4\lambda$.

**Cas 1 : $\lambda > 0$ ($\Delta < 0$)** : racines complexes $r = -1 \pm i\sqrt{\lambda}$.

$$y = e^{-x}(C_1\cos(\sqrt{\lambda}x) + C_2\sin(\sqrt{\lambda}x))$$

CL : $y(0) = C_1 = 0 \Rightarrow C_1 = 0$, puis $y(\pi) = e^{-\pi}C_2\sin(\sqrt{\lambda}\pi) = 0$.

Pour une solution non triviale ($C_2 \neq 0$) : $\sin(\sqrt{\lambda}\pi) = 0 \Rightarrow \sqrt{\lambda} = k, k \in \mathbb{N}_0$.

$$\lambda_k = k^2, \quad y_k(x) = e^{-x}\sin(kx), \quad k = 1, 2, 3, \ldots$$

**Cas 2 : $\lambda = 0$ ($\Delta = 0$)** : racine double $r = -1$.

$$y = (C_1 + C_2 x)e^{-x}$$

CL : $y(0) = C_1 = 0$, $y(\pi) = C_2\pi e^{-\pi} = 0 \Rightarrow C_2 = 0$. Seule solution triviale. **$\lambda = 0$ n'est pas valeur propre.**

**Cas 3 : $\lambda < 0$ ($\Delta > 0$)** : racines réelles $r = -1 \pm \sqrt{-\lambda}$.

$$y = C_1 e^{(-1+\sqrt{-\lambda})x} + C_2 e^{(-1-\sqrt{-\lambda})x}$$

CL : $y(0) = C_1 + C_2 = 0 \Rightarrow C_2 = -C_1$, puis $y(\pi) = C_1(e^{(-1+\sqrt{-\lambda})\pi} - e^{(-1-\sqrt{-\lambda})\pi}) = 0$.

Le facteur $e^{(-1+\sqrt{-\lambda})\pi} - e^{(-1-\sqrt{-\lambda})\pi} = e^{-\pi}(e^{\sqrt{-\lambda}\pi} - e^{-\sqrt{-\lambda}\pi}) = 2e^{-\pi}\sinh(\sqrt{-\lambda}\pi)$ est non nul sauf si $\sqrt{-\lambda} = 0$, càd $\lambda = 0$ déjà traité. Donc $C_1 = 0$, solution triviale. **Pas de valeur propre négative.**

**Résultat final :**
$$\boxed{\lambda_k = k^2 \;(k \in \mathbb{N}_0), \quad y_k(x) = e^{-x}\sin(kx)}$$

</details>

---

#### Type 4 : PAL avec conditions périodiques (Exercice 2c)

**Méthode :** Pour des conditions périodiques $y(a) = y(b)$, $y'(a) = y'(b)$, la résolution de l'EDO donne des conditions qui couplent les deux bords. On examine les 3 cas de $\lambda$.

**Exercice similaire d'après (2c) :**
$$
\begin{cases} y'' = \lambda y \\ y(0) = y(2\pi) \\ y'(0) = y'(2\pi) \end{cases}
$$

<details>
<summary>Voir la résolution complète</summary>

**Cas 1 : $\lambda = 0$**

$y'' = 0 \Rightarrow y = C_1 + C_2 x$

CL : $C_1 = C_1 + 2\pi C_2 \Rightarrow C_2 = 0$. $C_2 = C_2$ automatiquement.

Solution non triviale : $y = C_1$ (constante quelconque). **$\lambda_0 = 0$ est valeur propre**, fonctions propres $y_0 = \text{const}$.

**Cas 2 : $\lambda = -\mu^2 < 0$ ($\mu > 0$)**

$y = C_1\cos(\mu x) + C_2\sin(\mu x)$

CL périodiques : $y(0) = y(2\pi)$ donne $C_1 = C_1\cos(2\pi\mu) + C_2\sin(2\pi\mu)$

$y'(0) = y'(2\pi)$ donne $C_2\mu = -C_1\mu\sin(2\pi\mu) + C_2\mu\cos(2\pi\mu)$

Pour solution non triviale, le système en $(C_1, C_2)$ doit être singulier : cela arrive ssi $\cos(2\pi\mu) = 1$ et $\sin(2\pi\mu) = 0$, i.e., $2\pi\mu = 2k\pi$, donc $\mu = k \in \mathbb{N}_0$.

$$\lambda_k = -k^2, \quad y_k(x) = A\cos(kx) + B\sin(kx) \quad (k \geq 1)$$

Chaque valeur propre $\lambda_k = -k^2$ a une **multiplicité 2** (deux fonctions propres indépendantes).

**Cas 3 : $\lambda = \mu^2 > 0$**

$y = C_1 e^{\mu x} + C_2 e^{-\mu x}$

Conditions : $C_1(e^{2\pi\mu} - 1) = 0$ et $C_2(e^{-2\pi\mu} - 1) = 0$ (après simplification). Comme $\mu > 0$, ni $e^{2\pi\mu}-1$ ni $e^{-2\pi\mu}-1$ ne sont nuls, donc $C_1 = C_2 = 0$. **Pas de valeur propre positive.**

**Résultat final :**
$$\boxed{\lambda_0 = 0 \text{ (mult. 1)}, \quad \lambda_k = -k^2 \text{ (mult. 2)}, \; k = 1, 2, \ldots}$$

</details>

---
