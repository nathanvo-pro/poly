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

### Question 6.1 : Quel type de profil énergétique conditionne au voisinage fin et de détail un tel mouvement purement "harmonique" ?
- [ ] A) Forme quadratique en puits global grossièrement parabolique : $E_{\text{pot}} \propto x^2$
- [ ] B) Inversion en $1/r$ à type particule coulombenne cosmique universelle.
- [ ] C) Une tangente logarithmique asymétrique forte de liaison.
- [ ] D) Fonction Delta stricte d'impulsion infinie locale au pôle du puits de confinement fort et rigide de l'oscillateur.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Même une cuvette de relief tarabiscoté s'approxime par un $ax^2$ quadratique simple si on se positionne strictement à son minima via les développements rudimentaires locaux de Taylor-Maclaurin du deuxième ordre fin.
</details>

### Question 6.2 : Quelle fraction totale exprime universellement la pulsation sans dimension $\omega_0$ ?
- [ ] A) $(m / k)^{1/2}$
- [ ] B) $(k / m)^{1/2}$
- [ ] C) $k \cdot m$
- [ ] D) $(k \cdot m)^{1/2} \dots$

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est $\sqrt{\frac{k}{m}}$. La constante élastique de confinement (plus rigide) augmente farouchement sa fréquence, là où paradoxalement la forte inertie d'une lourde masse en freinera indubitablement net l'ébranlement global interne du système (la fréquence devient asthmatique et basse).
</details>

### Question 6.3 : Quel rôle joue fondamentalement l'amortissement classique dit purement "visqueux" (force de type Stokes vectorielle $\vec{F} = -b \cdot \vec{v}$) sur l'allure d'un pendule local ?
- [ ] A) Engendrer l'énergie quantiquement.
- [ ] B) Avancer sa phase orbitale au fil logistique exponentiel du balancement cyclique itératif asymptotique net de fuite de la matrice temps et espace local.
- [ ] C) Diminuer lentement et continuellement l'amplitude du balancement et augmenter légèrement et subtilement sa fameuse pseudo-période d'aller/retour classique habituelle d'oscillation.
- [ ] D) Aucune de ces propositions n'est recevable temporellement.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Amorti, le système est d'autant moins vif. Son $\omega_a = \sqrt{\omega_0^2 - \alpha^2}$ baisse incontestablement, du coup inévitablement sa fausse-période apparente s'allonge subtilement en parallèle inhérent du tassement graduel dissipatif de ses excursions d'amplitude au profit du lent mais inexorable réchauffement entropique ambiant de Joule / viscosité induite.
</details>

### Question 6.4 : À la "limite critique" globale du régime qualifié formellement et tristement d'"amorti", que se passe-t-il visuellement concrètement si on lâche notre lourd pendule visqueux dans le vide d'une mélasse parfaite absolue et paramétrée ad-hoc mathématiquement pur sans bavures grossières réelles de friction collante superflue mal dosée ?
- [ ] A) C'est la parfaite "résonance" universelle intemporelle sans perte.
- [ ] B) Le retour vers l'origine est d'une rapidité asymptotique optimale apériodique sans dépassement farfelu d'aucune sorte.
- [ ] C) Ça diverge exponentiellement ad-nauseam...
- [ ] D) Rien ne bouge jamais.

<details>
<summary>💡 Solution</summary>

**Réponse B**. $\alpha = \omega_0$. C'est typiquement l'exact amortisseur de voiture qui avale un dos-d'âne et ramène la carcasse sèchement de sa roue et position vers l'horizontal visé originel sans faire d'insupportables vagues oscillatoires nauséeuses et molles après l'impact du sol.
</details>

