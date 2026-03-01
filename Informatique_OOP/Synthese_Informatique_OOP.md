# 📖 Synthèse Complète — Informatique OOP (INFOH2001)

---

##  Cours 1 : De Python à C++

> 📚 **Objectif du cours :** Apprendre la syntaxe de base du C++ pour les étudiants venant de Python. Comprendre la compilation, les types, les structures de contrôle, et réaliser un premier mini-projet (BMD Regression Tree).

---

### Table des matières

1. [Pourquoi C++ ?](#1-pourquoi-c-)

2. [Compilation : du code source à l'exécutable](#2-compilation--du-code-source-à-lexécutable)

3. [Hello World — Anatomie d'un programme C++](#3-hello-world--anatomie-dun-programme-c)

4. [Types de données](#4-types-de-données)

5. [Caractères de contrôle](#5-caractères-de-contrôle)

6. [Structures de contrôle](#6-structures-de-contrôle)

7. [Les instructions (Statements)](#7-les-instructions-statements)

8. [Mini-projet : BMD Regression Tree](#8-mini-projet--bmd-regression-tree)

---

### 1. Pourquoi C++ ?

#### 1.1 Performance et efficacité

> 💡 **Idée clé :** C++ est un langage **compilé** et **bas niveau** — il vous donne le contrôle total sur la mémoire et les performances, ce qui le rend beaucoup plus rapide que Python.

| Critère | C++ | Python |

|---|---|---|

| **Type** | Compilé | Interprété |

| **Niveau** | Bas (proche machine) | Haut (abstrait) |

| **Vitesse** | Très rapide ⚡ | Plus lent 🐌 |

| **Mémoire** | Gestion manuelle | Automatique (GC) |

| **Typage** | Statique (compilation) | Dynamique (exécution) |

| **Utilisation** | Systèmes, jeux, IA (libs), embarqué | Prototypage, data science, scripting |

**Logiciels développés en C++ :** systèmes d'exploitation, navigateurs web (Chrome), moteurs de jeux (Unreal Engine), bibliothèques d'IA (TensorFlow, PyTorch en backend).

#### 1.2 Informatique verte 🌱

> 🎯 **Point important :** Moins de temps de calcul = moins d'électricité = moins de CO₂. Pour un même programme, C++ est **beaucoup plus rapide** que Python, ce qui réduit l'empreinte carbone.

#### 1.3 Culture d'ingénieur

> 🧠 **Philosophie :** En C++, vous êtes obligé de **penser comme une machine** : gérer la mémoire, concevoir des structures efficaces, anticiper les erreurs. C'est cette profondeur de compréhension qui vous distinguera.

---

### 2. Compilation : du code source à l'exécutable

#### 2.1 Compilé vs Interprété

```

COMPILÉ (C, C++, Rust, Go) :

   Code source → [Compilateur] → Code machine/Objet → Exécution directe

INTERPRÉTÉ (Python, JavaScript, PHP) :

   Code source → [Interpréteur] → Exécution instruction par instruction

```

| Aspect | Compilateur | Interpréteur |

|---|---|---|

| **Traduction** | Tout le programme d'un coup | Instruction par instruction |

| **Résultat** | Fichier exécutable autonome | Pas de fichier exécutable |

| **Optimisation** | Optimisations globales possibles | Optimisations limitées |

| **Vitesse exécution** | Rapide | Plus lent |

| **Débogage** | Erreurs détectées à la compilation | Erreurs à l'exécution |

> 🧠 **Hybrides modernes :** La compilation JIT (Just-In-Time), utilisée par la JVM, .NET CLR ou V8 (JavaScript), compile dynamiquement du bytecode en code natif au moment de l'exécution.

#### 2.2 Les étapes de la compilation C++

```

┌──────────│    ┌──────────────│    ┌──────────────│

│ fichier1 │───→│  Compilateur │───→│ Fichier objet│──│

│  .cpp    │    │     g++      │    │    .o        │  │    ┌────────│    ┌────────────│

│”──────────┘    │”──────────────┘    │”──────────────┘  ├───→│ Linker │───→│ Exécutable │

┌──────────│    ┌──────────────│    ┌──────────────│  │    │”───┬────┘    │”────────────┘

│ fichier2 │───→│  Compilateur │───→│ Fichier objet│──┘        │

│  .cpp    │    │     g++      │    │    .o        │     ┌─────┴──────│

│”──────────┘    │”──────────────┘    │”──────────────┘     │ Librairies │

                                                         │ standard   │

                                                         │”────────────┘

```

**Les deux étapes :**

1. **Compilation :** Chaque fichier `.cpp` est traduit en un **fichier objet** (code machine).

2. **Linkage (édition de liens) :** Le linker combine tous les fichiers objets + les bibliothèques standards en un **exécutable** unique.

> ⚠️ **Processus itératif :** Erreurs de compilation → correction → recompilation. Même après la compilation, des erreurs logiques peuvent subsister (le programme ne fait pas ce qu'on veut).

#### 2.3 Commande de compilation

```bash

$ g++ hello.cpp -o hello    # Compile hello.cpp en exécutable "hello"

$ ./hello                   # Lance le programme

Hello World !

```

> 🎯 **`g++`** est le compilateur C++ de GNU. Il traduit le code source en programme exécutable.

---

### 3. Hello World — Anatomie d'un programme C++

#### 3.1 Le code complet

```cpp

#include <iostream>         // ← Directive de préprocesseur : inclut les outils d'entrée/sortie (Input/Output Stream)

int main() {                // ← Point d'entrée obligatoire de tout programme C++

    std::cout << "Hello World !" << std::endl;   // ← Affiche "Hello World !" puis un retour à la ligne

    return 0;               // ← Retourne 0 au système d'exploitation (= pas d'erreur)

}

```

#### 3.2 Décortiquons chaque élément

| Élément | Rôle | Équivalent Python |

|---|---|---|

| `#include <iostream>` | Importe la bibliothèque I/O | `import sys` |

| `int main()` | Fonction principale (obligatoire) | Code au niveau du module |

| `{ }` | Délimitent un bloc d'instructions | Indentation |

| `std::cout` | Sortie console (*console output*) | `print()` |

| `<<` | Opérateur d'insertion (envoie vers cout) | `,` dans `print()` |

| `std::endl` | Retour à la ligne + vidage du tampon | `\n` |

| `;` | Fin d'instruction (obligatoire !) | Retour à la ligne |

| `return 0;` | Signal au système : « tout s'est bien passé » | `sys.exit(0)` |

| `std::` | Préfixe pour l'espace de noms standard | — |

#### 3.3 Commentaires

```cpp

// Ceci est un commentaire sur une seule ligne

/* Ceci est un

   commentaire sur

   plusieurs lignes */

```

> 🧠 **Bonne pratique :** Un bon code est lu plus souvent qu'il n'est écrit. Commentez pour expliquer le **pourquoi**, pas le **quoi**.

#### 3.4 `using namespace std;`

Pour éviter d'écrire `std::` à chaque fois :

```cpp

#include <iostream>

using namespace std;         // ← Rend tous les éléments de std accessibles directement

int main() {

    cout << "Hello World !" << endl;   // Plus besoin de std::

    return 0;

}

```

---

### 4. Types de données

#### 4.1 Les types de base

> 💡 **Différence fondamentale avec Python :** En C++, chaque variable a un type **fixé à la compilation**. On ne peut pas changer le type d'une variable après sa déclaration.

```cpp

int myNum = 5;               // Entier

float myFloatNum = 5.99;     // Flottant simple précision (4 bytes)

double myDoubleNum = 9.98;   // Flottant double précision (8 bytes)

char myLetter = 'D';         // Un seul caractère

bool myBoolean = true;       // Booléen (true/false)

string myText = "Hello";     // Chaîne de caractères (nécessite <string>)

```

| Type | Taille | Description | Plage approximative |

|---|---|---|---|

| `bool` | 1 byte | `true` ou `false` | 0 ou 1 |

| `char` | 1 byte | Un caractère / code ASCII | -128 à 127 |

| `int` | 2 ou 4 bytes | Entier | ±2 milliards (4 bytes) |

| `float` | 4 bytes | Flottant, ~6-7 chiffres significatifs | ±3.4 à— 10³⁸ |

| `double` | 8 bytes | Flottant, ~15 chiffres significatifs | ±1.8 à— 10³⁰⁸ |

#### 4.2 Qualificateurs de type

On peut modifier les types entiers :

| Qualificateur | Effet | Exemple |

|---|---|---|

| `short` | Entier court (≤ `int`) | `short int x;` ou `short x;` |

| `long` | Entier long (≥ `int`) | `long int x;` ou `long x;` |

| `signed` | Positif ou négatif (défaut pour `int`) | `signed int x;` |

| `unsigned` | ≥ 0 seulement, plage plus grande | `unsigned int x;` |

#### 4.3 Langage typé vs non typé

```cpp

// C++ — Erreur détectée à la COMPILATION

int a = 5;

std::string b = "hello";

// a + b;    // âŒ Erreur : impossible d'ajouter int et string

```

```python

# Python — Erreur détectée à l'EXÉCUTION

a = 5

b = "hello"

print(a + b)  # âŒ TypeError (mais seulement quand on exécute cette ligne)

```

> 🎯 **Avantage du typage statique :** Les erreurs sont détectées **avant** d'exécuter le programme. Plus sûr et plus rapide.

---

### 5. Caractères de contrôle

Les **séquences d'échappement** commencent par `\` et représentent des caractères spéciaux :

| Code | Signification | Exemple |

|---|---|---|

| `\n` | **Nouvelle ligne** | `cout << "A\nB";` → A puis B en dessous |

| `\t` | **Tabulation horizontale** | `cout << "A\tB";` → A     B |

| `\\` | Antislash littéral | `cout << "C:\\Users";` → C:\Users |

| `\"` | Guillemet double | `cout << "Il a dit : \"Salut !\"";` |

| `\'` | Guillemet simple | `cout << '\'';` |

| `\0` | **Caractère nul** (fin de C-string) | Marque la fin d'une chaîne C |

| `\a` | Alerte (bip sonore) | `cout << "Bip !\a";` |

| `\b` | Retour arrière (backspace) | |

| `\r` | Retour chariot | |

#### Exemple complet commenté

```cpp

#include <iostream>

#include <cstring>

using namespace std;

int main() {

    cout << "Hello\n\tWorld\n";            // Hello

                                           //     World

    cout << "Elle a dit : \"Salut !\"\n";  // Elle a dit : "Salut !"

    cout << "Bip !\a\n";                   // Bip ! (+ son système éventuel)

    // ⚠️ Caractère nul dans une chaîne : les fonctions C s'arrêtent à \0

    const char* s = "Jens\0Munk";

    cout << "strlen(s) = " << strlen(s) << "\n";  // strlen(s) = 4 (s'arrête à \0)

    cout << "s = " << s << "\n";                   // s = Jens (pas Munk !)

    return 0;

}

```

> 🧠 **Point subtil :** `\0` est **invisible** mais crucial. C'est lui qui dit aux fonctions C « la chaîne s'arrête ici ». Tout ce qui est après `\0` est ignoré par `strlen`, `cout`, etc.

---

### 6. Structures de contrôle

#### 6.1 `if` / `else`

```cpp

int i = 10;

if (i == 10)                // ⚠️ == pour tester l'égalité (pas = qui est l'affectation !)

    cout << "test passed";

else

    cout << "test failed";

// Affiche : test passed

```

**Pièges classiques :**

```cpp

// âŒ PIàˆGE : = au lieu de == (c'est une AFFECTATION, pas un test !)

if (i = 5)              // i prend la valeur 5, qui est non-nulle → true !

    cout << "test passed";  // Affiche TOUJOURS "test passed" !

// ✅ Valeurs de vérité en C++ :

if (5)   → true   // Tout entier ≠ 0 est "true"

if (0)   → false  // Seul 0 est "false"

// ⚠️ PIàˆGE : sans accolades, seule la PREMIàˆRE instruction après if est conditionnelle

if (true)

    cout << "test passed";

cout << "test failed";     // ← Cette ligne s'exécute TOUJOURS (pas dans le if) !

```

> 🧠 **Astuce mnémotechnique :** « `==` pour comparer, `=` pour copier. Deux yeux pour voir si c'est **é**gal ! »

#### 6.2 `switch` / `case`

```cpp

int day = 4;

switch (day) {

    case 1: cout << "Monday";    break;  // ← break est OBLIGATOIRE

    case 2: cout << "Tuesday";   break;  //    sinon on "tombe" dans le case suivant

    case 3: cout << "Wednesday"; break;

    case 4: cout << "Thursday";  break;  // ← Celui-ci s'exécute

    case 5: cout << "Friday";    break;

    case 6: cout << "Saturday";  break;

    case 7: cout << "Sunday";    break;

}

// Affiche : Thursday

```

> ⚠️ **Sans `break`**, l'exécution continue dans les `case` suivants (on appelle cela le *fall-through*).

#### 6.3 Boucle `for`

```cpp

// Syntaxe : for (initialisation; condition; incrémentation)

for (int i = 5; i < 10; i++)           // i va de 5 à 9

    cout << i << "\t" << i*i << "\n";  // Affiche i et i²

```

**Variantes :**

```cpp

for (int i = 5; i <= 10; i++)    // i va de 5 à 10 (inclus grâce à <=)

for (int i = 5; i < 10; i += 2) // i va de 5 à 9 avec un pas de 2 : 5, 7, 9

for (int i = 5; i < 5; i++)     // Jamais exécuté (condition fausse dès le départ)

for (int i = 5; ; )             // ⚠️ Boucle INFINIE (pas de condition d'arrêt)

for (;;)                         // ⚠️ Boucle INFINIE (tout est omis)

```

> 🧠 **Comparaison Python :** `for i in range(5, 10)` ↔ `for (int i = 5; i < 10; i++)`

#### 6.4 Boucle `while`

```cpp

int i = 0;

while (i < 5) {        // Tant que i < 5

    cout << i << ",\t";

    i++;                // Ne pas oublier l'incrémentation !

}

// Affiche : 0,  1,  2,  3,  4,

```

#### 6.5 Boucle `do...while`

```cpp

int i = 0;

do {

    cout << i << ",\t";

    i++;

} while (i < 5);       // La condition est testée APRàˆS chaque itération

// Affiche : 0,  1,  2,  3,  4,

```

> 🎯 **Différence clé :** `do...while` **exécute toujours au moins une fois** le corps de la boucle, même si la condition est fausse au départ. `while` peut ne jamais s'exécuter.

---

### 7. Les instructions (Statements)

> 💡 **Règle fondamentale :** En C++, une instruction se termine par `;` (point-virgule), pas par un retour à la ligne comme en Python. L'indentation et les espaces blancs **n'ont aucun rôle syntaxique** — ils servent uniquement à la lisibilité.

#### Types d'instructions

| Type | Exemples | Description |

|---|---|---|

| **Expression** | `x = 5;` `i++;` `cout << "Hi";` | La ligne de code la plus courante |

| **Composée (bloc)** | `{ instructions... }` | Groupe plusieurs instructions en une seule unité |

| **Sélection** | `if`, `switch` | Choisir un chemin d'exécution |

| **Boucle** | `for`, `while`, `do-while` | Répéter des instructions |

| **Saut** | `return`, `break`, `continue`, `goto` | Modifier le flux normal |

| **Déclaration** | `int x;` `double y = 3.14;` | Déclarer une variable (aussi une instruction en C++) |

> 🧠 **Portée (scope) :** Chaque bloc `{ }` crée une **portée**. Les variables déclarées dans un bloc sont **détruites** à la fin de ce bloc.

```cpp

{

    int x = 42;    // x existe ici

    cout << x;     // OK

}

// x n'existe plus ici ! → Erreur de compilation si on essaie de l'utiliser

```

---

### 8. Mini-projet : BMD Regression Tree

#### 8.1 Contexte

> 💡 **Qu'est-ce qu'un Regression Tree ?** Un modèle de machine learning qui prend des données en entrée et prédit une valeur. Le modèle a la forme d'un **arbre de décision** : à chaque nœud, on teste une condition et on descend à gauche ou à droite.

**Application :** Estimer la densité minérale osseuse (BMD — Bone Mineral Density) d'un patient à partir de son âge, poids, taille et temps d'attente.

#### 8.2 Version 0.1 — Test simple

```cpp

#include <iostream>

using namespace std;

// Fonction qui implémente l'arbre de décision

float estimate(float age, float weight_kg, float height_cm, float waiting_time) {

    // ... (arbre de décision codé en if-else imbriqués)

}

int main() {

    float bmd = estimate(60, 70, 165, 30);                   // Appel avec des données test

    std::cout << "Predicted BMD: " << bmd << std::endl;       // Devrait afficher 0.87

    return 0;

}

```

#### 8.3 Version 1.0 — Programme interactif complet

```cpp

int main() {

    char choice;                    // Pour stocker la réponse y/n

    float age, weight_kg, height_cm, waiting_time;

    cout << "=== BMD Estimator (Based on Trained Regression Tree) ===\n\n";

    do {

        // Demander les données du patient

        cout << "Enter patient details:\n";

        cout << "Age (years): ";     cin >> age;

        cout << "Weight (kg): ";     cin >> weight_kg;

        cout << "Height (cm): ";     cin >> height_cm;

        cout << "Waiting time (days): ";  cin >> waiting_time;

        // Calculer et afficher la prédiction

        float bmd = estimate(age, weight_kg, height_cm, waiting_time);

        cout << "\n--> Predicted BMD: " << bmd << "\n\n";

        // Continuer ?

        cout << "Estimate another patient? (y/n): ";

        cin >> choice;

        cout << "\n";

    } while (choice == 'y' || choice == 'Y');   // Boucle tant que l'utilisateur dit "oui"

    cout << "Thank you for using the BMD estimator!\n";

    return 0;

}

```

#### 8.4 L'arbre de décision (fonction `estimate`)

```cpp

float estimate(float age, float weight_kg, float height_cm, float waiting_time) {

    if (weight_kg <= 65.5) {                  // Premier test : poids ≤ 65.5 ?

        if (age <= 68.63) {                   // Deuxième test : âge ≤ 68.63 ?

            if (weight_kg <= 52.5) {

                return 0.68;                  // Feuille : BMD estimée = 0.68

            } else {

                if (height_cm <= 155.75) {

                    return 0.83;

                } else {

                    return 0.75;

                }

            }

        } else {                              // âge > 68.63

            if (waiting_time <= 19.5) {

                return 0.64;

            } else {

                return 0.56;

            }

        }

    } else {                                  // poids > 65.5

        if (height_cm <= 164.25) {

            // ... (suite de l'arbre)

        }

    }

}

```

> 🎯 **Ce qu'il faut retenir :** Cette version est **statique** — l'arbre est « codé en dur » dans le code. Si l'arbre change (nouveau modèle), il faut modifier le code et recompiler. La version 2.0 (cours suivant) résout ce problème en lisant l'arbre depuis un fichier.

#### 8.5 Concepts illustrés par ce mini-projet

| Concept | Utilisation dans le projet |

|---|---|

| `#include` | Importer `<iostream>` |

| Types (`float`, `char`) | Variables pour les données et le choix y/n |

| `cin` / `cout` | Interaction avec l'utilisateur |

| `if` / `else` | Arbre de décision |

| `do...while` | Boucle interactive « encore un patient ? » |

| Fonctions | `estimate()` séparée de `main()` |

| `return` | Valeur prédite ou code de sortie |

---

##  Cours 2 : File I/O, Strings, Structs & Fonctions

> 📚 **Objectif du cours :** Maîtriser la lecture/écriture de fichiers en C++, les différents types de chaînes de caractères (C-strings vs C++ strings), les structures (`struct`), les conversions de types, et les fonctions. Application au projet BMD Regression v2.0 (arbre dynamique lu depuis un fichier).

---

### Table des matières

1. [BMD Regression v2.0 — Architecture dynamique](#1-bmd-regression-v20--architecture-dynamique)

2. [File I/O : Lecture et écriture de fichiers](#2-file-io--lecture-et-écriture-de-fichiers)

3. [Streams : flux de données](#3-streams--flux-de-données)

4. [Arrays (Tableaux)](#4-arrays-tableaux)

5. [C-strings (`char[]`) vs C++ strings (`std::string`)](#5-c-strings-vs-c-strings)

6. [String Parsing : `sscanf` et `istringstream`](#6-string-parsing--sscanf-et-istringstream)

7. [Structures (`struct`)](#7-structures-struct)

8. [Conversion de types (Casting)](#8-conversion-de-types-casting)

9. [Fonctions](#9-fonctions)

---

### 1. BMD Regression v2.0 — Architecture dynamique

#### 1.1 Le problème de la v1.0

> 💡 **Rappel :** En v1.0, l'arbre de décision était codé en dur avec des `if-else` imbriqués. Tout changement de modèle nécessitait de modifier le code source et de recompiler.

**Problème :** Un outil de Machine Learning doit séparer :

1. **L'entraînement** (apprentissage du modèle → génère un fichier)

2. **L'inférence** (utilisation du modèle → lit le fichier)

#### 1.2 La solution v2.0

L'arbre est stocké dans un **fichier texte externe** (`bmd_tree_transitions.txt`) et lu dynamiquement à l'exécution.

```

Format du fichier : ID_nœud, ID_gauche, ID_droite, condition_ou_valeur

Exemple:

0,1,6,weight_kg <= 65.50

1,2,5,age <= 68.63

2,-1,-1,0.68             ← ID_gauche = ID_droite = -1 → feuille, valeur = 0.68

```

#### 1.3 Algorithme de parcours

```

1. nœudCourant = 1 (racine)

2. Lire nœudCourant depuis le fichier

3. Parser la ligne en <ID_nœud, ID_gauche, ID_droite, val_cond>

4. Si nœud terminal (ID_gauche == ID_droite == -1) :

      → Retourner val_cond (c'est la prédiction)

5. Sinon (val_cond encode une condition) :

      → Évaluer la condition

      → Si vraie : descendre à gauche

      → Sinon : descendre à droite

6. Retourner à l'étape 2

```

#### 1.4 Fonction `estimate` — Code commenté

```cpp

const char* filename = "bmd_tree_transitions.txt";

float estimate(float age, float weight_kg, float height_cm, float waiting_time) {

    ifstream tree(filename);             // Ouvre le fichier en lecture

    if (!tree.is_open())

        return 0.0;                      // Erreur : fichier introuvable

    int current = 1;                     // Commence à la racine (nœud ID = 1)

    char line[256];                      // Buffer pour stocker chaque ligne lue

    while (1) {                          // Boucle infinie (on sortira par return)

        tree.seekg(0);                   // Remet le curseur au DÉBUT du fichier

        while (!tree.eof()) {            // Parcourt toutes les lignes

            tree.getline(line, 256);     // Lit une ligne entière

            // Extrait l'ID du nœud (premier nombre avant la virgule)

            int node_id;

            sscanf(line, "%d,", &node_id);

            if (node_id == current) {    // Trouvé le nœud qu'on cherche !

                // Parse et évalue la ligne

                struct ParseResult res = parse_eval_line(

                    line, weight_kg, age, height_cm, waiting_time);

                if (res.is_leaf) {       // Si c'est une feuille...

                    tree.close();        // Ferme le fichier proprement

                    return res.value;    // Retourne la prédiction !

                } else

                    current = res.next_node;  // Descend vers l'enfant

            }

        }

    }

}

```

> 🧠 **Points clés :**

> - `seekg(0)` remet le curseur de lecture au début du fichier (nécessaire car on cherche un nœud différent à chaque itération)

> - On utilise une `struct ParseResult` pour retourner plusieurs valeurs corrélées depuis `parse_eval_line`

---

### 2. File I/O : Lecture et écriture de fichiers

#### 2.1 Les trois classes principales

```cpp

#include <fstream>    // ← Nécessaire pour les opérations sur fichiers

```

| Classe | Rôle | Équivalent Python |

|---|---|---|

| `ifstream` | **Lire** un fichier | `open("f", "r")` |

| `ofstream` | **Écrire** dans un fichier | `open("f", "w")` |

| `fstream` | **Lire et écrire** | `open("f", "r+")` |

#### 2.2 Écriture dans un fichier

```cpp

#include <iostream>

#include <fstream>

using namespace std;

int main() {

    ofstream myfile;                      // Déclare un flux de sortie

    myfile.open("example.txt");           // Ouvre (ou crée) le fichier

    myfile << "Writing this to a file.\n"; // Écrit avec << (comme cout)

    myfile.close();                       // ⚠️ TOUJOURS fermer le fichier !

    return 0;

}

```

#### 2.3 Lecture ligne par ligne

```cpp

string line;

ifstream myfile("example.txt");           // Ouverture directe dans le constructeur

if (myfile.is_open()) {                   // ⚠️ Toujours vérifier que l'ouverture a réussi

    while (getline(myfile, line))          // Lit chaque ligne complète (y compris les espaces)

        cout << line << '\n';             // Affiche la ligne

    myfile.close();

} else

    cout << "Unable to open file";

```

> 🎯 **`getline` vs `>>`** : `getline` lit toute la ligne (espaces compris). `>>` s'arrête au premier espace.

#### 2.4 Modes d'ouverture

```cpp

// Combinaison de modes avec | (ou logique)

fstream inoutFile("someName", ios::in | ios::out);  // Lecture ET écriture

```

| Mode | Description |

|---|---|

| `ios::in` | Lecture (défaut pour `ifstream`) |

| `ios::out` | Écriture (défaut pour `ofstream`) |

| `ios::app` | Écriture en fin de fichier (*append*) |

| `ios::trunc` | Écrase le contenu existant |

| `ios::binary` | Mode binaire (pas de conversion de caractères) |

#### 2.5 Pourquoi fermer un fichier ?

> ⚠️ **`close()` est essentiel :**

> 1. **Vide les tampons mémoire** → les données sont effectivement écrites sur le disque

> 2. **Libère le fichier** → d'autres programmes peuvent y accéder

> 3. En environnement partagé, un fichier non fermé reste **verrouillé**

---

### 3. Streams : flux de données

#### 3.1 Qu'est-ce qu'un stream ?

> 💡 Un **stream** (flux) est un courant d'octets entre votre programme et un périphérique externe (fichier, clavier, écran...).

#### 3.2 Mode texte vs mode binaire

| Aspect | Mode texte | Mode binaire |

|---|---|---|

| **Données** | Caractères, lignes (`\n`) | Octets bruts |

| **Opérateurs** | `<<` et `>>` | `write()` et `read()` |

| **Conversions** | Automatiques (ex: `\n` → `\r\n` sur Windows) | Aucune |

| **Taille de `1000000`** | 7 bytes (caractères '1','0','0','0','0','0','0') | 4 bytes (représentation en mémoire) |

| **Usage** | CSV, fichiers lisibles par l'homme | Images, données brutes |

#### 3.3 Hiérarchie des classes de streams

```

          ios (état + formatage)

         /                   \

    istream                ostream

    (lecture >>)           (écriture <<)

     /    \                 /    \

ifstream  iostream     ofstream  iostream

           \               /

            iostream → fstream

```

**Streams standards prédéfinis :**

- `cin` → objet `istream` (lecture au clavier)

- `cout` → objet `ostream` (écriture à l'écran)

- `cerr`, `clog` → objets `ostream` (erreurs)

> 🧠 **Grâce à l'héritage**, les mêmes opérateurs `<<` et `>>` fonctionnent partout : `cin >> x` et `fichier >> x` utilisent la même syntaxe !

#### 3.4 Manipulateurs de flux

```cpp

#include <iomanip>    // Nécessaire pour les manipulateurs

double pi = 3.14159;

cout << setprecision(3) << pi << endl;                    // 3.14 (3 chiffres au total)

cout << fixed << setprecision(3) << pi << endl;           // 3.142 (3 chiffres APRàˆS la virgule)

cout << setw(5) << setfill('.') << 42 << endl;            // ...42 (largeur 5, remplissage '.')

cout << left << setw(6) << setfill('.') << 100 << "end";  // 100...end

cout << right << setw(6) << setfill('.') << 100 << "end"; // ...100end

cout << scientific << setprecision(2) << 123.456 << endl;  // 1.23e+02

```

| Manipulateur | Effet | Persistant ? |

|---|---|---|

| `setprecision(n)` | Nombre de chiffres significatifs (ou après la virgule en mode `fixed`) | ✅ Oui |

| `setw(n)` | Largeur du champ d'affichage | âŒ Prochain affichage seulement |

| `setfill(ch)` | Caractère de remplissage | ✅ Oui |

| `fixed` | Notation décimale fixe | ✅ Oui |

| `scientific` | Notation scientifique | ✅ Oui |

| `left` / `right` | Alignement dans le champ | ✅ Oui |

| `endl` | Retour à la ligne + vidage du tampon | — |

| `flush` | Vidage du tampon sans retour à la ligne | — |

| `hex` / `oct` / `dec` | Base d'affichage des entiers | ✅ Oui |

---

### 4. Arrays (Tableaux)

#### 4.1 Déclaration et initialisation

```cpp

float grades[5];                       // Tableau de 5 float (non initialisé ⚠️)

int primes[5] = {1, 2, 3, 5, 7};      // Initialisé avec des valeurs

int primes[] = {1, 2, 3, 5, 7};       // Taille déduite automatiquement (5)

```

> 💡 Un **array** en C++ est une collection de cellules mémoire **contiguës**, toutes du **même type**, accessibles par un **index** commençant à 0.

#### 4.2 Accès aux éléments

```cpp

for (int i = 0; i < 5; i++)

    cout << primes[i] << '\t';         // Affiche : 1   2   3   5   7

```

> ⚠️ **Pas de vérification de bornes !** Accéder à `primes[10]` ne génère PAS d'erreur de compilation, mais lit de la mémoire invalide → comportement indéfini.

---

### 5. C-strings vs C++ strings

#### 5.1 C-string (`char[]`) — L'ancienne méthode

```cpp

// Character array simple (PAS une string !)

char vowels[5] = {'a', 'e', 'i', 'o', 'u'};  // Pas de \0 → DANGER avec cout/strlen

// C-string valide (terminée par \0)

char name[] = "Mae";      // 4 éléments : 'M', 'a', 'e', '\0'

char msg[10] = "Hi";      // 'H', 'i', '\0', puis 7 zéros

cout << name;             // Imprime "Mae" (s'arrête à \0)

cout << strlen(name);     // Affiche 3 (ne compte pas \0)

```

> ⚠️ **Règle critique :** Sans `\0`, les fonctions C (`strlen`, `strcpy`, `cout`) ne savent pas où la chaîne se termine → lecture de mémoire indéfinie, bugs, failles de sécurité.

#### 5.2 C++ string (`std::string`) — La méthode moderne ✅

```cpp

#include <string>

std::string name = "Mae West";     // Objet string complet

std::cout << name;                 // Imprime "Mae West"

std::cout << name.length();       // 8 (pas besoin de \0)

std::cout << name[0];             // 'M' (accès par index)

// Concaténation facile

std::string greeting = "Hello " + name;   // "Hello Mae West"

// Comparaison intuitive

if (name == "Mae West") { ... }           // Fonctionne directement !

if ("age" < "beauty") { ... }            // Comparaison lexicographique (ASCII)

// Recherche

size_t pos = name.find("West");           // pos = 4 (position de "West")

if (pos == string::npos) { ... }          // npos = "pas trouvé"

```

#### 5.3 Comparaison résumée

| Critère | C-string (`char[]`) | C++ string (`std::string`) |

|---|---|---|

| **Terminateur** | `\0` obligatoire | Pas nécessaire (longueur interne) |

| **Mémoire** | Gestion manuelle | Automatique |

| **Sécurité** | Risque de buffer overflow | Sûr |

| **Concaténation** | `strcat()` (dangereux) | Opérateur `+` |

| **Comparaison** | `strcmp()` | `==`, `<`, `>` |

| **Longueur** | `strlen()` (O(n)) | `.length()` ou `.size()` (O(1)) |

| **Usage recommandé** | API C, systèmes bas niveau | **Partout en C++** |

---

### 6. String Parsing : `sscanf` et `istringstream`

#### 6.1 `sscanf` — Parsing de style C

```cpp

#include <cstdio>

char line[] = "0,1,6,weight_kg <= 65.50";

int node_id, left_id, right_id;

char cond_val[128];

// Parse la ligne selon le format spécifié

// %d = entier, %127[^\n] = tout jusqu'à fin de ligne (max 127 chars)

sscanf(line, "%d,%d,%d,%127[^\n]", &node_id, &left_id, &right_id, cond_val);

// node_id=0, left_id=1, right_id=6, cond_val="weight_kg <= 65.50"

```

> 🧠 **`sscanf` retourne** le nombre de champs lus avec succès. Toujours vérifier : `if (sscanf(...) != 4) { erreur; }`

#### 6.2 `istringstream` — Parsing de style C++

```cpp

#include <sstream>

std::string input = "100 3.14";

std::istringstream inStr(input);      // Connecte le stream à la string

long value;

double data;

inStr >> value >> data;               // Extrait comme avec cin !

// value = 100, data = 3.14

```

#### 6.3 `ostringstream` — Construction de strings

```cpp

std::ostringstream outStr;

double number = 2.5;

outStr << "number = " << (number / 2.0);      // Écrit comme cout

std::string result = outStr.str();             // Récupère la string

// result == "number = 1.25"

```

#### 6.4 Application dans le projet BMD

La fonction `eval_condition` parse des conditions comme `"weight_kg <= 65.50"` :

```cpp

int eval_condition(char* cond,

    float weight_kg, float age, float height_cm, float waiting_time) {

    istringstream iss(cond);         // Connecte le stream à la C-String

    string feat, op;                 // feat = "weight_kg", op = "<="

    float threshold;                 // threshold = 65.50

    if (!(iss >> feat >> op >> threshold))   // Extraction des 3 composantes

        return 0;                            // Échec du parsing

    // Récupérer la valeur réelle de la caractéristique

    float feat_val = 0.0;

    if      (feat == "weight_kg")    feat_val = weight_kg;

    else if (feat == "age")          feat_val = age;

    else if (feat == "height_cm")    feat_val = height_cm;

    else if (feat == "waiting_time") feat_val = waiting_time;

    else return 0;                   // Caractéristique inconnue

    // Évaluer l'opérateur

    if      (op == "<=") return (feat_val <= threshold) ? 1 : 0;

    else if (op == "<")  return (feat_val < threshold)  ? 1 : 0;

    else if (op == "=")  return (feat_val == threshold) ? 1 : 0;

    else if (op == ">=") return (feat_val >= threshold) ? 1 : 0;

    else if (op == ">")  return (feat_val > threshold)  ? 1 : 0;

    else return 0;

}

```

> 🎯 **L'opérateur ternaire `? :`** est un raccourci pour `if-else` :

> ```cpp

> // Équivalent :

> res.next_node = take_left ? left_id : right_id;

> // ↔

> if (take_left) { res.next_node = left_id; } else { res.next_node = right_id; }

> ```

---

### 7. Structures (`struct`)

#### 7.1 Qu'est-ce qu'une struct ?

> 💡 Une `struct` regroupe des variables de **types différents** dans une seule unité nommée. C'est l'ancêtre de la classe en C++.

```cpp

struct Car {                // Définition d'un nouveau type "Car"

    std::string brand;      // Membre 1 : marque (string)

    std::string model;      // Membre 2 : modèle (string)

    int year;               // Membre 3 : année (int)

};                          // ⚠️ Point-virgule obligatoire après la }

// Utilisation

Car car1, car2;                                     // Déclare deux variables de type Car

car1.brand = "BMW";  car1.model = "X5";  car1.year = 1999;   // Accès via l'opérateur .

car2.brand = "Ford"; car2.model = "Mustang"; car2.year = 1969;

```

#### 7.2 Application dans le projet BMD

```cpp

struct ParseResult {

    int is_leaf;       // 1 = feuille (nœud terminal), 0 = nœud interne

    double value;      // Si feuille : la valeur prédite

    int next_node;     // Si interne : l'ID du prochain nœud

};

```

> 🧠 **Pourquoi utiliser une struct ?** Pour retourner **plusieurs valeurs corrélées** depuis une fonction, au lieu d'utiliser des paramètres de sortie ou des variables globales. L'interface est plus propre et le code plus lisible.

#### 7.3 Mémoire

Les membres d'une struct sont stockés de façon **contiguë** en mémoire (dans l'ordre de déclaration).

---

### 8. Conversion de types (Casting)

#### 8.1 Conversion implicite

```cpp

double x = 5;     // int → double automatiquement (pas de perte de données)

```

#### 8.2 Cast style C (déconseillé ⚠️)

```cpp

int n = (int)3.14;        // Syntaxe 1 : n = 3 (perte de la partie décimale)

int n = int(3.14);        // Syntaxe 2 : identique

```

> ⚠️ Le cast style C contourne les vérifications du compilateur → risque de masquer des erreurs.

#### 8.3 `static_cast` (recommandé ✅)

```cpp

double d = 3.14;

int n = static_cast<int>(d);   // Explicite, lisible, limité aux conversions compatibles

```

> 🎯 **Recommandation :** Toujours utiliser `static_cast` au lieu du cast style C. C'est plus explicite, facilement repérable dans le code, et offre une meilleure sécurité de typage.

---

### 9. Fonctions

#### 9.1 Structure d'une fonction

```cpp

// Prototype (déclaration) — avant main() ou dans un header

int addition(int, int);

// Définition — le corps de la fonction

int addition(int a, int b) {

    int r;

    r = a + b;

    return r;     // Retourne le résultat à l'appelant

}

// Appel

int main() {

    int z = addition(5, 3);               // z = 8

    cout << "The result is " << z;        // Affiche : The result is 8

}

```

#### 9.2 Concepts clés

| Concept | Description |

|---|---|

| **Prototype** | `type nom(params);` — Déclare l'interface avant utilisation |

| **Type de retour** | `int`, `double`, etc. — `void` si pas de valeur retournée |

| **Passage par valeur** | Les paramètres sont **copiés** (la fonction travaille sur des copies) |

| **`return`** | Transfère la valeur au contexte appelant et termine la fonction |

#### 9.3 Modularité et encapsulation

> 💡 Les fonctions réalisent l'**encapsulation logicielle** : elles exposent une interface minimaliste (prototype) tout en cachant leur implémentation interne.

**Avantages :**

- **Réutilisation** du code

- **Réduction** de la complexité cognitive

- **Isolation** des effets de bord

- Facilite la **maintenance** et les **tests unitaires**

> 🧠 **Bonne pratique :** Chaque fonction assume une **responsabilité unique** (*Single Responsibility Principle*).


## Cours 3 : Hiérarchie mémoire, Arrays avancés et Introduction à la POO

> 📚 **Objectif du cours :** Comprendre l'organisation de la mémoire (hiérarchie, tableaux explicites/pointeurs) et introduire la Programmation Orientée Objet (POO) en C++ avec les classes, l'encapsulation et les constructeurs, via la v3.0 du projet BMD.

---

#### 1. La Hiérarchie Mémoire

Pour optimiser un programme (comme l'arbre de régression BMD), il faut comprendre comment l'ordinateur stocke et accède aux données.

| Type de mémoire | Capacité temporelle | Temps d'accès | Coût |
|---|---|---|---|
| **Registres CPU** | Extrêmement faible (~KB) | < 0.3 ns | Très élevé (intégré) |
| **Cache L1/L2/L3** | Faible (KB à MB) | 1 à 20 ns | Très élevé (intégré) |
| **RAM (DRAM)** | Moyenne (Go) | ~ 50 ns | Moyen |
| **Storage (SSD/HDD)** | Énorme (To) | > 10 000 ns (µs/ms) | Faible |

> 🎯 **Règle d'or de l'optimisation :** **Privilégier la RAM aux accès disque**. C'est le principe de BMD v3.0 : au lieu de lire le fichier à chaque nœud (v2.0), on le charge *une fois* en RAM dans un Array. L'accès en RAM est des milliers de fois plus rapide que l'accès disque !

---

#### 2. Les Arrays (Tableaux) sous le capot

Un *array* en C++ est fondamentalement différent d'une liste Python.

##### 2.1 Adresse et contiguïté
```cpp
int primes[] = {1, 2, 3, 5, 7};
// primes pointe sur l'adresse mémoire de la PREMIÈRE case : primes[0]
```
- Chaque case occupe une taille fixe (ex: 4 bytes pour un `int`).
- Toutes les cases sont **contiguës** en mémoire.
- `primes + i` décale l'adresse de `i * sizeof(int)` bytes. L'arithmétique se fait en **éléments**, pas en octets bruts.

##### 2.2 Absence de contrôle des limites
> ⚠️ **Danger C++ :** Le C++ ne vérifie **JAMAIS** si vous dépassez la taille du tableau.

```cpp
int x = primes[10];  // ❌ Hors limites, mais compile !
```
Conséquences d'un accès hors limites :
1. **Segmentation Fault (Segfault) :** Le programme essaie d'accéder à une mémoire qui ne lui appartient pas → Crash immédiat.
2. **Corruption silencieuse :** L'accès se fait dans la zone mémoire d'une autre variable de votre programme → Bugs imprévisibles, difficiles à traquer (la valeur d'une autre variable change "toute seule").

##### 2.3 Calculer la taille d'un tableau
Idiome classique (style C) :
```cpp
int arrsize = sizeof(primes) / sizeof(primes[0]);
// Ex: (5 éléments * 4 bytes) / 4 bytes = 20 / 4 = 5
```

---

#### 3. Introduction aux Classes et à la POO

##### 3.1 POO vs Procédural
- **Procédural (C) :** Centré sur les **fonctions**. Les données et les fonctions qui les manipulent sont séparées. Dur à maintenir sur de gros projets.
- **Orienté Objet (POO - C++) :** Centré sur les **objets** métier. Les données (attributs) et les fonctions (méthodes) sont réunies au sein d'une même entité.

##### 3.2 Classe vs Objet
- Une **classe** (`class`) est un *nouveau type* de données défini par le programmeur. C'est le **patron** (blueprint).
- Un **objet** est une *instance* concrète créée à partir de cette classe.

```cpp
class Square {          // La classe (le patron)
    // ...
};                      // ⚠️ Point-virgule obligatoire

int main() {
    Square x;           // x est un OBJET de la classe Square
}
```

---

#### 4. Encapsulation et Masquage des données

L'**encapsulation** consiste à grouper l'État (données privées) et le Comportement (méthodes publiques).

##### 4.1 Spécificateurs d'accès
| Spécificateur | Visibilité |
|---|---|
| `private` | Uniquement accessible *depuis l'intérieur* de la classe (défaut). |
| `public` | Accessible *de partout* (c'est l'interface de la classe). |
| `protected` | Accessible à la classe et aux classes qui en héritent (vu plus tard). |

##### 4.2 Data Hiding
```cpp
class Square {
private:
    float side;         // Donnée cachée : l'utilisateur ne la manipule pas.
public:
    void setSide(float s) { side = s; }       // Setter (mutateur)
    float getSide() { return side; }          // Getter (accesseur)
};
```
> 🧠 **Pourquoi cacher `side` ?**
> 1. **Intégrité :** Dans `setSide`, on pourrait ajouter une vérification `if (s > 0)` pour refuser une longueur négative.
> 2. **Indépendance :** On peut réécrire l'intérieur de la classe sans casser le code de l'utilisateur.

---

#### 5. Séparation Interface / Implémentation

En C++, on sépare le "Quoi" (interface) du "Comment" (implémentation) :

##### 5.1 Fichier `.h` (Header - Interface)
Contient la déclaration de la classe et les prototypes.
```cpp
// square.h
class Square {
private:
    float side;
public:
    bool intersects(Square other);  // Prototype
};
```

##### 5.2 Fichier `.cpp` (Source - Implémentation)
Contient le code réel des fonctions longues.
```cpp
// square.cpp
#include "square.h"

// Le préfixe Square:: indique à quelle classe appartient la méthode
bool Square::intersects(Square other) {
    // Logique complexe...
}
```

---

#### 6. Les Constructeurs

Le **constructeur** est une méthode spéciale appelée *automatiquement* à la création de l'objet, pour l'initialiser dans un état propre.
- Toujours le **même nom que la classe**.
- **Pas de type de retour** (même pas `void`).

##### 6.1 Initialisation : syntaxe recommandée
Deux façons d'initialiser (utiliser la Liste d'Initialisation !) :

```cpp
// ❌ Méthode 1 : Affectation dans le corps (Moins performant)
Node::Node() {
    is_leaf = false;
    value = 0.0;
}

// ✅ Méthode 2 : Liste d'initialisation (Plus direct, obligatoire pour cont/références)
Node::Node() 
    : is_leaf(false), value(0.0), left_id(-1), right_id(-1) 
{
    // Le corps peut être vide
}
```

> ⚠️ Si vous créez un tableau d'objets (`Node tree[MAX_NODES]`), la classe **doit** avoir un constructeur vide (par défaut). Chaque case appellera ce constructeur.

---

#### 7. Énumérations (`enum`)

Créer un type dont les valeurs possibles sont limitées et nommées (internement, ce sont des entiers). Améliore considérablement la lisibilité (plus de "nombres magiques").

```cpp
enum Operator { OP_LE, OP_LT, OP_EQ, OP_GE, OP_GT };
// OP_LE vaut 0, OP_LT vaut 1, etc.

enum Fruit { apple = 15, grape, orange }; 
// grape vaut 16, orange 17.

Operator op = OP_EQ;
if (op == OP_EQ) { /* très lisible ! */ }
```

> ⚠️ On ne peut pas imprimer un enum directement avec `cout` : il affichera l'entier.

---

#### 8. Opérateurs d'incrémentation/décrémentation

- `++` ajoute 1, `--` soustrait 1.
- **Préfixe** (`++y`) : Incrémente PUIS utilise la valeur.
- **Suffixe** (`y++`) : Utilise la valeur PUIS incrémente.

```cpp
int x, y = 1;
x = ++y;  // PRE: y devient 2, puis on assigne 2 à x. (x=2, y=2)

int a, b = 1;
a = b++;  // POST: on assigne 1 à a, puis b devient 2. (a=1, b=2)
```

---

#### 9. Mini-Projet : BMD Regression v3.0

Avec nos notions de tableaux et de POO, nous pouvons optimiser le BMD.
L'idée : le fichier contient un ID de nœud pour chaque ligne. L'arbre est chargé dans un tableau : l'ID du nœud sert directement d'index dans le tableau `tree[MAX_NODES]`.

```cpp
// INFÉRENCE v3.0 (Boucle principale)
float estimate(float features[FEATURE_COUNT]) {
    int idx = 1; // La racine est à l'index 1
    
    while (idx < MAX_NODES) {
        if (tree[idx].test_leaf())          // Utilisation de méthode getter
            return tree[idx].get_value();
            
        bool go_left = tree[idx].eval_condition(features);
        // Descente vers l'enfant avec opérateur ternaire
        idx = go_left ? tree[idx].get_left() : tree[idx].get_right();
    }
    return 0.0;
}
```
L'accès direct par index `tree[idx]` se fait intégralement en RAM en quelques nanosecondes, contre de multiples lectures de fichier très lentes en v2.0.


---

## Cours 4 : Systèmes de numération, Pointeurs, Allocation dynamique & Opérations bit à bit

> 📚 **Objectif du cours :** Comprendre les systèmes de numération (binaire, hexadécimal), maîtriser les pointeurs et l'arithmétique des pointeurs, apprendre l'allocation dynamique de mémoire (new/delete), distinguer la Stack du Heap, et manipuler les données au niveau binaire avec les opérations bit à bit. Le tout est mis en pratique dans une version v4.0 de l'arbre de régression BMD utilisant des structures récursives avec pointeurs.

---

### 1. Systèmes de numération

#### 🔑 Pourquoi comprendre les systèmes de numération ?
Un ordinateur ne "pense" qu'en **binaire** (des 0 et des 1). Chaque donnée — un nombre, une lettre, une couleur — est au final stockée sous forme de bits. Comprendre comment convertir entre les bases numériques (décimal, binaire, octal, hexadécimal) est fondamental pour tout programmeur bas-niveau.

#### Les 4 systèmes principaux

| Système | Base | Chiffres | Usage principal |
|---|---|---|---|
| **Décimal** | 10 | 0-9 | Maths humaines |
| **Binaire** | 2 | 0, 1 | Mémoire machine |
| **Octal** | 8 | 0-7 | Rarement utilisé |
| **Hexadécimal** | 16 | 0-9, A-F | Affichage compact d'adresses mémoire |

#### Conversion Décimal → Binaire (méthode manuelle)

**Algorithme :** Divisions successives par 2, on note les restes de bas en haut.

**Exemple concret : convertir 42 en binaire :**

```
42 ÷ 2 = 21  reste 0  ← bit le moins significatif (LSB)
21 ÷ 2 = 10  reste 1
10 ÷ 2 = 5   reste 0
 5 ÷ 2 = 2   reste 1
 2 ÷ 2 = 1   reste 0
 1 ÷ 2 = 0   reste 1  ← bit le plus significatif (MSB)
```

On lit les restes **de bas en haut** : `42₁₀ = 101010₂`

**Vérification :** $1 \times 2^5 + 0 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 0 \times 2^0 = 32 + 8 + 2 = 42$ ✅

#### Conversion Décimal → Hexadécimal

Même algorithme, mais on divise par 16. Les restes de 10 à 15 deviennent les lettres A à F.

**Exemple : 255₁₀ → Hexadécimal**
```
255 ÷ 16 = 15  reste 15 → F
 15 ÷ 16 =  0  reste 15 → F
```
Résultat : `255₁₀ = FF₁₆`

#### Code C++ : conversion décimal → binaire

```cpp
#include <iostream>
#include <string>

std::string decimalToBinary(int n) {
    if (n == 0) return "0";
    
    std::string binary = "";
    while (n > 0) {
        // Préfixe le bit courant (le reste de la division par 2)
        // Si n est impair, le reste est 1, sinon 0
        binary = ((n % 2) ? '1' : '0') + binary;
        n /= 2;  // Division entière par 2
    }
    return binary;
}

int main() {
    int num = 42;
    std::cout << num << " en binaire = " << decimalToBinary(num) << std::endl;
    // Affiche : 42 en binaire = 101010
    return 0;
}
```

> 💡 **Astuce :** On préfixe chaque nouveau bit **à gauche** de la chaîne (`binary = ... + binary`), ce qui évite de devoir inverser la string à la fin, car les bits sont calculés du moins significatif au plus significatif.

#### Code C++ : conversion décimal → hexadécimal

```cpp
std::string decimalToHex(int n) {
    if (n == 0) return "0";

    std::string hex = "";
    while (n > 0) {
        int remainder = n % 16;
        char digit;
        if (remainder < 10)
            digit = '0' + remainder;        // 0-9 : on ajoute au code ASCII de '0'
        else
            digit = 'A' + (remainder - 10); // A-F : on décale à partir du code ASCII de 'A'
        hex = digit + hex;
        n /= 16;
    }
    return hex;
}
```

> 💡 **Pourquoi `'0' + remainder` ?** En C++, les caractères sont des entiers (code ASCII). `'0'` vaut 48. Donc `'0' + 3` donne 51, qui est le code ASCII de `'3'`. C'est un raccourci universel pour convertir un chiffre entier en son caractère correspondant !

---

### 2. L'opérateur d'adresse `&` et les variables pointeurs

#### 🔑 Concept clé : tout a une adresse

Chaque variable dans un programme est stockée physiquement quelque part dans la RAM. Cette position physique est appelée son **adresse mémoire**. L'opérateur `&` permet d'obtenir cette adresse.

```cpp
int num = -23;
cout << &num << '\t' << num;
// Affiche : 0x7fffffffd8e4    -23
//           ↑ adresse          ↑ valeur
```

> 💡 **Analogie :** Imaginez la RAM comme un immense casier de lycée. Chaque case a un numéro unique (l'adresse). La variable `num` est la valeur stockée dans la case. `&num` vous donne le numéro de la case.

#### 🔑 Les pointeurs : des variables qui stockent des adresses

Un **pointeur** est une variable spéciale dont le contenu n'est pas une donnée classique (int, float...), mais une **adresse mémoire**.

```cpp
int num = -23;        // num contient la valeur -23
int *ptr = &num;      // ptr contient l'ADRESSE de num

cout << ptr;          // Affiche l'adresse : 0x7fffffffd8dc
cout << *ptr;         // Affiche la VALEUR pointée : -23 (déréférencement)
cout << &ptr;         // Affiche l'adresse de ptr lui-même : 0x7fffffffd8e0
```

**Schéma mémoire :**
```
Variable   | Valeur              | Adresse
-----------|---------------------|------------------
num        | -23                 | 0x7fffffffd8dc
ptr        | 0x7fffffffd8dc      | 0x7fffffffd8e0
           | ↑ contient l'adresse de num
```

**Les 3 facettes d'un pointeur :**
- `ptr` → affiche l'adresse stockée (vers où il pointe)
- `*ptr` → affiche la valeur qui se trouve à l'adresse pointée (**déréférencement**)
- `&ptr` → affiche l'adresse du pointeur lui-même (car `ptr` est aussi une variable !)

#### Syntaxe de déclaration

Les espaces autour de `*` sont indifférents : `int* ptr`, `int *ptr`, `int * ptr` sont identiques.

```cpp
int *ptr, x, *y = nullptr, z = 12;
// ptr : pointeur vers int (non initialisé → dangereux !)
// x   : int classique (pas un pointeur !)
// y   : pointeur vers int, initialisé à nullptr (ne pointe vers rien)
// z   : int classique valant 12
```

> ⚠️ **Piège classique :** `int *ptr, x` → seul `ptr` est un pointeur ! `x` est un simple `int`. L'astérisque s'attache au nom de la variable, pas au type.

> 💡 **`nullptr`** est une adresse spéciale signifiant "ne pointe vers rien". Toujours initialiser un pointeur à `nullptr` s'il ne pointe pas encore vers quelque chose (évite les dangling pointers).

---

### 3. Arrays et Pointeurs : la relation fondamentale

#### 🔑 Le nom d'un array EST un pointeur constant

En C++, le nom d'un tableau se comporte comme un pointeur **constant** vers son premier élément.

```cpp
int val[] = {4, 7, 11};

// Ces deux expressions sont IDENTIQUES :
cout << val;        // adresse du premier élément
cout << &val[0];    // adresse du premier élément aussi !
```

**Mais attention** : `val` est un pointeur **constant**. On ne peut PAS faire `val = autre_array;` (erreur de compilation). En revanche, on peut créer un pointeur modifiable :
```cpp
int* p = val;       // p pointe vers val[0]
p = autre_array;    // OK, p est un vrai pointeur modifiable
```

#### 🔑 Arithmétique des pointeurs

Quand on ajoute un entier `n` à un pointeur, l'adresse se déplace de `n × sizeof(type)` bytes, pas de `n` bytes bruts !

```cpp
int val[] = {4, 7, 11};
// sizeof(int) = 4 bytes

cout << val;       // 0x...dc  (adresse de val[0])
cout << val + 1;   // 0x...e0  (adresse de val[1], +4 bytes)
cout << val + 2;   // 0x...e4  (adresse de val[2], +8 bytes)

// Déréférencement avec arithmétique :
cout << *val;       // 4   (= val[0])
cout << *(val + 1); // 7   (= val[1])
cout << *(val + 2); // 11  (= val[2])
```

**Équivalence fondamentale :** `val[i]` ≡ `*(val + i)`

> ⚠️ **Parenthèses obligatoires !** `*(ptr + 1)` et `*ptr + 1` sont très différents :
> - `*(ptr + 1)` → déréférence l'adresse suivante (la valeur de `val[1]`)
> - `*ptr + 1` → déréférence `ptr` d'abord, puis ajoute 1 à la valeur (= `val[0] + 1`)

> ⚠️ **Règle de sécurité :** L'arithmétique des pointeurs n'est valide que dans l'intervalle `[&array[0], &array[taille]]`. Dépasser ces limites → comportement indéfini (plantage ou corruption silencieuse de la mémoire).

---

### 4. Allocation dynamique de mémoire (new / delete)

#### 🔑 Pourquoi l'allocation dynamique ?

Avec l'allocation **statique** (`int tab[100];`), la taille est fixée à la compilation. Problème :
- Si les données réelles sont plus petites → **gaspillage de mémoire**
- Si les données sont plus grandes → **dépassement de tableau** (crash)

L'allocation **dynamique** résout ce problème : on réserve de la mémoire **à l'exécution**, au moment précis où on en a besoin, et on peut choisir exactement la taille nécessaire.

#### Syntaxe de base : `new` et `delete`

```cpp
// Allocation d'un SEUL objet :
float *number = new float(-6);     // Alloue un float sur le Heap, initialisé à -6
cout << *number;                   // -6

// Modification via déréférencement :
*number = 3.14;

// Libération de la mémoire :
delete number;        // Rend la mémoire au système
number = nullptr;     // Bonne pratique : éviter le dangling pointer
```

#### Allocation d'arrays dynamiques : `new[]` et `delete[]`

```cpp
int n = 5;                              // n peut être déterminé à l'exécution !
double *decimals = new double[n];       // Alloue un array de 5 doubles sur le Heap

// Utilisation classique :
for (int i = 0; i < n; i++) {
    decimals[i] = i * 1.5;
}

// Libération avec CROCHETS (obligatoire pour les arrays !)
delete[] decimals;    // ← les [] sont indispensables
decimals = nullptr;
```

> ⚠️ **Règle absolue :** `new` → `delete`. `new[]` → `delete[]`. Confondre les deux (utiliser `delete` au lieu de `delete[]` pour un array) provoque un **comportement indéfini** : seul le premier élément serait libéré, les autres resteraient en mémoire.

#### Les dangers : Memory Leaks et Dangling Pointers

**Memory Leak (Fuite de mémoire) :** Si on oublie `delete`, la mémoire reste réservée jusqu'à la fin du programme.
```cpp
void mauvaise_fonction() {
    int* p = new int(42);
    // On oublie delete p → fuite mémoire !
    // Quand la fonction se termine, le pointeur p est détruit (il était sur la Stack),
    // mais le bloc mémoire sur le Heap reste alloué et INACCESSIBLE à jamais.
}
```

**Dangling Pointer :** Après un `delete`, le pointeur conserve l'ancienne adresse (désormais invalide). Accéder à cette adresse → comportement indéfini.
```cpp
int* p = new int(42);
delete p;       // Mémoire libérée, mais p contient encore l'ancienne adresse !
cout << *p;     // DANGER : comportement indéfini !
p = nullptr;    // Bonne pratique : réinitialiser immédiatement après delete
```

---

### 5. Structure de la mémoire : Stack vs Heap

#### 🔑 Les 4 zones mémoire d'un programme

Lors de l'exécution d'un programme C++, le système d'exploitation lui alloue un espace mémoire partitionné en 4 régions :

| Zone | Contenu | Gestion |
|---|---|---|
| **Text** | Instructions machine (code compilé) | Fixe |
| **Global/Static** | Variables globales et `static` | Allouées au démarrage, libérées à la fin |
| **Stack (Pile)** | Variables locales, paramètres de fonctions | **Automatique** (LIFO) |
| **Heap (Tas)** | Objets alloués avec `new` | **Manuelle** (new/delete) |

#### La Stack (Pile) en détail

- Fonctionne en **LIFO** (Last-In, First-Out) : comme une pile d'assiettes.
- Quand une fonction est appelée → ses variables locales sont "poussées" (push) sur la pile.
- Quand la fonction retourne → ses variables sont "dépilées" (pop) et la mémoire est automatiquement restituée.
- **Avantages :** Extrêmement rapide (un simple ajustement de pointeur de sommet).
- **Limites :** Taille limitée (~1-8 Mo), durée de vie liée à la fonction.

```cpp
void exemple() {
    int x = 42;       // x est sur la Stack
    double y = 3.14;  // y est sur la Stack
}   // Ici, x et y sont automatiquement détruits et leur mémoire libérée
```

#### Le Heap (Tas) en détail

- Permet d'allouer et libérer des blocs mémoire **dans n'importe quel ordre**.
- La taille peut être déterminée **à l'exécution** (saisie utilisateur, taille d'un fichier...).
- La durée de vie des objets **dépasse celle de la fonction** qui les a créés.
- **Avantages :** Flexible, très grande capacité.
- **Inconvénients :** Plus lent (recherche de blocs libres, fragmentation), et le programmeur DOIT libérer explicitement la mémoire.

```cpp
int* creerTableau(int taille) {
    int* tab = new int[taille];  // Alloué sur le Heap
    return tab;                  // Le tableau SURVIT à la fin de la fonction !
}

int main() {
    int* monTab = creerTableau(100);
    // monTab pointe vers le tableau sur le Heap
    delete[] monTab;  // L'appelant est responsable de la libération
}
```

---

### 6. Pointeur vers une Classe (ou struct) : l'opérateur `->`

Lorsqu'un pointeur pointe vers un objet (instance d'une classe ou d'une struct), on utilise l'opérateur **flèche** `->` pour accéder aux membres.

```cpp
class Box {
public:
    double length;
    double volume() { return length * length * length; }
};

int main() {
    Box* pbox = new Box();      // pbox est un POINTEUR vers un objet Box sur le Heap
    pbox->length = 5.0;         // Accès au membre via ->
    double v = pbox->volume();  // Appel de méthode via ->

    // Équivalent plus verbeux (déréférencement explicite + point) :
    (*pbox).length = 5.0;
    double v2 = (*pbox).volume();

    delete pbox;
    return 0;
}
```

**Règle simple :**
- Objet direct (ex: `Box b;`) → utiliser le **point** : `b.length`
- Pointeur vers objet (ex: `Box* p;`) → utiliser la **flèche** : `p->length`

---

### 7. Structures de données récursives : l'arbre binaire (BMD v4.0)

#### 🔑 L'astuce fondamentale : un type qui se contient lui-même (via pointeurs)

Pour modéliser un arbre, il faut un **type de données récursif** : la classe `Node` contient des pointeurs vers d'autres `Node`.

```cpp
class Node {
private:
    float value;          // Valeur de la feuille
    float threshold;      // Seuil de décision (nœud interne)
    Node* left;           // Pointeur vers le sous-arbre gauche
    Node* right;          // Pointeur vers le sous-arbre droit
public:
    // Getters et Setters
    void set_left(Node* l) { left = l; }
    void set_right(Node* r) { right = r; }
    Node* get_left() { return left; }
    Node* get_right() { return right; }
    bool test_leaf() { return (left == nullptr && right == nullptr); }
    
    // Constructeurs et Destructeur
    Node();
    Node(const char* cond_val, const bool is_leaf);
    ~Node();
};
```

> 💡 **Pourquoi des pointeurs (`Node*`) et pas des objets directs (`Node`) ?** Si on écrivait `Node left; Node right;`, chaque Node contiendrait deux Node complets, qui contiendraient eux-mêmes deux Node, etc. → **taille mémoire infinie !** Les pointeurs brisent cette récursion car un pointeur a toujours une taille fixe (8 bytes sur 64 bits), quelle que soit la taille de l'objet pointé.

#### Constructeur par défaut et constructeur paramétré

```cpp
// Constructeur par défaut : initialise un Node "vide" et sûr
Node::Node()
    : left(nullptr), right(nullptr), value(0), feature(WEIGHT_KG)
{}
// left et right à nullptr = pas d'enfants
// value à 0 = valeur neutre
// feature initialisé par défaut

// Constructeur paramétré : crée un Node depuis une chaîne parsée
Node::Node(const char* cond_val, const bool is_leaf)
    : left(nullptr), right(nullptr), feature(WEIGHT_KG) {
    parse_condition(cond_val, is_leaf);
    // Délègue le parsing à une méthode dédiée
}
```

#### 🔑 Le destructeur récursif : libérer tout l'arbre automatiquement

```cpp
Node::~Node() {
    if (left != nullptr) delete left;
    if (right != nullptr) delete right;
}
```

**Comment ça marche ?** Quand on fait `delete root;` sur la racine :
1. Le destructeur de `root` est invoqué.
2. Il fait `delete left;` → ce qui invoque le destructeur du nœud gauche.
3. Ce destructeur fait lui-même `delete` sur SES enfants, etc.
4. La récursion se propage jusqu'aux feuilles (dont `left` et `right` sont `nullptr`).
5. Les tests `if (left != nullptr)` brisent la récursion aux feuilles.
6. Résultat : **tout l'arbre est libéré proprement en un seul `delete root`**.

> ⚠️ **Sans les gardes `if (left != nullptr)` :** supprimer un nœud feuille (dont les enfants sont `nullptr`) déclencherait une descente sans fin sur la stack, accumulant des appels récursifs jusqu'au **stack overflow** (dépassement de pile).

#### La fonction `read_tree` : construire l'arbre depuis un fichier

```cpp
Node* read_tree(const char* filename) {
    // Ouvrir le fichier...
    Node* root = NULL;
    while (fp.getline(line, sizeof(line))) {
        // Parser chaque ligne...
        if (root == nullptr) {
            // Premier nœud → créer la racine
            root = new Node(cond_val, is_leaf);
        } else {
            // Trouver le parent du nœud courant
            Node* parent = find_parent(root, node_id);
            if (node_id % 2 == 0)   // Enfant gauche (index pair)
                parent->set_left(new Node(cond_val, is_leaf));
            else                     // Enfant droit (index impair)
                parent->set_right(new Node(cond_val, is_leaf));
        }
    }
    fp.close();
    return root;  // L'appelant est désormais propriétaire de ce pointeur
}
```

#### La fonction `estimate` : parcourir l'arbre pour prédire

```cpp
float estimate(Node* root, float features[FEATURE_COUNT]) {
    Node* cur = root;  // Commencer à la racine
    while (cur != nullptr) {
        float res = cur->eval_condition(features);
        if (res == -1)         // Aller à gauche
            cur = cur->get_left();
        else if (res == 0)     // Aller à droite
            cur = cur->get_right();
        else                   // Feuille : retourner le résultat
            return res;
    }
    return 0.0; // Fallback
}
```

#### La fonction `print_tree` : parcours infixe récursif

```cpp
void Node::print_tree(Node* cur) {
    if (cur->left != nullptr) print_tree(cur->left);   // Visiter gauche
    cout << cur->value << ", " << cur->feature          // Afficher nœud
         << ", " << cur->threshold << endl;
    if (cur->right != nullptr) print_tree(cur->right);  // Visiter droite
}
```

Ce parcours **infixe** (gauche → racine → droite) affiche les nœuds dans un ordre cohérent pour un arbre de décision.

---

### 8. Opérations bit à bit (Bitwise Operations)

#### 🔑 Pourquoi manipuler les bits directement ?

Les opérations bit à bit permettent de manipuler la **représentation binaire** des entiers. Elles sont exécutées en un seul cycle processeur et sont donc extrêmement performantes. Elles sont utilisées pour :
- Le calcul haute performance
- La configuration de registres matériels
- La gestion de permissions/drapeaux
- La navigation dans les arbres binaires (comme `find_parent`)

#### Décalage de bits : `<<` et `>>`

**Décalage à gauche (`<<`) = Multiplication par une puissance de 2**

```cpp
int x = 5;       // Binaire : 00000101
int y;

y = x << 1;      // 00001010 → valeur 10  (5 × 2¹)
y = x << 2;      // 00010100 → valeur 20  (5 × 2²)
```

**Décalage à droite (`>>`) = Division entière par une puissance de 2**

```cpp
y = 20;           // 00010100
y >>= 1;          // 00001010 → valeur 10  (20 / 2¹)
y >>= 2;          // 00000010 → valeur 2   (10 / 2²)
```

#### AND bit à bit (`&`) : le masquage

L'opérateur `&` compare chaque bit individuellement. Le résultat est `1` uniquement si les deux bits sont `1`.

```cpp
int flags = 0b11010110;  // 214 en décimal
int mask  = 0b00001111;  // Masque : on ne garde que les 4 bits de poids faible

int result = flags & mask;
// 11010110
// 00001111
// --------
// 00000110 → 6
```

> 💡 **Utilité :** Extraire des champs spécifiques d'un registre. Par exemple, isoler les 4 bits de poids faible d'un octet de configuration.

#### OR bit à bit (`|`) : activer des bits

L'opérateur `|` met un bit à `1` si au moins un des deux bits est `1`.

```cpp
int reg = 0b00000001;    // Valeur initiale : 1
reg |= (1 << 3);         // (1 << 3) = 0b00001000 = masque avec bit 3 activé

// 00000001
// 00001000
// --------
// 00001001 → 9
```

> 💡 **Utilité :** Activer un drapeau spécifique sans toucher aux autres bits. Exemple : activer le bit 3 d'un registre de configuration matériel.

#### Application pratique : `find_parent` dans l'arbre

La fonction `find_parent` utilise le masquage binaire pour naviguer dans l'arbre :

```cpp
Node* find_parent(Node* root, int node_idx) {
    int level = floor(log2(node_idx));
    int mask = pow(2, level - 1);

    Node* cur = root, *prev;
    while (mask > 0) {
        prev = cur;
        if (node_idx & mask)          // Le bit courant est-il 1 ?
            cur = cur->get_right();   // Oui → aller à droite
        else
            cur = cur->get_left();    // Non → aller à gauche
        mask >>= 1;                   // Passer au bit suivant
    }
    return prev;
}
```

> 💡 **Idée géniale :** Dans un arbre binaire complet, la représentation binaire de l'index d'un nœud encode son chemin depuis la racine ! Chaque bit (après le premier `1`) indique : `0` = gauche, `1` = droite.

---

### 9. Le programme `main()` complet (BMD v4.0)

```cpp
int main() {
    Node* root = read_tree("bmd_tree_transition.txt");  // Allocation dynamique
    float age, weight_kg, height_cm, waiting_time;
    char choice;

    do {
        // Lire les données du patient...
        float features[FEATURE_COUNT] = {weight_kg, age, height_cm, waiting_time};
        float bmd = estimate(root, features);
        cout << "\n--> Predicted BMD: " << bmd << "\n\n";
        cout << "Estimate another patient? (y/n): ";
        cin >> choice;
    } while (choice == 'y');

    delete root;  // Désallocation propre : le destructeur récursif libère tout l'arbre
    return 0;
}
```

> 💡 **Point clé :** Un seul `delete root` suffit pour libérer l'intégralité de l'arbre grâce au destructeur récursif défini dans la classe `Node`. Chaque nœud supprime ses enfants, qui suppriment les leurs, etc., jusqu'aux feuilles.
