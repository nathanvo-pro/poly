# 📖 Synthèse Complète — Informatique OOP (INFOH2001)

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
#Compiler le fichier hello.cpp et créer l'exécutable 'hello'
$ g++ hello.cpp -o hello

#Lancer l'exécutable
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
## Annexes : Python vs C++

**Python — typage dynamique**
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

---

##  Cours 3 : Hiérarchie Mémoire, Arrays & Introduction aux Classes

### 3.1 Hiérarchie de la mémoire

**Définition** : La hiérarchie mémoire est l'ensemble des niveaux de stockage d'un système informatique, classés par vitesse d'accès et coût.

**Intuition** : Plus la mémoire est rapide, plus elle est chère et petite. Le processeur cherche d'abord dans les registres, puis le cache, puis la RAM, et enfin le disque. Un programme rapide maximise les accès aux niveaux supérieurs de la hiérarchie.

**Tableau comparatif** :

| Niveau | Taille typique | Vitesse | Coût |
|---|---|---|---|
| Registres CPU | ~0.5 KB | 0.1–0.3 ns | Très élevé (intégré CPU) |
| Cache L1 | 32–64 KB | 0.3–1.2 ns | Très élevé (intégré CPU) |
| Cache L2 | 0.5–2 MB | 2–5 ns | Élevé |
| Cache L3 | 16–128 MB | 10–20 ns | Moyen |
| RAM (DRAM) | 16–64 GB | 40–60 ns | ~15 $/GB |
| SSD NVMe | 0.5–4 TB | 10–100 µs | ~0.08 $/GB |
| HDD | 1–20 TB | 5–20 ms | ~0.02 $/GB |

**Conséquence pour la programmation** : Les accès au disque sont 100 000× plus lents qu'à la RAM. C'est pour cela que la v3.0 du projet BMD charge l'arbre entier en mémoire RAM plutôt que de relire le fichier à chaque nœud.

---

### 3.2 Variables Array et arithmétique des pointeurs

**Définition** : Le nom d'un array est une **adresse mémoire constante** pointant vers son premier élément. L'indexation `arr[i]` est strictement équivalente à l'arithmétique de pointeurs `*(arr + i)`.

**Intuition** : Tous les éléments d'un array sont contigus en mémoire. Accéder à l'élément `i` revient à partir de l'adresse du premier élément et avancer de `i × sizeof(type)` bytes.

**Exemple complet avec adresses mémoire** :
```cpp
int primes[] = {1, 2, 3, 5, 7};    // sizeof(int) = 4 bytes

// Affichage des adresses mémoire
for (int i = 0; i < 5; i++) {
    cout << "Adresse : " << (primes + i)
         << " Valeur : " << primes[i]
         << "\n";
}
/* Résultat (adresses fictives) :
   Adresse : 0x7ffd8000  Valeur : 1
   Adresse : 0x7ffd8004  Valeur : 2   ← +4 bytes (1 int)
   Adresse : 0x7ffd8008  Valeur : 3   ← +8 bytes
   Adresse : 0x7ffd800c  Valeur : 5   ← +12 bytes
   Adresse : 0x7ffd8010  Valeur : 7   ← +16 bytes
*/

// Équivalences fondamentales :
cout << primes[2];          // 3
cout << *(primes + 2);      // 3  — strictement équivalent
cout << primes + 2;         // Adresse du 3ème élément
cout << &primes[2];         // Même adresse, autre notation
```

**Opérations valides sur les pointeurs** :
```cpp
int* p = primes;  // p pointe vers primes[0]
p + 3;            // Adresse de primes[3]  (p avance de 3×4 = 12 bytes)
p - 1;            // Adresse précédente
p++;              // p pointe maintenant vers primes[1]
*(p - 1);         // Valeur de primes[0]
```

**Calculer la taille d'un array — idiome classique** :
```cpp
int arrsize = sizeof(primes) / sizeof(primes[0]);
// = (5 × 4 bytes) / (4 bytes) = 5
```

**⚠️ Piège classique — Out-of-bounds silencieux** :
```cpp
int arr[5] = {1, 2, 3, 4, 5};
arr[5] = 99;   // COMPORTEMENT INDÉFINI !
// Deux cas possibles :
// 1. Segmentation fault (crash immédiat)
// 2. Corruption silencieuse (écrase une autre variable en mémoire)
//    Le bug se manifeste bien plus tard, dans un endroit du code totalement différent.
```

---

### 3.3 BMD Regression Tree v3.0 — Chargement dans un array

**Amélioration v2.0 → v3.0** : Au lieu de relire le fichier entier pour chaque nœud, on charge l'arbre **une seule fois** dans un array en mémoire (accès O(1)).

**Stratégie** : Stocker chaque nœud à l'**indice correspondant à son ID** dans l'array.

```cpp
const int MAX_NODES = 32;
Node tree[MAX_NODES];    // Array de 32 nœuds (type Node défini plus loin)

// Chargement (une seule lecture du fichier)
bool read_tree(char* filename) {
    ifstream fp(filename);
    while (fp.getline(line, sizeof(line))) {
        sscanf(line, "%d,%d,%d,%127[^\n]", &node_id, &left_id, &right_id, cond_val);
        tree[node_id].set_children(left_id, right_id);  // Stocke à l'indice node_id
        // ...
    }
    return true;
}

// Inférence (accès direct, pas de recherche dans le fichier)
float estimate(float features[FEATURE_COUNT]) {
    int idx = 1;  // Commence à la racine
    while (idx < MAX_NODES) {
        if (tree[idx].test_leaf()) return tree[idx].get_value();  // O(1) !
        bool go_left = tree[idx].eval_condition(features);
        idx = go_left ? tree[idx].get_left() : tree[idx].get_right();
    }
    return 0.0;
}
```

---

### 3.4 Introduction aux Classes

