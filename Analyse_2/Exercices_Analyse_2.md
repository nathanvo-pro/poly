# Exercices — Analyse 2

## Chapitre 14 : Séries de Fourier

> 📈 **Difficulté croissante :** De la compréhension des bases de l'orthogonalité (⭐) jusqu'à la résolution complète de l'équation de la chaleur par séparation des variables (⭐⭐⭐⭐⭐). **Les réponses exigent des démonstrations complètes.**

---

### ⭐ Niveau 1 — Produit Scalaire et Orthogonalité

---

**Exercice 1 — Produit scalaire $L^2$**

Soient $f(x) = x$ et $g(x) = x^2$ sur l'intervalle $[-1, 1]$.
Calculez le produit scalaire $\langle f, g \rangle = \int_{-1}^{1} f(x) g(x) \, dx$ et déduisez-en si ces deux fonctions sont orthogonales.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

$$
\langle f, g \rangle = \int_{-1}^{1} x \cdot x^2 \, dx = \int_{-1}^{1} x^3 \, dx
$$
La fonction $x^3$ est **impaire**. L'intégrale d'une fonction impaire sur un intervalle symétrique $[-a, a]$ est toujours nulle :
$$
\langle f, g \rangle = 0
$$
Donc $f(x) = x$ et $g(x) = x^2$ **sont orthogonales** sur $[-1, 1]$ pour le produit scalaire $L^2$ !

> 💡 Ce n'est pas un hasard : toute fonction impaire est orthogonale à toute fonction paire sur un intervalle symétrique.
</details>

---

**Exercice 2 — Norme $L^2$ d'une constante**

Calculez la norme $L^2$ de la fonction constante $f(x) = 1$ sur l'intervalle $[-\pi, \pi]$. Puis normalisez-la (trouvez $c$ tel que $\|c \cdot 1\|_2 = 1$).

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

$$
\|1\|_2^2 = \int_{-\pi}^{\pi} 1^2 \, dx = 2\pi \implies \|1\|_2 = \sqrt{2\pi}
$$
Pour normaliser : $c \cdot \|1\|_2 = 1 \implies c = \frac{1}{\sqrt{2\pi}}$.

La fonction normalisée est $\varphi_0(x) = \frac{1}{\sqrt{2\pi}}$.
</details>

---

**Exercice 3 — Preuve d'orthogonalité de $\cos(jx)$ et $\sin(kx)$**

**Démontrez** que $\langle \cos(jx), \sin(kx) \rangle = 0$ sur $[-\pi, \pi]$ pour tous $j, k \in \mathbb{N}$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

$$
\langle \cos(jx), \sin(kx) \rangle = \int_{-\pi}^{\pi} \cos(jx) \sin(kx) \, dx
$$
Le produit $\cos(jx) \sin(kx)$ est une fonction impaire (produit d'une fonction paire par une impaire) :
- $\cos(j(-x)) = \cos(jx)$ (paire)
- $\sin(k(-x)) = -\sin(kx)$ (impaire)
- Donc $\cos(j(-x))\sin(k(-x)) = -\cos(jx)\sin(kx)$ (impaire)

L'intégrale d'une fonction impaire sur l'intervalle symétrique $[-\pi, \pi]$ est **toujours nulle** :
$$
\int_{-\pi}^{\pi} h(x) \, dx = 0 \quad \text{si } h(-x) = -h(x)
$$
Donc $\langle \cos(jx), \sin(kx) \rangle = 0$ pour tous $j, k$.
</details>

---

### ⭐⭐ Niveau 2 — Calcul des Coefficients de Fourier

---

**Exercice 4 — Coefficients de la fonction créneau**

Soit $f(x) = \begin{cases} 1 & \text{si } 0 < x < \pi \\ -1 & \text{si } -\pi < x < 0 \end{cases}$ (fonction créneau impaire de période $2\pi$).

Calculez tous les coefficients de Fourier $a_k$ et $b_k$ de $f$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Observation clé :** $f$ est **impaire** ($f(-x) = -f(x)$). Donc :
- Le produit $f(t)\cos(kt)$ est **impair** $\implies$ $a_k = 0$ pour tout $k \geq 0$.
- Le produit $f(t)\sin(kt)$ est **pair** $\implies$ on peut simplifier l'intégrale.

**Calcul de $b_k$ :**
$$
b_k = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(kt) \, dt = \frac{2}{\pi} \int_0^{\pi} 1 \cdot \sin(kt) \, dt
$$
(car la fonction est paire sur $[-\pi, \pi]$ après multiplication par $\sin$).

$$
= \frac{2}{\pi} \left[ -\frac{\cos(kt)}{k} \right]_0^{\pi} = \frac{2}{\pi k} \left( -\cos(k\pi) + 1 \right) = \frac{2}{\pi k} (1 - (-1)^k)
$$

- Si $k$ est **pair** : $(-1)^k = 1 \implies b_k = 0$.
- Si $k$ est **impair** : $(-1)^k = -1 \implies b_k = \frac{4}{\pi k}$.

**Résultat final :** La série de Fourier du créneau est :
$$
f(x) = \frac{4}{\pi} \left( \sin(x) + \frac{\sin(3x)}{3} + \frac{\sin(5x)}{5} + \cdots \right) = \frac{4}{\pi} \sum_{n=0}^{\infty} \frac{\sin((2n+1)x)}{2n+1}
$$
</details>

---

**Exercice 5 — Coefficients de $f(x) = x$ sur $[-\pi, \pi]$**

Calculez les coefficients de Fourier de $f(x) = x$ sur $[-\pi, \pi]$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

$f(x) = x$ est **impaire**, donc $a_k = 0$ pour tout $k$.

**Calcul de $b_k$ par intégration par parties :**
$$
b_k = \frac{1}{\pi} \int_{-\pi}^{\pi} t \sin(kt) \, dt = \frac{2}{\pi} \int_0^{\pi} t \sin(kt) \, dt
$$
Intégration par parties avec $u = t$, $dv = \sin(kt) dt$ :
$$
= \frac{2}{\pi} \left[ -\frac{t\cos(kt)}{k} \right]_0^{\pi} + \frac{2}{\pi k} \int_0^{\pi} \cos(kt) \, dt
$$
$$
= \frac{2}{\pi} \left( -\frac{\pi \cos(k\pi)}{k} \right) + \frac{2}{\pi k} \left[ \frac{\sin(kt)}{k} \right]_0^{\pi}
$$
Le sinus vaut $\sin(k\pi) = 0$ pour tout $k$ entier. Il reste :
$$
b_k = -\frac{2\cos(k\pi)}{k} = -\frac{2(-1)^k}{k} = \frac{2(-1)^{k+1}}{k}
$$

**Série de Fourier :**
$$
x = 2\left( \sin(x) - \frac{\sin(2x)}{2} + \frac{\sin(3x)}{3} - \cdots \right) = 2\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} \sin(kx)
$$
</details>

---

**Exercice 6 — Coefficients de $f(x) = |x|$ sur $[-\pi, \pi]$**

Calculez les coefficients de Fourier de la fonction valeur absolue $f(x) = |x|$ sur $[-\pi, \pi]$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

