# 📊 Dashboard — Physique PHYSH1002 Vols. I & II

> **Cours** : Électromagnétisme — PHYS-H-1002, Volumes I & II  
> **Professeur** : P. Kockaert, 2025–2026  
> **Thèmes** : Gradient, Flux, Circulation, Faraday, Maxwell, Lenz, Circuits dynamiques, Oscillateurs, Ondes mécaniques, EM et stationnaires, Doppler

---

## 🗂️ Matériels disponibles

| # | Chapitre | Fiche | Statut |
|---|----------|-------|--------|
| 1 | Potentiel et Gradient | [Fiche_Chapitre1_Gradient.md](Fiche_Chapitre1_Gradient.md) | ✅ |
| 2 | Flux et Circulation | [Fiche_Chapitre2_Flux_Circulation.md](Fiche_Chapitre2_Flux_Circulation.md) | ✅ |
| 3 | Loi de Faraday | [Fiche_Chapitre3_Loi_de_Faraday.md](Fiche_Chapitre3_Loi_de_Faraday.md) | ✅ |
| 4 | Ampère, Maxwell & Lenz | [Fiche_Chapitre4_Ampere_Maxwell_Lenz.md](Fiche_Chapitre4_Ampere_Maxwell_Lenz.md) | ✅ |
| 5 | Dynamique des circuits | [Fiche_Chapitre5_Dynamique_Circuits.md](Fiche_Chapitre5_Dynamique_Circuits.md) | ✅ |

| Ressource | Fichier | Statut |
|-----------|---------|--------|
| 📝 Exercices | [Exercices_Physique.md](Exercices_Physique.md) | ✅ 15 exercices (⭐→⭐⭐⭐⭐⭐) |
| 🧾 Cheat Sheet | [CheatSheet_Physique.md](CheatSheet_Physique.md) | ✅ 12 sections de formules |
| 🃏 Flashcards | [Flashcards_Physique.csv](Flashcards_Physique.csv) | ✅ 30 cartes Anki |

---

## 📋 Checklist de révision

### Chapitre 1 — Gradient
- [ ] Maillage : triangles (2D), tétraèdres (3D)
- [ ] Gradient en cartésien, cylindrique, sphérique
- [ ] Dérivée directionnelle = projection du gradient
- [ ] Base conjuguée et gradient sur un maillage
- [ ] rot(grad f) = 0 toujours

### Chapitre 2 — Flux et Circulation
- [ ] Circulation = intégrale de ligne → rotationnel (Stokes)
- [ ] Flux = intégrale de surface → divergence (Gauss)
- [ ] div(rot A) = 0 toujours
- [ ] Équation de continuité (conservation de la charge)
- [ ] Les 4 équations de Maxwell (forme locale + intégrale)

### Chapitre 3 — Loi de Faraday
- [ ] Force de Lorentz : F = q(E + v × B)
- [ ] É.m.f. = -dΦ_B/dt (Faraday intégral)
- [ ] rot E = -∂B/∂t (Faraday local = Maxwell)
- [ ] Transformation galiléenne : E' = E + u₀ × B
- [ ] Potentiel vecteur : E = -grad V - ∂A/∂t

### Chapitre 4 — Ampère, Maxwell & Lenz
- [ ] Courant de déplacement ε₀∂E/∂t — résolution du problème du condensateur
- [ ] div(rot B) = 0 → conservation de la charge
- [ ] Loi de Lenz : B_induit s'oppose à ∂B/∂t
- [ ] Lenz ↔ conservation de l'énergie
- [ ] Diamagnétisme : μ_r < 1, force répulsive

### Chapitre 5 — Dynamique des circuits
- [ ] Auto-induction, Φ_M = LI, V_L = L dI/dt
- [ ] Circuit RL : I(t) = (V/R)(1 - e^{-t/τ}), τ = L/R
- [ ] Énergie : W_L = ½LI²
- [ ] Transformateur : V_s/V_p = N_s/N_p
- [ ] AC : valeurs efficaces I_eff = I_m/√2
- [ ] Réactances : X_L = ωL (passe-bas), X_C = 1/(ωC) (passe-haut)
- [ ] Déphasage : L retarde I de π/2, C avance I de π/2

### Chapitre 6 — Oscillateurs harmoniques et amortis
- [ ] Équation et solutions de l'oscillateur harmonique (OH)
- [ ] Modèles OH : masse-ressort, pendule (petit angle), circuit LC, molécules
- [ ] Pulsations propres : $\omega_0 = \sqrt{\kappa/m}$, $\sqrt{g/l}$, $1/\sqrt{LC}$
- [ ] OLA (amorti) : équation caractéristique $\lambda^2 + \gamma\lambda + \omega_0^2 = 0$
- [ ] Les 3 régimes : sous-critique (pseudo-périodique), critique, sur-critique (apériodique)
- [ ] Facteur de qualité $Q = \omega_0 / \gamma$

### Chapitre 7 — Oscillateur linéaire amorti forcé (OLAF)
- [ ] Équation différentielle avec forcage $F_0 \cos(\omega t)$
- [ ] Utilisation des phaseurs pour la solution stationnaire
- [ ] Résonance d'amplitude : fréquence de résonance $\omega_R = \sqrt{\omega_0^2 - \gamma^2/2}$
- [ ] Largeur de résonance $\delta\omega^* \approx \gamma = \omega_0/Q$
- [ ] Déphasage en quadrature à la résonance
- [ ] Circuit RLC forcé : Impédance complexe $Z = R + i(X_L - X_C)$

### Chapitre 8 — Ondes de corde et de compression
- [ ] Équation d'onde 1D : $\partial_t^2 x = v^2 \partial_z^2 x$
- [ ] Corde tendue : $v = \sqrt{F_T/\mu}$
- [ ] Ondes sonores dans les gaz : $v = \sqrt{\gamma P / \rho}$
- [ ] Solutions de d'Alembert $f(z-vt) + g(z+vt)$ et superposition
- [ ] Lien entre accélération et courbure locale de la corde

### Chapitre 9 — Ondes électromagnétiques
- [ ] Équations de Maxwell dans le vide
- [ ] Équation d'onde vectorielle pour $\vec{E}$ et $\vec{B}$
- [ ] Vitesse de propagation universelle : $c = 1/\sqrt{\mu_0\varepsilon_0}$
- [ ] Ondes planes harmoniques transversales : $v = \omega/k = c$
- [ ] Polarisation rectiligne et trièdre de propagation orthogonale

### Chapitre 10 — Ondes stationnaires, battements et effet Doppler
- [ ] Onde stationnaire : $y(z,t) = 2a\sin(kz)\sin(\omega t + \phi)$
- [ ] Différence entre nœuds et ventres (séparés de $\lambda/4$)
- [ ] Modes propres d'une corde de longueur $L$ fixée : $\lambda_n = 2L/n$
- [ ] Phénomène de battement d'amplitude : $f_B = |f_1 - f_2|$
- [ ] Effet Doppler acoustique : $f_{per\c{c}ue} = f_{émise} \frac{v \pm v_{obs}}{v \mp v_{source}}$