### Question 6.5 : Comment note-t-on le concept abstrait généraliste d'amplitude-phase pour simplifier exponentiellement le maniement arithmétique de toutes ces maudites horloges sinusoïdales simultanées croisées ?
- [ ] A) Via le vecteur/nombre qualifié mathématiquement de purement Complexe "Phaseur" $\underline{A} = A \cdot e^{i\phi}$.
- [ ] B) La matrice de passage 3D du tenseur Jacobien non-lié du plan équatorial du balancier et de la roue de l'ancre dentée d'un pendule coucou bernois.
- [ ] C) Logarithme hyper-tangentiel réciproque pur imaginaire $t_c = \ln(i\theta)$.
- [ ] D) Méthode des rectangles finaux intégrés de Runge-Kutta.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'éternel, classique et incontournable "Phaseur".
</details>

---

## Chapitre 7 — Oscillateur linéaire amorti forcé (OLAF) et résonance

### Question 7.1 : À la "résonance" (excitation $F_0 \cdot \cos(\omega t)$ calée parfaitement sur la fréquence endogène pure intrinsèque locale $\omega_0$), que devient l'impédance théorique perçue en module total au sein complet d'un OLAF mécanique ou électrique série typique générique fondamental du plan généraliste commun modélisé simple ?
- [ ] A) L'impédance diverge infiniment au blocage des bobines associées.
- [ ] B) Elle chute pour devenir minimale et purement strictement "Résistive/visqueuse", autorisant net des débits (en courant/vitesse de phase) absolument astronomiques, uniquement modérés par le frein résiduel local passif et dissipeur visqueux interne.
- [ ] C) Purement imaginaire totale sans dissipation aucune réelle d'énergie en joule globale intégrale interne nette fermée close stricte close.
- [ ] D) Constante universelle valant grossièrement $4\pi \times 10^{-7}$ en ohms/mètre de propagation du son ambiant d'éther vibratoire.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le principe des filtres coupe/passe. À la sacro-sainte résonance, l'effet lourd inductif est miraculeusement compensé et contre-balancé au Volt près en temps réel inverse diamétral parfait par l'effet ressort capacitif d'en-face en opposition de miroir conjuré spectral complet dans la danse croisée globale. Reste plus mystiquement que la simple bête résistance R nue et pure de $V/I$ ! (ou de $F/v$ en langage des ressorts purs mécano virtuels formels académiques de tableau noir mathématique théoriel).
</details>

### Question 7.2 : Quel paramètre fondamental résume crûment à lui tout seul le "nombre d'oscillations libres nécessaires" à un circuit OLAF à très faible perte visqueuse isolée fine locale pour dissiper naturellement sa fameuse bouffée initiale d'énergie avant sa lente mais inexorable extinction locale éteinte fatale par de-saturation d'excursion des amplitudes décroissantes de phase intégrales ?
- [ ] A) La pulsation complexe asymptotique vectorisée intrinsèque.
- [ ] B) Le simple temps total final fini (en sec ou millisecondes).
- [ ] C) Les radians carrés sténo-harmoniques croisés et intriqués (sauf à l'éther vide du vide de l'espace non remplumé).
- [ ] D) Le majestueux "Facteur de Qualité : $Q$".

<details>
<summary>💡 Solution</summary>

**Réponse D**. Par exemple le majestueux "Facteur de Qualité : $Q$" d'un quartz de montre (très aigu, résonance abrupte avec le moins de perte et un isolement frictionnel énorme) tape vers les 100 000 ! Un vulgaire RLC au TP vaut $Q=10$.
</details>

### Question 7.3 : Déphasage fondamental net à la pure Résonance Amplitude en déplacement strict local ?
- [ ] A) Le mouvement est exactement collé et calé global en phase de force stricte d'accompagnement direct (0 déphasage mathématique formel).
- [ ] B) Excursion totale infinie stochastique par fractale incontrôlable (chaos de rebond).
- [ ] C) Mouvement fatal excentré décalé rigoureusement en quadrature mathématique de phase absolue, se faisant violemment mener ou tirer en permanence avec un quart de cycle pur local net mathématique brut de retard fondamental perpétuel constant ($-\pi/2$ radians ronds en déphasage complexe) sur la fine force l'animant sans discontinuer sa danse mécanique endogène fine forcée intriquée et pure continue.
- [ ] D) Déphasage stagne global net d'opposition totale intrapolaire pur plat direct en opposition d'un bon cycle brut et plat formel brut d'inversion plate locale ($\pi$ de rebond absolu fixe temporel et continu continu de miroir intemporel stable clos et ferme).

