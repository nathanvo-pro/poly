# Exercices — Informatique OOP (INFOH2001)

## Cours 1 : Fondamentaux C++

> 📈 **Difficulté croissante :** ⭐ (définitions) → ⭐⭐⭐⭐⭐ (code complexe)

---

### ⭐ Niveau 1 — Définitions et concepts de base

---

**Exercice 1 — Hello World**

Écrivez un programme C++ complet qui affiche `Bonjour le monde !` suivi d'un retour à la ligne. Identifiez chaque élément syntaxique.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
#include <iostream>       // Inclusion de la bibliothèque d'entrée/sortie
using namespace std;      // Pour utiliser cout sans std::

int main() {              // Fonction principale, point d'entrée
    cout << "Bonjour le monde !" << endl;  // Affichage + retour à la ligne
    return 0;             // Fin sans erreur
}
```

Éléments :
- `#include` : directive de préprocesseur (équivalent de `import`)
- `main()` : seule fonction obligatoire
- `cout` : sortie console
- `<<` : opérateur d'insertion
- `endl` : fin de ligne + vidage tampon
- `;` : fin d'instruction
- `return 0` : signal « pas d'erreur » au système

</details>

---

**Exercice 2 — Compilé vs Interprété**

1. Quelle est la différence fondamentale entre un langage compilé et un langage interprété ?
2. Citez 2 langages compilés et 2 langages interprétés.
3. Qu'est-ce que la compilation JIT ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

1. Un **compilateur** traduit tout le code source d'un coup en code machine (fichier exécutable autonome), puis on exécute ce fichier. Un **interpréteur** lit et exécute le code instruction par instruction, sans produire de fichier exécutable persistant.

2. Compilés : **C++**, **Rust** (aussi Go, C). Interprétés : **Python**, **JavaScript** (aussi Ruby, PHP).

3. La compilation **JIT** (Just-In-Time) est un hybride : le code est d'abord compilé en bytecode, puis ce bytecode est compilé en code natif **au moment de l'exécution**, avec des optimisations adaptatives basées sur le profil d'exécution réel. Utilisée par la JVM (Java), .NET CLR, V8 (JavaScript).

</details>

---

**Exercice 3 — Types de données**

Pour chaque valeur, indiquez le type C++ le plus approprié :
1. Le nombre de jours dans une année
2. Le prix d'un produit en euros (précision importante)
3. La lettre 'A'
4. Le fait qu'un étudiant a réussi ou non
5. Le nom d'un étudiant

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

1. `int` — Le nombre de jours (365 ou 366) est un entier qui tient dans un `int`.
2. `double` — Pour les prix, on veut une bonne précision (~15 chiffres significatifs). `float` (~7 chiffres) serait insuffisant pour des calculs financiers.
3. `char` — Un seul caractère, stocké sur 1 byte.
4. `bool` — `true` ou `false`.
5. `std::string` — Une chaîne de caractères de longueur variable.

</details>

---

**Exercice 4 — Séquences d'échappement**

Qu'affiche le code suivant ?
```cpp
cout << "Ligne1\nLigne2\n";
cout << "Col1\tCol2\n";
cout << "Il a dit : \"Oui\"\n";
cout << "C:\\Users\\moi\n";
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```
Ligne1
Ligne2
Col1    Col2
Il a dit : "Oui"
C:\Users\moi
```

- `\n` → retour à la ligne
- `\t` → tabulation horizontale
- `\"` → guillemet double littéral
- `\\` → antislash littéral

</details>

---

### ⭐⭐ Niveau 2 — Structures de contrôle

---

**Exercice 5 — Piège du `if`**

Qu'affiche le code suivant et pourquoi ?
```cpp
int x = 10;
if (x = 0)
    cout << "A";
else
    cout << "B";
cout << "C";
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Affiche : `BC`**

`x = 0` est une **affectation** (pas une comparaison !). Elle :
1. Met `x` à 0
2. Retourne la valeur 0
3. `0` est interprété comme `false`

Donc le `else` s'exécute → `"B"`. Puis `"C"` s'exécute toujours car il n'est pas dans le `else`.

**Correction :** `if (x == 0)` avec **deux** signes `=`.

</details>

---

**Exercice 6 — Boucle `for` : prédiction de sortie**

Qu'affiche chaque boucle ?
```cpp
// A
for (int i = 0; i < 5; i++) cout << i << " ";

