# ✅ Quiz / QCM — Physique (PHYSH1002)

> Quiz avec questions à choix multiples pour réviser chaque chapitre.
> Cliquez sur **💡 Solution** pour vérifier votre réponse et voir l'explication.

---

## Chapitre 1 — Gradient

### Question 1.1 : Quelle est la principale propriété géométrique du gradient d'une fonction scalaire ?
- [ ] A) Il est toujours tangent aux courbes de niveau.
- [ ] B) Il pointe dans la direction où la fonction décroît le plus vite.
- [ ] C) Son rotationnel n'est jamais nul.
- [ ] D) Il est toujours perpendiculaire aux surfaces équipotentielles.

<details>
<summary>💡 Solution</summary>

**Réponse D**. Le gradient $\vec{\text{grad}}\, f$ est toujours orthogonal aux courbes de niveau (ou surfaces équipotentielles en 3D) et pointe vers la direction de croissance maximale.
</details>

### Question 1.2 : Comment calcule-t-on la dérivée directionnelle de $f$ selon une direction $\vec{u}$ (unitaire) ?
- [ ] A) $\frac{\partial f}{\partial \vec{u}} = \vec{\text{grad}}\, f \cdot \vec{u}$
- [ ] B) $\frac{\partial f}{\partial \vec{u}} = \vec{\text{grad}}\, f \times \vec{u}$
- [ ] C) $\frac{\partial f}{\partial \vec{u}} = \text{div}(\vec{\text{grad}}\, f) \cdot \vec{u}$
- [ ] D) $\frac{\partial f}{\partial \vec{u}} = \|\vec{\text{grad}}\, f\|$

<details>
<summary>💡 Solution</summary>

**Réponse A**. La dérivée directionnelle est le produit scalaire entre le gradient et le vecteur unitaire définissant la direction.
</details>

### Question 1.3 : Que vaut toujours le rotationnel d'un champ qui dérive d'un potentiel (i.e., un gradient) ?
- [ ] A) Une constante non nulle
- [ ] B) Le laplacien du potentiel
- [ ] C) Le vecteur nul ($\vec{0}$)
- [ ] D) Le gradient de la divergence

<details>
<summary>💡 Solution</summary>

**Réponse C**. Par identité vectorielle fondamentale, $\text{rot}(\vec{\text{grad}}\, V) = \vec{0}$. C'est la signature d'un champ conservatif.
</details>

### Question 1.4 : En coordonnées cylindriques $(r, \theta, z)$, quelle est l'expression correcte du gradient de $f$ ?
- [ ] A) $\frac{\partial f}{\partial r}\vec{1}_r + \frac{\partial f}{\partial \theta}\vec{1}_\theta + \frac{\partial f}{\partial z}\vec{1}_z$
- [ ] B) $\frac{\partial f}{\partial r}\vec{1}_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec{1}_\theta + \frac{\partial f}{\partial z}\vec{1}_z$
- [ ] C) $\frac{\partial f}{\partial r}\vec{1}_r + r\frac{\partial f}{\partial \theta}\vec{1}_\theta + \frac{\partial f}{\partial z}\vec{1}_z$
- [ ] D) $\frac{\partial f}{\partial r}\vec{1}_r + \frac{1}{r\sin\theta}\frac{\partial f}{\partial \theta}\vec{1}_\theta + \frac{\partial f}{\partial z}\vec{1}_z$

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est la bonne définition. Ne pas oublier le facteur $1/r$ devant la dérivée partielle angulaire $\theta$ car $dl_\theta = r d\theta$.
</details>

### Question 1.5 : Quelle force fondamentale s'exprime par $\vec{F} = -\vec{\text{grad}}\, V$ ?
- [ ] A) Seulement la force électrostatique
- [ ] B) Seulement la force gravitationnelle
- [ ] C) Toute force conservative
- [ ] D) La force de frottement visqueux

<details>
<summary>💡 Solution</summary>

**Réponse C**. Toute force conservative (dont le travail sur un chemin fermé est nul) dérive d'une énergie potentielle scalaire $V$. Électrique et gravitationnelle en sont de parfaits exemples.
</details>

---

## Chapitre 2 — Flux Circulation

### Question 2.1 : Que mesure la divergence d'un champ vectoriel ?
- [ ] A) Sa tendance à tourner autour d'un point.
- [ ] B) Sa densité de flux, indiquant la présence de sources ou de puits.
- [ ] C) L'énergie totale contenue dans le champ.
- [ ] D) Sa différence de potentiel entre deux points.

<details>
<summary>💡 Solution</summary>