<details>
<summary>💡 Solution</summary>

**Réponse C**. À l'équilibre résonant absolu pur, l'amplitude crête pointe et arrive rigoureusement toujours avec un imperturbable "- 90 degrés" de "retard" chronique absolu sur les pics moteurs formels.
</details>

### Question 7.4 : Dans l'OLAF électrique ($R, L, C$), que remplace fondamentalement et mathématiquement la "masse inertielle (m) mécanique" typique d'un bloc sur un bête ressort en acier trempé ordinaire terrien simple bête standard générique trivial et banal rudimentaire local usuel grossier pur bête fondamental basique local complet typique des tables en formica à plots intégrés du secondaire supérieur général local pur et brutal dur classique standard commun banal ?
- [ ] A) L'inductance (ou la bobine) L (Henri), via la rudesse inertielle de "mise en route du courant".
- [ ] B) Le Condensateur (C) (Farad).
- [ ] C) Sa tension de claquage complexe.
- [ ] D) Une force constante absolue d'Archimède liée au plasma du fil et la pseudo gravité de la chaleur induite des grilles d'antennes (effet dynamo inverse du rotor de masse à vide du tore de charge électrique à perte infinitésimale non récupérable purement et intimement non inductive stricto-sensu intrinsèquement).

<details>
<summary>💡 Solution</summary>

**Réponse A**. Sans doute l'inductance (L) est l'équivalent parfait fondamental de la masse lourde "m". Elle rend la variation du courant ($di/dt$) "difficile" par sa $V = -L di/dt$, tout comme la masse (m) se rebelle global contre tout changement $dv/dt$ dans un univers $F=m.a$.
</details>

### Question 7.5 : Comment lit-on le taux global formel de perte par la dissipation de la fine lèvre d'amortissement dans le graphique spectral du facteur d'amplification d'amplitude d'une fonction de transfert type Bode pour le bélier marteau pilon forcement entretenu par l'excitabilité continue non finie infinie pur absolue fermée de laboratoire hermétique close strict ?
- [ ] A) Plus l'amortissement alpha est gigantesque, plus le clocher fin, précis fin tranchant est d'un aigu démoniaque imprenable absolu pur sans faille pointue acérée stricte fine.
- [ ] B) Plus les pertes et frottements sont dégueulassement élevés (grosses pertes d'amortissement R lourd ou friction lourde pure collante pâteuse), et alors grossièrement plus la courbe du pic va misérablement "s'écraser/s'affaisser lamentablement misérablement" sans gloire en s'étalant/bavant pitoyablement large sans aucun pouvoir filtrant pur distinct net ou discriminant net précis fin coupant ciblé ferme précis formel ponctuel sur l'axe asymptotique brut d'affichage global net total.
- [ ] C) L'amplitude s'affaisse pas la vitesse.
- [ ] D) Le maximum grimpe exponentiellement tout droit à droite à gauche puis retourne en dessous et ne croise jamais l'axe central complexe.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Un haut frottement = amortissement brut = un $Q$ facteur minable. La courbe ne fait pas un haut pic aigu (résonateur), mais au contraire un très misérable dôme aplati grassouillet sur les fréquences contiguës.
</details>

---

## Chapitre 8 — Ondes de corde et de compression

### Question 8.1 : Pour une pure et bête bête onde unidimensionnelle progressant peinardement sans perte dans l'espace vers les "$X$ positifs forts constants", de quelle forme f( ) sa solution est-elle structurellement forcément inéluctablement issue intimement logée ?
- [ ] A) $f(x - vt)$
- [ ] B) $f(x + vt)$
- [ ] C) $f(v - xt)$
- [ ] D) $f(x) \cdot \sin(vt)$

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'éternel, majestueux argument couplé " $x - vt$ " traduit exactement à la perfection et d'un bloc entier et formel la fameuse translation rigide invariante mathématique et formelle vers l'avant à la vitesse positive fixe " $v$ " sans déformation ni altération grossière aucune de la poche spatiale modulant le front d'onde général au fil des secondes s'égrainant implacablement sans fin ni fond apparents purs ou absolus concrets clairs.
</details>

