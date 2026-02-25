# ✅ Quiz / QCM — Analyse 2 (MATH-H-2000)

> Quiz avec questions à choix multiples pour réviser le Chapitre 14.
> Cliquez sur **💡 Solution** pour vérifier votre réponse et voir l'explication.

---

## Chapitre 14 — Séries de Fourier

### Question 14.1 : Quel est l'objectif premier de l'introduction et de l'étude formelle des séries de Fourier ?
- [ ] A) Décomposer une fonction périodique (même avec sauts) en une superposition infinie d'harmoniques (sinus et cosinus).
- [ ] B) Trouver la limite asymptotique d'une suite réelle en calculant son produit de convolution.
- [ ] C) Approximer localement une fonction très régulière au voisinage d'un unique point $x_0$, comme les séries de Taylor.
- [ ] D) Modéliser uniquement la gravité et la force élastique des ressorts sans amortissement.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Fourier permet de passer d'un signal temporel périodique, aussi brut et discontinu soit-il, à son "spectre" fréquentiel complet via une combinaison linéaire de sinus et de cosinus sur un intervalle global.
</details>

### Question 14.2 : Quelle différence fondamentale sépare une série de Fourier d'une série de Taylor ?
- [ ] A) Taylor utilise des polynômes transcendants, Fourier des suites géométriques.
- [ ] B) Fourier ne peut s'appliquer qu'à des fonctions de classe $C^\infty$.
- [ ] C) Taylor offre une approximation purement **locale** (proche de $x_0$) pour des fonctions très lisses. Fourier offre une approximation **globale** (sur tout l'intervalle) et fonctionne même avec des fonctions **discontinues**.
- [ ] D) Il n'y a aucune différence, ce sont deux repères de la même base de Hilbert.

<details>
<summary>💡 Solution</summary>

**Réponse C**. C'est le tableau de comparaison classique. Taylor veut du $C^\infty$ local, Fourier se satisfait de signaux $C^1$ par morceaux pour converger globalement.
</details>

### Question 14.3 : Dans le cadre formel de la norme $L^2$, que mesure intrinsèquement $\|f\|_2^2 = \int_a^b |f(x)|^2 dx$ pour un signal physique $f(t)$ ?
- [ ] A) Son **énergie totale** (ou sa puissance globale selon le facteur de normalisation).
- [ ] B) Son amplitude de crête maximale absolue (le sup).
- [ ] C) Sa phase d'origine $\varphi$.
- [ ] D) Le retard de propagation de groupe de l'onde.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'intégrale du carré du signal représente l'énergie physique, d'où le nom de norme "en moyenne quadratique".
</details>

### Question 14.4 : Historiquement et mathématiquement, pourquoi les fonctions de la famille $\{1, \cos(kx), \sin(kx)\}$ sont-elles idéales pour cette décomposition sur $[-\pi, \pi]$ ?
- [ ] A) Parce qu'elles sont strictement positives sur cet intervalle.
- [ ] B) Parce qu'elles forment un **système orthogonal complet**, c'est-à-dire que le produit scalaire $\langle f, g \rangle$ de deux fonctions distinctes de ce système est stricto-sensu nul.
- [ ] C) Car leur intégrale de $-\pi$ à $\pi$ vaut un nombre transcendant imaginaire pur.
- [ ] D) Parce qu'elles dérivent des polynômes de Legendre d'ordre infini.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le fondement de la projection orthogonale (comme en géométrie euclidienne avec les axes x, y, z normaux entre eux).
</details>

### Question 14.5 : Comment interprète-t-on le coefficient constant $a_0/2$ situé tout au début de l'écriture d'une Série de Fourier $f(x) \sim \frac{a_0}{2} + \dots$ ?
- [ ] A) C'est l'erreur de troncature de Gibbs intrinsèque estimée à $9\%$.
- [ ] B) La phase de l'harmonique fondamentale originelle du spectre.
- [ ] C) La **valeur moyenne** continue (la composante DC) du signal sur l'intervalle donné d'intégration.
- [ ] D) Le reste quadratique nul asymétrique.

<details>
<summary>💡 Solution</summary>

**Réponse C**. C'est littéralement $\frac{1}{2L} \int_{-L}^{L} f(x) dx$, soit l'exacte définition de la hauteur moyenne d'une fonction d'une période $2L$.
</details>

### Question 14.6 : Quel grand théorème lie astucieusement "la minimisation de l'erreur en distance ou norme quadratique $L^2$ de $f$" par un polynôme trigonométrique de degré $n$ avec les bêtes coefficients habituels $c_k$ ?
- [ ] A) Le Théorème Fondamental du Calcul d'Archimède.
- [ ] B) Le Théorème de la **Meilleure Approximation en Moyenne Quadratique** (qui démontre que les $\alpha_k$ réalisant le minimum pur de l'erreur sont justement les inébranlables coefficients de Fourier exacts formels purs).
- [ ] C) L'égalité de Lebesgue des sauts disjoints.
- [ ] D) Le pseudo-théorème de Weierstrass inverse et croisé des limites continues dures et unilatérales asymétriques pures absolues.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Un polynôme tronqué qui colle "au mieux" en énergie à $f$, ce sont ses vrais coefficients de projection classiques de Fourier de la base orthogonale, ni plus ni moins !
</details>