**Définition** : Une **classe** est un type de données défini par le programmeur qui regroupe des données (**attributs**) et des fonctions qui les manipulent (**méthodes**), formant une entité cohérente.

**Intuition** : Un `struct` regroupe des données. Une classe fait la même chose mais lui ajoute des **comportements** (méthodes) et un **contrôle d'accès** (public/private). C'est le passage de la programmation procédurale à la Programmation Orientée Objet (POO).

**Programmation procédurale vs POO** :

| Approche | Procédurale | Orientée Objet |
|---|---|---|
| Centré sur | Les fonctions à exécuter | Les entités du domaine |
| Organisation | Variables + fonctions séparées | Données + comportements réunis = objet |
| Exemple | `longueur`, `largeur` + `calcul_surface()` | `Box box1;  box1.surface();` |
| Maintenance | Difficile sur gros projets | Plus lisible et évolutif |

**Syntaxe de base** :
```cpp
class Square {
private:              // Accessible UNIQUEMENT depuis l'intérieur de la classe
    float side;       // Attribut (membre de données)

public:               // Accessible depuis n'importe où
    void setSide(float s) { side = s; }   // Setter (mutateur)
    float getSide()        { return side; } // Getter (accesseur)
};

int main() {
    Square x;            // Création d'un objet ('instance') de la classe Square
    // x.side = 5;      // ERREUR DE COMPILATION : 'side' est privé
    x.setSide(5);        // OK : passe par l'interface publique
    cout << x.getSide(); // Affiche : 5
}
```

---

### 3.5 Encapsulation et Spécificateurs d'accès

**Définition** : L'**encapsulation** consiste à regrouper données et comportements au sein d'une classe, et à contrôler qui peut accéder à quoi via des spécificateurs d'accès.

**Les 3 spécificateurs** :

| Spécificateur | Accessible de | Usage typique |
|---|---|---|
| `public` | Partout (hors de la classe) | Interface externe, méthodes utilisateurs |
| `private` | Seulement au sein de la classe | Données internes, implémentation |
| `protected` | Classe + classes dérivées | Héritage (avancé) |

**Pourquoi `private` pour les données ?**

1. **Intégrité** : un setter peut valider l'entrée avant de modifier l'attribut :
```cpp
void setSide(float s) {
    if (s <= 0) {
        cerr << "Erreur : côté négatif !\n";
        return;
    }
    side = s;  // Modification validée
}
```

2. **Indépendance de l'implémentation** : changer la représentation interne (ex: stocker `side*side` au lieu de `side`) n'affecte pas le code utilisateur, car ce dernier ne dépend que de l'interface publique.

3. **Lisibilité** : on programme en termes d'**objets** du domaine métier, pas de bits internes.

**⚠️ Piège classique** : Déclarer tous les membres en `public` "pour simplifier". C'est le meilleur moyen de créer des objets dans des états incohérents (ex: `shape.side = -5`).

---

### 3.6 Séparation Interface / Implémentation (.h et .cpp)

**Définition** : En C++, on sépare généralement la **déclaration** de la classe (le `.h`, ce que l'utilisateur voit) de son **implémentation** (le `.cpp`, comment c'est fait).

**Intuition** : Comme un manuel d'utilisation (interface publique) vs les plans d'ingénierie internes (implémentation). L'utilisateur a seulement besoin du manuel.

**Exemple — classe Square** :

```cpp
// ===== square.h (interface — ce que l'utilisateur voit) =====
class Square {
private:
    float side;
public:
    void setSide(float s);      // Prototype seulement
    float getSide();            // Prototype seulement
    bool intersects(Square other);  // Prototype seulement
};
```

```cpp
// ===== square.cpp (implémentation — comment c'est fait) =====
#include "square.h"

void Square::setSide(float s) { side = s; }   // Square:: = opérateur de résolution de portée
float Square::getSide()       { return side; } // Lie la définition à la classe Square

bool Square::intersects(Square other) {
    // ... Logique complexe d'intersection ici ...
}
```

**Avantages** :
- **Compiler séparément** : changer `square.cpp` → recompiler seulement `square.cpp`, pas le reste
- **Distribuer une librairie** : donner uniquement `square.h` + `square.o` (compilé) → l'algorithme reste secret
- **Encapsulation renforcée** : l'utilisateur ne voit que le `.h`, jamais l'implémentation

**Méthodes inline** : toute méthode définie **dans** le bloc `{}` de la classe (dans le `.h`) est implicitement `inline`. Le compilateur copie directement son code à l'endroit de l'appel (économise un appel de fonction).

---

### 3.7 Constructeurs

**Définition** : Un **constructeur** est une méthode spéciale appelée **automatiquement** à la création d'un objet. Il porte le même nom que la classe et n'a **aucun type de retour** (même pas `void`).

**Intuition** : Sans constructeur, les attributs d'un objet contiennent des valeurs aléatoires (« garbage »). Le constructeur garantit un état initial propre et valide.

**Exemple concret — Constructeur de Node** :
```cpp
// node.h — déclaration
class Node {
private:
    bool is_leaf;
    float value;
    int left_id, right_id;
public:
    Node();  // Constructeur par défaut (sans paramètre)
    // ...
};

// node.cpp — définition avec liste d'initialisation
Node::Node()
    : is_leaf(false), value(0.0), left_id(-1), right_id(-1)
//  ↑ Liste d'initialisation : initialise les membres AVANT le corps du constructeur
{}  // Corps vide — tout est déjà initialisé
```

**Liste d'initialisation vs affectation dans le corps** :

| | Affectation dans le corps | Liste d'initialisation |
|---|---|---|
| Syntaxe | `Node::Node() { is_leaf = false; }` | `Node::Node() : is_leaf(false) {}` |
| Mécanisme | Construction par défaut → puis copie | Construction directe avec valeur |
| Performance | Moins efficace (2 opérations) | Plus efficace (1 opération) |
| Nécessaire pour | Rien de particulier | Membres `const` et références |

