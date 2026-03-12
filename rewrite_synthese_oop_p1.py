import os

BASE = 'Informatique_OOP'
filepath = os.path.join(BASE, 'Synthese_Informatique_OOP.md')

content = r'''# 📖 Synthèse Complète — Informatique OOP (INFOH2001)

---

##  Cours 1 : De Python à C++

### 1.1 Pourquoi C++ ?

**Définition** : C++ est un langage de programmation **compilé, statiquement typé, et bas niveau**, créé par Bjarne Stroustrup dans les années 1980 comme extension orientée objet du langage C.

**Intuition** : Python te permet d'aller vite en prototypage mais il est lent à l'exécution. C++ t'oblige à être précis (gestion manuelle de la mémoire, types déclarés), mais en échange tu obtiens des performances proches du matériel. En ingénierie, cette maîtrise fine est souvent indispensable (systèmes embarqués, jeux vidéo, IA côté entraînement, systèmes d'exploitation).

**Tableau comparatif** :

| Critère | C++ | Python |
|---|---|---|
| **Type** | Compilé | Interprété |
| **Niveau** | Bas (proche machine) | Haut (abstrait) |
| **Vitesse** | Très rapide ⚡ (×10 à ×100) | Plus lent 🐌 |
| **Mémoire** | Gestion manuelle | Automatique (GC) |
| **Typage** | Statique (à la compilation) | Dynamique (à l'exécution) |
| **Utilisation** | Systèmes, jeux, IA libs, embarqué | Prototypage, data science |

**Exemples d'applications C++** : Chrome, Windows, macOS, PyTorch/TensorFlow (backend), Unreal Engine.

**⚠️ Piège classique** : Croire que « C++ = Python mais plus rapide ». C++ est fondamentalement **différent** : types obligatoires, gestion de la mémoire manuelle, compilation. Ce n'est pas un simple changement de syntaxe.

---

### 1.2 Compilation : du code source à l'exécutable

**Définition** : La **compilation** est le processus qui traduit tout le code source en code machine **avant** l'exécution, produisant un fichier exécutable autonome.

**Intuition** : Imagine un traducteur qui traduit intégralement un roman du français vers l'anglais **une fois pour toutes** (compilateur), versus un interprète qui traduit phrase par phrase en temps réel à voix haute (interpréteur). Le traducteur est plus lent au départ mais le roman traduit peut être lu à toute vitesse.

**Développement — Les deux modes de traduction** :

```
COMPILÉ (C, C++, Rust, Go) :
   Code source (.cpp) → [Compilateur g++] → Code machine/Objet (.o) → [Linker] → Exécutable
                                                                          ↑
                                                              Librairies standard

INTERPRÉTÉ (Python, JavaScript) :
   Code source → [Interpréteur] → Exécution instruction par instruction
```

**Les 3 étapes de la compilation C++ :**
1. **Préprocesseur** : traite les `#include`, `#define` (avant compilation)
2. **Compilation** : traduit chaque fichier `.cpp` en fichier objet `.o` (code machine)
3. **Linkage** : combine tous les `.o` + librairies en un seul exécutable

**Exemple concret — compiler et exécuter** :
```bash
# Compiler le fichier hello.cpp et créer l'exécutable 'hello'
$ g++ hello.cpp -o hello

# Lancer l'exécutable
$ ./hello
Hello World !
```

**⚠️ Piège classique** : Il existe **deux types d'erreurs** :
- **Erreur de compilation** : le compilateur refuse de produire l'exécutable (syntaxe incorrecte, type incompatible). Détectée tôt.
- **Erreur logique** : le programme compile et tourne, mais produit un résultat faux. La plus difficile à trouver.

---

### 1.3 Hello World — Anatomie d'un programme C++

**Définition** : `main()` est la fonction obligatoire qui constitue le **point d'entrée** de tout programme C++ exécutable. Le système d'exploitation y démarre l'exécution.

**Exemple complet commenté** :

```cpp
#include <iostream>   // Directive préprocesseur : importe la librairie d'entrées/sorties
                      // Équivalent de 'import sys' en Python

using namespace std;  // Évite d'écrire 'std::' devant chaque fonction standard
                      // (optionnel mais pratique pour débuter)

int main() {          // OBLIGATOIRE. Retourne int (code de sortie) au système d'exploitation.
    cout << "Hello World !" << endl;
    //  ↑          ↑              ↑
    //  flux stdout  message   retour à la ligne + flush du buffer
    return 0;         // 0 = succès. Tout autre valeur = erreur signalée à l'OS.
}
```

**Détail des éléments clés** :
- `#include <iostream>` : ajoute le contenu de la librairie iostream (Input/Output Stream) qui contient `cout`, `cin`, etc.
- `std::` : préfixe indiquant que les symboles appartiennent au **namespace** standard
- `<<` : opérateur d'insertion dans le flux de sortie (envoie des données vers `cout`)
- `>>` : opérateur d'extraction (lit depuis `cin`)
- `endl` : insère `\n` **et** vide le buffer. `'\n'` seul est plus rapide si le flush n'est pas nécessaire.
- `return 0;` : retourne le code 0 (succès) au système d'exploitation

**Commentaires** :
```cpp
// Commentaire sur une ligne

/* Commentaire
   sur plusieurs
   lignes */
```

**⚠️ Piège classique** : Oublier le point-virgule `;` à la fin d'une instruction. En Python, les fins de ligne suffisent. En C++, chaque instruction **doit** se terminer par `;`.

---

### 1.4 Types de données

**Définition** : En C++, toute variable doit avoir un **type déclaré avant utilisation**. Ce type est vérifié à la compilation (typage statique).

**Intuition** : Déclarer un type, c'est réserver exactement la bonne case mémoire. Déclarer `int x` réserve 4 bytes. Le compilateur sait alors comment interpréter ces bytes.

**Types fondamentaux** :

| Type | Taille | Plage approximative | Exemple |
|---|---|---|---|
| `bool` | 1 byte | `true` / `false` | `bool actif = true;` |
| `char` | 1 byte | `-128` à `127` (ou caractère ASCII) | `char c = 'A';` |
| `int` | 4 bytes | `−2 147 483 648` à `+2 147 483 647` | `int n = 42;` |
| `float` | 4 bytes | ~6-7 décimales de précision | `float f = 3.14f;` |
| `double` | 8 bytes | ~15-16 décimales de précision | `double d = 3.14159265;` |

**Qualificateurs de type** :
```cpp
short int s = 100;          // Entier court (≤ 2 bytes)
long int  l = 1000000;      // Entier long (≥ 4 bytes)
unsigned int u = 65000;     // Entier non signé (valeurs ≥ 0 uniquement, double la plage positive)
unsigned char uc = 255;     // 0 à 255
```

**Exemple complet avec comparaison Python vs C++** :

```python
# Python — typage dynamique
a = 5       # 'a' peut changer de type
b = "hello"
print(a + b)  # Erreur à l'EXÉCUTION : TypeError
```

```cpp
// C++ — typage statique
int a = 5;
string b = "hello";
// a + b;  // ERREUR À LA COMPILATION — le compilateur refuse avant même d'exécuter
return 0;
```

**⚠️ Piège classique** : En C++, `5 / 2` vaut `2` (division entière !), pas `2.5`. Pour obtenir `2.5`, il faut écrire `5.0 / 2` ou `(double)5 / 2`.

---

### 1.5 Caractères de contrôle (Escape sequences)

**Définition** : Séquences spéciales dans les chaînes de caractères, préfixées par `\`, qui représentent des caractères non imprimables ou des caractères spéciaux.

**Tableau** :

| Code | Signification | Exemple d'utilisation |
|---|---|---|
| `\n` | Nouvelle ligne | `cout << "Ligne 1\nLigne 2";` |
| `\t` | Tabulation horizontale | `cout << "Col1\tCol2";` |
| `\\` | Backslash littéral | `cout << "C:\\Users\\";` |
| `\"` | Guillemet double littéral | `cout << "Elle dit \"Bonjour\"";` |
| `\0` | Caractère nul (fin de C-string) | Utilisé implicitement dans les tableaux de char |

**Exemple complet** :
```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    cout << "Hello\n\tWorld\n";
    // Affiche :
    // Hello
    //     World

    cout << "Elle a dit : \"Salut !\"\n";
    // Affiche : Elle a dit : "Salut !"

    const char* s = "Jens\0Munk";  // Chaîne avec un \0 au milieu
    cout << strlen(s) << "\n";      // Affiche : 4   (s'arrête au premier \0)
    cout << s << "\n";              // Affiche : Jens (idem)
    return 0;
}
```

**⚠️ Piège classique** : Le caractère nul `\0` **termine** toute C-string. Insérer un `\0` au milieu d'une chaîne coupe la chaîne à cet endroit pour toutes les fonctions standard comme `strlen()`, `cout <<`.

---

### 1.6 Structures de contrôle

**Définition** : Les structures de contrôle dirigent le **flux d'exécution** du programme (branchements, erreurs, répétitions).

#### if / else

```cpp
int i = 10;
if (i == 10) {
    cout << "test passed";
} else {
    cout << "test failed";
}
// Affiche : test passed
```

**Attention — piège d'affectation dans le if** :
```cpp
if (i = 5)   // PIÈGE : ce n'est PAS un test d'égalité, c'est une AFFECTATION !
             // i vaut maintenant 5, et comme 5 != 0, la condition est vraie
    cout << "test passed";  // Sera toujours affiché !

if (i == 5)  // CORRECT : double == pour la comparaison
    cout << "test passed";
```

#### switch / case

```cpp
// Utile quand on teste plusieurs valeurs entières ou de type char
int day = 4;
switch (day) {
    case 1: cout << "Monday";    break;  // break OBLIGATOIRE pour éviter le 'fall-through'
    case 2: cout << "Tuesday";   break;
    case 3: cout << "Wednesday"; break;
    case 4: cout << "Thursday";  break;  // Exécuté ici
    case 5: cout << "Friday";    break;
    default: cout << "Weekend";  break;
}
// Affiche : Thursday
```

**⚠️ Piège classique — fall-through** :
```cpp
switch (day) {
    case 3: cout << "Wednesday";  // Si pas de break, continue vers case 4 !
    case 4: cout << "Thursday";   // Les deux sont affichés si day == 3
    break;
}
```

#### Boucles for, while, do-while

```cpp
// FOR : quand le nombre d'itérations est connu
for (int i = 5; i < 10; i++) {         // init ; condition ; incrément
    cout << i << "\t" << i*i << "\n";  // Affiche 5 25, 6 36, ..., 9 81
}

// Variantes for moins courantes mais importantes :
for (int i = 5; i <= 10; i += 2)       // Pas de 2 : 5, 7, 9
for (int i = 5; ; )                    // Boucle infinie (condition toujours vraie si vide)
for (;;)                               // Boucle infinie classique

// WHILE : quand la condition est testée AVANT l'itération
int i = 0;
while (i < 5) {
    cout << i << ", ";   // 0, 1, 2, 3, 4,
    i++;
}

// DO-WHILE : la boucle s'exécute AU MOINS UNE FOIS (condition testée APRÈS)
int i = 0;
do {
    cout << i << ", ";   // 0, 1, 2, 3, 4,
    i++;
} while (i < 5);
```

**⚠️ Piège classique** : `do-while` s'exécute **toujours au moins une fois**, même si la condition est fausse dès le départ. À utiliser intentionnellement (ex: interface utilisateur demandant au moins une saisie).

---

### 1.7 Instructions (Statements)

**Définition** : Une **instruction** (statement) est une unité d'exécution de base en C++, terminée généralement par un `;`.

**Les 7 types d'instructions en C++** :

1. **Instruction-expression** : `x = 5;`, `i++;`, `cout << "Bonjour";`
2. **Instruction composée (bloc)** : `{ instr1; instr2; }` — regroupe plusieurs instructions et crée une portée (scope)
3. **Instruction de sélection** : `if`, `switch`
4. **Instruction de boucle** : `for`, `while`, `do-while`
5. **Instructions de saut** : `return`, `break`, `continue`, `goto`
6. **Déclaration de variable** : `int x = 5;` — valide à n'importe quel endroit en C++
7. **Blocs try/catch** : gestion des exceptions (avancé)

**Portée (scope)** :
```cpp
{
    int x = 10;     // x existe seulement dans ce bloc
    cout << x;      // OK : 10
}
// cout << x;       // ERREUR : x n'existe plus (détruit à la fermeture du bloc)
```

**Différence Python vs C++ sur l'indentation** : en Python, l'indentation **définit** les blocs. En C++, l'indentation est **décorative** — ce sont les accolades `{}` qui définissent les blocs.

---

### 1.8 Mini-projet : BMD Regression Tree v0.1 et v1.0

**Contexte** : Le projet fil rouge du cours est un estimateur de la Densité Minérale Osseuse (BMD) basé sur un **arbre de décision** (modèle de Machine Learning). On part de la phase d'inférence : utiliser un modèle déjà entraîné.

**BMD v0.1 — test d'un cas codé en dur** :

```cpp
#include <iostream>
using namespace std;

// L'arbre de décision est codé directement dans la fonction estimate()
float estimate(float age, float weight_kg, float height_cm, float waiting_time) {
    if (weight_kg <= 65.5) {
        if (age <= 68.63) {
            if (weight_kg <= 52.5) {
                return 0.68;
            } else {
                if (height_cm <= 155.75) return 0.83;
                else                     return 0.75;
            }
        } else {
            if (waiting_time <= 19.5) return 0.64;
            else                      return 0.56;
        }
    }
    // ... (autres branches)
    return 0.0;
}

int main() {
    // Test avec un patient fixe
    float bmd = estimate(60, 70, 165, 30);
    cout << "Predicted BMD: " << bmd << endl;  // Devrait afficher 0.87
    return 0;
}
```

**BMD v1.0 — interface utilisateur interactive** :

```cpp
int main() {
    char choice;
    float age, weight_kg, height_cm, waiting_time;

    do {
        cout << "Enter patient details:\n";
        cout << "Age (years): ";      cin >> age;
        cout << "Weight (kg): ";      cin >> weight_kg;
        cout << "Height (cm): ";      cin >> height_cm;
        cout << "Waiting time (days): "; cin >> waiting_time;

        float bmd = estimate(age, weight_kg, height_cm, waiting_time);
        cout << "\n--> Predicted BMD: " << bmd << "\n\n";

        cout << "Estimate another patient? (y/n): ";
        cin >> choice;
    } while (choice == 'y' || choice == 'Y');  // do-while car on veut au moins une saisie

    return 0;
}
```

**⚠️ Limitation de v1.0** : L'arbre est **codé en dur**. Si on entraîne un nouveau modèle (arbre différent), il faut modifier le code source C++ et recompiler. Ce n'est pas scalable → sera résolu en v2.0.

---

##  Cours 2 : File I/O, Strings, Structs & Fonctions

### 2.1 File I/O — Lire et écrire des fichiers

**Définition** : Les classes `ifstream`, `ofstream` et `fstream` permettent de lire et écrire des fichiers en C++, de la même façon que `cin`/`cout` mais vers un fichier.

**Intuition** : Un **stream** (flux) est une abstraction d'un canal de communication. Tout flux fonctionne avec les mêmes opérateurs (`<<` pour écrire, `>>` pour lire). Que ce soit vers l'écran, le clavier ou un fichier, la syntaxe est identique — seul le nom du flux change.

**Les 3 classes de fichier** :

| Classe | Direction | Équivalent console |
|---|---|---|
| `ifstream` | Lecture seule | `cin` |
| `ofstream` | Écriture seule | `cout` |
| `fstream` | Lecture + Écriture | `cin` + `cout` |

**Exemple complet — Écriture dans un fichier** :
```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream myfile;           // Déclare le flux de sortie
    myfile.open("example.txt"); // Ouvre (ou crée) le fichier en mode écriture

    if (!myfile) {             // Toujours vérifier si l'ouverture a réussi
        cerr << "Erreur: impossible d'ouvrir le fichier\n";
        return 1;
    }

    myfile << "Writing this to a file.\n";  // Même syntaxe que cout
    myfile.close();  // INDISPENSABLE : vide le buffer et libère le fichier
    return 0;
}
```

**Exemple complet — Lecture ligne par ligne** :
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string line;
    ifstream myfile("example.txt");  // Ouvre directement dans le constructeur

    if (myfile.is_open()) {
        while (getline(myfile, line)) {    // Lit une ligne entière (y compris les espaces)
            cout << line << '\n';          // Affiche la ligne
        }
        myfile.close();
    } else {
        cout << "Unable to open file\n";
    }
    return 0;
}
```

**Modes d'ouverture** :
```cpp
// Combiner les modes avec | (OU logique)
fstream f("data.txt", ios::in | ios::out);  // Lecture ET écriture
ofstream f2("log.txt", ios::app);           // Mode append (ajout en fin de fichier)
ifstream f3("data.bin", ios::binary);       // Mode binaire (bytes bruts)
```

**Mode texte vs mode binaire** :

| | Mode texte | Mode binaire |
|---|---|---|
| Encodage | Caractères lisibles | Bytes bruts (comme en mémoire) |
| Taille de 1000000 | 7 bytes (`'1','0','0','0','0','0','0'`) | 4 bytes (représentation int sur 32 bits) |
| Conversion automatique | \n → \r\n (Windows) | Aucune |
| Usage | Fichiers texte, CSV, logs | Images, audio, sérialisation |

**⚠️ Piège classique** : Oublier `myfile.close()`. Si le programme plante avant la fermeture, le contenu du buffer ne sera jamais écrit sur le disque. Toujours fermer explicitement, ou utiliser un pattern RAII (le fichier se ferme automatiquement quand l'objet sort de portée).

---

### 2.2 Manipulateurs de stream

**Définition** : Les manipulateurs sont des objets spéciaux qu'on insère dans un flux `<<` pour modifier la façon dont les données sont formatées en sortie.

**Intuition** : Pense à un « mode d'affichage » : une fois activé, il reste actif pour les affichages suivants (sauf exceptions comme `setw`). Utile pour aligner des colonnes, afficher des floats avec une précision fixe, etc.

**Exemple complet** :
```cpp
#include <iostream>
#include <iomanip>   // Nécessaire pour setprecision, setw, setfill
using namespace std;

int main() {
    double pi = 3.14159265;

    // setprecision(n) : contrôle le nombre de chiffres significatifs
    cout << setprecision(3) << pi << endl;        // Affiche : 3.14  (3 chiffres totaux)

    // fixed + setprecision(n) : n chiffres APRÈS la virgule
    cout << fixed << setprecision(3) << pi << endl; // Affiche : 3.142

    // setw(n) : largeur du prochain champ (appliqué UNE FOIS seulement)
    // setfill(ch) : caractère de remplissage (par défaut : espace)
    cout << setw(8) << setfill('0') << 42 << endl; // Affiche : 00000042

    // Alignement left/right dans le champ setw
    cout << left  << setw(8) << setfill('.') << 100 << "end\n"; // Affiche : 100.....end
    cout << right << setw(8) << setfill('.') << 100 << "end\n"; // Affiche : .....100end

    // scientific : notation scientifique
    cout << scientific << setprecision(2) << 123.456 << endl;   // Affiche : 1.23e+02

    // Bases d'affichage pour les entiers
    cout << hex << 255 << endl;      // Affiche : ff (hexadécimal)
    cout << oct << 255 << endl;      // Affiche : 377 (octal)
    cout << dec << 255 << endl;      // Affiche : 255 (retour en décimal)
    return 0;
}
```

**Récapitulatif des manipulateurs** :

| Manipulateur | Effet | Persistant ? |
|---|---|---|
| `setprecision(n)` | Précision des floats | ✅ Oui |
| `fixed` | Notation décimale fixe | ✅ Oui |
| `scientific` | Notation scientifique | ✅ Oui |
| `setw(n)` | Largeur du prochain affichage | ❌ Non (une fois) |
| `setfill(ch)` | Caractère de remplissage | ✅ Oui |
| `left`/`right` | Alignement | ✅ Oui |
| `hex`/`oct`/`dec` | Base des entiers | ✅ Oui |
| `endl` | `\n` + flush buffer | — |
| `flush` | Flush buffer sans `\n` | — |

**⚠️ Piège classique** : `setw()` ne s'applique qu'à la **prochaine** valeur. Si tu veux aligner une colonne entière, il faut réappliquer `setw()` à chaque ligne.

---

### 2.3 Arrays

**Définition** : Un array est une collection d'éléments **du même type** stockés en mémoire de façon **contiguë**, accessibles via un index.

**Intuition** : Imagine une rangée de cases mémoire numérotées de 0 à N-1. Toutes les cases ont la même taille (celle du type). Pour accéder à la case `i`, C++ calcule son adresse en faisant `adresse_base + i × sizeof(type)`.

**Déclaration et initialisation** :
```cpp
float grades[5];                         // Déclaré mais NON initialisé (valeurs indéfinies)
int primes[] = {1, 2, 3, 5, 7};         // Initialisé — taille déduite automatiquement (5)
int primes[5] = {1, 2, 3, 5, 7};        // Équivalent explicite
int zeros[10] = {};                      // Tous les éléments initialisés à 0
```

**Accès et itération** :
```cpp
int primes[] = {1, 2, 3, 5, 7};

cout << primes[0] << "\n";   // Affiche : 1 (premier élément — index 0)
cout << primes[4] << "\n";   // Affiche : 7 (cinquième élément — index 4)

// Calculer la taille : idiome classique C++
int arrsize = sizeof(primes) / sizeof(primes[0]);
// sizeof(primes) = 5 × 4 = 20 bytes
// sizeof(primes[0]) = 4 bytes
// arrsize = 20 / 4 = 5

for (int i = 0; i < arrsize; i++) {
    cout << primes[i] << "\t";  // Affiche : 1  2  3  5  7
}
```

**⚠️ Piège classique — Out-of-Bounds** : C++ ne vérifie **jamais** si l'indice est dans les limites valides. Accéder à `primes[5]` (indice 5 sur un array de 5 éléments) est **indéfini** — soit plantage immédiat (segmentation fault), soit corruption silencieuse d'une variable voisine.

```cpp
int primes[5] = {1, 2, 3, 5, 7};
cout << primes[10];  // COMPORTEMENT INDÉFINI — peut afficher n'importe quoi, planter, etc.
```

---

### 2.4 C-Strings vs std::string

#### C-Strings (char[] avec `\0`)

**Définition** : Une C-string est un tableau de `char` terminé par le caractère nul `\0`. C'est la façon héritée du langage C de représenter des chaînes de caractères.

**Exemple** :
```cpp
char name[] = "Mae";        // Stocke : 'M', 'a', 'e', '\0' — 4 éléments !
char msg[10] = "Hi";        // Stocke : 'H', 'i', '\0', puis 7 zéros

cout << name;               // Affiche : Mae (s'arrête au premier '\0')
cout << strlen(name);       // Affiche : 3 (longueur sans le '\0')
```

**Danger** :
```cpp
char vowels[5] = {'a', 'e', 'i', 'o', 'u'};  // PAS de '\0' — ce n'est PAS une C-string !
cout << vowels;     // DANGEREUX : continue à lire en mémoire jusqu'à trouver un '\0' par hasard
strlen(vowels);     // DANGEREUX : valeur arbitraire ou crash
```

#### std::string (C++ moderne)

**Définition** : `std::string` est une classe de la bibliothèque standard C++ qui encapsule une séquence de caractères avec gestion automatique de la mémoire.

**Avantages sur les C-strings** :

| | C-string (`char[]`) | `std::string` |
|---|---|---|
| `\0` requis | Oui, manuellement | Non (géré intern.) |
| Longueur | `strlen()` (O(n)) | `.length()` (O(1)) |
| Concaténation | `strcat()` (risqué) | `s1 + s2` (sûr) |
| Comparaison | `strcmp()` | `==`, `<`, `>` |
| Redimensionnement | Impossible | Automatique |

```cpp
#include <string>
using namespace std;

string name = "Mae West";
cout << name.length();         // 8
cout << name[0];               // 'M'
string full = name + " !!!";   // Concaténation sûre
cout << name.find("West");     // 4 (position de "West")
cout << name.substr(0, 3);     // "Mae"

// Comparaisons lexicographiques sensibles à la casse
if (name == "Mae West") cout << "Même nom\n";    // true
if ("age" < "beauty")   cout << "age < beauty\n"; // true (ordre ASCII)
```

**⚠️ Piège classique** : Mélanger C-string et `std::string`. Les fonctions C (`strlen`, `strcpy`) ne fonctionnent pas avec `std::string`. Pour convertir : `name.c_str()` retourne un `const char*`.

---

### 2.5 Stringstreams — parser des strings

**Définition** : `<sstream>` fournit des flux en mémoire pour lire/écrire dans un objet `std::string` en utilisant les mêmes opérateurs `<<` et `>>` qu'avec `cin`/`cout`.

**Intuition** : Un stringstream te permet de « faire semblant » qu'une chaîne de texte est une entrée clavier (`cin`), ou de construire une string complexe comme si tu écrivais dans `cout`.

**Exemple complet — parsing d'une condition** :
```cpp
#include <sstream>
#include <string>
#include <iostream>
using namespace std;

int main() {
    // Cas d'usage : parser la condition "weight_kg <= 65.50" extraite d'un fichier
    string cond = "weight_kg <= 65.50";
    istringstream iss(cond);  // Créer un flux de lecture à partir de la string

    string feat, op;
    float threshold;
    iss >> feat >> op >> threshold;  // Extrait les tokens séparés par des espaces
    // feat = "weight_kg", op = "<=", threshold = 65.50

    cout << "Feature: " << feat << ", Op: " << op << ", Threshold: " << threshold << "\n";
    // Affiche : Feature: weight_kg, Op: <=, Threshold: 65.5

    // ostringstream : construire une string
    ostringstream outStr;
    double number = 2.5;
    outStr << "number = " << (number / 2.0);
    string result = outStr.str();  // Récupère la string construite
    cout << result << "\n";        // Affiche : number = 1.25

    return 0;
}
```

| Classe | Direction | Usage |
|---|---|---|
| `istringstream` | Lecture depuis string | Parser/découper une string |
| `ostringstream` | Écriture vers string | Construire une string formatée |
| `stringstream` | Lecture + Écriture | Les deux |

---

### 2.6 Structs

**Définition** : Un `struct` (structure) est un type de données composite qui regroupe plusieurs variables de types différents sous un même nom.

**Intuition** : Là où un array stocke N valeurs du **même type**, un struct stocke plusieurs valeurs de **types différents** mais qui décrivent la même entité (ex: les informations d'une voiture).

**Exemple complet** :
```cpp
struct Car {          // Définition d'un nouveau type de données
    string brand;     // Membre
    string model;     // Membre
    int year;         // Membre
};                    // Le ';' après la définition est OBLIGATOIRE

Car car1, car2;       // Déclare deux variables du type Car

// Accès aux membres via l'opérateur '.' (point)
car1.brand = "BMW";
car1.model = "X5";
car1.year  = 1999;

car2 = {"Ford", "Mustang", 1969};  // Initialisation directe

cout << car1.brand << " " << car1.model << " " << car1.year << "\n";
// Affiche : BMW X5 1999
```

**Cas d'usage dans le projet BMD — struct ParseResult** :

```cpp
// Problème : une fonction ne peut retourner qu'une seule valeur
// Solution : regrouper les données à retourner dans un struct
struct ParseResult {
    int is_leaf;    // 1 = feuille, 0 = noeud interne
    double value;   // Valeur estimée (si feuille)
    int next_node;  // ID du noeud suivant (si interne)
};

ParseResult parse_eval_line(char* line, ...) {
    struct ParseResult res = {0};
    // ... traitement ...
    if (left_id == -1 && right_id == -1) {
        res.is_leaf = 1;
        res.value = atof(cond_val);
    } else {
        res.is_leaf = 0;
        res.next_node = take_left ? left_id : right_id;
    }
    return res;  // Retourne le struct entier
}
```

**⚠️ Piège classique** : Oublier le `;` après la définition d'un struct. Le compilateur interprétera la ligne suivante comme une déclaration de variable du type struct — erreur cryptique garantie.

---

### 2.7 Conversion de types (Casts)

**Définition** : La conversion de type (cast) transforme une valeur d'un type en un autre.

**Intuition** : Les conversions implicites (automatiques) sont pratiques mais dangereuses (perte de données possible). Les conversions explicites expriment clairement l'intention du programmeur.

```cpp
// Conversion implicite (automatique) — C++ le fait seul
double x = 5;       // int 5 → double 5.0 (pas de perte)
int n = 3.7;        // double 3.7 → int 3 (TRONCATURE, perte de .7, pas d'arrondi !)

// Cast style C — éviter, dangereux car contourne les vérifications
int n1 = (int)3.7;       // Style C
int n2 = int(3.7);       // Style C (notation fonctionnelle)

// static_cast — à préférer en C++ moderne
int n3 = static_cast<int>(3.7);  // RECOMMANDÉ : explicite, lisible, vérifié
```

**Exemple important — division entière** :
```cpp
int a = 5, b = 2;
cout << a / b;                          // Affiche : 2 (division entière !)
cout << (double)a / b;                  // Affiche : 2.5 (conversion d'un des opérandes)
cout << static_cast<double>(a) / b;    // Affiche : 2.5 (recommandé)
```

---

### 2.8 Fonctions

**Définition** : Une fonction est un bloc de code nommé et réutilisable qui accomplit une tâche spécifique. Elle peut recevoir des paramètres et retourner une valeur.

**Anatomy d'une fonction C++** :
```cpp
// Prototype (déclaration) : interf que le compilateur voit avant d'utiliser la fonction
int addition(int a, int b);   // Suffisant pour que le compilateur valide les appels

// Corps (définition) : l'implémentation réelle
int addition(int a, int b) {
    int r = a + b;
    return r;
}

int main() {
    int z = addition(5, 3);  // Appel de la fonction
    cout << "The result is " << z;  // Affiche : The result is 8
}
```

**Types de retour** :

| Type de retour | Signification | Exemple |
|---|---|---|
| `int`, `double`, etc. | La fonction retourne une valeur | `int sum(int a, int b)` |
| `void` | La fonction ne retourne rien | `void print(string s)` |
| `bool` | La fonction retourne vrai/faux | `bool isEven(int n)` |

**Passage par valeur vs par référence** :
```cpp
// Par valeur : la fonction reçoit une COPIE (modifications n'affectent pas l'original)
void doubleIt(int n) {
    n = n * 2;    // Modifie uniquement la copie locale
}

// Par référence : la fonction reçoit l'ORIGINAL (modifications affectent l'original)
void doubleItRef(int &n) {
    n = n * 2;    // Modifie la variable originale !
}

int x = 5;
doubleIt(x);       // x vaut encore 5
doubleItRef(x);    // x vaut maintenant 10
```

---

### 2.9 BMD Regression Tree v2.0

**Problème de v1.0** : L'arbre était codé en dur. Changer le modèle = modifier + recompiler tout le programme.

**Solution v2.0** : Lire dynamiquement la structure de l'arbre depuis un **fichier texte** au moment de l'inférence.

**Format du fichier** (`bmd_tree_transitions.txt`) :
```
1,2,3,weight_kg <= 65.5      # ID, enfant_gauche, enfant_droite, condition
2,4,5,age <= 68.63
4,-1,-1,0.68                 # -1,-1 = feuille, valeur prédite = 0.68
```

**Algorithme de lecture** :
```
Initialiser nœudCourant = 1 (racine)
Boucle :
  Lire le fichier depuis le début (seekg(0))
  Chercher la ligne dont l'ID correspond à nœudCourant
  Si nœud terminal (gauche == droite == -1) :
    Retourner la valeur de la feuille
  Sinon :
    Évaluer la condition booléenne
    Si vrai → descendre à gauche ; Si faux → descendre à droite
```

**Opérateur ternaire** (concept introduit ici) :
```cpp
// Syntaxe : condition ? valeur_si_vrai : valeur_si_faux
int next = take_left ? left_id : right_id;
// Équivalent à :
// if (take_left) next = left_id;
// else           next = right_id;
```

**⚠️ Limitation de v2.0** : On relit le _fichier entier_ à chaque nœud visité → lent. Solution → v3.0 (charger dans un array mémoire).
'''

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Part 1 (Cours 1 & 2) written — {len(content)} chars")