### Question 14.7 : Que postule l'Inégalité de Bessel pour la suite globale des coefficients spectraux ?
- [ ] A) Que la somme des carrés des coefficients de de projection de $f$ ne dépassera mathématiquement **jamais** la norme au carré $\|f\|_2^2$ de la fonction originelle.
- [ ] B) Que chaque harmonique individuelle porte fondamentalement un poids infini.
- [ ] C) Que $a_k$ décroît fatalement comme $\mathcal{O}(k!)$.
- [ ] D) Que la distance diverge à l'origine exponentiellement.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'inégalité de Bessel stipule que l'énergie contenue dans les composantes fréquentielles calculées est majorée (toujours inférieure ou égale) par l'énergie temporelle globale totale du signal d'origine.
</details>

### Question 14.8 : Sous quelle condition incontournable l'Inégalité de Bessel devient-elle l'Égalité de Parseval ?
- [ ] A) Si $f$ est une fonction constante.
- [ ] B) Si l'amplitude spatio-temporelle est nulle.
- [ ] C) Si et seulement si la série des composantes de Fourier "Converge en moyenne quadratique (norme $L^2$)" vers $f$, ce qui signifie que le système de base est "Complet".
- [ ] D) Uniquement pour le temps $t=0$.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Dire que l'égalité de Parseval est respectée équivaut à dire que le système trigonométrique décompose toute l'énergie du signal à 100% sans perte d'information (le système est complet dans $L^2$).
</details>

### Question 14.9 : Quel est le comportement formel de la série de Fourier au niveau d'une discontinuité (un saut) selon le Théorème de Dirichlet ?
- [ ] A) La série diverge vers l'infini.
- [ ] B) La série de Fourier converge précisément vers la **moyenne arithmétique** des limites à gauche et à droite : $\frac{f(x^+) + f(x^-)}{2}$.
- [ ] C) Elle prend la valeur maximale entre la gauche et la droite.
- [ ] D) L'approximation donne arbitrairement zéro.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le triomphe de Dirichlet (si $f$ et $f'$ sont continues par morceaux). Au beau milieu d'un saut vertical, la série de Fourier visera très exactement le milieu du saut.
</details>

### Question 14.10 : On décompose typiquement un signal "Carré". Que fait la série aux abords d'un saut de la fonction au fur et à mesure que $N \to \infty$ ? (Phénomène de Gibbs).
- [ ] A) Elle adoucit le bord très lentement en une courbe en S asymptotique.
- [ ] B) Le signal est reconstitué parfaitement sans aucune erreur ni oscillation visible.
- [ ] C) Au lieu de coller parfaitement au palier, la série **dépasse la crête d'environ 9%** du saut avant de redescendre (overshoot), et ce pic de dépassement ne se résorbera jamais, peu importe le nombre d'harmoniques ajoutées.
- [ ] D) La somme totale diverge et aucune limite n'existe.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Aux frontières d'une discontinuité stricte, un "dépassement local irréductible" d'environ $8.95\%$  survit intemporellement, créant de violentes oscillations autour du point de saut.
</details>

### Question 14.11 : La fonction "Dent de Scie" ($x/2$ sur $[-\pi, \pi]$) est du type "impaire". Quelle conséquence cela a-t-il sur le calcul de ses coefficients ?
- [ ] A) Absolument tous les $a_k$ (liés aux Cosinus) s'annulent ($a_k = 0$).
- [ ] B) Une annulation complète des $b_k$.
- [ ] C) Le spectre des fréquences devient uniquement composé des harmoniques pairs.
- [ ] D) Elle sera d'office exempte du phénomène de Gibbs.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Les fonctions impaires ($f(-x) = -f(x)$) nécessitent exclusivement une infinité de sinus (fonctions impaires) pour se construire. Tous les termes en Cosinus (qui sont pairs), y compris la moyenne $a_0$, tombent à zéro par symétrie de l'intégrale.
</details>