// B
for (int i = 10; i > 0; i -= 3) cout << i << " ";

// C
for (int i = 1; i <= 1; i++) cout << i << " ";
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```
A: 0 1 2 3 4
B: 10 7 4 1
C: 1
```

- **A** : `i` va de 0 à 4 (5 itérations)
- **B** : `i` commence à 10, décrémente de 3 : 10, 7, 4, 1. Quand `i` vaut 1, `1 > 0` est vrai donc on affiche. Ensuite `i = -2`, `-2 > 0` est faux → boucle terminée.
- **C** : `i = 1`, `1 <= 1` vrai → affiche 1. `i = 2`, `2 <= 1` faux → terminé.

</details>

---

**Exercice 7 — `while` vs `do...while`**

Quelle est la sortie de chacun ?
```cpp
// Version A
int i = 10;
while (i < 5) { cout << i; i++; }
cout << "FIN";

// Version B
int j = 10;
do { cout << j; j++; } while (j < 5);
cout << "FIN";
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```
Version A: FIN
Version B: 10FIN
```

- **A** (`while`) : La condition `10 < 5` est **fausse dès le départ** → le corps n'est jamais exécuté.
- **B** (`do...while`) : Le corps est exécuté **au moins une fois** avant de tester la condition → affiche `10`, puis teste `11 < 5` (faux) → arrêt.

C'est LA différence clé : `do...while` garantit au moins une exécution.

</details>

---

## Cours 2 : File I/O, Strings, Structs

### ⭐⭐⭐ Niveau 3 — File I/O et Strings

---

**Exercice 8 — Écriture et lecture de fichier**

Écrivez un programme qui :
1. Crée un fichier `notes.txt` et y écrit 3 lignes : "Alice 18", "Bob 15", "Charlie 12"
2. Relit le fichier et affiche chaque ligne à la console

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    // --- Écriture ---
    ofstream out("notes.txt");           // Ouvre en écriture (crée le fichier)
    out << "Alice 18" << endl;
    out << "Bob 15" << endl;
    out << "Charlie 12" << endl;
    out.close();                          // Ferme pour vider les tampons

    // --- Lecture ---
    string line;
    ifstream in("notes.txt");            // Ouvre en lecture
    if (in.is_open()) {
        while (getline(in, line))         // Lit ligne par ligne
            cout << line << endl;
        in.close();
    } else {
        cout << "Erreur d'ouverture !" << endl;
    }

    return 0;
}
```

Points clés :
- `ofstream` pour écrire, `ifstream` pour lire
- Toujours vérifier `is_open()` avant de lire
- `getline` lit toute la ligne (espaces compris), contrairement à `>>` qui s'arrête au premier espace
- Toujours appeler `close()` après utilisation

</details>

---

**Exercice 9 — C-string vs `std::string`**

Qu'affiche le code suivant ? Expliquez pourquoi.
```cpp
const char* s1 = "Hello\0World";
cout << s1 << endl;
cout << strlen(s1) << endl;

string s2 = "Hello";
s2 += " World";
cout << s2 << endl;
cout << s2.length() << endl;
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```
Hello
5
Hello World
11
```

- `s1` : Le `\0` au milieu marque la **fin de la C-string**. `cout` et `strlen` s'arrêtent à ce `\0`, donc seul "Hello" est affiché et la longueur est 5.
- `s2` : `std::string` stocke la longueur en interne, donc `\0` n'a pas de rôle spécial. La concaténation avec `+=` fonctionne naturellement et `length()` retourne 11.

**Leçon :** Préférez `std::string` à `char[]` — plus sûr, plus flexible, pas de piège `\0`.

</details>

---

**Exercice 10 — Parsing avec `istringstream`**

Complétez le code pour extraire les trois composantes de la string `"age <= 68.63"` :
```cpp
#include <sstream>
#include <string>
#include <iostream>
using namespace std;

int main() {
    string condition = "age <= 68.63";
    // À COMPLÉTER : extraire feat, op, threshold
    
    cout << "Feature: " << feat << endl;
    cout << "Operator: " << op << endl;
    cout << "Threshold: " << threshold << endl;
    return 0;
}
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
#include <sstream>
#include <string>
#include <iostream>
using namespace std;