$f(x) = |x|$ est **paire**, donc $b_k = 0$ pour tout $k$.

**Calcul de $a_0$ :**
$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} |t| \, dt = \frac{2}{\pi} \int_0^{\pi} t \, dt = \frac{2}{\pi} \cdot \frac{\pi^2}{2} = \pi
$$

**Calcul de $a_k$ pour $k \geq 1$ (intégration par parties) :**
$$
a_k = \frac{1}{\pi} \int_{-\pi}^{\pi} |t| \cos(kt) \, dt = \frac{2}{\pi} \int_0^{\pi} t \cos(kt) \, dt
$$
Intégration par parties ($u = t$, $dv = \cos(kt) dt$) :
$$
= \frac{2}{\pi} \left[ \frac{t\sin(kt)}{k} \right]_0^{\pi} - \frac{2}{\pi k} \int_0^{\pi} \sin(kt) \, dt
$$
$$
= 0 + \frac{2}{\pi k^2} \left[ \cos(kt) \right]_0^{\pi} = \frac{2}{\pi k^2} (\cos(k\pi) - 1) = \frac{2}{\pi k^2}((-1)^k - 1)
$$

- Si $k$ pair : $a_k = 0$.
- Si $k$ impair : $a_k = \frac{-4}{\pi k^2}$.

**Série de Fourier :**
$$
|x| = \frac{\pi}{2} - \frac{4}{\pi} \left( \cos(x) + \frac{\cos(3x)}{9} + \frac{\cos(5x)}{25} + \cdots \right) = \frac{\pi}{2} - \frac{4}{\pi} \sum_{n=0}^{\infty} \frac{\cos((2n+1)x)}{(2n+1)^2}
$$
</details>

---

### ⭐⭐⭐ Niveau 3 — Parseval et Applications Numériques

---

**Exercice 7 — Utiliser Parseval pour calculer $\sum 1/k^2$**

En utilisant l'égalité de Parseval appliquée au résultat de l'exercice 5 ($f(x) = x$), **démontrez** la célèbre formule :
$$
\sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6}
$$

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Démonstration par Parseval :**
L'égalité de Parseval dit que pour le système orthogonal $\{1, \cos(kx), \sin(kx)\}$ sur $[-\pi, \pi]$ :
$$
\frac{a_0^2}{2} \cdot \pi + \sum_{k=1}^{\infty} (a_k^2 + b_k^2) \cdot \pi = \frac{1}{\pi} \|f\|_2^2
$$
attendons, reformulons proprement. L'égalité de Parseval pour $f(x) = x$ sur $[-\pi, \pi]$ s'écrit :
$$
\|f\|_2^2 = \frac{a_0^2}{2} \cdot 2\pi + \sum_{k=1}^{\infty} (a_k^2 + b_k^2) \cdot \pi
$$
Mais plus directement, comme le système est $\{\frac{1}{2}, \cos(kx), \sin(kx)\}$ avec les normes $\|1/2\|^2 = \pi/2$, $\|\cos(kx)\|^2 = \|\sin(kx)\|^2 = \pi$ :

**Étape 1 : Calcul de $\|f\|_2^2$.**
$$
\|x\|_2^2 = \int_{-\pi}^{\pi} x^2 \, dx = \frac{2\pi^3}{3}
$$

**Étape 2 : Application de Parseval.**
On sait que $a_k = 0$ et $b_k = \frac{2(-1)^{k+1}}{k}$, donc $|b_k|^2 = \frac{4}{k^2}$.

L'égalité de Parseval donne :
$$
\sum_{k=1}^{\infty} |b_k|^2 \|\sin(kx)\|_2^2 = \|f\|_2^2
$$
$$
\sum_{k=1}^{\infty} \frac{4}{k^2} \cdot \pi = \frac{2\pi^3}{3}
$$
$$
4\pi \sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{2\pi^3}{3}
$$
$$
\boxed{\sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6}}
$$

C'est le **problème de Bâle**, résolu originellement par Euler en 1734 !
</details>

---

**Exercice 8 — Utiliser Parseval pour $\sum 1/k^4$**

En appliquant l'égalité de Parseval à $f(x) = x^2$ sur $[-\pi, \pi]$ (dont les coefficients sont $a_0 = \frac{2\pi^2}{3}$, $a_k = \frac{4(-1)^k}{k^2}$, $b_k = 0$), **démontrez** que :
$$
\sum_{k=1}^{\infty} \frac{1}{k^4} = \frac{\pi^4}{90}
$$

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Étape 1 :** $\|x^2\|_2^2 = \int_{-\pi}^{\pi} x^4 \, dx = \frac{2\pi^5}{5}$

**Étape 2 :** Parseval :
$$
\frac{|a_0|^2}{2} \cdot 2\pi + \sum_{k=1}^{\infty} |a_k|^2 \cdot \pi = \|f\|_2^2
$$
Le terme $a_0/2$ du système vaut $a_0 = 2\pi^2/3$, sa norme dans le système classique : $\frac{(2\pi^2/3)^2}{4} \cdot 2\pi = \frac{2\pi^5}{9}$.

Hmm, utilisons la formule standard directement :
$$
\frac{a_0^2}{2} + \sum_{k=1}^{\infty} (a_k^2 + b_k^2) = \frac{1}{\pi}\int_{-\pi}^{\pi} |f|^2
$$
$$
\frac{1}{2}\left(\frac{2\pi^2}{3}\right)^2 + \sum_{k=1}^{\infty} \frac{16}{k^4} = \frac{1}{\pi} \cdot \frac{2\pi^5}{5}
$$
$$
\frac{2\pi^4}{9} + 16 \sum_{k=1}^{\infty} \frac{1}{k^4} = \frac{2\pi^4}{5}
$$
$$
16 \sum_{k=1}^{\infty} \frac{1}{k^4} = \frac{2\pi^4}{5} - \frac{2\pi^4}{9} = 2\pi^4 \left(\frac{1}{5} - \frac{1}{9}\right) = 2\pi^4 \cdot \frac{4}{45} = \frac{8\pi^4}{45}
$$
$$
\boxed{\sum_{k=1}^{\infty} \frac{1}{k^4} = \frac{8\pi^4}{45 \cdot 16} = \frac{\pi^4}{90}}
$$
</details>

---

### ⭐⭐⭐⭐ Niveau 4 — Convergence et Régularisation

---

**Exercice 9 — Application du Théorème de Dirichlet**

Soit $f(x) = \begin{cases} 0 & \text{si } -\pi < x < 0 \\ x & \text{si } 0 \leq x < \pi \end{cases}$, prolongée par périodicité de période $2\pi$.

1. Vers quelle valeur converge la série de Fourier de $f$ au point $x = 0$ ?
2. Vers quelle valeur converge-t-elle au point $x = \pi$ ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Par le **Théorème de Dirichlet**, la série converge vers la fonction régularisée $\tilde{f}(x) = \frac{f(x^-) + f(x^+)}{2}$.

**1. Au point $x = 0$ :**
$f$ a un saut en $x = 0$ :
- $f(0^-) = \lim_{x \to 0^-} 0 = 0$
- $f(0^+) = \lim_{x \to 0^+} x = 0$

