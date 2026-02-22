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