**Réponse B**. La divergence mesure si un point spécifique génère du flux ($\text{div} > 0$, source) ou en absorbe ($\text{div} < 0$, puits).
</details>

### Question 2.2 : Le Théorème de Stokes relie deux intégrales, lesquelles ?
- [ ] A) Le flux à la circulation
- [ ] B) Le flux de la divergence à l'intégrale volumique
- [ ] C) La circulation du gradient au flux
- [ ] D) La circulation d'un champ sur un contour fermé au flux de son rotationnel à travers la surface bordée.

<details>
<summary>💡 Solution</summary>

**Réponse D**. C'est l'essence du théorème de Stokes : $\oint_C \vec{A} \cdot d\vec{\ell} = \iint_{S_C} \text{rot}\,\vec{A} \cdot d\vec{S}$.
</details>

### Question 2.3 : Et le Théorème de la Divergence (Gauss-Ostrogradski) ?
- [ ] A) Le flux d'un champ à travers une surface fermée égale l'intégrale volumique de sa divergence.
- [ ] B) La circulation d'un champ sur un contour égale sa divergence volumique.
- [ ] C) Le rotationnel d'un flux est toujours nul sur une surface ouverte.
- [ ] D) L'intégrale de volume du champ égale l'intégrale de surface du rotationnel.

<details>
<summary>💡 Solution</summary>

**Réponse A**. $\oiint_S \vec{A} \cdot d\vec{S} = \iiint_V \text{div}\,\vec{A} \,dV$.
</details>

### Question 2.4 : L'équation de continuité pour la conservation de la charge s'écrit :
- [ ] A) $\text{div}\,\vec{E} = \rho/\varepsilon_0$
- [ ] B) $\frac{\partial \vec{J}}{\partial t} + \text{rot}\,\rho = 0$
- [ ] C) $\frac{\partial \rho}{\partial t} + \text{div}\,\vec{J} = 0$
- [ ] D) $\text{rot}\,\vec{J} = -\frac{\partial \rho}{\partial t}$

<details>
<summary>💡 Solution</summary>

**Réponse C**. Loi fondamentale de conservation locale : la variation temporelle de la densité de charge compense exactement le courant qui diverge de ce point.
</details>

### Question 2.5 : Que dire du rotationnel si un champ vectoriel est solénoïdal ($\text{div}\,\vec{A} = 0$) ?
- [ ] A) Le rotationnel est nul.
- [ ] B) Le champ $\vec{A}$ peut s'écrire comme le rotationnel d'un potentiel vecteur ($\vec{A} = \text{rot}\,\vec{B}$).
- [ ] C) Le champ est nécessairement conservatif.
- [ ] D) Le théorème de Stokes ne s'applique plus.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Par l'identité vectorielle $\text{div}(\text{rot}\,\vec{V}) = 0$, tout champ dont la divergence est strictement nulle peut être exprimé comme le rotationnel d'un autre champ. C'est le cas du champ magnétique $\bar{B}$.
</details>

---

## Chapitre 3 — Loi de Faraday

### Question 3.1 : Quelle est l'expression complète de la force de Lorentz subie par une charge $q$ de vitesse $\vec{v}$ ?
- [ ] A) $\vec{F}_L = q\vec{E} \times \bar{B}$
- [ ] B) $\vec{F}_L = q(\bar{B} + \vec{v} \times \vec{E})$
- [ ] C) $\vec{F}_L = q(\vec{E} + \vec{v} \times \bar{B})$
- [ ] D) $\vec{F}_L = \frac{q}{\varepsilon_0}(\vec{E} + \bar{B})$

<details>
<summary>💡 Solution</summary>

**Réponse C**. La charge interagit avec le champ électrique linéairement et avec le champ magnétique via un produit vectoriel avec la vitesse.
</details>

### Question 3.2 : Est-ce que la force magnétique effectue un travail sur une particule libre ?
- [ ] A) Oui, toujours.
- [ ] B) Oui, mais seulement si la charge accélère en ligne droite.
- [ ] C) Non, jamais, car elle est toujours perpendiculaire à la vitesse.
- [ ] D) Non, sauf dans les matériaux diamagnétiques.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le produit scalaire $\vec{F}_M \cdot d\vec{s} = (q\vec{v} \times \bar{B}) \cdot (\vec{v}dt) = 0$. La force magnétique modifie la direction (tourne) mais ne modifie pas le module de la vitesse (ne change pas l'énergie cinétique).
</details>

### Question 3.3 : Dans la forme locale de la loi de Faraday ($\text{rot}\,\vec{E} = -\frac{\partial \bar{B}}{\partial t}$), que peut-on affirmer sur le champ électrique induit ?
- [ ] A) Il s'agit d'un champ conservatif (il dérive d'un potentiel).
- [ ] B) Il pointe toujours dans la même direction que $\bar{B}$.
- [ ] C) Il est non conservatif, sa circulation sur un chemin fermé produit l'é.m.f.
- [ ] D) Il ne s'exerce que sur des tiges en mouvement.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Puisque $\text{rot}\,\vec{E} \neq 0$, le champ n'est pas un simple gradient, son travail sur une boucle fermée est non nul.
</details>