### Question 8.2 : D'Alembert l'a bien dit (et on l'a crû), l'onde unidimensionnelle c'est typique :
- [ ] A) Une racine carrée pure locale asymptotique de l'écart au fond d'un tube creux semi-ouvert clos net dur.
- [ ] B) Le laplacien absolu sans résidus exponentiel inversé en $1/r^2$ asymptotique du centre formel fixe et stable originel d'émergence ponctuelle dur net franc d'un bout plat global universel local plan simple carré plat et trivial.
- [ ] C) La multiplication des ondes planes de Fourier complexe via une matrice tri-diagonale locale de bloc simple direct par matrice Jacobienne fermée locale continue discrète complexe absolue vectorielle et mathématique absolue fermée non diagonale intégrée absolue globale brute lourde forte plate dur fermée mathématisée.
- [ ] D) L'équation d'onde absolue globale unie liant la seconde dérivée "temporelle" d'une excitation souple formelle à très exactement $v^2$ fois et de fait la seconde dérivée "spatiale" pure simple du grand profil d'onde local général global et uni fin franc pur général commun formel complet direct classique canonique propre formel académique exact absolu dur incontestable vrai net continu.

<details>
<summary>💡 Solution</summary>

**Réponse D**. C'est globalement résumé la fameuse équation : $\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}$.
</details>

### Question 8.3 : À quelle très exacte brutale implacable brut d'implacabilité absolue de vitesse de phase brute " $v$ " se déplace (en module sans direction apparente complexe d'éther formel asymétrique ou bizarre), un pauvre mais honnête dur pli de secousse simple impulsé initialement d'un leste coup bref transversal brutal transversal orthogonal de la main crasse sur et au travers d'une grande corde à linge longue de jardin local de banlieue classique (la corde étant simplement crânement mais classiquement paramétrisée via bête module complet et strict un et absolu par $T$ pour tension brutale dur de bout et paramétrée $\mu$ (mu) pur d'absolu comme grande et inébranlable masse apparente pure par seule misérable unité locale fin pure métrique absolue linéaire droite unie) ?
- [ ] A) $v = \mu \cdot T^2$
- [ ] B) $v = \sqrt{T/\mu}$
- [ ] C) $v = \sqrt{\mu/T}$
- [ ] D) $v = T \cdot \mu$

<details>
<summary>💡 Solution</summary>

**Réponse B**. Exact. Une énorme Tension au tirage allonge la prestesse d'ébranlement de diffusion du couplage brut inter-atomique cristallin transverse et un leste fil lourd à gogo pesant comme un âne mort freine net et grève lamentablement de la diffusion dynamique macroscopique transversale visuelle et locale l'allure molle et pataude et pure grossière d’ébranlement globale.
</details>

### Question 8.4 : Quel lien indéfectible basique, trivial et fondamental absolu existe inébranlablement intemporel et inéluctablement liant et couplant mathématiquement, dimensionnellement, spatialement et par et pur cycle total fini fermé complet intrinsèquement brut net entre Lambda ($\lambda$), $f$, et $c$ (la vitesse ou célérité constante) au coeur fin du cœur intime formel intègre et fermé de l'évanescente onde libre harmonique continue transversale se déplaçant crânement isolée sur le seul plan spatial strict un local net fort en une coordonnée fine d'espace $x$ abstrait seul infini rectiligne ?
- [ ] A) $c = \lambda \cdot f$
- [ ] B) $\lambda = c \cdot f$
- [ ] C) $c = \lambda / f$
- [ ] D) $f = c \cdot \lambda$

<details>
<summary>💡 Solution</summary>