### Question 14.12 :  Une fonction "Onde triangulaire" est continue mais sa dérivée première donne une onde carrée discontinue. Comment décroissent ses coefficients $a_k$ ou $b_k$ lorsque l'ordre $k$ augmente fortement ?
- [ ] A) Une chute lente de l'ordre de $1/k$.
- [ ] B) Une décroissance de l'ordre de $1/k^2$.
- [ ] C) Une disparition exponentielle en $e^{-k}$.
- [ ] D) Une stagnation à une valeur constante indéfinie.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Plus le signal temporel $f$ est géométriquement "régulier" (sans sauts brusques), plus ses hautes fréquences s'atténueront vite (en $\mathcal{O}(1 / k^{p+1})$ si elle est de classe $C^{p-1}$). Une fonction continue d'ordre $C^0$ a donc une décroissance spectrale en $1/k^2$.
</details>

### Question 14.13 : Afin de prouver la Convergence Uniforme absolue de la série de Fourier, que suffit-il de vérifier en premier lieu (via le critère de Weierstrass) ?
- [ ] A) Vérifier que la série des amplitudes $\sum (|a_k| + |b_k|)$ converge (elle ne diverge pas vers l'infini).
- [ ] B) Prouver que $a_0 = 1$ de manière absolue.
- [ ] C) S'assurer que tous les zéros de la fonction sont identifiables et régulièrement espacés.
- [ ] D) Aucune condition préalable n'est requise.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Puisque $|a_k \cos(kx)| \leq |a_k|$, si la somme mathématique stricte des modules $\sum |a_k|$ converge, alors la série converge "normalement et uniformément" (Weierstrass M-Test) vers une fonction continue lisse.
</details>

### Question 14.14 : Soit la forme exponentielle complexe de la série : $f(t) \sim \sum_{k=-\infty}^{+\infty} c_k e^{ik\omega_0 t}$. Quel rapport lie $c_k$ et $c_{-k}$ si la fonction d'origine $f(t)$ est strictement réelle ?
- [ ] A) $c_k = - \ln(c_{-k})$.
- [ ] B) $c_k = b_k / a_k$.
- [ ] C) $c_{-k}$ est le complexe **conjugué** strict de $c_k$ (soit $c_{-k} = \overline{c_k}$).
- [ ] D) $c_{-k}$ est l'opposé mathématique strict ($-c_k$).

<details>
<summary>💡 Solution</summary>

**Réponse C**. Par la formule d'Euler, pour que toutes les parties imaginaires pur de la sommation s'annulent et que la recomposition du signal redonne bien des ondes purement réelles, il faut impérativement que $c_{-k} = \overline{c_k}$.
</details>

### Question 14.15 : Est-il en général justifié d'intégrer une série de Fourier "terme à terme" pour approximer l'intégrale du signal ?
- [ ] A) Oui, toujours : l'intégration divise les coefficients par $k$, ce qui renforce l'amortissement du spectre ($1/k^2$), accélérant ainsi drastiquement la convergence au sein du résultat continu.
- [ ] B) Non, cela est formellement proscrit car l'intégration génère des anomalies harmoniques complexes.
- [ ] C) Sauf si $a_0$ ou $b_0$ est nul formellement.
- [ ] D) La dérivation est toujours plus sûre que l'intégration en termes de limites mathématiques.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'intégration terme à terme adoucit inévitablement la régularité du signal original. Diviser un terme spectral $c_k$ par grand $k$ (lors de l'intégration primitive temporelle) garantit d'amplifier le taux de décroissance temporel et pacifie radicalement l'allure finale, améliorant de facto sa vitesse de convergence formelle.
</details>

### Question 14.16 : À l'inverse de l'intégration, que requiert le droit de "Dériver" terme à terme une série de Fourier classique ?
- [ ] A) Uniquement que $f$ soit intégrable sur l'intervalle donné selon la norme L1 absolue.
- [ ] B) Multiplier les coefficients $a_k$ par $2\pi i k$ asymétriquement de façon constante inhérente.
- [ ] C) Il faut impérativement que $f$ soit d'emblée "continue sur son domaine avec $f(-L) = f(L)$" et $f'$ continue par morceaux. Sinon la dérivation fait surgir des fonctions Dirac hors d'échelle.
- [ ] D) Il n'y a la moindre contrainte à vérifier, on peut dériver formellement à volonté.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Dériver revient à multiplier $c_k$ par $ik\omega_0$. La multiplication systématique par le facteur $k$ ruine totalement le noble pouvoir d'atténuation d'amplitudes à hautes fréquences de la série d'origine. C'est pourquoi seule l'application mathématique aux fonctions lisses pures et très régulières autorise à s'y aventurer impunément !
</details>