### Question 3.4 : On exprime le champ électrique avec les potentiels selon :
- [ ] A) $\vec{E} = -\vec{\text{grad}}\, V - \frac{\partial \vec{A}}{\partial t}$
- [ ] B) $\vec{E} = -\vec{\text{grad}}\, V + \text{rot}\,\vec{A}$
- [ ] C) $\vec{E} = \text{div}\,\vec{A} - \frac{\partial V}{\partial t}$
- [ ] D) $\vec{E} = \vec{\text{grad}}\, A - \frac{\partial V}{\partial t}$

<details>
<summary>💡 Solution</summary>

**Réponse A**. Cette expression montre la part statique (conservative, $\vec{\text{grad}}\, V$) et la part de l'induction (non conservative, dynamique grâce au potentiel vecteur $\vec{A}$).
</details>

### Question 3.5 : L'électromotance d'un disque tournant (dynamo de Faraday) est due à...
- [ ] A) La variation du flux $\bar{B}$ car l'aimant s'approche.
- [ ] B) La force de Lorentz (magnétique) séparant les charges de conduction à l'intérieur du disque animé d'une vitesse purement mécanique.
- [ ] C) La conversion directe de la chaleur Joule en tension.
- [ ] D) Un effet purement électrostatique.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est l'électromotance "de mouvement". Le disque tourne, chaque électron est entraîné à la vitesse $\vec{v} = \vec{\omega} \times \vec{r}$, subit $q \vec{v} \times \bar{B}$ radialement, ce qui force un courant entre le centre et la périphérie de la roue.
</details>

---

## Chapitre 4 — Ampère, Maxwell, Lenz

### Question 4.1 : Quel terme Maxwell a-t-il ajouté à la loi d'Ampère ?
- [ ] A) La divergence de la charge
- [ ] B) Le courant de déplacement ($\mu_0\varepsilon_0 \frac{\partial \vec{E}}{\partial t}$)
- [ ] C) La conservation du flux magnétique
- [ ] D) Le potentiel vecteur $\vec{A}$

<details>
<summary>💡 Solution</summary>

**Réponse B**. Maxwell a découvert que l'équation d'Ampère originale imposait une divergence nulle du courant, interdisant le rechargement d'un condensateur. Y ajouter la dérivée temporelle de $\vec{E}$ résout cette ambiguïté (rétablissement de l'équation de continuité globale).
</details>

### Question 4.2 : Quelle est la conséquence principale de la « Symétrie Faraday–Ampère » dans le vide ?
- [ ] A) La dualité onde-corpuscule des atomes matériels.
- [ ] B) Le besoin impératif d'éther pour la propagation EM.
- [ ] C) L'existence potentielle des ondes électromagnétiques où $\vec{E}$ et $\bar{B}$ s'engendrent mutuellement.
- [ ] D) La stabilité temporelle exclusive des forces statiques.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Les variations de $\vec{E}$ génèrent un $\bar{B}$ ondulatoire, qui en variant regénère $\vec{E}$ un peu plus loin, formant la source des phénomènes autopropagés constituant la lumière rayonnante.
</details>

### Question 4.3 : La loi de Lenz dicte que :
- [ ] A) Le courant induit a un sens tel que ses effets s'opposent à la cause qui lui a donné naissance (ex: variation de flux).
- [ ] B) Le flux s'amplifie exponentiellement avec le temps.
- [ ] C) Les forces magnétiques travaillent proportionnellement à l'induction $\mathcal{E}$.
- [ ] D) Les aimants pointent toujours vers l'Est induit par effet Foucault.

<details>
<summary>💡 Solution</summary>

**Réponse A**. C'est tout le secret du repoussement/attraction inductif d'un aimant à l'approche de la spire et c'est une traduction fidèle du principe global de conservation de l'énergie de l'univers.
</details>

### Question 4.4 : Le diamagnétisme, observable en approchant un aimant près d'un métal parfait ou matériau apparié (exeau ou grenouille), crée toujours une force...
- [ ] A) Nulle.
- [ ] B) Transverse.
- [ ] C) Attractive.
- [ ] D) Répulsive.

