import re

with open('Analyse_2/Seances_Exercices_Analyse_2.md', 'r', encoding='utf-8') as f:
    text = f.read()

tp1_content = r'''## Séance 1 — Séries de Fourier (première partie)

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
'''

# Use an explicit exact substring match instead of regex to avoid DOTALL pitfalls
match = re.search(r'(## Séance 1.*?)(## Séance 2)', text, flags=re.DOTALL)
if match:
    new_text = text.replace(match.group(1), tp1_content + '\n\n')
    with open('Analyse_2/Seances_Exercices_Analyse_2.md', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('SUCCESS')
else:
    print('NOT FOUND')