int main() {
    string condition = "age <= 68.63";
    
    istringstream iss(condition);     // Connecte le stream à la string
    string feat, op;                   // Variables pour feature et opérateur
    float threshold;                   // Variable pour le seuil
    iss >> feat >> op >> threshold;    // Extraction séquentielle avec >>

    cout << "Feature: " << feat << endl;       // age
    cout << "Operator: " << op << endl;         // <=
    cout << "Threshold: " << threshold << endl;  // 68.63
    return 0;
}
```

`>>` extrait les tokens séparés par des espaces. C'est exactement le même fonctionnement que `cin >>`, mais depuis une string en mémoire.

</details>

---

### ⭐⭐⭐⭐ Niveau 4 — Structs et code plus complexe

---

**Exercice 11 — Créer et utiliser une struct**

Créez une `struct Student` avec les champs `name` (string), `grade` (double), `passed` (bool). Écrivez une fonction qui prend un `Student` et retourne `true` si sa note est ≥ 10.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    double grade;
    bool passed;
};

bool hasPassed(Student s) {       // Passage par valeur (copie)
    return s.grade >= 10.0;       // Retourne true si note ≥ 10
}

int main() {
    Student alice;
    alice.name = "Alice";
    alice.grade = 14.5;
    alice.passed = hasPassed(alice);

    cout << alice.name << " a " << (alice.passed ? "réussi" : "échoué") << endl;
    // Affiche : Alice a réussi

    Student bob = {"Bob", 8.0, false};     // Initialisation directe
    bob.passed = hasPassed(bob);
    cout << bob.name << " a " << (bob.passed ? "réussi" : "échoué") << endl;
    // Affiche : Bob a échoué

    return 0;
}
```

Points clés :
- `;` obligatoire après la `}` de la struct
- Accès aux membres avec l'opérateur `.`
- Une struct définit un **nouveau type** réutilisable
- L'opérateur ternaire `? :` est utilisé pour l'affichage conditionnel

</details>

---

**Exercice 12 — Manipulateurs de flux**

Qu'affiche le code suivant ?
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double x = 3.14159265;
    cout << setprecision(4) << x << endl;
    cout << fixed << setprecision(2) << x << endl;
    cout << scientific << setprecision(1) << x << endl;
    cout << setw(10) << setfill('*') << 42 << endl;
    return 0;
}
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```
3.142
3.14
3.1e+00
********42
```

- `setprecision(4)` sans `fixed` : 4 chiffres significatifs au total → `3.142`
- `fixed << setprecision(2)` : 2 chiffres **après** la virgule → `3.14`
- `scientific << setprecision(1)` : notation scientifique avec 1 chiffre après la virgule → `3.1e+00`
- `setw(10) << setfill('*') << 42` : largeur 10, rempli avec `*` → 8 étoiles + "42"

Note : `setprecision` et `setfill` sont **persistants** (restent actifs). `setw` ne s'applique qu'au **prochain** affichage.

</details>

---

**Exercice 13 — Programme de lecture de fichier CSV**