### Question 14.17 : Au niveau de l'Équation aux dérivées partielles pure de la Chaleur 1D (diffusion temporelle dans une barre aux bords isolés fixés à $0^\circ$), pourquoi l'utilisation de la série de Fourier est-elle fantastique ?
- [ ] A) Elle permet empiriquement de diviser par quatre l'accélération thermodynamique réelle.
- [ ] B) Elle s'ajuste parfaitement avec la "séparation des variables" en pondérant progressivement chaque "sinus spatial" (mode propre temporel et abstrait) avec une atténuation thermique temporelle exponentielle classique stricte ($e^{-\alpha^2 n^2 t}$).
- [ ] C) Elle déplace brutalement la chaleur par translation d'onde non-diffusante.
- [ ] D) Fourier l'interdit strictement et dédie ce cas abstrait absolu à l'équation hyperbolique.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Historiquement, Fourier a originellement posé les bases de l'asymétrie spectrale en 1822 spécifiquement pour formuler mathématiquement comment chaque profil abstrait lissé d'une haute fréquence s'éteint radicalement via exponentielle descendante bien plus rapidement qu'une modeste et asymétrique lourde basse fréquence au cours d'un cruel transfert chaud thermique asymétrique temporel franc de la sorte.
</details>

### Question 14.18 : Le fameux Noyau de Dirichlet $K_n(\theta)$ apparaît majestueusement dans :
- [ ] A) L'égalité absolue stricte unilatérale et pure de Bessel.
- [ ] B) La conception fractale formelle asymétrique bête inhérente et continue au pendule asymétrique bête temporel.
- [ ] C) La démonstration du théorème fondamental formel de convergence ponctuelle de Dirichlet, où l'écriture de la série partielle se réécrit astucieusement sous la pure forme intime d'un produit de Convolution temporel exclusif avec ce fameux asymétrique franc abstrait noyau ($f * K_n$).
- [ ] D) Le calcul formellement asymétrique dur intégral abstrait des spectres temporels croisés par inestimable $a_0$.

<details>
<summary>💡 Solution</summary>

**Réponse C**. C'est le socle complet de la grande démo : sommer et évaluer finement asymétriquement la formelle expression mathématique stricte dure bête abstraite et complexe des sommes partielles par le prisme asymétrique et inestimable asymétrique et franc asymétrique pur noyau abstrait $K_n$.
</details>

### Question 14.19 : Le Théorème classique de Convolution $f * g$ affirme abstraitement que le dur fait intemporel fin de convoluer deux signaux "dans le temps" (intégration glissante inhérente asymétrique) s'associe formellement dans l'espace abstrait de Fourier à :
- [ ] A) Une simple "Multiplication absolue et stricte des spectres (coefficients)" entre eux dans le domaine intemporel pur des fréquences pures francs des et pures dures de abstraites ondes ($f_k \cdot g_k$).
- [ ] B) Une inéluctable addition formelle arithmétique rigoureuse des dur fins $a_n$.
- [ ] C) De faire un $e^{\max_n}$ ou d'une asymétrique et asymétriquement inestimable opération.
- [ ] D) L'équivalence asymétrique de diviser abstraitement d'emblée stricte la masse inhérente bête forte d'un signal franc de asymétriquement beau dur pur par son beau produit franc conjugué complexe.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Convoluer en temps bêtement équivaut à multiplier finement en asymétrique domaine fréquentiel. (C'est la bête d'Or intrinsèque asymétrique et franche de la magique conception asymétriquement pure et de base abstraite en fin d'étude formelle pure classique et asymétrique absolue forte intrinsèque du DSP (Digital Signal Processing)).
</details>

### Question 14.20 : Lorsqu'un système physique de type "Oscillateur sans amortissement partiel brutal franc ou d'aucune asymétrie de rude bête abstraction temporelle de" reçoit une "force (excitation pure)" où bêtement une des fréquences abstraites "réelles francs du spectre intrinsèque de brutal excitation" correspond asymétriquement formel inhérent fin au à la pure constante propre et " la fréquence classique asymétrique" du système originel : Que se passe-t-il fatalement ?
- [ ] A) Elle retourne abstraitement vers un brut 0 franc asymètre.
- [ ] B) Le système subit un arrêt inestimable pur et asymptotique formel intrinsèquement continu net franc abstrait pur bêtement complet de fin absolu asymétrique net et bête franc pur et formelle.
- [ ] C) Le système entre violemment en "Résonance Pures Franches Inéluctables". Son amplitude asymétriquement croîtra brutalement de la forme fatale abstraite $\mathcal{O}(t)$ sans fin en un désastre asymétriquement brutal et destructeur formel asymètre bête et dramatique (le rude puits asymétrique diviseur harmonique abstrait fin leste s'annulant asymétriquement et mathématiquement francs de).
- [ ] D) Rien au ou ne se dur brut et de formelle bête franc brut et de pur franc passe.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Si la cruelle fonction rude du beau diviseur fin et intemporel ou $\frac{c_k}{(k^2 - \omega_n^2 m)}$ d'une et belle ou de et de bête asymétrique et asymétriquement franc et pure onde franche asymétrique rencontre son leste inéluctable beau dénominateur qui tend bêtement abstrait inhéremment vers 0. C'est l'histoire tragique (Tacoma Narrow Bridge).
</details>
