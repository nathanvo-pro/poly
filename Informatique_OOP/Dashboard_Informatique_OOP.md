# 📊 Dashboard — Informatique OOP (INFOH2001)

> **Dernière mise à jour :** 22 février 2026

---

## TL;DR

Le cours INFOH2001 enseigne la **programmation orientée objet en C++** pour les étudiants venant de Python. Les deux premiers cours couvrent les **fondamentaux du C++** : compilation (`g++`), types de données, structures de contrôle (`if`, `switch`, `for`, `while`), entrées/sorties avec `cin`/`cout`, lecture/écriture de fichiers (`fstream`), strings (C-strings vs `std::string`), structures (`struct`), parsing (`sscanf`, `istringstream`), conversions de types et fonctions. Le tout est illustré par un mini-projet BMD Regression Tree évoluant d'une version statique (v1.0) à dynamique (v2.0).

---

## 📚 Fiches de synthèse

| # | Sujet | Fiche | Avancement |
|---|---|---|---|
| 1 | De Python à C++ — Les fondamentaux | [Synthèse (Cours 1)](Synthese_Informatique_OOP.md#1-pourquoi-c) | [ ] Lu |
| 2 | File I/O, Strings, Structs, Fonctions | [Synthèse (Cours 2)](Synthese_Informatique_OOP.md#cours-2--file-io-strings-structs-et-fonctions) | [ ] Lu |
| 3 | Hiérarchie mémoire, Arrays avancés et POO | [Synthèse (Cours 3)](Synthese_Informatique_OOP.md#cours-3--hiérarchie-mémoire-arrays-avancés-et-introduction-à-la-poo) | [ ] Lu |

---

## ✅ Suivi de révision — Cours 1

### Compilation et environnement
- [ ] Je sais la différence entre compilé et interprété
- [ ] Je sais compiler avec `g++ fichier.cpp -o nom`
- [ ] Je comprends les étapes compilation → linkage → exécutable

### Syntaxe de base
- [ ] Je sais écrire un Hello World complet en C++
- [ ] Je connais le rôle de `#include`, `main()`, `return 0`
- [ ] Je sais utiliser `cout`, `cin`, `<<`, `>>`

### Types et variables
- [ ] Je connais les types de base : `int`, `float`, `double`, `char`, `bool`, `string`
- [ ] Je sais la différence entre typage statique (C++) et dynamique (Python)
- [ ] Je connais les qualificateurs `short`, `long`, `unsigned`

### Structures de contrôle
- [ ] `if` / `else` (et les pièges `=` vs `==`)
- [ ] `switch` / `case` (avec `break`)
- [ ] `for`, `while`, `do...while`
- [ ] Je connais la différence entre `while` et `do...while`

## ✅ Suivi de révision — Cours 2

### File I/O
- [ ] `ifstream`, `ofstream`, `fstream` — lecture et écriture de fichiers
- [ ] `getline` vs `>>` pour la lecture
- [ ] Modes d'ouverture (`ios::in`, `ios::out`, `ios::app`, etc.)
- [ ] Importance de `close()`

### Streams et manipulateurs
- [ ] Hiérarchie des streams (`ios` → `istream`/`ostream` → `ifstream`/`ofstream`)
- [ ] Manipulateurs : `setprecision`, `setw`, `setfill`, `fixed`, `scientific`
- [ ] Mode texte vs mode binaire

### Strings
- [ ] Différence entre C-string (`char[]`) et C++ string (`std::string`)
- [ ] Importance du caractère nul `\0` pour les C-strings
- [ ] Méthodes de `std::string` : `length()`, `find()`, `[]`, `+`

### Parsing
- [ ] `sscanf` — parsing de style C
- [ ] `istringstream` / `ostringstream` — parsing de style C++
- [ ] `stringstream` — lecture et écriture bidirectionnelle

### Structs, types et fonctions
- [ ] Déclarer et utiliser une `struct`
- [ ] `static_cast` vs cast style C
- [ ] Prototype, définition et appel de fonctions

### Exercices
- [ ] QCM et exercices réalisés ([Exercices](Exercices_Informatique_OOP.md))
- [ ] Flashcards révisées

---

## ✅ Suivi de révision — Cours 3

### Mémoire et Arrays
- [ ] Hiérarchie mémoire (L1, L2, L3, RAM, SSD)
- [ ] Arrays : pointeur premier élément, contiguïté en mémoire
- [ ] Conséquence de l'absence de vérification de bornes (Segfault)
- [ ] Calculer la taille d'un array avec `sizeof`

### Initiation POO
- [ ] Différence entre Procédural et POO
- [ ] Différence entre Classe et Objet
- [ ] Encapsulation : public vs private, Getters/Setters
- [ ] Séparation Interface (.h) et Implémentation (.cpp)

### Concepts avancés C++
- [ ] Constructeurs (rôle et déclaration)
- [ ] Listes d'initialisation (syntaxe recommandée)
- [ ] Énumérations (`enum`)
- [ ] Opérateurs ++ préfixe vs ++ suffixe

### Exercices
- [ ] QCM et exercices réalisés ([Exercices](Exercices_Informatique_OOP.md))
- [ ] Flashcards révisées

---

## 📁 Fichiers du cours

| Fichier | Type | Description |
|---|---|---|
| [Synthèse globale](Synthese_Informatique_OOP.md) | Synthèse | Synthèse unifiée des cours 1, 2 et 3 |
| [Exercices](Exercices_Informatique_OOP.md) | Exercices | QCM + problèmes de code (réponses cachées) |
| [Flashcards CSV](Flashcards_Informatique_OOP.csv) | Flashcards | Import Anki/Quizlet |
| [Cheat Sheet](CheatSheet_Informatique_OOP.md) | Aide-mémoire | Syntaxe vitale pour l'examen |