Écrivez un programme qui lit un fichier CSV `data.csv` au format `nom,age,note` et affiche chaque ligne formatée. Utilisez `getline` et `istringstream`.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ifstream file("data.csv");
    if (!file.is_open()) {
        cout << "Erreur : fichier introuvable" << endl;
        return 1;
    }

    string line;
    while (getline(file, line)) {           // Lit chaque ligne
        istringstream iss(line);
        string name;
        int age;
        double note;

        // getline avec délimiteur ',' pour extraire le nom
        getline(iss, name, ',');

        char comma;   // Pour consommer la virgule
        iss >> age >> comma >> note;

        cout << "Nom: " << name
             << " | Age: " << age
             << " | Note: " << note << endl;
    }

    file.close();
    return 0;
}
```

Points clés :
- `getline(stream, string, delimiteur)` permet de lire jusqu'à un caractère spécifique (ici `,`)
- On combine `getline` (pour le nom qui peut contenir des espaces) et `>>` (pour les nombres)
- Toujours vérifier `is_open()` et appeler `close()`

</details>

---

### ⭐⭐⭐⭐⭐ Niveau 5 — Problèmes de synthèse

---

**Exercice 14 — Mini Regression Tree**

Écrivez un programme complet qui :
1. Définit une `struct Node` avec les champs `id`, `left`, `right`, `condition` (string)
2. Lit un fichier `tree.txt` contenant des lignes au format `id,left,right,condition`
3. Parcourt l'arbre en fonction de valeurs d'entrée pour atteindre une feuille

Indice : une feuille a `left == -1` et `right == -1`.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdio>
using namespace std;

struct Node {
    int id;
    int left;
    int right;
    string condition;    // Pour les nœuds internes: "var op seuil"
                          // Pour les feuilles: la valeur prédite
};

// Parse une ligne du fichier en un Node
Node parseLine(const string& line) {
    Node n;
    char cond[128];
    sscanf(line.c_str(), "%d,%d,%d,%127[^\n]",
           &n.id, &n.left, &n.right, cond);
    n.condition = cond;
    return n;
}

// Évalue une condition simple "variable op seuil"
bool evalCondition(const string& cond, double x) {
    istringstream iss(cond);
    string var, op;
    double threshold;
    iss >> var >> op >> threshold;

    if (op == "<=") return x <= threshold;
    if (op == "<")  return x < threshold;
    if (op == ">=") return x >= threshold;
    if (op == ">")  return x > threshold;
    if (op == "==") return x == threshold;
    return false;
}

int main() {
    double input_value;
    cout << "Entrez la valeur de x : ";
    cin >> input_value;

    ifstream file("tree.txt");
    if (!file.is_open()) {
        cout << "Erreur : fichier introuvable" << endl;
        return 1;
    }

    int current = 0;    // Commence à la racine
    string line;

    while (true) {
        file.seekg(0);  // Repart du début du fichier
        while (getline(file, line)) {
            Node node = parseLine(line);
            if (node.id == current) {
                if (node.left == -1 && node.right == -1) {
                    // Feuille : affiche la prédiction
                    cout << "Prédiction : " << node.condition << endl;
                    file.close();
                    return 0;
                }
                // Nœud interne : évaluer et descendre
                if (evalCondition(node.condition, input_value))
                    current = node.left;
                else
                    current = node.right;
                break;  // Sort de la boucle de recherche
            }
        }
    }
}
```

Ce programme illustre l'utilisation combinée de : `struct`, file I/O (`ifstream`, `seekg`, `getline`), parsing (`sscanf`, `istringstream`), et structures de contrôle.

</details>

---

**Exercice 15 — Réflexion conceptuelle**

Expliquez pourquoi la version 2.0 (arbre lu depuis un fichier) est nettement préférable à la version 1.0 (arbre codé en dur) pour un outil de Machine Learning. Discutez au moins 3 avantages.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**3 avantages majeurs de la v2.0 :**

1. **Séparation entraînement/inférence :** Le modèle peut être entraîné par un programme séparé qui produit un fichier. Le même programme d'inférence peut être utilisé pour n'importe quel modèle sans le recompiler.

2. **Flexibilité et maintenabilité :** Changer le modèle = changer un fichier texte. Pas besoin de modifier le code source, pas besoin de recompiler. En production, on peut mettre à jour le modèle sans arrêter le service.

3. **Généricité :** Le code d'inférence est indépendant de la structure spécifique de l'arbre. Qu'il ait 5 nœuds ou 5000, le même programme fonctionne. Les variables et les seuils sont lus dynamiquement.

**Avantages bonus :**
4. **Testabilité :** On peut tester le programme d'inférence avec différents fichiers d'arbres sans toucher au code.
5. **Collaboration :** Un data scientist peut entraîner le modèle (en Python, R...) et un développeur C++ peut écrire le code de déploiement — ils communiquent via le fichier de l'arbre.

</details>

---

### Exercice Bonus — Code à trous

Complétez les trous (`____`) dans ce programme qui lit un fichier et compte les lignes :

