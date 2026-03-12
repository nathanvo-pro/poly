import os

BASE = 'Informatique_OOP'
filepath = os.path.join(BASE, 'Synthese_Informatique_OOP.md')

part2 = r'''
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
'''

with open(filepath, 'a', encoding='utf-8') as f:
    f.write(part2)

print(f"✅ Part 2 (Cours 3 & 4) appended — {len(part2)} chars")
print("🎉 Complete synthesis rewrite done!")