**Obligation du constructeur sans paramètre dans les arrays** :
```cpp
Node tree[MAX_NODES];  // Chaque case appelle le constructeur par défaut Node()
                       // → OBLIGATOIRE d'avoir un constructeur sans paramètre
```

**Plusieurs constructeurs (surcharge)** :
```cpp
class Node {
public:
    Node();                            // Constructeur par défaut
    Node(const char* cond, bool leaf); // Constructeur avec paramètres
};

Node n1;                       // Appelle Node()
Node n2("weight_kg <= 65", false);  // Appelle le constructeur paramétré
```

**⚠️ Piège classique** : Dès qu'on définit **un seul** constructeur avec paramètres, le constructeur par défaut (sans paramètre) **disparaît** automatiquement. Si on veut garder les deux, il faut les déclarer tous les deux explicitement.

---

### 3.8 Destructeur

**Définition** : Le **destructeur** est une méthode spéciale appelée automatiquement juste avant qu'un objet soit détruit (fin de portée ou `delete`). Syntaxe : `~NomClasse()`.

**Intuition** : Le constructeur réserve des ressources. Le destructeur les libère. C'est lui qui évite les fuites mémoire pour les objets qui allouent dynamiquement.

```cpp
class Node {
public:
    ~Node() {
        if (left  != nullptr) delete left;   // Libère le sous-arbre gauche
        if (right != nullptr) delete right;  // Libère le sous-arbre droit
        // Les destructeurs de left et right sont appelés récursivement !
    }
};
```

---

### 3.9 Enums (Types énumérés)

**Définition** : Un type énuméré (`enum`) définit un type dont les valeurs possibles sont un ensemble de **constantes entières nommées**.

**Intuition** : Au lieu de mémoriser que `0 = lundi` et `6 = dimanche`, on définit des noms expressifs. Le code devient lisible et le compilateur vérifie qu'on n'utilise pas des valeurs invalides.

**Exemple complet** :
```cpp
enum Days { Mon, Tue, Wed, Thu, Fri, Sat, Sun };
// Par défaut : Mon=0, Tue=1, Wed=2, ...

enum Fruit { apple = 15, grape, orange };
// apple = 15, grape = 16 (15+1), orange = 17 (16+1)

Days workDay = Wed;          // CORRECT — pas de guillemets
if (workDay == Wed)
    cout << "C'est mercredi\n";

Fruit snack = orange;        // snack a la valeur 17
cout << snack;               // Affiche : 17  (cout affiche la valeur entière)
// cout >> snack;            // ERREUR : cin/cout ne savent pas lire un enum directement
```

**Enums dans le projet BMD** :
```cpp
enum Feature {
    WEIGHT_KG = 0,   // Correspond à l'index dans le tableau features[]
    AGE,
    HEIGHT_CM,
    WAITING_TIME,
    FEATURE_COUNT = 4  // Utile pour déclarer : float features[FEATURE_COUNT]
};

enum Operator { OP_LE, OP_LT, OP_EQ, OP_GE, OP_GT };
```

**⚠️ Piège classique** : `cout` n'affiche pas le nom de l'énumérateur mais sa **valeur entière**. Il faut écrire soi-même une fonction de conversion si on veut « Wed » au lieu de `2`.

---

### 3.10 Opérateurs prefix/postfix (++ et --)