```cpp
#include <iostream>
#include <____>                // Bibliothèque pour les fichiers
using namespace std;

int main() {
    ____ file("data.txt");     // Ouvrir en lecture
    if (!file.____()) {        // Vérifier l'ouverture
        cout << "Erreur" << endl;
        return 1;
    }

    string line;
    int count = 0;
    while (____(file, line))   // Lire ligne par ligne
        ____++;

    cout << "Nombre de lignes : " << count << endl;
    file.____();               // Fermer le fichier
    return 0;
}
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
#include <iostream>
#include <fstream>             // Bibliothèque pour les fichiers
using namespace std;

int main() {
    ifstream file("data.txt"); // ifstream pour lire
    if (!file.is_open()) {     // is_open() pour vérifier
        cout << "Erreur" << endl;
        return 1;
    }

    string line;
    int count = 0;
    while (getline(file, line)) // getline pour lire ligne par ligne
        count++;                 // Incrémenter le compteur

    cout << "Nombre de lignes : " << count << endl;
    file.close();               // Toujours fermer !
    return 0;
}
```

</details>

---

## Chapitre 3 — Hiérarchie mémoire, Arrays avancés et POO

> 📈 **Difficulté croissante :** ⭐ (définitions) → ⭐⭐⭐⭐⭐ (code complexe)

---

### ⭐ Niveau 1 — Concepts Fondamentaux

---

**Exercice 1 — Hiérarchie Mémoire**

Classez ces types de mémoire du **plus rapide** au **plus lent** en temps d'accès : RAM (DDR5), Cache L1, Disque dur (SSD), Registres CPU, Cache L3. Pourquoi charge-t-on le BMD (v3.0) en RAM plutôt que de le lire depuis le disque ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

**Ordre (plus rapide au plus lent) :**
1. Registres CPU (< 0.3 ns)
2. Cache L1 (0.3 - 1.2 ns)
3. Cache L3 (10 - 20 ns)
4. RAM DDR5 (~ 50 ns)
5. Disque SSD (10 à 100 µs, soit > 10 000 ns)

**Pourquoi le charger en RAM ?**
Parce que l'accès RAM est environ 1000 fois plus rapide que l'accès SSD. Au lieu de subir ce temps d'attente à chaque lecture de nœud (V2.0), on paie le prix d'une seule lecture séquentielle globale au début, et les inférences sur les patients se font quasi-instantanément depuis la RAM.

</details>

---

**Exercice 2 — Arrays vs Listes Python**

Quelle est la différence fondamentale dans la façon dont un tableau C++ gère l'accès aux index par rapport à une liste Python ? Que se passe-t-il si j'accède à `tab[15]` dans un tableau de 5 éléments en C++ ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Contrairement à Python qui vérifie les limites (et lance un `IndexError`), **C++ ne fait aucune vérification de bornes.** L'accès à `tab[15]` ira simplement lire la mémoire située 15 "cellules" plus loin que l'adresse de départ du tableau, qu'elle lui appartienne ou non.

Conséquences possibles :
- **Segmentation Fault :** Crash immédiat si la mémoire est protégée (hors du processus).
- **Corruption de mémoire (Buffer Overflow) :** Lecture ou écriture dans une zone mémoire appartenant à une autre variable de votre programme (bug très dangereux et muet).

</details>

---

### ⭐⭐ Niveau 2 — Programmation Orientée Objet (POO)

---

**Exercice 3 — Classe vs Objet**

Expliquez avec vos propres mots la différence entre une `class` et un `objet`. Donnez une analogie de la vie réelle.

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Une **classe** est un "plan" ou un "moule". C'est un type de données abstrait (ex: la classe Voiture).
Un **objet** est une instance concrète fabriquée à partir de ce plan, qui existe en mémoire (ex: la Voiture rouge de Paul, garée devant la maison).

</details>

---

**Exercice 4 — Encapsulation et Sécurité**

Pourquoi déclare-t-on les attributs d'une classe en `private` au lieu de `public` ? Comment fait-on pour les modifier ?

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

Mettre les données en `private` permet l'**Encapsulation** (masquage des données).
Cela empêche l'utilisateur d'affecter accidentellement une valeur invalide (ex: un âge négatif, un pointeur nul) directement via `monObjet.age = -5`.

Pour les modifier, on passe par l'interface `public` avec des méthodes mutateurs (**Setters**) et accesseurs (**Getters**). Le setter peut contenir des validations (ex: `if (a > 0) age = a;`).

</details>

---

### ⭐⭐⭐ Niveau 3 — Constructeurs et Syntaxe avancée

---

**Exercice 5 — Listes d'initialisation**

Identifiez la différence de comportement (et de performance) entre ces deux constructeurs :