**Réponse A**. Il suffit de comprendre qu’en $1$ seconde complète pleine, la fameuse perturbation génère " $f$ " motifs temporels et s'allonge en espace local direct de $f$ grand modules répétés "$\lambda$"-fois. La vitesse résultante linéaire en long espace parcouru effectif vaut de surcroit et d'allure pure d'une longueur exacte totale de très et en fait crânement précisément $f \cdot \lambda$ de distance couverte.
</details>

### Question 8.5 : L'onde de compression "sonore" (acoustique pure longitudinale fine) voyage trivialement, platement et formellement dans tous les bêtes lests fluides banaux fluides communs en tout lieu absolu net du fluide global uni net avec de fait d'allure stricte pure formelle complète mathématique canonique ferme fin de :
- [ ] A) $v = \sqrt{\rho \cdot B}$
- [ ] B) $v = \sqrt{\rho / B}$
- [ ] C) $v = \sqrt{B / \rho}$
- [ ] D) $v = B \cdot \rho^2$

<details>
<summary>💡 Solution</summary>

**Réponse C**. (Où $B$ en est le brave et gros module d'élasticité global fin "Bulk Modulus" brut inélastique réversible isotrope compressif fin local thermodynamiquement formel de gradient moyen dur total fin adiabatique typique et $\rho$ bêtement simplement l'inerte densité de masse par unité stricte globale cube volumique bête brute dur local brut fine classique). La souplesse ralentit/facilite la transmission locale de choc inter-grains. Les chocs lourds d'air pesant inerte freinent fatalement net le déploiement pur global brut spatial rapide local ferme.
</details>

---

## Chapitre 9 — Ondes électromagnétiques

### Question 9.1 : Formellement et mathématiquement dérivée fine locale de ce petit malin Maxwell génial écossais historique formel absolu : Les grandioses dantesques ondes du spectre "EM" avancent trivialement dans le triste "Vide absolu fin pur plat dur classique non massif d'éther" (sic) à du...
- [ ] A) $1 / \sqrt{\mu_0 \cdot \epsilon_0}$
- [ ] B) Exactement (selon définition originelle) : $c = 1 / \sqrt{\varepsilon_0 \cdot \mu_0}$
- [ ] C) $v = \lambda \cdot T$
- [ ] D) Nulle part, le vide n'existe simplement bêtement platement et inlassablement pas.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le postulat de triomphe éclatant inouï et dément de Maxwell que de se rendre brusquement et mathématiquement bien et lourdement compte que le décompte de sa grosse et pure formule donnait au final la bête et commune célérité de notre chère et habituelle vitesse et forme typique classique unie pure simple stricte fine de notre banale "lumière".
</details>

### Question 9.2 : C'est un trait fondamental basique, inhérent intime fin et très caractéristiquement local pur structurel à type formel unilatéral continu global : La belle et brillante (oui) onde plane finie pure transversale électromagnétique ("EM"), force et astreint implacablement à jamais : les champs indissociables purs croisés fins $E$ et $B$ d'être systématiquement crânement et localement intrinsèquement et à jamais purement global complet... :
- [ ] A) Totalement orientés parallèles et en exacte résonance pure avec l'axe intime du bout de l'extrême avancement et de l'avancée stricte unie formelle frontale pointue absolue ferme de l'onde $k$ dans un espace tridimensionnel non relativiste abstrait pseudo euclidien ferme.
- [ ] B) Désordonnés de par et crânement pure indécence de forme inhérente vectorisée locale absolue sans forme nette.
- [ ] C) Toujours implacablement "Orthogonaux ou perpendiculaires" finement et rigoureusement entre leur pauvre soi croisé et aussi purement toujours bêtement brut orthogonaux stricts face fin de fait net total plat à la fameuse direction de propagation stricte nette forte $\vec{k}$.
- [ ] D) $E$ et $B$ sont bêtement un et seul même scalaire imaginaire d'éther vide d'esprit.

<details>
<summary>💡 Solution</summary>

**Réponse C**. À travers le vide total uni classique commun plat et parfait isotrope, tout trièdre $( \vec{E}, \bar{B}, \vec{k} )$ de repère d'avancée reste à la perfection direct abstrait orthogonal intègre pur et fermé (angle crâne carré absolu en tous sens locaux vectoriels).
</details>