**Définition** : Les opérateurs `++` et `--` incrémentent/décrémentent une variable de 1. Ils existent en deux formes : **préfixe** (agit puis retourne la nouvelle valeur) et **postfixe** (retourne l'ancienne valeur puis agit).

```cpp
int x = 1, y = 1;

// Préfixe (++avant) : incrémente D'ABORD, retourne la NOUVELLE valeur
x = ++y;   // y devient 2, puis x reçoit 2
cout << x << " " << y;   // Affiche : 2 2

// Postfixe (après++) : retourne l'ANCIENNE valeur, puis incrémente
x = y++;   // x reçoit 2 (ancienne valeur), puis y devient 3
cout << x << " " << y;   // Affiche : 2 3
```

**⚠️ Piège classique** :
```cpp
int arr[5] = {0, 1, 2, 3, 4};
int i = 0;
cout << arr[i++];  // Affiche arr[0] = 0, PUIS i devient 1
cout << arr[++i];  // i devient 2, PUIS affiche arr[2] = 2
```

---

##  Cours 4 : Systèmes de Numération, Pointeurs, Allocation Dynamique & Structures Récursives

### 4.1 Systèmes de numération

**Définition** : Un système de numération est une façon d'écrire des nombres en utilisant des chiffres et une base. La base détermine combien de chiffres différents on utilise.

**Intuition** : Un ordinateur ne stocke que des 0 et des 1 (bits). Mais lire 111110100111000101101001 est difficile. Les notations hexadécimale et octale sont des abréviations pratiques du binaire.

#### Binaire (base 2)

**Conversion décimal → binaire (divisions successives par 2)** :

```
Exemple : convertir 42 en binaire
42 ÷ 2 = 21  reste 0   ← bit le moins significatif (LSB, bit 0)
21 ÷ 2 = 10  reste 1
10 ÷ 2 = 5   reste 0
 5 ÷ 2 = 2   reste 1
 2 ÷ 2 = 1   reste 0
 1 ÷ 2 = 0   reste 1   ← bit le plus significatif (MSB)

Lire de bas en haut : 42₁₀ = 101010₂
```

**Vérification** : $1×2^5 + 0×2^4 + 1×2^3 + 0×2^2 + 1×2^1 + 0×2^0 = 32 + 8 + 2 = 42$ ✓

**Conversion binaire → décimal** :
```
1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰
      = 8    + 4    + 0    + 1
      = 13₁₀
```

#### Hexadécimal (base 16)

**Chiffres** : 0-9 puis A(10), B(11), C(12), D(13), E(14), F(15)

**Conversion décimal → hexadécimal (divisions successives par 16)** :
```
Exemple : convertir 255 en hexadécimal
255 ÷ 16 = 15  reste 15 → F
 15 ÷ 16 =  0  reste 15 → F

Lire de bas en haut : 255₁₀ = FF₁₆
```

**Astuce binaire ↔ hex** : 1 chiffre hex = 4 bits (un « nibble »).
```
1111 1111₂  = F F₁₆ = 255₁₀
1010 0010₂  = A 2₁₆ = 162₁₀
```

**Code C++ — conversion décimal → binaire** :
```cpp
#include <iostream>
#include <string>
using namespace std;

string decimalToBinary(int n) {
    if (n == 0) return "0";
    string binary = "";
    while (n > 0) {
        binary = ((n % 2) ? '1' : '0') + binary;  // Préfixe le bit (évite un reverse)
        n /= 2;
    }
    return binary;
}

int main() {
    cout << 42 << " en binaire = " << decimalToBinary(42) << endl;
    // Affiche : 42 en binaire = 101010
}
```

**Code C++ — conversion décimal → hexadécimal** :
```cpp
string decimalToHex(int n) {
    if (n == 0) return "0";
    string hex = "";
    while (n > 0) {
        int rem = n % 16;
        char digit;
        if (rem < 10)
            digit = '0' + rem;           // Chiffres '0' à '9'
        else
            digit = 'A' + (rem - 10);    // Lettres 'A' à 'F' (via table ASCII)
        hex = digit + hex;
        n /= 16;
    }
    return hex;
}
// decimalToHex(255) → "FF"
// decimalToHex(42)  → "2A"
// decimalToHex(10)  → "A"
```

**⚠️ Piège classique** : Confondre `10` en décimal (dix) et `10` en binaire (deux). Toujours préciser la base : `10₁₀` vs `10₂`. En C++, les littéraux binaires s'écrivent `0b1010`, hexadécimaux `0xFF`, octaux `0377`.

---

### 4.2 Opérateur d'adresse `&` et variables pointeur

**Définition** : 
- L'opérateur `&` (adresse) retourne l'adresse mémoire d'une variable.
- Un **pointeur** est une variable dont la valeur est une adresse mémoire.

**Intuition** : Toute variable est stockée à une adresse précise en mémoire (comme l'adresse d'une maison dans une rue). Un pointeur, c'est cette adresse. Au lieu de stocker directement une valeur, il stocke l'emplacement où se trouve cette valeur.

**Exemple concret** :
```cpp
int num = -23;
cout << num   << "\n";   // Affiche : -23          (la valeur)
cout << &num  << "\n";   // Affiche : 0x7fffffffq8e4 (l'adresse mémoire)

int* ptr = &num;         // ptr est un pointeur vers int, et contient l'adresse de num
cout << ptr   << "\n";   // Affiche : 0x7fffffffq8e4  (l'adresse — même valeur que &num)
cout << *ptr  << "\n";   // Affiche : -23             (déréférencement : accède à la valeur pointée)
cout << &ptr  << "\n";   // Affiche : 0x7fffffffq8e0  (l'adresse du pointeur lui-même)
```

**Schéma mémoire** :
```
Variable num :
  Adresse : 0x7ffd8e4   |  Valeur : -23

Variable ptr :
  Adresse : 0x7ffd8e0   |  Valeur : 0x7ffd8e4   (= adresse de num)
              ↑ adresse du pointeur    ↑ valeur du pointeur (=addresse de num)
```

**Syntaxe de déclaration** : les espaces sont insignifiants, mais l'`*` s'applique variable par variable :
```cpp
int* ptr;             // 'ptr' est un pointeur vers int
int *ptr;             // Identique — style souvent préféré car *ptr est l'accès
int * ptr;            // Identique

int *ptr1, x, *ptr2;  // ptr1 et ptr2 sont des pointeurs, x est un int ordinaire !
                      // Piège : 'int* ptr1, ptr2' → ptr2 est un int, PAS un pointeur
```

**`nullptr`** : L'adresse spéciale « ne pointe vers rien ». Toujours initialiser les pointeurs.
```cpp
int* ptr = nullptr;  // Pointeur nul — déréférencer causerait un crash immédiat (plutôt que comportement silencieux)
if (ptr != nullptr) {
    cout << *ptr;    // Sûr : on vérifie avant de déréférencer
}
```

**⚠️ Piège classique — `*` a plusieurs significations** :
```cpp
int* ptr;         // '*' dans une déclaration : déclare un pointeur
cout << *ptr;     // '*' dans une expression : déréférencement (accède à la valeur)
int a = 3 * 4;    // '*' en expression arithmétique : multiplication
```

---

### 4.3 Arrays et pointeurs — relation fondamentale

**Le nom d'un array EST une adresse** (pointeur constant vers son premier élément) :
```cpp
int val[] = {4, 7, 11};

// Ces 4 lignes affichent toutes la même chose :
cout << val;        // Adresse du premier élément = 0x7ffd...
cout << &val[0];    // Idem
cout << val + 0;    // Idem

// val[i] est STRICTEMENT ÉQUIVALENT à *(val + i) :
cout << val[0];     // 4
cout << *val;       // 4  — identique

cout << val[1];     // 7
cout << *(val + 1); // 7  — identique : avance d'un int (4 bytes)

cout << val[2];     // 11
cout << *(val + 2); // 11 — identique : avance de deux ints (8 bytes)
```

**Différence array vs pointeur modifiable** :
```cpp
int tab[5] = {1, 2, 3, 4, 5};
int* p = tab;       // p peut être réaffecté (p pointe vers tab[0])

p++;                // OK : p avance vers tab[1]
// tab++;           // ERREUR : tab est une adresse CONSTANTE, ne peut pas être modifiée
```

**⚠️ Piège classique — priorité des opérateurs** :
```cpp
int* p = val;
*(p + 1)    // CORRECT : avance le pointeur d'un, puis déréférence → val[1] = 7
*p + 1      // INCORRECT (si c'est ce qu'on voulait) : déréférence d'abord → *p = 4, puis + 1 = 5
```

---

### 4.4 Allocation dynamique de mémoire — `new` et `delete`

**Définition** : Les opérateurs `new` et `delete` permettent d'**allouer et libérer manuellement** de la mémoire sur le **heap** (tas) pendant l'exécution.

**Intuition** : Quand tu déclares `int x;`, la mémoire est réservée automatiquement dans le stack et libérée à la fin de la fonction. Avec `new`, tu réserves de la mémoire dans le heap à l'exécution (taille décidée à runtime), et tu es **entièrement responsable** de la libérer avec `delete`.

#### Allocation d'un objet unique

```cpp
float* number;                  // Déclare un pointeur (ne pointe encore nulle part)
number = new float(-6);         // Alloue un float sur le HEAP, initialisé à -6
                                // Retourne l'adresse du bloc alloué

cout << *number << "\n";        // Affiche : -6   (déréférencement)
*number = 3.14;                 // Modifie la valeur via le pointeur

delete number;                  // Libère le bloc mémoire (OBLIGATOIRE)
number = nullptr;               // Bonne pratique : réinitialiser pour éviter le 'dangling pointer'
```

#### Allocation d'un array dynamique

```cpp
int n;
cout << "Combien d'éléments ? ";
cin >> n;                            // n connu SEULEMENT À L'EXÉCUTION

double* arr = new double[n];         // Alloue n doubles contigus sur le heap
                                     // La notation [] est OBLIGATOIRE pour un array

for (int i = 0; i < n; i++) {
    arr[i] = i * 2.5;               // Accès identique à un array statique
}

delete[] arr;                        // OBLIGATOIRE — les [] indiquent que c'est un array
arr = nullptr;                       // Bonne pratique

// PIÈGE FATAL :
// delete arr;    // Si on oublie les [] → comportement indéfini (libère peut-être 1 seul élément)
```

#### Fuites mémoire (Memory leaks)

```cpp
void fuite() {
    double* p = new double[1000];  // Alloue 8000 bytes
    // ... traitement ...
    // OUBLI de delete[] → la mémoire reste allouée même après la fin de la fonction !
}

// Si fuite() est appelée 1 000 000 fois → 8 GB gaspillés progressivement → crash
```

**Règle de base** : pour chaque `new`, il doit exister exactement un `delete`. Pour chaque `new[]`, exactement un `delete[]`.

**⚠️ Piège classique — Dangling pointer** :
```cpp
int* p = new int(42);
delete p;          // La mémoire est libérée
cout << *p;        // DANGEREUX : p pointe vers de la mémoire désallouée (comportement indéfini)
p = nullptr;       // Bonne pratique : rend le pointeur invalide clairement
// cout << *p;     // Maintenant : crash net et prévisible (plutôt que comportement silencieux)
```

---

### 4.5 Structure de la mémoire : Stack vs Heap

**Définition** : La mémoire d'un programme est divisée en plusieurs régions. Les deux plus importantes pour le programmeur sont le **stack** (pile) et le **heap** (tas).

**Intuition** : Le stack est comme une pile d'assiettes — on ne peut ajouter/retirer qu'au sommet, et c'est automatique et très rapide. Le heap est comme un entrepôt libre — tu peux réserver n'importe quel bloc et le libérer quand tu veux, mais c'est à toi de gérer.

| Région | Contenu | Gestion | Vitesse | Taille |
|---|---|---|---|---|
| **Texte (code)** | Instructions machine (.exe) | — | — | Fixe |
| **Globales/statiques** | Variables `global`, `static` | Automatique (programme entier) | Rapide | Limité |
| **Stack** | Variables locales, paramètres | Automatique (LIFO) | Très rapide | ~1-8 MB |
| **Heap** | `new`/`delete` | Manuel (programmeur) | Plus lent | Limité uniquement par la RAM |

**Schéma** :
```
Adresses hautes
   ┌─────────────┐
   │   Stack     │  ← Grandit vers le bas à chaque appel de fonction
   │   (Pile)    │    Variables locales, paramètres
   ├─────────────┤
   │     ↕       │  ← Espace libre entre les deux
   ├─────────────┤
   │   Heap      │  ← Grandit vers le haut avec new
   │   (Tas)     │    Allocation dynamique
   ├─────────────┤
   │  Globales   │  Variables globales et statiques
   ├─────────────┤
   │   Texte     │  Instructions machine (code compilé)
   └─────────────┘
Adresses basses
```

**Exemple illustratif** :
```cpp
int g = 10;  // Variable GLOBALE — stockée dans la section globales, dure toute la durée du programme

void foo() {
    int x = 5;               // Variable LOCALE — stockée sur le STACK, détruite à la fin de foo()
    double* p = new double;  // p est sur le Stack, mais *p est sur le HEAP
    *p = 3.14;
    // Si on oublie delete p → fuite mémoire (le heap ne se libère pas tout seul)
    delete p;                // Libération explicite du bloc heap
}                            // x est détruit automatiquement ici (stack)
```

---

### 4.6 Pointeur vers une classe — Opérateur `->`

**Définition** : Lorsqu'un pointeur pointe vers un objet, on ne peut pas utiliser l'opérateur `.` directement. On utilise l'opérateur `->` (flèche), qui combine déréférencement et accès.

**Intuition** : `->` est un raccourci syntaxique pour `(*ptr).membre`. Il "suit le pointeur" puis accède au membre.

```cpp
class Box {
public:
    double length;
    double volume() { return length * length * length; }
};

int main() {
    Box  box;               // Objet normal (sur le stack)
    box.length = 5.0;       // Accès direct avec '.'
    cout << box.volume();   // Accès direct avec '.'

    Box* pbox = new Box();  // Pointeur vers un objet (sur le heap)
    pbox->length = 5.0;     // Accès via pointeur avec '->'     ← SYNTAXE POINTEUR
    cout << pbox->volume(); // Accès via pointeur avec '->'

    // Équivalent (mais plus verbeux et moins lisible) :
    (*pbox).length = 5.0;    // *(déréférence) puis . (accès)

    delete pbox;             // Ne pas oublier !
    return 0;
}
```

**⚠️ Piège classique** : Appeler `pbox.volume()` au lieu de `pbox->volume()`. Le compilateur donnera une erreur claire ("base operand of `->` has non-pointer type"), mais c'est une confusion fréquente.

---

### 4.7 Structures de données récursives (Arbres)

**Définition** : Une structure de données récursive est un type dont les instances peuvent contenir des **pointeurs vers d'autres instances du même type**.

**Intuition** : Un arbre est naturellement défini récursivement : un arbre est soit vide, soit un nœud contenant un sous-arbre gauche et un sous-arbre droit. Pour modéliser cela en C++, on utilise des pointeurs.

**Pourquoi on NE PEUT PAS écrire `Node left; Node right;` directement** :
```cpp
class Node {
    Node left;   // IMPOSSIBLE : un Node contiendrait un Node, qui contiendrait un Node...
    Node right;  // → taille infinie, le compilateur refuse
};
```

**Solution — pointeurs pour briser la récursion** :
```cpp
class Node {
private:
    float value;       // Valeur de la feuille
    float threshold;   // Seuil de comparaison (nœud interne)
    Node* left;        // Pointeur vers enfant gauche (taille fixe : 8 bytes sur 64-bit)
    Node* right;       // Pointeur vers enfant droit  (8 bytes)
    Feature feature;   // Quelle caractéristique tester
    Operator op;       // Quel opérateur de comparaison

public:
    bool test_leaf() { return (left == nullptr && right == nullptr); }
    // ...

    // Constructeur par défaut — nœud "vide"
    Node() : left(nullptr), right(nullptr), value(0), feature(WEIGHT_KG) {}

    // Constructeur paramétré
    Node(const char* cond_val, const bool is_leaf)
        : left(nullptr), right(nullptr), feature(WEIGHT_KG) {
        parse_condition(cond_val, is_leaf);
    }

    // Destructeur RÉCURSIF — libère tout le sous-arbre
    ~Node() {
        if (left  != nullptr) delete left;   // Déclenche ~Node() sur le fils gauche
        if (right != nullptr) delete right;  // Déclenche ~Node() sur le fils droit
    }
};
```

**Schéma d'un arbre BMD en mémoire** :
```
racine (Node*)
    ↓
  Node (weight_kg <= 65.5)
  ├── left (Node*) → Node (age <= 68.63)
  │   ├── left (Node*) → Node [feuille, value=0.68]
  │   └── right (Node*) → Node [...] 
  └── right (Node*) → Node [feuille, value=0.56]
```

**Traversée et inférence** :
```cpp
float estimate(Node* root, float features[FEATURE_COUNT]) {
    Node* cur = root;
    while (cur != nullptr) {
        float res = cur->eval_condition(features);
        if      (res == -1) cur = cur->get_left();   // Condition vraie → aller à gauche
        else if (res ==  0) cur = cur->get_right();  // Condition fausse → aller à droite
        else                return res;              // Feuille → retourner la valeur
    }
    return 0.0;  // Fallback
}
```

**⚠️ Piège classique — destructeur récursif** : Si on omet les vérifications `if (left != nullptr)`, le destructeur appelle `delete nullptr`. En C++, `delete nullptr` est défini et ne fait rien — mais si l'implémentation du destructeur elle-même accède à des membres sur `nullptr`, c'est un crash. Toujours tester avant de supprimer.

---

### 4.8 Opérations bit à bit (Bitwise operations)

**Définition** : Les opérations bit à bit agissent directement sur la **représentation binaire** des entiers, bit par bit.

**Intuition** : Chaque bit d'un entier est une "case". Les opérations bit à bit permettent de lire, activer, désactiver ou basculer des cases individuelles. C'est l'outil de prédilection pour la configuration de registres matériels, les permissions, la compression.

**Les opérateurs** :

| Opérateur | Nom | Description |
|---|---|---|
| `<<` | Décalage gauche | Multiplie par 2ⁿ |
| `>>` | Décalage droit | Divise par 2ⁿ (entier) |
| `&` | AND bit à bit | Garde uniquement les bits à 1 dans les DEUX opérandes |
| `\|` | OR bit à bit | Activé si AU MOINS un des deux bits est à 1 |
| `^` | XOR bit à bit | Activé si exactement UN des deux bits est à 1 |
| `~` | NOT bit à bit | Inverse tous les bits |

**Exemples complets et détaillés** :

```cpp
int x = 5;    // 00000101 en binaire

// 1. DÉCALAGE GAUCHE << : multiplie par 2ⁿ
int y = x << 1;   // 00001010 = 10  (5 × 2¹)
    y = x << 2;   // 00010100 = 20  (5 × 2²)
    y = x << 3;   // 00101000 = 40  (5 × 2³)

// 2. DÉCALAGE DROIT >> : divise par 2ⁿ (arrondi vers le bas)
    y = 20;       // 00010100
    y >>= 1;      // 00001010 = 10  (20 / 2)
    y >>= 2;      // 00000010 = 2   (10 / 4, arrondi vers le bas)

// 3. AND & : masquage (extraire des bits spécifiques)
int flags = 0b11010110;   // 214 en décimal
int mask  = 0b00001111;   // Garde seulement les 4 bits du bas
cout << (flags & mask);   // 0b00000110 = 6

// 4. OR | : activer un bit
int reg = 0b00000001;         // Bit 0 activé
reg |= (1 << 3);              // 1<<3 = 0b00001000 → reg = 0b00001001 = 9
// Bit 3 activé, bit 0 inchangé

// 5. XOR ^ : basculer (toggle) un bit
reg ^= (1 << 3);              // Bascule le bit 3 → reg = 0b00000001 = 1
// Si bit 3 était 1, il devient 0

// 6. Application : fonction find_parent dans BMD v4.0
// Utilise les décalages bit à bit pour naviguer dans l'arbre binaire équilibré :
int mask_bits = pow(2, level - 1);
while (mask_bits > 0) {
    if (node_idx & mask_bits) cur = cur->get_right();  // Bit à 1 = droite
    else                      cur = cur->get_left();   // Bit à 0 = gauche
    mask_bits >>= 1;           // Passe au bit suivant
}
```

**Tableau de véritê AND, OR, XOR** :

| A | B | A & B | A \| B | A ^ B |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

**⚠️ Pièges classiques** :
1. Confondre `&&` (AND logique, retourne bool) et `&` (AND bit à bit, agit sur chaque bit)
2. `1 << 31` peut déborder pour des `int` 32-bit signés. Utiliser `1u << 31` (unsigned) ou `1LL << 31` (long long).
3. Le décalage droit `>>` sur un entier **négatif signé** est défini par l'implémentation (peut propager le bit de signe ou non). Utiliser des entiers **non signés** (`unsigned int`) pour des décalages fiables.

---

## Cours 5 : Fonctions, Passage de Paramètres et Portée

### 5.1 Fonctions et Pile d'Appels (Call Stack)

**Définition** : Une fonction est un bloc de code autonome qui accomplit une tâche spécifique. Lors de l'exécution, les appels imbriqués sont gérés par la **pile d'appels** (call stack), qui mémorise d'où provient chaque appel pour y retourner à la fin.

**Intuition** : Pense à la pile d'appels comme une pile d'assiettes. Quand `main()` appelle `estimate()`, on pose l'assiette `estimate` sur `main`. L'exécution se concentre toujours sur l'assiette du dessus. Quand `estimate()` se termine (via `return`), son assiette est retirée (les variables locales sont détruites) et on reprend l'exécution sur l'assiette en dessous (`main`).

**Développement étape par étape (Prototypes et Définitions)** :
- **Prototype (Déclaration)** : Informe le compilateur de l'existence de la fonction (`type_retour nom(parametres);`). Indispensable si la fonction est définie après son utilisation, ou dans un autre fichier.
- **Définition** : Contient le code effectif entre `{ ... }`.
- **Paramètres vs Arguments** : Les *paramètres* sont les variables déclarées dans l'en-tête de la fonction. Les *arguments* sont les valeurs réelles fournies lors de l'appel.

**Exemple concret commenté** :
```cpp
#include <iostream>
using namespace std;

// Prototype (Déclaration en haut de fichier)
double power(double x, int n);

int main() {
    double result = power(2.0, 3); // '2.0' et '3' sont les arguments
    cout << result << endl;
    return 0;
}

// Définition (Implémentation détaillée - peut être placée n'importe où)
double power(double x, int n) { // 'x' et 'n' sont les paramètres
    if (n < 0) return 0.0;      // Premier point de sortie
    double res = 1.0;
    for (int i = 0; i < n; ++i) res *= x;
    return res;                 // Second point de sortie (la copie de 'res' est retournée)
} // 'res', 'i', 'x', et 'n' sont détruits ici (retirés du Call Stack)
```

**⚠️ Piège classique** : Oublier le prototype. Le compilateur lit le code de haut en bas. S'il rencontre l'appel `power(2.0, 3)` avant de l'avoir vu déclaré ou défini, il génèrera une erreur ("power was not declared in this scope"). Il faut toujours déclarer le prototype en amont !

---

### 5.2 Mécanismes de Passage de Paramètres

**Définition** : Il existe trois façons de transmettre un argument à une fonction : par **valeur** (copie), par **référence** (alias utilisant `&`), ou par **pointeur** (adresse utilisant `*`).

**Intuition** : 
- **Par valeur** : Donner une photocopie d'un rapport à un collègue. Ses modifications n'affectent pas ton original. Sûr mais lent (si le rapport fait 1000 pages).
- **Par référence** : Donner la clé de ton bureau partagé. Les modifications faites par le collègue *sont* tes modifications. Rapide (pas de copie) mais dangereux sans garanties (`const`).
- **Par pointeur** : Donner l'adresse postale du bureau. Le collègue doit s'y rendre (déréférencement `*`) pour interagir avec. Peut être "aucune adresse" (`nullptr`).

**Cas d'usage : in, out, inout** :
- **Entrée (in)** : La donnée est lue, non modifiée. (Valeur ou `const` référence).
- **Sortie / Modification (out / inout)** : La donnée existante est altérée pour l'appelant. (Référence ou pointeur).

**Exemple concret commenté — L'indexation salariale** :
```cpp
void applyIndexByVal(float k) { k *= 1.375; }            // Copie locale, modif perdue
void applyIndexByRef(float& k) { k *= 1.375; }           // Modifie DIRECTEMENT l'original (alias)
void applyIndexByPtr(float* k) { (*k) *= 1.375; }        // Suit l'adresse, modifie l'original

int main() {
    float salary = 3500;
    
    applyIndexByVal(salary); 
    cout << salary << "\n";      // Affiche 3500 (Original INTACT, la copie 'k' a été modifiée)
    
    applyIndexByRef(salary);     // Pas besoin de symbole spécial à l'appel
    cout << salary << "\n";      // Affiche 4812.5 (Original MODIFIÉ)
    
    salary = 3500;
    applyIndexByPtr(&salary);    // On passe l'adresse explicitement avec '&'
    cout << salary << "\n";      // Affiche 4812.5 (Original MODIFIÉ)
}
```

**Passage d'Arrays** : En C++, **un array est toujours passé par référence** implicitement (en fait, en tant que pointeur pointant sur son premier élément `&arr[0]`). C'est pourquoi un tableau altéré dans une fonction le sera dans `main()`. Par conséquent, on doit toujours fournir la taille de l'array séparément à la fonction (`void calc(int arr[], size_t n)`).

**⚠️ Piège extrêmement mortel** : Retourner une référence (ou un pointeur) vers une variable locale !
```cpp
// PIÈGE CLASSIQUE : Segfault garanti ou Bug silicieux
int& bad_function() {
    int local_var = 42;
    return local_var;   // DANGEREUX ! On retourne une référence...
} // ... mais local_var est détruite à l'accolade fermante ! La réf pointe dans le vide.
```

---

### 5.3 Les Paramètres Constants (`const`)

**Définition** : `const` appliqué à un paramètre de fonction établit un **contrat de non-modification** garanti par la compilation. C'est l'essence du mécanisme défensif de type (const-correctness) en C++.

**Intuition** : Le mot-clé `const` rassure le développeur utilisant ta fonction : "Je te passe mon gros array ou mon gros objet par référence (parce que copier est lent), mais je te promets que je ne le modifierai pas, c'est en lecture seule".

**Exemple concret commenté** :
```cpp
void printString(const string& s) {
    // s[0] = 'X';   // ERREUR DE COMPILATION ! Le compilateur interdit toute modification.
    cout << s << endl; // Autorisé (lecture seule)
}

void printArray(const double* arr, size_t n) {
    // arr[0] = 99.0; // ERREUR ! Pointeur constant, la donnée au bout est verrouillée.
}

class Rectangle {
public:
    int area() const { // <-- Placé à la fin : garantit qu'appeler .area() ne modifiera pas l'objet
        return width * height;
    }
};
```

**⚠️ Piège classique** : Oublier le `const` pour du "passage par référence d'entrée" `void print(string& s)`. Non seulement ce n'est pas sécurisé, mais ça empêche de passer des "valeurs r-values" (littéraux constants), comme `print("Hello")`.  Le compilateur les rejettera, demandant un `const string&`.

---

### 5.4 Paramètres par Défaut

**Définition** : Le C++ permet d'offrir une valeur par défaut à un paramètre (seulement depuis la déclaration/prototype), qui s'applique si l'appelant choisit de l'omettre.

**Exemple concret commenté** :
```cpp
// Le prototype déclare le défaut (qui va TOUJOURS à droite)
void log_message(string msg, string level = "INFO");

int main() {
    log_message("All good");               // Appelle avec msg="All good", level="INFO"
    log_message("Disk full", "ERROR");     // Appelle avec msg="Disk full", level="ERROR"
}

// La définition OMET le défaut pour éviter des doubles définitions
void log_message(string msg, string level) {
    cout << "[" << level << "] " << msg << endl;
}
```

**⚠️ Piège classique** : Les arguments manquants lors de l'appel sont assignés de gauche à droite. Par conséquent, il est **OBLIGATOIRE que tous les paramètres par défaut se trouvent à la fin (à droite) de la signature** (`f(int a, int b=0, int c=1)` est légal, `f(int a=0, int b)` est interdit).

---

### 5.5 Les fonctions `inline`

**Définition** : `inline` est un mot-clé (une requête suggérée au compilateur) incitant le compilateur à remplacer la totalité de la fonction appelée par son "copier coller" au point de l'appel, plutôt que de suivre la routine classique de la pile d'appels.

**Intuition** : Faire sauter l'exécution au bout de la mémoire a un "coup d'appel" en temps processeur (création du contexte, copie des paramètres, empilage/dépilage). Pour une fonction simple comme `square(x)`, cet *overhead* dépasse le coût réel de l'opération ($x \times x$). C'est ici que `inline` est magique : il optimise le temps, en prenant potentiellement un poil plus d'espace binaire.

**Exemple discret** :
```cpp
inline int square(int x) { return x * x; }
int main() {
    int y = square(5);  // Le compilateur compile ce code en secret comme: int y = 5 * 5;
}
```

---

### 5.6 Portée (Scope) vs Durée de Vie (Lifetime)

**Définition** : 
- **La Portée (Lexicale)** détermine OÙ dans les lignes de code le nom de la variable est connu et utilisable (règle du compilateur).
- **La Durée de vie** définit QUAND l'objet existe matériellement en RAM depuis sa création via constructeur jusqu'à sa destruction.

**Les Types de Variables** :
1. **Automatique / Locale** : Par défaut. Créée `{` → Détruite `}`. (Stack).
2. **Dynamique (`new`/`delete`)** : Durée de vie infinie jusqu'à effacement manuel. N'a pas de "portée", le pointeur est son seul moyen d'accès. (Heap).
3. **Globale** : Déclarée en-dehors. Dure toute l'application. Très mauvaise pratique d'encapsulation.
4. **Statique Locale (`static int x = 0`)** : La variable n'a qu'une portée *locale* (accès impossible ailleurs), MAIS d'une durée de vie *globale* (elle se souviendra de son état d'un appel à l'autre).

**Exemple concret commenté — Le compteur mémoire** :
```cpp
void hit_counter() {
    static int count = 0;   // Ce '= 0' n'est exécuté qu'UNE SEULE fois dans tout le programme.
    count++;                // Variable partagée secrètement au travers des appels successifs.
    cout << "Vous êtes le visiteur n°" << count << "\n";
}

int main() {
    hit_counter(); // Affiche 1
    hit_counter(); // Affiche 2
    // count++;    // ERREUR ! La portée (Scope) de 'count' ne sort pas de la fonction !
} // OUF : Même si la durée de vie était infinie, l'encapsulation empêche de corrompre count de l'extérieur.
```

**⚠️ Piège classique** : Croire que `static` dans une méthode de classe ou fonction a le même sens qu'en Java. En C++, `static` a le privilège de déconnecter la durée de vie (globale) de sa portée réelle locale, générant un cache interne extrêmement lisible qui ne pollue pas l'espace global du projet.