<details>
<summary>💡 Solution</summary>

**Réponse D**. Par la loi de Lenz au format infiniment microscopique (déformation orbitale subie par $\partial \bar{B}/\partial t$), la réaction diamagnétique s'oppose intrinsèquement et repousse l'action initiale.
</details>

### Question 4.5 : Une des 4 équations s'écrit $\text{div}\,\bar{B} = 0$. Que traduit ce principe fondamental de la nature ?
- [ ] A) Les charges magnétiques quantifiées pullulent dans l'univers lointain.
- [ ] B) L'absence observée (jusqu'ici) de monopôle magnétique isolé ; le champ se reboucle toujours inlassablement.
- [ ] C) Le champ EM ne peut exister intrinsèquement isolé loin des courants cosmiques.
- [ ] D) La masse inertielle ne dépend pas de son accélération angulaire de Fourier.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Cela implique le rebouclage inéluctable strict des lignes quantitatives de $\bar{B}$. Chaque pôle N correspond inexorablement sur place à son ombrelle opposée S connectée à l'horizon des bobinages générateurs infinitésimaux de Dirac.
</details>

---

## Chapitre 5 — Dynamique des Circuits

### Question 5.1 : Quelle est l'expression de l'énergie stockée par magnétisme dans une inductance $L$ traversée par $I$ ?
- [ ] A) $W_L = \frac{1}{2}\frac{L^2}{I}$
- [ ] B) $W_L = L \cdot I$
- [ ] C) $W_L = \frac{1}{2}LI^2$
- [ ] D) $W_L = \frac{1}{2\mu_0}LI^2$

<details>
<summary>💡 Solution</summary>

**Réponse C**. Par analogie stricte au condensateur à savoir $W_C = \frac{1}{2}CV^2$.
</details>

### Question 5.2 : Dans un circuit RL en charge alimenté par un échelon E, que devient l'é.m.f d'auto-induction de la bobine de choc à long terme ($t \to \infty$) ?
- [ ] A) L'auto-induction s'estompe jusqu'à devenir parfaitement $0$V car le régime permanent en courant continu implique un $dI/dt=0$.
- [ ] B) Elle conserve intrinsèquement ses $V = E$.
- [ ] C) L'ensemble décharge un mode purement exponentiel décroissant indéterminé non bornable à long terme (infini).
- [ ] D) Impédance infinie.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'inducteur n'offre aucune résistance aux courants permanents DC non-fluctuants. Sans fluctuation $dI/dt$, la tension résistantiale d'opposition de Faraday n'apparaît tout simplement et logiquement jamais.
</details>

### Question 5.3 : Un transformateur "idéal" modifie drastiquement $V$ et $I$. Quelle grandeur fondamentale conserve-t-il obligatoirement entre primaire et secondaire ?
- [ ] A) Impédance
- [ ] B) La Puissance électrique active (à chaque instant)
- [ ] C) Le Ratio des tours
- [ ] D) Le Flux unitaire total

<details>
<summary>💡 Solution</summary>

**Réponse B**. $P_{in} = P_{out}$. Par conséquent stricto-sensu $V_1 I_1 = V_2 I_2$ sur ces composantes idéales d'acheminement réseau.
</details>

### Question 5.4 : Pour un courant alternatif sinusoïdal classique, on a $V_{\text{eff}} = 230$ V. À quoi correspond l'amplitude crête maximale $V_m$ ?
- [ ] A) $V_m = 230 / \sqrt{3}$
- [ ] B) $V_m = 230$
- [ ] C) $V_m = 230 \times \sqrt{2}$
- [ ] D) $V_m = 230 \times \pi$

<details>
<summary>💡 Solution</summary>

**Réponse C**. $V_{\text{eff}}$ d'une simple sinusoïde vaut inexorablement $V_m / \sqrt{2}$. Donc la valeur maximale atteinte temporairement par nos prises en pointe européenne tutoit farouchement les presque $325$ Volts crête sur crête alternée.
</details>

### Question 5.5 : Le fonctionnement qualitatif d'une self (bobine inductance) en réseau de fréquence alternative tend à :
- [ ] A) Agir invariablement comme simple court-circuit invisible inopportun.
- [ ] B) Devenir un simple filtre haut, favorisant globalement les parasites HF.
- [ ] C) Freiner d'autant plus les hautes fréquences, s'opposant vivement comme un filtre « passe-bas ».
- [ ] D) Déphaser radicalement la source sur l'effet capacitif anticipé direct net du cosinus ambiant local de rémanence.

<details>
<summary>💡 Solution</summary>