```cpp
// Constructeur A
Point::Point(int x_val, int y_val) {
    x = x_val;
    y = y_val;
}

// Constructeur B
Point::Point(int x_val, int y_val) : x(x_val), y(y_val) {
}
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

- **Constructeur A** : crée l'objet par défaut (avec des valeurs poubelles ou par défaut), *puis* fait une copie (affectation) dans le corps de la fonction. C'est en fait composé de 2 étapes.
- **Constructeur B (Liste d'initialisation)** : initialise *directement* la mémoire allouée au moment de la création avec les bonnes valeurs en une seule étape.

La version B est la **bonne pratique** car elle évite des copies inutiles et est la seule façon d'initialiser des attributs `const` ou des références (`&`).

</details>

---

**Exercice 6 — Enums vs Constantes Magiques**

Corrigez cette vérification "sale" en utilisant une `enum` propre.

```cpp
int STATE_IDLE = 0;
int STATE_RUNNING = 1;
int STATE_ERROR = 2;

int currentState = 1;
if (currentState == STATE_ERROR) { /* ... */ }
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
// Enumération proprement déclarée
enum State { STATE_IDLE, STATE_RUNNING, STATE_ERROR };

State currentState = STATE_RUNNING;
if (currentState == STATE_ERROR) { /* ... */ }
```
L'enumérateur attribue automatiquement 0 à IDLE, 1 à RUNNING, 2 à ERROR. Le code n'est plus risqué (on ne peut affecter que des valeurs valides de type `State` à un `State`).

</details>

---

### ⭐⭐⭐⭐ Niveau 4 — Arithmétique de pointeurs et Opérateurs

---

**Exercice 7 — Pièges de l'incrémentation**

Que va afficher ce code exactement ?

```cpp
int x = 5, y = 10;
int a = ++x;
int b = y++;

cout << a << " " << x << endl;
cout << b << " " << y << endl;
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```
6 6
10 11
```
- `++x` (PRE-incrément) : "Incrémente d'abord, donne la valeur après". `x` devient 6, puis `a` reçoit 6.
- `y++` (POST-incrément) : "Donne la valeur actuelle d'abord, incrémente après". `b` reçoit l'ancienne valeur 10, PUIS `y` devient 11.

</details>

---

### ⭐⭐⭐⭐⭐ Niveau 5 — Synthèse et Code à trous

---

**Exercice 8 — Mini-BMD Array Logic**

Complétez le parcours iteratif d'un arbre binaire représenté sous forme de tableau (V3.0). La racine est à l'index `1`. `max_nodes` est `100`.

```cpp
float estimate_tree(float record[]) {
    int idx = ____; // 1. Par où commence-t-on?
    
    while (idx < ____) { // 2. Condition de sécurité
        if (tree[idx].____()) { // 3. Est-on arrivé à la fin de la branche?
            return tree[idx].get_value();
        }
        
        bool left = tree[idx].eval_condition(record);
        
        // 4. Utilisation de l'opérateur ternaire pour descendre
        idx = left ? ____ : ____; 
    }
    return 0.0;
}
```

<details>
<summary>Voir la réponse et l'explication détaillée</summary>

```cpp
float estimate_tree(float record[]) {
    int idx = 1; // 1. Par où commence-t-on? (Racine à l'index 1)
    
    while (idx < 100) { // 2. Condition de sécurité (MAX_NODES = 100)
        if (tree[idx].test_leaf()) { // 3. Est-on arrivé à une feuille ?
            return tree[idx].get_value();
        }
        
        bool left = tree[idx].eval_condition(record);
        
        // 4. Utilisation de l'opérateur ternaire
        idx = left ? tree[idx].get_left() : tree[idx].get_right(); 
    }
    return 0.0; // Ne devrait jamais arriver si l'arbre est bien formé
}
```
Cette boucle est l'essence même de l'optimisation v3.0 : chaque étape correspond juste à lire `idx` dans le tableau (0.3 ns en cache L1) contre une lecture de disque dur (1 ms) en V2.0.

</details>


---

## Cours 4 — Systèmes de numération, Pointeurs & Allocation dynamique

### Exercice 4.1 ⭐ — Conversion décimal → binaire

Convertissez les nombres suivants de décimal vers binaire **à la main** (méthode des divisions successives) :
a) 13
b) 100
c) 255