### Question 9.3 : La noble loi "d'intensité et flux d'énergie en transport" pure locale formelle canonique vraie rayonnée s'établit en $W/m^2$ de belle grâce par l'ingénieux, illustre, fin mathématicien intègre britannique local complet du beau nom franc local complet pur dur et exact entier final et académique unifié net :
- [ ] A) Force de Faraday-Lenz pure
- [ ] B) Le célèbre bien nommé noble repère du vecteur net de "Poynting" ($\vec{S} = \frac{\vec{E} \times \bar{B}}{\mu_0}$).
- [ ] C) L'Onde finie unie vraie et finie plane harmonique stationnaire plate.
- [ ] D) Constante inhérente absolue stricte vraie finie du fin $\hbar$ de Planck de photon discret fin.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Poynting l'anglais a mis en équation et le sens pointé (Poynting!) et la force énergétique totale croisée portée par le front radiatif transversal d'onde EM continue fin en flux watts rayonnés et continus constants locaux d'espace au carré pur de croisé. (Et pas Planck qui fragmente les gros morceaux et tout l'édifice par paquets granulaires discontinus locaux discrets sans gloire apparente de front plan infini non temporel absolu fin.)
</details>

### Question 9.4 : Comment varie en "intensité moyenne fine formelle captée et brute nette reçue localement à une pure bête surface finie fixe" ($I_{moy} \propto E_m^2$) le pauvre fin front d'énergie de fait de forme bête d'Onde Plane classiquement formel uni et pur finie brute (et classiquement fin "non sphérique non divergent local plat fini"!) classique sans fin dans l'espace triste vide isolant d'air frais ?
- [ ] A) Décroît fort en $\sim 1/r^2$ depuis tout endroit fini initial local d'émission et lointainement en infiniment asymptotique dur brut de chute violente nette exponentielle stricte fermée inverse croisée simple fin forte plate.
- [ ] B) Demeure parfaitement constante (idéalement) éternellement fin pur brut local de forme inaltérée ferme tant que son chemin n'est pas coupé croisé bouché.
- [ ] C) Diffracte son $E$ autour du point nodal aveugle noir en $e^{-\alpha x}$.
- [ ] D) Croît de la fameuse $\sqrt{2}$ asymptotique vraie en approchant les forts murs intimes nets durs locaux du fond brut absolu vide et infini de confins fins célestes et croisés purs noirs du continuum inerte inaltérable et vaste plein pur noir sombre vide total inepte fin vide vide infini pur pur plat...

<details>
<summary>💡 Solution</summary>

**Réponse B**. Une onde rigoureusement plane ne voit aucune surface de front grandir, son énergie d'étalement de surface est conservée au fil du temps. Évidemment une onde d'antenne filaire fine ou d'une boule dipôle est sphérique localement et chutera bien fort de $\sim 1/r^2$ d'inverse géométrique trivial.
</details>