**Réponse C**. L'impédance de la self $Z_L = i\omega L$ est fondamentalement proportionnelle à $\omega$. Aux hautes fréquences son effet résistif (bouchon) grandit et étouffe mathématiquement le passage intensif (d'où l'appellation générique et classique de "bobine de choc anti-parasite passe-bas").
</details>

---

## Chapitre 6 — Oscillateurs harmoniques et amortis

### Question 6.1 : Quelle est l'équation différentielle caractéristique d'un oscillateur harmonique simple non amorti ?
- [ ] A) $\frac{d^2x}{dt^2} + \omega_0 x = 0$
- [ ] B) $\frac{d^2x}{dt^2} + \omega_0^2 x = 0$
- [ ] C) $\frac{dx}{dt} + \omega_0 x = 0$
- [ ] D) $\frac{d^2x}{dt^2} - \omega_0^2 x = 0$

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est l'équation fondamentale de l'oscillateur harmonique où $\omega_0 = \sqrt{k/m}$ est la pulsation propre (en rad/s). La solution est de la forme $x(t) = A\cos(\omega_0 t + \phi)$.
</details>

### Question 6.2 : Dans un système masse-ressort, de quels paramètres dépend la fréquence propre $f_0$ ?
- [ ] A) Uniquement de la masse $m$.
- [ ] B) Uniquement de l'amplitude initiale.
- [ ] C) De la constante de raideur $k$ et de la masse $m$.
- [ ] D) De la masse $m$, de $k$ et de la gravité $g$.

<details>
<summary>💡 Solution</summary>

**Réponse C**. La fréquence $f_0 = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$. L'amplitude n'affecte pas la fréquence (isochronisme des oscillations) et la gravité déplace seulement la position d'équilibre, pas la fréquence.
</details>

### Question 6.3 : Quel est l'effet d'une force de frottement visqueux $\vec{F} = -b\vec{v}$ sur les oscillations (régime sous-critique) ?
- [ ] A) L'amplitude reste constante mais la fréquence diminue.
- [ ] B) L'amplitude décroît de manière linéaire et la fréquence augmente.
- [ ] C) L'amplitude décroît de manière exponentielle et la pseudo-pulsation est inférieure à la pulsation propre.
- [ ] D) Le système s'arrête instantanément sans osciller.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Dans le régime pseudo-périodique (sous-critique), l'amplitude décroît en $e^{-\alpha t}$ et le système oscille à une pseudo-pulsation $\omega_a = \sqrt{\omega_0^2 - \alpha^2}$, qui est strictement inférieure à $\omega_0$.
</details>

### Question 6.4 : Qu'est-ce que le régime d'amortissement critique ?
- [ ] A) Le régime où le système oscille éternellement avec une amplitude constante.
- [ ] B) Le régime où l'amortissement est si faible que les pertes sont négligeables.
- [ ] C) Le régime où le système met un temps infini à rejoindre sa position d'équilibre.
- [ ] D) Le régime assurant le retour le plus rapide à la position d'équilibre sans aucune oscillation.

<details>
<summary>💡 Solution</summary>

**Réponse D**. Le régime critique ($\alpha = \omega_0$) est la frontière entre le régime pseudo-périodique et apériodique. Il permet le retour optimal et le plus rapide à l'équilibre (utilisé pour les amortisseurs de voiture ou les portes battantes).
</details>

### Question 6.5 : Comment évolue l'énergie mécanique totale d'un oscillateur harmonique non amorti en fonction du temps ?
- [ ] A) Elle oscille sinusoïdalement à la pulsation $\omega_0$.
- [ ] B) Elle est nulle à la position d'équilibre.
- [ ] C) Elle est constante au cours du temps.
- [ ] D) Elle décroît exponentiellement.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Sans frottement (forces non conservatives absentes), l'énergie mécanique $E = E_c + E_p = \frac{1}{2}mv^2 + \frac{1}{2}kx^2$ est strictement conservée. L'énergie cinétique se transforme en énergie potentielle et inversement, mais leur somme reste constante.
</details>

---

## Chapitre 7 — Oscillateur linéaire amorti forcé et résonance

### Question 7.1 : Qu'observe-t-on lors du phénomène de résonance d'amplitude dans un oscillateur forcé ?
- [ ] A) L'amplitude des oscillations devient infinie, indépendamment de l'amortissement.
- [ ] B) L'amplitude des oscillations passe par un maximum lorsque la fréquence d'excitation est proche de la fréquence propre.
- [ ] C) Le déphasage entre la force excitatrice et le déplacement s'annule exactement.
- [ ] D) L'oscillateur s'arrête de bouger car la force excitatrice est compensée par la force de rappel.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est la définition de la résonance. Plus l'amortissement est faible, plus le pic d'amplitude est haut et étroit, et se rapproche exactement de $\omega_0$.
</details>