<details>
<summary>Voir la réponse</summary>

**a) 13₁₀ → 1101₂**
13÷2=6 r1, 6÷2=3 r0, 3÷2=1 r1, 1÷2=0 r1 → lu de bas en haut : 1101

**b) 100₁₀ → 1100100₂**
100÷2=50 r0, 50÷2=25 r0, 25÷2=12 r1, 12÷2=6 r0, 6÷2=3 r0, 3÷2=1 r1, 1÷2=0 r1 → 1100100

**c) 255₁₀ → 11111111₂**
255÷2=127 r1, 127÷2=63 r1... tous les restes sont 1 → 8 bits tous à 1.

</details>

### Exercice 4.2 ⭐ — Pointeurs : lecture de code

Quel est l'affichage produit par ce programme ?

```cpp
int a = 10, b = 20;
int *p = &a;
*p = 30;
p = &b;
*p = 40;
cout << a << " " << b << endl;
```

<details>
<summary>Voir la réponse</summary>

**Affichage : `30 40`**

Explication :
1. `p` pointe vers `a`. `*p = 30` → modifie `a` qui vaut maintenant 30.
2. `p` pointe maintenant vers `b`. `*p = 40` → modifie `b` qui vaut maintenant 40.

</details>

### Exercice 4.3 ⭐⭐ — Arithmétique des pointeurs

Quel est l'affichage de ce code ?

```cpp
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;
cout << *(p + 2) << endl;
p += 3;
cout << *p << endl;
cout << p - arr << endl;
```

<details>
<summary>Voir la réponse</summary>

**Affichage :**
```
30
40
3
```
- `*(p + 2)` : p pointe vers arr[0], p+2 pointe vers arr[2] → 30.
- `p += 3` : p pointe maintenant vers arr[3] → *p = 40.
- `p - arr` : la distance en nombre d'éléments entre p et le début du tableau → 3.

</details>

### Exercice 4.4 ⭐⭐ — Stack vs Heap

Pour chacune de ces variables, indiquez si elle est allouée sur la **Stack** ou le **Heap** :

```cpp
int main() {
    int x = 5;                    // a)
    int* p = new int(10);         // b) la variable p ? et l'objet pointé ?
    double tab[100];              // c)
    double* dyn = new double[50]; // d) la variable dyn ? et le tableau ?
    static int count = 0;         // e)
    delete p;
    delete[] dyn;
    return 0;
}
```

<details>
<summary>Voir la réponse</summary>

- **a) `x`** : Stack (variable locale)
- **b) `p`** : Stack (le pointeur lui-même), mais l'objet `new int(10)` est sur le **Heap**.
- **c) `tab`** : Stack (tableau statique de taille fixe)
- **d) `dyn`** : Stack (le pointeur), le tableau `new double[50]` est sur le **Heap**.
- **e) `count`** : Zone **Global/Static** (mot-clé `static`)

</details>

### Exercice 4.5 ⭐⭐ — Détection de Memory Leaks

Identifiez toutes les fuites mémoire dans ce code :

```cpp
void processData() {
    int* a = new int(5);
    int* b = new int(10);
    a = b;                   // Ligne suspecte !
    delete a;
}
```

<details>
<summary>Voir la réponse</summary>

**1 fuite mémoire détectée :**

À la ligne `a = b;`, le pointeur `a` est réaffecté pour pointer vers le même objet que `b`. L'ancien objet pointé par `a` (le `new int(5)`) n'est plus accessible par aucun pointeur → **Memory Leak** : impossible de faire `delete` sur ce bloc.

`delete a;` libère l'objet originalement alloué pour `b`, mais l'objet `new int(5)` est perdu à jamais.

**Correction :**
```cpp
delete a;    // Libérer l'ancien objet AVANT de réaffecter
a = b;
// ... utiliser a ...
delete a;    // Libérer le second objet
```

</details>

### Exercice 4.6 ⭐⭐⭐ — new[] et delete[]

Écrivez une fonction `createArray(int n)` qui alloue dynamiquement un tableau de `n` entiers, les initialise aux valeurs 0, 1, 2, ..., n-1, et retourne le pointeur. Écrivez le `main` qui appelle cette fonction, affiche le tableau, et libère proprement la mémoire.

<details>
<summary>Voir la réponse</summary>