### Question 9.5 : Comment passe-t-on fin trivialement fin mathématiquement d'un pur d'amplitudes champ vrai fin $\vec{E}$ au $\vec{B}$ bêtement couplé frère lié au front plane onde (module dur vrai strict lié dans le vide pur plat ferme classique complet) ?
- [ ] A) Par l'application en cosinus inverse (arc-cos) fort du de l'angle d'avance locale vectorisée absolue fine (et très ferme).
- [ ] B) Par une division bête de temps par vitesse locale $\vec{B} = E / v^2$ fine ferme close.
- [ ] C) Trivialement un bête scalaire brut et ferme de division fin plat d'ordre $c$ ferme vrai formel ($B_0 = E_0 / c$).
- [ ] D) On ajoute le fameux grand courant de polarisation brut intime intègre complexe vide formel fin pur ferme abstrait fort dense continu intime constant local pur du pseudo-déplacement et glissement asymétrique de flux constant local en angle fini en $dt$ fort vrai fermé constant asymptotique d'absolu complexe intègre vectoriel paramétrique unifié continu.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Avec $c = 3 \times 10^8\; m/s$, le fin champ lourd et complet d'attraction "$\vec{B}$" de nos ondes classiques et éther et vides fin de vide, se révèle d'une faiblesse apparente totale d'échelle infime par rapport à $\vec{E}$ au niveau du simple module formel chiffré trivial classique pur standard. (Bien que portant paradoxalement et miraculeusement exactement crânement une même vraie moitié fine énergie fin croisée d'énergie vraie locale $\frac{1}{2}\varepsilon E^2 \approx \frac{1}{2} B^2 / \mu$).
</details>

---

## Chapitre 10 — Ondes stationnaires, battements et effet Doppler

### Question 10.1 : Par une bête et stricte "Onde Stationnaire" pure on désigne classiquement sans artifice de bête construction :
- [ ] A) L'onde bête fine d'un simple ébranlement fini solitaire dur local (bruit claque).
- [ ] B) Une onde de rotation bête sphérique de champ électrique de gradient statique fixe et dur invariant platement localement unie en force ferme.
- [ ] C) Le bête pur strict complet vrai franc simple "superpositionnement" fin fin local inhérent d'au moins stricte deux ondes parfaitement semblables de pulsation mais dures de fait opposées en avancement d'espace brut et qui s'additionnent ou interférent inlassablement continuellement fixent fermement sans bouger les noeuds absolus plats de zéros intemporels fins et locaux de noeud fixes récurrents de leur parcours fin vrai bête brut.
- [ ] D) L'onde bête fin du front et du bord des cordes d'arc d'inertie forte transversale.

<details>
<summary>💡 Solution</summary>

**Réponse C**. L'onde ne "semble plus avancer" car ses ventres dansent sur place inlassablement autour fixement posés crânement stables de "zéro / nœuds" bêtes infranchissables de position neutres qui crânement mathématiquement ne débougent de fait inlassablement pas. (Typiquement dans les boîtes de résonance bêtes fermées des gros violoncelles lourds ou bêtes des de résonateurs clairs de flute et corde fixe de piano pur d'accordement classique local).
</details>

### Question 10.2 : Quelle fraction de la longueur d'onde spatiale fine $\lambda$ brute standard classique ferme exacte franche locale et de fait sépare crânement exactement imperturbable de deux bêtes et franc "Noeuds purs" intriqués continuellement liés et contigus d'une fine intime belle douce classique onde "Stationnaire" ?
- [ ] A) Le quart pur ou fin du $\lambda / 4$.
- [ ] B) Du entier grand et total complet bête du bête et $\lambda$ plat classique unifié inhérent complet et fermé ferme pur fin franc continu complet fort.
- [ ] C) Toujours et à jamais une stricte fine petite et pauvre modeste inaltérable "Moitié de Lambda" pure fin vrai franc brut simple ($\lambda / 2$).
- [ ] D) Deux Lambda ferme fins et absolus clairs complet intègre net absolu en continu mathématique continu vectorisé net local simple dur net vrai brut total.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Nœud-à-nœud vaudra bien la demi-longueur d'onde de la belle onde originelle. (Nœud à Ventre adjacent = le pur et simple bête quart quart : $\lambda / 4$).
</details>