### Question 7.2 : Que vaut le déphasage $\phi$ entre l'élongation $x(t)$ et la force excitatrice $F(t)$ à la stricte résonance de vitesse ?
- [ ] A) $\phi = 0$
- [ ] B) $\phi = \pi/2$ (quadrature de phase)
- [ ] C) $\phi = \pi$ (opposition de phase)
- [ ] D) $\phi = 2\pi$

<details>
<summary>💡 Solution</summary>

**Réponse B**. À la résonance, la force excitatrice compense exactement la force de frottement. La force est alors en phase avec la vitesse, et donc en quadrature de phase ($\pi/2$) avec l'élongation.
</details>

### Question 7.3 : Qu'est-ce que le facteur de qualité $Q$ pour un oscillateur harmonique ?
- [ ] A) Il quantifie la masse du système $m$.
- [ ] B) Il est proportionnel au taux d'amortissement $\alpha$.
- [ ] C) Il caractérise l'acuité de la résonance et est inversement proportionnel à l'amortissement.
- [ ] D) Il représente l'énergie totale du système.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le facteur de qualité $Q = \frac{\omega_0}{2\alpha}$ (ou $Q = 2\pi\frac{E_{stockee}}{E_{dissipee\_par\_cycle}}$). Un $Q$ élevé indique de très faibles pertes visqueuses, un pic de résonance très aigu, et un grand nombre d'oscillations libres avant l'arrêt.
</details>

### Question 7.4 : Dans l'analogie électromécanique, à quelle grandeur mécanique correspond l'inductance $L$ d'un circuit RLC ?
- [ ] A) À la raideur du ressort $k$.
- [ ] B) À la masse inertielle $m$.
- [ ] C) Au coefficient de frottement visqueux $b$.
- [ ] D) À la force excitatrice $F(t)$.

<details>
<summary>💡 Solution</summary>

**Réponse B**. L'inductance s'oppose aux variations du courant ($V_L = -L\frac{di}{dt}$), tout comme la masse s'oppose aux variations de vitesse (inertie, $F = m\frac{dv}{dt}$).
</details>

### Question 7.5 : Quel est l'effet de l'augmentation de la résistance $R$ sur la courbe de résonance d'un circuit RLC série ?
- [ ] A) La résonance devient plus aiguë et la fréquence de résonance augmente.
- [ ] B) Le pic de résonance s'élargit et la tension maximale diminue.
- [ ] C) La courbe de résonance n'est pas modifiée, seul le déphasage change.
- [ ] D) La résonance disparaît immédiatement et le circuit devient continu.

<details>
<summary>💡 Solution</summary>

**Réponse B**. $R$ est la dissipation. Un amortissement plus grand (pertes Joule) écrase le pic d'amplitude (diminue le facteur de qualité) et élargit la bande passante $\Delta\omega = R/L$.
</details>

---

## Chapitre 8 — Ondes de corde et de compression

### Question 8.1 : Quelle expression décrit une onde progressive se déplaçant vers les $x$ positifs sans déformation ?
- [ ] A) $y(x,t) = f(x + vt)$
- [ ] B) $y(x,t) = f(vx - t)$
- [ ] C) $y(x,t) = f(x - vt)$
- [ ] D) $y(x,t) = f(x)g(t)$

<details>
<summary>💡 Solution</summary>

**Réponse C**. L'argument $(x - vt)$ assure que si $t$ augmente, $x$ doit augmenter pour conserver une même phase constante, décrivant bien une translation rigide vers les $x$ positifs.
</details>

### Question 8.2 : Quelle est la vitesse de propagation $v$ d'une onde transversale sur une corde tendue ?
- [ ] A) $v = T \cdot \mu$
- [ ] B) $v = \sqrt{T/\mu}$
- [ ] C) $v = \sqrt{\mu/T}$
- [ ] D) $v = \mu \cdot T^2$

<details>
<summary>💡 Solution</summary>

**Réponse B**. La vitesse dépend de la tension (la force de rappel intermoléculaire) et inversement de l'inertie linéaire globale $\mu$ (masse linéique).
</details>

### Question 8.3 : Comment se relient la vitesse $c$, la fréquence $f$ et la longueur d'onde $\lambda$ ?
- [ ] A) $\lambda = c \cdot f$
- [ ] B) $c = \lambda \cdot f$
- [ ] C) $c = \lambda / f^2$
- [ ] D) $f = c \cdot \lambda$