```cpp
#include <iostream>
using namespace std;

int* createArray(int n) {
    int* arr = new int[n];
    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }
    return arr;  // Le tableau survit à la fonction car il est sur le Heap
}

int main() {
    int taille = 10;
    int* tab = createArray(taille);
    
    for (int i = 0; i < taille; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
    
    delete[] tab;     // Libérer avec delete[] car c'est un array
    tab = nullptr;    // Bonne pratique
    return 0;
}
```

</details>

### Exercice 4.7 ⭐⭐⭐ — Opérateur flèche `->`

Complétez le code suivant pour créer un objet `Student` sur le Heap, remplir ses champs via `->`, afficher ses données, et libérer la mémoire :

```cpp
struct Student {
    string name;
    int age;
    float gpa;
};

int main() {
    // TODO : créer un Student sur le Heap
    // TODO : remplir les champs
    // TODO : afficher les données
    // TODO : libérer la mémoire
    return 0;
}
```

<details>
<summary>Voir la réponse</summary>

```cpp
int main() {
    Student* s = new Student();
    s->name = "Alice";
    s->age = 20;
    s->gpa = 3.8;
    
    cout << "Nom: " << s->name << endl;
    cout << "Age: " << s->age << endl;
    cout << "GPA: " << s->gpa << endl;
    
    delete s;
    s = nullptr;
    return 0;
}
```

</details>

### Exercice 4.8 ⭐⭐⭐ — Opérations bit à bit

Évaluez manuellement les expressions suivantes :
a) `12 & 10`
b) `12 | 10`
c) `5 << 3`
d) `40 >> 2`

<details>
<summary>Voir la réponse</summary>

**a) 12 & 10 = 8**
```
  1100  (12)
& 1010  (10)
------
  1000  (8)
```

**b) 12 | 10 = 14**
```
  1100  (12)
| 1010  (10)
------
  1110  (14)
```

**c) 5 << 3 = 40**
5 = 00000101, décalé de 3 → 00101000 = 40 (= 5 × 2³)

**d) 40 >> 2 = 10**
40 = 00101000, décalé de 2 → 00001010 = 10 (= 40 / 2²)

</details>

### Exercice 4.9 ⭐⭐⭐⭐ — Destructeur récursif

Dessinez l'arbre suivant et indiquez dans quel ordre les nœuds sont détruits lorsqu'on fait `delete root;` :

```
root
├── left
│   ├── left->left (feuille)
│   └── left->right (feuille)
└── right (feuille)
```

<details>
<summary>Voir la réponse</summary>

**Ordre de destruction (en supposant que le destructeur appelle d'abord `delete left` puis `delete right`) :**

1. `delete root` déclenche le destructeur de root.
2. `delete root->left` déclenche le destructeur de left.
3. `delete left->left` → c'est une feuille (left=nullptr, right=nullptr) → rien à supprimer récursivement → le nœud est détruit.
4. `delete left->right` → feuille → détruit.
5. Le nœud `left` est maintenant détruit.
6. `delete root->right` → feuille → détruit.
7. Le nœud `root` est maintenant détruit.

**Ordre : left->left, left->right, left, right, root** (destruction des feuilles en premier, puis remontée vers la racine).

</details>

### Exercice 4.10 ⭐⭐⭐⭐⭐ — Arbre binaire complet

Implémentez une classe `TreeNode` simple contenant un `int value`, et deux pointeurs `TreeNode* left` et `TreeNode* right`. Écrivez :
1. Un constructeur qui initialise `value` et met les enfants à `nullptr`.
2. Un destructeur récursif.
3. Une fonction libre `int countNodes(TreeNode* root)` qui compte récursivement le nombre total de nœuds dans l'arbre.

<details>
<summary>Voir la réponse</summary>

```cpp
#include <iostream>
using namespace std;

class TreeNode {
public:
    int value;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int val) : value(val), left(nullptr), right(nullptr) {}
    
    ~TreeNode() {
        if (left != nullptr) delete left;
        if (right != nullptr) delete right;
    }
};

int countNodes(TreeNode* root) {
    if (root == nullptr) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    
    cout << "Nombre de noeuds: " << countNodes(root) << endl;  // 5
    
    delete root;  // Libère tout l'arbre récursivement
    return 0;
}
```

</details>
