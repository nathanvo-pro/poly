# Dashboard — Analyse Numérique

## 🎯 TL;DR du Cours
Ce cours traite de l'utilisation des ordinateurs pour résoudre des problèmes mathématiques complexes de manière approchée. 
L'ordinateur n'utilisant qu'une mémoire finie (flottants), il est inévitable de commettre des erreurs d'arrondi. L'Analyse Numérique étudie comment ces minuscules erreurs se propagent lors des milliers d'opérations d'un algorithme (concept de **stabilité** algorithmique), et surtout si le problème physique initial est fondamentalement trop sensible (concept de **conditionnement**).

---

## 📌 Chapitre 1 : Représentation, Stabilité et Conditionnement

### 📝 Plan de révision
1. **La Virgule Flottante :** Comprendre l'architecture de la mantisse, de la base et de l'exposant.
2. **Le Standard IEEE 754 :** Simple et double précision, et limites physiques (Overflow, Underflow, NaN).
3. **L'unité d'arrondi $u$ :** La borne universelle de tolérance des machines à chaque calcul.
4. **Erreur d'Annulation :** Le danger mortel de la soustraction de deux nombres extrêmement proches.
5. **Stabilité Inverse vs Directe :** Juger si un algorithme perd la boule ou non face aux flottants.
6. **Conditionnement Absolu $\kappa$ :** Qualifier si une fonction (comme $\sqrt{x}$ vs la soustraction) est naturellement "Saine" ou profondément "Chaotique".

### ☑️ Suivi de progression

| Statut | Sujet |
| :---: | :--- |
| [ ] | Synthèse lue et comprise |
| [ ] | Flashcards étudiées (score > 80%) |
| [ ] | Exercices Niveau 1 ⭐ et 2 ⭐⭐ (Fondamentaux virgule & IEEE) |
| [ ] | Exercices Niveau 3 ⭐⭐⭐ (Modèle arithmétique & Annulation) |
| [ ] | Exercices Niveau 4 ⭐⭐⭐⭐ (Stabilité & $\kappa$) |
| [ ] | Exercices Niveau 5 ⭐⭐⭐⭐⭐ (Analyse pointue du piège de la soustraction) |

---

## 📌 Chapitre 2 : Systèmes d'équations & Méthodes directes

### 📝 Plan de révision
1. **Généralités :** Conditionnement d'un système $\kappa(A)$ et Normes matricielles.
2. **Méthode Inutile :** Comprendre le désastre absolu du coût de la méthode de Cramer $O(n!)$.
3. **Approche Triangulaire :** Pourquoi la substitution (Avant/Arrière) est la reine en $O(n^2)$.
4. **Factorisation LU :** L'élimination de Gauss réduite en un produit matriciel parfait $A = LU$.
5. **Le Danger et la Solution :** Instabilité face aux petits pivots et son remède absolu : $PA = LU$.
6. **Bonus LU :** Calculer instantanément un déterminant massif ou inverser la matrice via $\frac{8}{3}n^3$.

### ☑️ Suivi de progression

| Statut | Sujet |
| :---: | :--- |
| [ ] | Synthèse du Chapitre 2 lue et comprise |
| [ ] | Flashcards étudiées (score > 80%) |
| [ ] | Exercices Niveau 1 ⭐ et 2 ⭐⭐ (Conditionnement & Normes) |
| [ ] | Exercices Niveau 3 ⭐⭐⭐ (Le sauvetage par matrices Triangulaires) |
| [ ] | Exercices Niveau 4 ⭐⭐⭐⭐ (Théorème et exécution LU) |
| [ ] | Exercices Niveau 5 ⭐⭐⭐⭐⭐ (Maîtriser $PA=LU$ et le $\det(A)$) |

---

## 📌 Chapitre 3 : Factorisation QR et systèmes surdéterminés

### 📝 Plan de révision
1. **La Factorisation QR :** Comprendre l'orthogonalité de $Q$ et la décomposition en matrices idéales.
2. **Le Miroir de Householder :** L'isométrie algébrique et la fabrication de la matrice $H = I - 2 \frac{vv^T}{\|v\|^2}$.
3. **Les Moindres Carrés :** Pourquoi un système surdéterminé n'a pas de solution parfaite. L'approche du résidu minimal $\min \|r\|_2$.
4. **Les Équations Normales :** Démonstration par la Jacobienne et la naissance de $A^T A x = A^T b$.
5. **Le Pseudo-Inverse ($A^\dag$) :** La formule de projection $(A^T A)^{-1} A^T$.
6. **Le Duel Final :** LU sur Équations Normales (rapide mais détruit le conditionnement en $\kappa^2$) vs Householder QR (Lent, inconditionnellement stable).

### ☑️ Suivi de progression

| Statut | Sujet |
| :---: | :--- |
| [ ] | Synthèse du Chapitre 3 lue et comprise |
| [ ] | Flashcards étudiées (score > 80%) |
| [ ] | Exercices Niveau 1 ⭐ et 2 ⭐⭐ (Orthogonalité $Q^TQ$ et Preuve de $H$) |
| [ ] | Exercices Niveau 3 ⭐⭐⭐ (Moindres Carrés et Jacobienne) |
| [ ] | Exercices Niveau 4 ⭐⭐⭐⭐ (Analyse CPU : $A^TA$ vs Householder) |
| [ ] | Exercices Niveau 5 ⭐⭐⭐⭐⭐ (Preuve intégrale du Conditionnement $\kappa^2$) |

---

## 🏋️ Séances de Travaux Pratiques

| Statut | Séance |
| :---: | :--- |
| [ ] | Séance 1 — Prise en main d'Octave (rappels lus + exercices similaires faits) |
| [ ] | Séance 2 — Erreurs d'arrondi et propagation |
| [ ] | Séance 3 — Conditionnement et factorisation LU |
| [ ] | Séance 4 — Factorisation PA=LU et QR à la main |
| [ ] | Séance 5 — Moindres carrés : équations normales vs QR |
| [ ] | Séance 6 — Méthodes itératives (Jacobi, Gauss-Seidel) et splines |
| [ ] | Séances 7-8 — Recherche de zéros d'équations non-linéaires |
| [ ] | Séance 9 — Intégration numérique (Trapèzes, Simpson, Romberg) |