<details>
<summary>💡 Solution</summary>

**Réponse B**. En une seconde, l'onde génère $f$ cycles, chacun mesurant $\lambda$ mètres. L'onde couvre donc au total $f \times \lambda$ mètres par seconde.
</details>

### Question 8.4 : L'équation d'onde classique de D'Alembert s'écrit sous la forme :
- [ ] A) $\frac{\partial y}{\partial t} = D \frac{\partial^2 y}{\partial x^2}$
- [ ] B) $\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}$
- [ ] C) $\frac{\partial^2 y}{\partial x^2} + \frac{\partial y}{\partial t} = 0$
- [ ] D) $\nabla^2 y = \frac{1}{v} \frac{\partial y}{\partial t}$

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est l'équation des ondes non dispersives où la dérivée seconde temporelle est proportionnelle à la courbure spatiale. (La réponse A correspond à l'équation de diffusion/chaleur).
</details>

### Question 8.5 : De quoi dépend la vitesse du son (onde longitudinale) dans un fluide ?
- [ ] A) De la masse molaire uniquement.
- [ ] B) Uniquement de la densité métrique du gaz.
- [ ] C) De la racine carrée du rapport entre le module de compressibilité volumique $B$ et la masse volumique $\rho$ ($v = \sqrt{B/\rho}$).
- [ ] D) De la pression atmosphérique divisée par la température.

<details>
<summary>💡 Solution</summary>

**Réponse C**. La célérité acoustique macroscopique est formellement liée à la rigidité élastique du milieu (Bulk modulus $B$) et son inertie massique globale ($\rho$).
</details>

---

## Chapitre 9 — Ondes électromagnétiques

### Question 9.1 : Maxwell a unifié l'optique et l'électromagnétisme en calculant la vitesse théorique des ondes EM dans le vide. Quelle est sa valeur ?
- [ ] A) $c = 1 / \sqrt{\mu_0 \cdot \epsilon_0}$
- [ ] B) $c = \mu_0 \cdot \epsilon_0$
- [ ] C) $c = \sqrt{\mu_0 / \epsilon_0}$
- [ ] D) $c = 1 / (\mu_0 \cdot \epsilon_0)$

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'équation d'onde pour $\vec{E}$ et $\vec{B}$ dérivée des équations de Maxwell montre que la célérité formelle de l'onde est liée aux constantes fondamentales du vide par cette relation stricte.
</details>

### Question 9.2 : Quelle est la caractéristique géométrique des vecteurs $\vec{E}$, $\vec{B}$ et $\vec{k}$ (vecteur d'onde) dans une onde électromagnétique plane se propageant dans le vide ?
- [ ] A) Les champs $\vec{E}$ et $\vec{B}$ sont colinéaires et transverses à la direction $\vec{k}$.
- [ ] B) Les champs $\vec{E}$ et $\vec{B}$ sont perpendiculaires entre eux et tous environ colinéaires à $\vec{k}$.
- [ ] C) Les vecteurs $(\vec{E}, \vec{B}, \vec{k})$ forment un trièdre orthogonal direct.
- [ ] D) Il n'y a pas de relation géométrique stricte en champ lointain.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Les ondes électromagnétiques dans le vide sont des ondes purement transversales : le champ électrique et le champ magnétique oscillent perpendiculairement à la direction de propagation et perpendiculairement l'un à l'autre.
</details>

### Question 9.3 : Quel est le lien entre les amplitudes du champ électrique $E_0$ et du champ magnétique $B_0$ d'une onde EM plane dans le vide ?
- [ ] A) $E_0 = \mu_0 B_0$
- [ ] B) $B_0 = c E_0$
- [ ] C) $E_0 = c B_0$
- [ ] D) $E_0 = B_0 / c^2$

<details>
<summary>💡 Solution</summary>

**Réponse C**. Dans le vide, en appliquant la loi de Faraday ($\text{rot}\vec{E} = -\frac{\partial \vec{B}}{\partial t}$) à une onde plane harmonique, on obtient la relation d'amplitude $E_0 = c B_0$.
</details>

### Question 9.4 : Le vecteur de Poynting $\vec{S}$ caractérise le flux d'énergie d'une onde EM. Quelle est son expression ?
- [ ] A) $\vec{S} = \frac{\vec{E} \cdot \vec{B}}{\mu_0} \vec{k}$
- [ ] B) $\vec{S} = \frac{1}{\mu_0} (\vec{E} \times \vec{B})$
- [ ] C) $\vec{S} = \varepsilon_0 \vec{E}^2 \vec{k}$
- [ ] D) $\vec{S} = c (\vec{B} \times \vec{E})$