Donc $\tilde{f}(0) = \frac{0 + 0}{2} = 0$. La série converge vers **$0$**.

**2. Au point $x = \pi$ :**
En pensant au prolongement périodique, $x = \pi$ est le point de jonction entre la fin de la période $[0, \pi[$ et le début de la suivante (qui est une copie de $[-\pi, 0[$) :
- $f(\pi^-) = \lim_{x \to \pi^-} x = \pi$
- $f(\pi^+) = f(-\pi^+) = \lim_{x \to -\pi^+} 0 = 0$

Donc $\tilde{f}(\pi) = \frac{\pi + 0}{2} = \frac{\pi}{2}$. La série converge vers **$\pi/2$**.
</details>

---

**Exercice 10 — Le phénomène de Gibbs**

Expliquez pourquoi les sommes partielles de la série de Fourier du créneau (Exercice 4) présentent des oscillations parasites (dépassement d'environ 9%) au voisinage des discontinuités, même quand le nombre d'harmoniques $n \to \infty$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Le **phénomène de Gibbs** est un artefact fondamental de la reconstruction de Fourier. Au voisinage d'un saut de discontinuité d'amplitude $\Delta$, les sommes partielles $s_n(x)$ de la série de Fourier :

1. **Oscillent** de plus en plus rapidement autour de la vraie valeur de $f$.
2. **Dépassent** systématiquement la valeur cible de $\Delta \cdot \frac{1}{\pi}\int_0^{\pi} \frac{\sin t}{t} dt \approx 0.0895 \cdot \Delta$ (soit environ $8.95\%$ du saut).
3. Ce dépassement **ne disparaît pas** quand $n \to \infty$ : il se concentre dans un voisinage de plus en plus étroit du point de discontinuité, mais garde la même amplitude maximale.

Cela montre que la **convergence simple** de la série de Fourier vers $\tilde{f}$ aux points de discontinuité **ne peut pas être uniforme** au voisinage de ces points.
</details>

---

### ⭐⭐⭐⭐⭐ Niveau 5 — Équation de la Chaleur et Séparation des Variables

---

**Exercice 11 — Résoudre l'Équation de la Chaleur**

Une barre métallique de longueur $L = \pi$ a ses deux extrémités maintenues à $0°$. La distribution initiale de température est $f(x) = \sin(x) + 3\sin(2x)$.
Résolvez l'EDP de la chaleur $\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2}$ avec $\alpha = 1$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Étape 1 :** La solution générale par séparation des variables est :
$$
u(x,t) = \sum_{n=1}^{\infty} b_n \sin(nx) e^{-n^2 t}
$$

**Étape 2 :** Condition initiale $u(x, 0) = f(x)$ :
$$
\sin(x) + 3\sin(2x) = \sum_{n=1}^{\infty} b_n \sin(nx)
$$
Par identification (les $\sin(nx)$ sont orthogonaux) : $b_1 = 1$, $b_2 = 3$, $b_n = 0$ pour $n \geq 3$.

**Solution exacte :**
$$
\boxed{u(x, t) = \sin(x) e^{-t} + 3\sin(2x) e^{-4t}}
$$

**Interprétation :** La composante $\sin(2x)$ (fréquence plus élevée) décroît 4 fois plus vite ($e^{-4t}$ vs $e^{-t}$). Après un certain temps, seule la composante fondamentale $\sin(x)$ subsiste.
</details>

---

**Exercice 12 — Séparation des variables complète**

Résolvez l'équation de la chaleur pour une barre de longueur $L = 1$ ($\alpha = 1$), extrémités à $0°$, et température initiale $f(x) = x(1-x)$. Exprimez la solution sous forme de série.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Étape 1 :** La solution est de la forme :
$$
u(x,t) = \sum_{n=1}^{\infty} b_n \sin(n\pi x) e^{-(n\pi)^2 t}
$$

**Étape 2 :** Calcul des $b_n$ (coefficients en sinus de $f(x) = x(1-x)$ sur $[0, 1]$) :
$$
b_n = 2\int_0^1 x(1-x) \sin(n\pi x) \, dx = 2\int_0^1 (x - x^2) \sin(n\pi x) \, dx
$$

Par double intégration par parties :
$$
b_n = \frac{4}{n^3\pi^3}(1 - (-1)^n)
$$

- $n$ pair : $b_n = 0$
- $n$ impair : $b_n = \frac{8}{n^3\pi^3}$

**Solution :**
$$
\boxed{u(x,t) = \frac{8}{\pi^3} \sum_{\substack{n=1 \\ n \text{ impair}}}^{\infty} \frac{1}{n^3} \sin(n\pi x) e^{-(n\pi)^2 t}}
$$
</details>

---

**Exercice 13 — Série de Fourier complexe d'un train d'impulsions**

Soit $f(t)$ un train d'impulsions rectangulaires de période $T$, d'amplitude $V$ et de largeur $\tau$ centré en $t = 0$.
Calculez les coefficients complexes $c_n$ et montrez que $c_n = \frac{V\tau}{T} \text{sinc}\left(\frac{n\pi\tau}{T}\right)$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

$$
c_n = \frac{1}{T}\int_{-T/2}^{T/2} f(t) e^{-in\omega_0 t} dt = \frac{1}{T}\int_{-\tau/2}^{\tau/2} V e^{-in\omega_0 t} dt
$$
$$
= \frac{V}{T}\left[\frac{e^{-in\omega_0 t}}{-in\omega_0}\right]_{-\tau/2}^{\tau/2} = \frac{V}{-in\omega_0 T}\left(e^{-in\omega_0 \tau/2} - e^{in\omega_0 \tau/2}\right)
$$
Comme $\omega_0 = 2\pi/T$ :
$$
= \frac{V}{-in \cdot 2\pi}(-2i\sin(n\pi\tau/T)) = \frac{V}{n\pi}\sin\left(\frac{n\pi\tau}{T}\right) = \frac{V\tau}{T} \cdot \frac{\sin(n\pi\tau/T)}{n\pi\tau/T}
$$
$$
\boxed{c_n = \frac{V\tau}{T} \operatorname{sinc}\left(\frac{n\pi\tau}{T}\right)}
$$
La fonction $\operatorname{sinc}(x) = \sin(x)/x$ est le **sinus cardinal**, fondamental en traitement du signal.
</details>

---

**Exercice 14 — Série de Fourier de l'onde triangulaire**

Soit $f(x) = |x|$ sur $[-L, L]$ (l'onde triangulaire). En utilisant les résultats de l'Exercice 6, **démontrez** par convergence simple que :
$$
1 + \frac{1}{3^2} + \frac{1}{5^2} + \frac{1}{7^2} + \cdots = \frac{\pi^2}{8}
$$

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

D'après l'Exercice 6 (avec $L = \pi$), la série de Fourier de $|x|$ converge vers $f$ en tout point de continuité (par Dirichlet, car $f$ est continue et $f'$ est $C^0_{\text{morc}}$). Évaluons en $x = 0$ :
$$
|0| = 0 = \frac{\pi}{2} - \frac{4}{\pi}\sum_{n=0}^{\infty} \frac{\cos(0)}{(2n+1)^2} = \frac{\pi}{2} - \frac{4}{\pi}\sum_{n=0}^{\infty} \frac{1}{(2n+1)^2}
$$
$$
\frac{4}{\pi}\sum_{n=0}^{\infty} \frac{1}{(2n+1)^2} = \frac{\pi}{2}
$$
$$
\boxed{\sum_{n=0}^{\infty} \frac{1}{(2n+1)^2} = 1 + \frac{1}{9} + \frac{1}{25} + \cdots = \frac{\pi^2}{8}}
$$
</details>

---

### ⭐⭐⭐ Niveau 3 bis — Techniques intermédiaires

---

**Exercice 15 — Coefficients de $f(x) = x(\pi - x)$ sur $[0, \pi]$ (série sinus)**

Calculez le développement en série de sinus de $f(x) = x(\pi - x)$ sur $[0, \pi]$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

On utilise la formule de la série sinus sur $[0, \pi]$ :
$$
b_k = \frac{2}{\pi}\int_0^{\pi} x(\pi - x)\sin(kx) \, dx = \frac{2}{\pi}\int_0^{\pi} (\pi x - x^2)\sin(kx) \, dx
$$
Par double intégration par parties (en intégrant $\sin(kx)$ et en dérivant $\pi x - x^2$) :

Première IPP ($u = \pi x - x^2$, $dv = \sin(kx)dx$) :
$$
= \frac{2}{\pi}\left[-\frac{(\pi x - x^2)\cos(kx)}{k}\right]_0^{\pi} + \frac{2}{\pi k}\int_0^{\pi} (\pi - 2x)\cos(kx) \, dx
$$
Le crochet vaut $0$ (les deux bornes s'annulent). Deuxième IPP sur l'intégrale restante :
$$
= \frac{2}{\pi k}\left[\frac{(\pi - 2x)\sin(kx)}{k}\right]_0^{\pi} + \frac{2}{\pi k} \cdot \frac{2}{k}\int_0^{\pi}\sin(kx) \, dx
$$
Le crochet vaut encore $0$. L'intégrale restante :
$$
= \frac{4}{\pi k^2}\left[-\frac{\cos(kx)}{k}\right]_0^{\pi} = \frac{4}{\pi k^3}(1 - \cos(k\pi)) = \frac{4}{\pi k^3}(1 - (-1)^k)
$$

- $k$ pair : $b_k = 0$
- $k$ impair : $b_k = \frac{8}{\pi k^3}$

$$
x(\pi - x) = \frac{8}{\pi}\sum_{\substack{k=1 \\ k \text{ impair}}}^{\infty} \frac{\sin(kx)}{k^3}
$$
</details>

---

**Exercice 16 — Parité et simplification : la fonction échelon**

Soit $f(x) = \begin{cases} 0 & \text{si } -\pi < x < 0 \\ \pi & \text{si } 0 < x < \pi \end{cases}$

1. Décomposez $f$ en une partie paire et une partie impaire.
2. Utilisez les résultats connus du créneau (Ex. 4) pour écrire directement la série de Fourier de $f$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1. Décomposition :** Toute fonction se décompose en :
$f(x) = \underbrace{\frac{f(x) + f(-x)}{2}}_{\text{partie paire}} + \underbrace{\frac{f(x) - f(-x)}{2}}_{\text{partie impaire}}$

- Partie paire : $\frac{f(x) + f(-x)}{2} = \frac{\pi}{2}$ (constante !)
- Partie impaire : $\frac{f(x) - f(-x)}{2} = \frac{\pi}{2}\text{sgn}(x)$ (créneau d'amplitude $\pi/2$)

**2. Série de Fourier :** La constante $\pi/2$ contribue $a_0/2 = \pi/2$. Le créneau normalisé (Ex. 4) donne :
$$
f(x) = \frac{\pi}{2} + 2\sum_{\substack{k=1 \\ k \text{ impair}}}^{\infty} \frac{\sin(kx)}{k} = \frac{\pi}{2} + 2\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots\right)
$$
</details>

---

**Exercice 17 — Coefficients de la dérivée (vérification)**

Soit $f(x) = x^2$ sur $[-\pi, \pi]$, de coefficients $a_0 = 2\pi^2/3$, $a_k = 4(-1)^k/k^2$, $b_k = 0$.

1. Calculez les coefficients de Fourier de $f'(x) = 2x$ directement.
2. Vérifiez que la formule $a_k(f') = kb_k(f)$ et $b_k(f') = -ka_k(f)$ donne le même résultat. **Attention au piège : $f(\pi) \neq f(-\pi)$ !**

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1. Directement :** $f'(x) = 2x$ est impaire, donc $a_k(f') = 0$. Et $b_k(f') = b_k(2x) = 2 \cdot \frac{2(-1)^{k+1}}{k} = \frac{4(-1)^{k+1}}{k}$ (par l'Ex. 5).

**2. Par la formule :** Comme $f(-\pi) = \pi^2 \neq f(\pi) = \pi^2$... en fait ici $f(-\pi) = f(\pi) = \pi^2$. La discontinuité est absente !

Donc : $b_k(f') = -ka_k(f) = -k \cdot \frac{4(-1)^k}{k^2} = \frac{-4(-1)^k}{k} = \frac{4(-1)^{k+1}}{k}$ ✅

Et $a_k(f') = kb_k(f) = k \cdot 0 = 0$ ✅

Les deux méthodes concordent parfaitement.

> ⚠️ Si $f(-\pi) \neq f(\pi)$, il faudrait ajouter un terme correctif $\frac{(-1)^k}{\pi}(f(\pi) - f(-\pi))$ aux coefficients de la dérivée !
</details>

---

### ⭐⭐⭐⭐ Niveau 4 bis — Démonstrations et Noyau de Dirichlet

---

**Exercice 18 — Le Noyau de Dirichlet**

**Démontrez** que le noyau de Dirichlet $K_n(\theta) = 1 + 2\sum_{k=1}^{n}\cos(k\theta)$ admet la forme fermée :
$$
K_n(\theta) = \frac{\sin\left((n + \frac{1}{2})\theta\right)}{\sin(\theta/2)}
$$
en utilisant les sommes géométriques d'exponentielles complexes.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

On écrit $\cos(k\theta) = \frac{e^{ik\theta} + e^{-ik\theta}}{2}$, donc :
$$
K_n(\theta) = 1 + \sum_{k=1}^{n}(e^{ik\theta} + e^{-ik\theta}) = \sum_{k=-n}^{n} e^{ik\theta}
$$
C'est une somme géométrique de raison $r = e^{i\theta}$ avec $2n + 1$ termes :
$$
= e^{-in\theta} \cdot \frac{1 - e^{i(2n+1)\theta}}{1 - e^{i\theta}}
$$
On factorise numérateur et dénominateur :
$$
= e^{-in\theta} \cdot \frac{e^{i(2n+1)\theta/2}}{e^{i\theta/2}} \cdot \frac{e^{-i(2n+1)\theta/2} - e^{i(2n+1)\theta/2}}{e^{-i\theta/2} - e^{i\theta/2}}
$$
$$
= e^{-in\theta} \cdot e^{in\theta} \cdot \frac{-2i\sin((n+1/2)\theta)}{-2i\sin(\theta/2)} = \frac{\sin((n+1/2)\theta)}{\sin(\theta/2)}
$$
</details>

---

**Exercice 19 — Convergence uniforme : vérification des hypothèses**

Soit $f(x) = \pi - |x|$ sur $[-\pi, \pi]$.
1. Vérifiez que $f$ satisfait les hypothèses du théorème de convergence uniforme.
2. En déduire que sa série de Fourier converge uniformément vers $f$.
3. Déterminer la vitesse de décroissance des coefficients.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1. Hypothèses :**
- $f$ est **continue** sur $[-\pi, \pi]$ ✅ ($f$ est le « chapeau »).
- $f'$ est $C^0_{\text{morc}}$ ✅ ($f'(x) = \pm 1$ sauf en $x = 0$ où la dérivée saute de $+1$ à $-1$).
- $f(-\pi) = f(\pi) = 0$ ✅ (continuité du prolongement périodique).

**2.** Toutes les hypothèses sont satisfaites, donc par le théorème de convergence uniforme, la série de Fourier converge **uniformément** vers $f$ sur $[-\pi, \pi]$.

**3.** $f$ est paire donc $b_k = 0$. Par calcul (similaire à l'Ex. 6 avec transformation $f = \pi - |x|$) :
- $a_0 = \pi$
- $a_k = \frac{2}{\pi k^2}(1 - (-1)^k)$ : non nul seulement pour $k$ impair, valeur $\frac{4}{\pi k^2}$.

Les coefficients décroissent en $1/k^2$. C'est typique d'une fonction **continue** dont la dérivée a des sauts (la dérivée est en $C^0_{\text{morc}}$).
</details>

---

### ⭐⭐⭐⭐⭐ Niveau 5 bis — Applications avancées

---

**Exercice 20 — Intégration terme à terme et primitive**

En intégrant terme à terme la série de Fourier de $f(x) = x/2$ (Ex. 5 divisé par 2) sur $[-\pi, \pi]$, trouvez la série de Fourier de la primitive $G(x) = \int_{-\pi}^{x}(t/2 - 0) dt = \frac{x^2}{4} - \frac{\pi^2}{4}$.

Vérifiez votre résultat en calculant directement les coefficients de $G(x) + \pi^2/4 = x^2/4$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

La série de $f(x) = x/2$ est : $\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k}\sin(kx)$.

Par la formule d'intégration : $a_k(G) = -\frac{b_k(f)}{k} = -\frac{(-1)^{k+1}}{k^2} = \frac{(-1)^k}{k^2}$ et $b_k(G) = \frac{a_k(f)}{k} = 0$.

Donc $G(x) = c_0 + \sum_{k=1}^{\infty} \frac{(-1)^k}{k^2}\cos(kx)$ pour une certaine constante $c_0$.

On retrouve bien la série de $x^2/4$ (à constante $\pi^2/4$ près) :
$$
\frac{x^2}{4} = \frac{\pi^2}{12} + \sum_{k=1}^{\infty} \frac{(-1)^k}{k^2}\cos(kx)
$$
Ce qui est cohérent avec $a_0(x^2/4) = \frac{1}{\pi}\int_{-\pi}^{\pi}\frac{x^2}{4}dx = \frac{\pi^2}{6}$, et $a_0/2 = \pi^2/12$. ✅
</details>

---

**Exercice 21 — EDL forcée périodiquement : vérifier la non-résonance**

Un système masse-ressort ($m = 1$, $k = 5$) est soumis à la force impaire de période $2$ avec $f_n = (-1)^{n+1} \frac{2}{n\pi}$.

1. Y a-t-il résonance ? Justifier.
2. Écrivez les 3 premiers termes de la solution périodique $y(t)$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1. Condition de résonance :** Il y a résonance si $\sqrt{k/m}/\pi \in \mathbb{N}_0$, i.e. si $\sqrt{5}/\pi \in \mathbb{N}_0$. Or $\sqrt{5}/\pi \approx 0.712...$, qui n'est pas un entier. **Pas de résonance.**

**2. Solution :** $b_n = \frac{f_n}{k - mn^2\pi^2} = \frac{(-1)^{n+1} \cdot 2}{n\pi(5 - n^2\pi^2)}$

- $n = 1$ : $b_1 = \frac{2}{\pi(5 - \pi^2)} = \frac{2}{\pi(5 - 9.87)} = \frac{2}{\pi \cdot (-4.87)} \approx -0.131$
- $n = 2$ : $b_2 = \frac{-2}{2\pi(5 - 4\pi^2)} = \frac{-1}{\pi(5 - 39.5)} = \frac{-1}{\pi(-34.5)} \approx 0.00922$
- $n = 3$ : $b_3 = \frac{2}{3\pi(5 - 9\pi^2)} = \frac{2}{3\pi(5 - 88.8)} \approx -0.00254$

$$
y(t) \approx -0.131\sin(\pi t) + 0.00922\sin(2\pi t) - 0.00254\sin(3\pi t) + \cdots
$$

Les termes décroissent très vite car le dénominateur croît en $n^3$.
</details>

---

**Exercice 22 — Démontrer la convergence $C^{\infty}$ de la solution de la chaleur**

Montrez que la série solution de l'équation de la chaleur $u(x,t) = \sum b_n \sin(n\pi x/L) e^{-\alpha^2(n\pi/L)^2 t}$ est $C^{\infty}$ pour tout $t > 0$, même si la condition initiale $f$ n'est que $L^2$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Idée :** Pour tout $t \geq t_0 > 0$, le facteur exponentiel $e^{-\alpha^2(n\pi/L)^2 t}$ décroît **super-exponentiellement** avec $n$ : il se comporte comme $e^{-An^2}$ où $A = \alpha^2\pi^2 t_0 / L^2 > 0$.

**Preuve :** Pour toute dérivée partielle $\frac{\partial^{p+q}}{\partial x^p \partial t^q}$, le terme général de la série dérivée est :
$$
b_n \cdot \left(\frac{n\pi}{L}\right)^p \cdot \left(-\frac{\alpha^2 n^2\pi^2}{L^2}\right)^q \cdot \sin\left(\frac{n\pi x}{L}\right) e^{-\alpha^2(n\pi/L)^2 t}
$$
En valeur absolue : $\leq |b_n| \cdot P(n) \cdot e^{-An^2}$ où $P(n)$ est un polynôme en $n$.

Par Bessel, $|b_n| \leq B$ (borné car $f \in L^2$). Et $\sum_{n=1}^{\infty} B \cdot P(n) \cdot e^{-An^2} < +\infty$ pour tout polynôme $P$ (l'exponentielle bat tout polynôme).

Par le critère de Weierstrass, la série dérivée converge **uniformément** sur $[0,L] \times [t_0, +\infty[$. Par les théorèmes d'analyse, la somme est donc dérivable et la dérivée est la somme de la série dérivée.

Ceci est vrai pour **tout** ordre de dérivation $(p, q)$, donc $u \in C^{\infty}([0,L] \times ]0, +\infty[)$.

> 💡 **Régularisation instantanée :** Même si $f$ est discontinue, la solution $u$ devient instantanément infiniment lisse pour tout $t > 0$. C'est un phénomène physiquement naturel : la chaleur « lisse » immédiatement les irrégularités.
</details>




---

### ⭐⭐ Niveau 2 ter — Les Trois Ondes Canoniques

---

**Exercice 23 — Série de Fourier de l'onde carrée**

Soit $f(x) = \\begin{cases} -1/2 & \\text{si } -\\pi < x < 0 \\\\ 1/2 & \\text{si } 0 < x < \\pi \\end{cases}$, prolongée par périodicité.

1. Calculez les coefficients $a_k$ et $b_k$.
2. Vers quelle valeur la série converge-t-elle en $x = 0$ et $x = \\pi$ ?
3. La convergence est-elle **uniforme** ? Justifiez.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** $f$ est **impaire** donc $a_k = 0$. $b_k = \\frac{1-(-1)^k}{\\pi k}$ : nul pour $k$ pair, $\\frac{2}{\\pi k}$ pour $k$ impair.
$$\\tilde{f}_{\\rm pro}(x) \\sim \\frac{2}{\\pi}\\left(\\sin x + \\frac{\\sin 3x}{3} + \\frac{\\sin 5x}{5} + \\cdots\\right)$$

**2.** Par Dirichlet : en $x = 0$, $\\tilde{f}(0) = \\frac{-1/2+1/2}{2} = \\mathbf{0}$. En $x = \\pi$, $\\tilde{f}(\\pi) = \\frac{f(\\pi^-)+f(-\\pi^+)}{2} = \\frac{1/2-1/2}{2} = \\mathbf{0}$.

**3. Non, la convergence n'est pas uniforme.** $f_{\\rm pro}$ est **discontinue** (sauts en $x=0, \\pm\\pi$). De plus $\\sum|b_k|=\\frac{2}{\\pi}\\sum_{\\rm impairs}\\frac{1}{k}$ **diverge**. Phénomène de Gibbs (~9%) visible.
</details>

---

**Exercice 24 — Onde triangulaire : convergence uniforme et formule $\\pi^2/8$**

Soit $f(x) = |x|$ sur $[-\\pi, \\pi]$ prolongée par périodicité.

1. Calculez $a_0$ et $a_k$ pour $k \\geq 1$ (la parité $b_k=0$).
2. Vérifiez les **trois conditions** du théorème de convergence uniforme.
3. En évaluant la série en $x = 0$, prouvez que $\\displaystyle\\sum_{n=0}^\\infty \\frac{1}{(2n+1)^2} = \\frac{\\pi^2}{8}$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** $f$ paire donc $b_k = 0$. $a_0 = \\pi$. Pour $k\\geq 1$ :
$$a_k = \\frac{2((-1)^k-1)}{\\pi k^2} \\implies \\begin{cases} 0 & k \\text{ pair} \\\\ -\\frac{4}{\\pi k^2} & k \\text{ impair}\\end{cases}$$
$$|x| = \\frac{\\pi}{2} - \\frac{4}{\\pi}\\left(\\cos x + \\frac{\\cos 3x}{9} + \\frac{\\cos 5x}{25}+\\cdots\\right)$$

**2. Conditions C.U. :**
- $f$ **continue** sur $[-\\pi,\\pi]$ ✅
- $f' = \\pm 1 \\in C^0_{\\rm morc}$ ✅
- $f(-\\pi)=f(\\pi)=\\pi$ donc $f_{\\rm pro}$ **continu** ✅ → **convergence uniforme** ✓

**3.** En $x=0$ :
$$0 = \\frac{\\pi}{2} - \\frac{4}{\\pi}\\sum_{n=0}^\\infty \\frac{1}{(2n+1)^2} \\implies \\boxed{\\sum_{n=0}^\\infty \\frac{1}{(2n+1)^2} = \\frac{\\pi^2}{8}}$$
</details>

---

**Exercice 25 — Onde dents de scie : décroissance des coefs et Parseval**

Soit $f(x) = x/2$ sur $]-\\pi,\\pi[$, prolongée par périodicité (sauts en $\\pm\\pi$).

1. Calculez les $b_k$ (impaire $\\Rightarrow a_k = 0$).
2. $\\sum|b_k|$ converge-t-elle ? Qu'implique cela pour la C.U. ?
3. Retrouvez $\\displaystyle\\sum_{k=1}^\\infty \\frac{1}{k^2} = \\frac{\\pi^2}{6}$ par Parseval.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** Par IBP : $b_k = \\frac{(-1)^{k+1}}{k}$. Série : $f(x) = \\sin x - \\frac{\\sin 2x}{2} + \\frac{\\sin 3x}{3} - \\cdots$

**2.** $\\sum|b_k| = \\sum 1/k$ **diverge**. Par contraposée de Weierstrass, pas de C.U. (cohérent : $f_{\\rm pro}$ discontinue).

**3.** Parseval : $\\|f\\|_2^2 = \\int_{-\\pi}^\\pi(x/2)^2dx = \\pi^3/6$ et $\\pi\\sum_{k=1}^\\infty \\frac{1}{k^2} = \\frac{\\pi^3}{6}$, donc $\\boxed{\\sum 1/k^2 = \\pi^2/6}$.

> 💡 $f$ est $C^\\infty$ sur $]-\\pi,\\pi[$, mais c'est la **continuité du prolongement** qui détermine la C.U. !
</details>

---



---

### ⭐⭐ Niveau 2 bis — Questions Conceptuelles (Vrai / Faux)

---

**Exercice 22 bis — QCM : Continuité et Convergence**

Indiquez si les affirmations suivantes sont **Vraies** ou **Fausses** et justifiez brièvement (sans calcul).

**1. Vrai ou Faux ?** « Si une fonction $f$ est continue sur $]-\pi, \pi[$ et $C^\infty$ sur cet intervalle, alors sa série de Fourier convergera nécessairement uniformément vers $f$ sur cet intervalle. »
**2. Vrai ou Faux ?** « Le phénomène de Gibbs disparaît si on calcule la somme partielle de Fourier jusqu'à un ordre $N$ suffisamment grand (ex: $N=1000$). »
**3. Vrai ou Faux ?** « Si tous les coefficients $b_k$ d'une série de Fourier sont nuls, alors la fonction $f$ d'origine est nécessairement une fonction paire. »
**4. Vrai ou Faux ?** « Parseval s'applique même si la série de Fourier ne converge pas uniformément. »
**5. Vrai ou Faux ?** « L'onde triangulaire ($f(x) = |x|$) a des coefficients qui décroissent plus vite que l'onde en dents de scie ($f(x) = x/2$). »

<details>
<summary>Voir les réponses et justifications</summary>

**1. FAUX.** La régularité sur $]-\pi, \pi[$ ne suffit pas. C'est la continuité de son **prolongement périodique** sur tout $\mathbb{R}$ qui est requise. Si $f(\pi^-) 
eq f(-\pi^+)$ (comme pour l'onde en dents de scie), le prolongement saute, empêchant toute convergence uniforme.

**2. FAUX.** Le phénomène de Gibbs (dépassement d'environ 9% de l'amplitude du saut) ne disparaît *jamais*, peu importe la taille de $N$. L'oscillation devient de plus en plus "étroite" (proche du saut horizontalement), mais sa hauteur reste de 9%.

**3. VRAI.** Si tous les $b_k = 0$, la série de Fourier ne contient que des cosinus (et potentiellement une constante $a_0/2$). Comme la fonction cosinus est paire, toute combinaison linéaire (finie ou infinie) de cosinus donne une fonction (ou du moins un signal) globalement **paire**.

**4. VRAI.** Le théorème de Parseval est une égalité de normes dans l'espace $L^2$. Il requiert seulement que la fonction soit de carré intégrable (énergie finie), ce qui est beaucoup moins restrictif que la convergence uniforme. $f$ peut même avoir quelques discontinuités !

**5. VRAI.** L'onde triangulaire a un prolongement continu, donc ses coefficients décroissent en $\mathcal{O}(1/n^2)$. L'onde en dents de scie a un prolongement avec des sauts, ses coefficients décroissent beaucoup plus lentement en $\mathcal{O}(1/n)$.
</details>

---
### ⭐⭐⭐ Niveau 3 ter — Dérivées Généralisées et Formule Corrigée

---

**Exercice 26 — Reconnaître la classe $C^1_{\\rm morc}$**

Pour chacune des fonctions sur $[-\\pi,\\pi]$, dire si elle est dans $C^1_{\\rm morc}([-\\pi,\\pi])$ :

(a) $f_1(x)=\\begin{cases}x^2 & 0\\leq x\\leq\\pi \\\\ -x & -\\pi\\leq x<0\\end{cases}$ ; (b) $f_2(x)=\\begin{cases}x^2\\sin(1/x) & x\\neq 0 \\\\ 0 & x=0\\end{cases}$ ; (c) $f_3(x)=|x|^{1/2}$

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**(a) $f_1 \\in C^1_{\\rm morc}$ ✅** — En $x=0$ : $f_1(0^\\pm) = 0$, $f_1'(0^-)=-1$, $f_1'(0^+)=0$. Toutes finies.

**(b) $f_2 \\notin C^1_{\\rm morc}$ ❌** — $f_2'(x) = 2x\\sin(1/x)-\\cos(1/x)$ pour $x\\neq 0$. La limite en $0^+$ n'existe **pas** (oscillations de $\\cos(1/x)$).

**(c) $f_3 \\notin C^1_{\\rm morc}$ ❌** — $f_3'(x) = \\pm\\frac{1}{2}|x|^{-1/2} \\to +\\infty$ quand $x\\to 0$ : limite **infinie**, pas dans $\\mathbb{R}$.
</details>

---

**Exercice 27 — Formule corrigée des coefs de la dérivée**

Soit $f(x) = x$ sur $]-\\pi,\\pi[$. Rappel : $b_k(f) = \\frac{2(-1)^{k+1}}{k}$, $a_k(f) = 0$.

1. $f_{\\rm pro}$ est-il continu ? Calculez le saut $\\delta = f(\\pi^-)-f(-\\pi^+)$.
2. Appliquez la formule corrigée $a_k(f') = kb_k(f)+\\frac{(-1)^k}{\\pi}\\delta$ et $b_k(f')=-ka_k(f)$ pour trouver les coefs de $f'=1$.
3. Vérifiez directement les coefs de la constante $1$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** $f_{\\rm pro}$ est **discontinue** en $\\pm\\pi$. $\\delta = \\pi-(-\\pi)=2\\pi$.

**2.** $a_k(f') = k\\cdot\\frac{2(-1)^{k+1}}{k}+\\frac{(-1)^k}{\\pi}\\cdot 2\\pi = 2(-1)^{k+1}+2(-1)^k = 0$ ; $b_k(f') = 0$ ; $a_0/2=1$.
La série de $f'$ est bien la constante $1$.✓

**3.** Direct : $a_0(1) = \\frac{1}{\\pi}\\int_{-\\pi}^\\pi dt = 2$ ✓, $a_k(1) = b_k(1) = 0$ ✓.

> ⚠️ **Sans le terme correctif** $\\frac{(-1)^k\\delta}{\\pi}$, on aurait faussement $a_k(f')=2(-1)^{k+1}\\neq 0$.
</details>

---

### ⭐⭐⭐⭐ Niveau 4 ter — Produit de Séries et Identification des Coefficients

---

**Exercice 28 — Produit $\\sin(x)\\cdot\\cos(x)$ par convolution discrète**

En utilisant $c_k(f\\cdot g) = \\sum_\\ell f_\\ell\\cdot g_{k-\\ell}$, calculez la série de Fourier de $h(x)=\\sin(x)\\cos(x)$. Vérifiez par la formule trigonométrique.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Coefs de $\\sin x$ : $f_1=-i/2$, $f_{-1}=i/2$. Coefs de $\\cos x$ : $g_1=g_{-1}=1/2$. Tous les autres nuls.

Seuls $k=\\pm 2$ sont non nuls :
$$c_2(h) = f_1 g_1 = \\frac{-i}{4}, \\quad c_{-2}(h) = f_{-1}g_{-1} = \\frac{i}{4}, \\quad c_0 = f_1g_{-1}+f_{-1}g_1 = 0$$

$$h(x) = \\frac{i}{4}e^{-2ix}-\\frac{i}{4}e^{2ix} = \\frac{\\sin(2x)}{2}$$

Vérification : $\\sin(x)\\cos(x) = \\frac{\\sin(2x)}{2}$ ✅ (formule $\\sin(2\\theta)=2\\sin\\theta\\cos\\theta$)
</details>

---

**Exercice 29 — Identifier les coefficients d'une série uniformément convergente**

On sait que $S(x) = \\sum_{k=1}^\\infty \\frac{\\cos(kx)}{k^2}$ converge uniformément sur $[-\\pi,\\pi]$.

1. Justifiez la C.U. (critère de Weierstrass).
2. Calculez $\\int_{-\\pi}^\\pi S(x)\\cos(nx)\\,dx$ en intervertissant somme et intégrale.
3. Que vaut $\\int_{-\\pi}^\\pi S(x)\\,dx$ ? Interprétez.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** $|\\cos(kx)/k^2|\\leq 1/k^2$ et $\\sum 1/k^2 < +\\infty$ → Weierstrass → C.U. ✅

**2.** Interversion autorisée (C.U.) :
$$\\int_{-\\pi}^\\pi S(x)\\cos(nx)\\,dx = \\sum_{k=1}^\\infty\\frac{1}{k^2}\\underbrace{\\int_{-\\pi}^\\pi\\cos(kx)\\cos(nx)\\,dx}_{=\\pi\\,\\delta_{kn}} = \\frac{\\pi}{n^2}$$
On retrouve $a_n(S)=1/n^2$ : les coefs d'origine. (Proposition d'identification ✓)

**3.** $\\int_{-\\pi}^\\pi S\\,dx = \\sum(1/k^2)\\cdot 0 = 0$. Valeur moyenne nulle (pas de terme constant).
</details>

---

**Exercice 30 — Convergence uniforme et vitesse de décroissance**

Soit $f(x) = x^3-\\pi^2 x$ sur $[-\\pi,\\pi]$.

1. Vérifiez les conditions de C.U. (continuité, $C^1_{\\rm morc}$, bords).
2. En analysant les sauts de $f, f', f''$ prolongées, estimez la décroissance des coefs en $1/k^p$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** $f$ polynôme ($C^\\infty$) ✅ ; $f'=3x^2-\\pi^2\\in C^0_{\\rm morc}$ ✅ ; $f(-\\pi)=f(\\pi)=0$ → $f_{\\rm pro}$ continu ✅ → **C.U.** ✓

**2.** $f_{\\rm pro}$ : continu ✅. $f'_{\\rm pro}$ : $f'(-\\pi)=f'(\\pi)=2\\pi^2$ → continu ✅. $f''_{\\rm pro}$ : $f''(x)=6x$, $f''(-\\pi)=-6\\pi\\neq f''(\\pi)=6\\pi$ → **saut de $12\\pi$** ❌.

Première rupture à $p=3$ → coefs de $f$ décroissent en $\\mathbf{1/k^3}$.

> 💡 **Règle :** Si le premier prolongement discontinu est $f^{(p)}$, les coefs de $f$ décroissent en $1/k^p$.
</details>

---

### ⭐⭐⭐⭐⭐ Niveau 5 ter — Applications Avancées

---

**Exercice 31 — EDP de la chaleur avec condition initiale $f(x)=x(\\pi-x)$**

Résolvez l'EDP de la chaleur $\\partial_t u = \\partial_{xx} u$ sur $[0,\\pi]$, extrémités à $0°$, condition initiale $u(x,0)=x(\\pi-x)$. Donnez la solution en série et interprétez pour $t\\to+\\infty$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Solution :** $u(x,t) = \\sum_{n=1}^\\infty b_n\\sin(nx)\\,e^{-n^2t}$

**Coefs $b_n$** (série sinus de $x(\\pi-x)$ sur $[0,\\pi]$, cf. Exercice 15) :
$$b_n = \\frac{8}{\\pi n^3}\\text{ (n impair)}, \\qquad b_n = 0\\text{ (n pair)}$$

$$\\boxed{u(x,t) = \\frac{8}{\\pi}\\sum_{\\substack{n=1\\\\n\\,\\rm impair}}^\\infty\\frac{\\sin(nx)}{n^3}\\,e^{-n^2t}}$$

**Pour $t\\to+\\infty$ :** Le mode fondamental $n=1$ domine ($e^{-t}$) ; les harmoniques $n\\geq 3$ décroissent en $e^{-9t}, e^{-25t},\\ldots$ La barre tend vers $\\frac{8}{\\pi}\\sin(x)e^{-t}$ puis vers $0$ uniformément. Les coefs $b_n\\sim 1/n^3$ garantissent une convergence rapide + $C^\\infty$ pour tout $t>0$ (régularisation instantanée).
</details>

---

**Exercice 32 — Filtrage par convolution : le noyau de Dirichlet comme filtre passe-bas**

Posons $g_N(x) = \\frac{K_N(x)}{2N+1}$ où $K_N(\\theta) = \\sum_{k=-N}^N e^{ik\\theta}$ est le noyau de Dirichlet.

1. Calculez $c_k(g_N)$ pour tout $k\\in\\mathbb{Z}$.
2. Montrez que $(f*g_N)(x) = \\frac{s_N(x)}{2N+1}$ ($s_N$ = somme partielle d'ordre $N$ de $f$).
3. Interprétez $g_N$ comme un filtre passe-bas en traitement du signal.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** Par identification directe : $c_k(g_N) = \\frac{1}{2N+1}$ si $|k|\\leq N$, $0$ sinon.

**2.** Par le théorème de convolution :
$$c_k(f*g_N) = c_k(f)\\cdot c_k(g_N) = \\frac{c_k(f)}{2N+1}\\text{ si }|k|\\leq N, \\;0\\text{ sinon}$$
$$(f*g_N)(x) = \\sum_{|k|\\leq N}\\frac{c_k(f)}{2N+1}e^{ikx} = \\frac{s_N(x)}{2N+1}\\checkmark$$

**3.** $g_N$ **conserve exactement** les harmoniques $|k|\\leq N$ et **bloque** toutes les fréquences supérieures : c'est un **filtre passe-bas idéal** d'ordre $N$. Augmenter $N$ = plus de détails du signal, mais phénomène de Gibbs aux discontinuités.
</details>

---

**Exercice 33 — Parseval : calculer $\\int_{-\\pi}^\\pi x^2\\cos(x)\\,dx$ sans IBP**

Utilisez $\\langle f,g\\rangle = \\pi\\sum_{k=1}^\\infty(a_k(f)a_k(g)+b_k(f)b_k(g)) + \\pi a_0(f)a_0(g)$ pour calculer $I = \\int_{-\\pi}^\\pi x^2\\cos(x)\\,dx$.

Rappel : $a_k(x^2) = 4(-1)^k/k^2$ pour $k\\geq 1$.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Coefs de $g=\\cos(x)$ : $a_1=1$, tous les autres nuls.

$$I = \\langle x^2, \\cos x\\rangle = \\pi \\cdot a_1(x^2) \\cdot 1 = \\pi \\cdot \\frac{4(-1)^1}{1} = \\boxed{-4\\pi}$$

> 💡 Aucune IBP — on lit directement le bon coefficient de Fourier de $x^2$ !
</details>

---

**Exercice 34 — Unicité de la représentation et formule de Leibniz**

On admet que $\\displaystyle\\sum_{k=1}^\\infty\\frac{\\sin(kx)}{k} = \\frac{\\pi-x}{2}$ pour $x\\in]0,2\\pi[$.

1. Vérifiez en $x=\\pi$ (cohérence avec Dirichlet).
2. En $x=\\pi/2$, déduisez la formule $1-\\frac{1}{3}+\\frac{1}{5}-\\frac{1}{7}+\\cdots$
3. Si $\\sum c_k\\sin(kx) \\overset{C.U.}{=} \\frac{\\pi-x}{2}$, que vaut $c_k$ ? Justifiez par la proposition d'identification.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**1.** En $x=\\pi$ : $\\sum\\frac{\\sin(k\\pi)}{k}=0=\\frac{\\pi-\\pi}{2}$ ✓

**2.** En $x=\\pi/2$ : $\\sum_{k=1}^\\infty\\frac{\\sin(k\\pi/2)}{k}=\\frac{\\pi}{4}$.
Or les termes non nuls alternent ($\\pm 1$ pour $k$ impairs, $0$ pour $k$ pairs) :
$$\\boxed{1-\\frac{1}{3}+\\frac{1}{5}-\\frac{1}{7}+\\cdots = \\frac{\\pi}{4}} \\quad \\text{(Formule de Leibniz)}$$

**3.** Par la **proposition d'identification** : la C.U. permet d'intervertir somme/intégrale. L'orthogonalité du système $\\{\\sin(kx)\\}$ impose alors $c_k = \\frac{1}{k}$ (coefs de Fourier de $\\frac{\\pi-x}{2}$). **Unicité garantie** par la complétude du système.
</details>