### Question 10.3 : Formellement, il y a un battement bête ou fin local "Battement" ou pseudo-vibrato d'onde fine sonore ou intime quand on couple et conjugue (fusion addition de fronts sonores de clarté de bruit brut ou fin croisé pur de superposition simple addition de superposition de linéarite unie ferme franche classique) :
- [ ] A) Des ondes rigoureusement de longueurs d'onde de paires inverses net fort complexes purs asymétriques pures francs brutes et d'harmonie croisée double pur absolu vide inerte plat inverse carré ferme simple bête continu et fixe formel local clair vrai dense pur et vrai double carré inerte fort complet d'asymétrie totale croisée d'anomalie globale ferme fermement complète continue...
- [ ] B) Des ondes fines de bête "Pulsations/Fréquences" très crânement juste fort presque de justesse bêtement proches fin l'une de la presque autre (du genre 500 Hz plus 505 Hz). Le déphasage intime du croisement avance leste lentement et la sourde "enveloppe modulée locale d'amplitude de battement" croisée apparente fin va grandir fort puis flétrir fin rythmiquement "lentement" (5Hz bêtes apparent de "Wouaaah Wouaaah" fin musical et local franc et dur classique net unifié total complet constant fort fin brut).
- [ ] C) Deux simples cordes pures croisées qui tournent ensemble en harmonique fine unilatérale de champ fixe formel dense pur continu fort dur franc net classique continu.
- [ ] D) L'effet doppler d'attraction croisé local simple abstrait complexe franc direct net pur double vectorisé ferme dur clair continu plat local net unifié abstrait abstrait plat croisé net plat fixe complexe fin brut ferme.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le principe de l'accordeur. Proche du La fondamental (440Hz), la corde 442hz chantera et geindra finement un bête et long "wouah wouah" clair de fréquence 2 Hz. Ce qui trahit très clairement d'audition la stricte franche pure classique différence mathématique entre ce couplage des deux signaux intimes croisés.
</details>

### Question 10.4 : Au classique fin intime franc vrai absolu simple et formel vrai Doppler banal (Effet bêtement Doppler typique et dur classique standard continu) : Lors de bête et simple stricte vraie approche intime fine brute forte d'une bête "Source sonore" mobile vraie leste d'allure vectorielle avançante fine vers "un pauvre Observateur inerte local pur classique inébranlable et stoïque immobile" absolu classique : La Fréquence Franc formelle intime et exacte reçue en son pauvre tympan local dur pur net :
- [ ] A) Devient "aigue" de par la brut compression front devant (raccourcissement franc absolu et brut simple des pures rides des fronts d'ondes bêtes).
- [ ] B) Chute en fréquence de par le dur écartement abstrait fort absolu croisé franc fort recu net du rebond franc absolu plat vrai net inerte plat continu fort vrai clair local fin net brutal asymétrique lourd pur vrai...
- [ ] C) Demeure constante asymptotique croisée sans décalage bête franc vrai ferme dur formel complet vrai.
- [ ] D) Modifie l'amplitude non la bête et pauvre fréquence de frappe des tympans.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'ambulance arrive = pitch aigu = le front des rides sonores son est comprimé $\lambda$ (raccourci franc vectoriel dynamique absolu). Sa longue mais inerte fuite après le croisement allonge de fait les fronces d'ondes et l'air nous joue un do/son/bruit d'échappement traînant grave à son passage et recul franc ferme lourd et inerte pur vectoriel net vrai clair.
</details>

### Question 10.5 : La formule doppler magique : de fait comment est modifiée fin franc vrai bête typique pur et net clair total ferme complet "longueur l'onde $\lambda$" émise s'échappant d'un bolide lourd d'approche (vitesse d'avance de train de $v_s$ vrai vif brutal dur net de source) en pleine et franche accélération radiale front devant fine devant un pauvre micro fixe local fort ?
- [ ] A) $\lambda_{\text{reçu}} = \lambda_{\text{emis}} \cdot (1 + v_s / c)$
- [ ] B) $\lambda_{\text{reçu}} = \lambda_{\text{emis}} \cdot (1 - v_s / c)$
- [ ] C) $\lambda_{\text{reçu}} = \lambda_{\text{emis}} / (1 + v_s \cdot c)$
- [ ] D) Ne se modifie formellement aucunement en rien du fin du banal du tout trivial ou formel d'ailleurs pur.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Un train et klaxon à $v_s=100 m/s$ poursuivant sa propre honnête propagation du crâne son qu'il fait dans l'air franc $(340 m/s)$, va inexorablement "mordre / ratiboiser ou bouffer" allègrement finement dur son triste espace d'avance, amputant son brave pauvre "$\lambda$" perçu par l'infortuné piéton de presque un pur tiers bête de sa forme formelle de dimension étalée et propre.
</details>