<details>
<summary>💡 Solution</summary>

**Réponse B**. Le vecteur de Poynting décrit la direction de propagation de la puissance rayonnnée et sa densité surfacique de puissance en $W/m^2$.
</details>

### Question 9.5 : Comment décroît l'intensité moyenne perçue par unité de surface pour une onde rayonnée par une source isotrope (sphérique) ?
- [ ] A) L'intensité est constante.
- [ ] B) Elle décroît en $1/r$.
- [ ] C) Elle décroît exponentiellement avec la distance.
- [ ] D) Elle décroît en $1/r^2$.

<details>
<summary>💡 Solution</summary>

**Réponse D**. Par conservation de l'énergie, la puissance totale $P$ se répartit sur la surface d'une sphère $S = 4\pi r^2$. L'intensité $I = P/S$ décroît donc en inverse du carré de la distance.
</details>

---

## Chapitre 10 — Ondes stationnaires, battements et effet Doppler

### Question 10.1 : Comment se forme mathématiquement une onde stationnaire ?
- [ ] A) Par l'accélération d'une onde progressive atteignant la vitesse du son.
- [ ] B) Par un changement brutal de milieu diélectrique.
- [ ] C) Par la superposition de deux ondes progressives de même fréquence et amplitude se propageant en sens opposés.
- [ ] D) Par l'interférence de deux ondes de fréquences très différentes dans la même direction.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Lorsqu'une onde incidente et une onde réfléchie se superposent, si elles ont même fréquence et amplitude, elles créent un motif de ventres (amplitude maximale) et de nœuds (amplitude nulle) qui ne se déplace plus spatialement.
</details>

### Question 10.2 : Quelle est la distance séparant deux nœuds consécutifs dans une onde stationnaire sur une corde ?
- [ ] A) Une longueur d'onde complète $\lambda$.
- [ ] B) La moitié d'une longueur d'onde $\lambda / 2$.
- [ ] C) Le quart d'une longueur d'onde $\lambda / 4$.
- [ ] D) Une distance arbitraire qui dépend du mode propre.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Les nœuds (points immobiles) sont distants exactement de $\lambda / 2$. La distance entre un nœud et le ventre adjacent est $\lambda / 4$.
</details>

### Question 10.3 : Lors de la superposition de deux ondes sonores de fréquences proches ($f_1$ et $f_2$), on perçoit un battement. Quelle est la fréquence de ce battement ?
- [ ] A) $(f_1 + f_2)/2$
- [ ] B) $|f_1 - f_2|$
- [ ] C) $\sqrt{f_1 \cdot f_2}$
- [ ] D) L'amplitude s'additionne mais la fréquence reste $f_1$.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Le phénomène de battement se manifeste par une modulation lente de l'amplitude totale. L'oreille perçoit un son de fréquence moyenne $(f_1+f_2)/2$ dont l'intensité fluctue à la fréquence de battement $f_{battement} = |f_1 - f_2|$.
</details>

### Question 10.4 : En quoi consiste l'effet Doppler acoustique classique lorsqu'une source s'approche de l'observateur fixe ?
- [ ] A) Le son devient plus grave car la longueur d'onde apparente augmente.
- [ ] B) La vitesse de propagation du son ambiant augmente localement.
- [ ] C) La fréquence perçue par l'observateur est plus aiguë (plus élevée) que la fréquence émise.
- [ ] D) La fréquence perçue reste identique mais l'intensité double.

<details>
<summary>💡 Solution</summary>

**Réponse C**. À cause du mouvement de la source, les fronts d'onde sont comprimés dans la direction d'approche (la longueur d'onde diminue), ce qui conduit l'observateur à percevoir un son de fréquence plus aiguë.
</details>

### Question 10.5 : Quelle formule modélise la longueur d'onde perçue $\lambda'$ lorsqu'une source s'éloigne à la vitesse $v_s$ d'un observateur fixe, $c$ étant la célérité de l'onde ?
- [ ] A) $\lambda' = \lambda (1 - v_s/c)$
- [ ] B) $\lambda' = \lambda (1 + v_s/c)$
- [ ] C) $\lambda' = \lambda / (1 + v_s/c)$
- [ ] D) $\lambda' = \lambda (v_s/c)$

<details>
<summary>💡 Solution</summary>

**Réponse B**. En s'éloignant, la source "étire" l'espace entre chaque front d'onde. La longueur d'onde perçue augmente donc proportionnellement de $\Delta\lambda = \lambda \cdot v_s/c$.
</details>
