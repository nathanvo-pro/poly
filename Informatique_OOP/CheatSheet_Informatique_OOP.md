# 🧾 Cheat Sheet — Informatique OOP (INFOH2001) — Cours 1 & 2

> ⚡ Fiche ultra-condensée — syntaxe vitale pour l'examen

---

## Structure minimale d'un programme

```cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Hello" << endl;
    return 0;
}
```

---

## Compilation

```bash
g++ fichier.cpp -o prog    # Compiler
./prog                     # Exécuter
```

---

## Types de base

| Type | Taille | Exemple |
|---|---|---|
| `int` | 4 bytes | `int x = 42;` |
| `double` | 8 bytes | `double pi = 3.14;` |
| `char` | 1 byte | `char c = 'A';` |
| `bool` | 1 byte | `bool ok = true;` |
| `string` | variable | `string s = "hi";` |

Qualificateurs : `short`, `long`, `unsigned`

---

## I/O Console

```cpp
cout << "Texte" << variable << endl;   // Sortie
cin >> variable;                        // Entrée (arrête aux espaces)
getline(cin, string_var);               // Entrée ligne complète
```

---

## Structures de contrôle

```cpp
// IF (⚠️ == pas = !)
if (cond) { ... } else if (cond2) { ... } else { ... }

// SWITCH (⚠️ break obligatoire !)
switch (val) { case 1: ...; break; default: ...; }

// FOR
for (int i = 0; i < n; i++) { ... }

// WHILE
while (cond) { ... }

// DO-WHILE (au moins 1 exécution)
do { ... } while (cond);
```

---

## Séquences d'échappement

`\n` nouvelle ligne · `\t` tabulation · `\\` antislash · `\"` guillemet · `\0` nul

---

## File I/O

```cpp
#include <fstream>

// Écriture
ofstream out("file.txt");
out << "data" << endl;
out.close();

// Lecture
ifstream in("file.txt");
string line;
while (getline(in, line)) { cout << line << endl; }
in.close();
```

Modes : `ios::in` | `ios::out` | `ios::app` | `ios::binary`

---

## Strings

```cpp
// C-string (ancien) : char name[] = "Mae";  // Terminée par \0
// C++ string (moderne, recommandé) :
#include <string>
string s = "Hello";
s += " World";        // Concaténation
s.length();            // Longueur
s[0];                  // Accès par index
s.find("lo");          // Recherche → position ou string::npos
```

---

## Parsing

```cpp
#include <sstream>

// Depuis une string :
istringstream iss("100 3.14");
int a; double b;
iss >> a >> b;          // a=100, b=3.14

// Vers une string :
ostringstream oss;
oss << "val=" << 42;
string result = oss.str();   // "val=42"

// sscanf (style C) :
sscanf(line, "%d,%d,%d,%127[^\n]", &a, &b, &c, buf);
```

---

## Arrays

```cpp
int arr[5] = {1, 2, 3, 4, 5};   // Taille fixe
arr[0];                           // Accès (commence à 0)
// ⚠️ Pas de vérification de bornes !
```

---

## Structs

```cpp
struct Point {
    double x;
    double y;
};                    // ⚠️ ; obligatoire

Point p;
p.x = 3.0;           // Accès avec .
p.y = 4.0;
```

---

## Fonctions

```cpp
int add(int a, int b);        // Prototype (déclaration)

int add(int a, int b) {       // Définition
    return a + b;
}

int z = add(5, 3);            // Appel → z = 8
```

---

## Conversions de type

```cpp
int n = static_cast<int>(3.14);   // ✅ Recommandé
int n = (int)3.14;                 // ⚠️ Style C, déconseillé
```

---

## Manipulateurs de flux

```cpp
#include <iomanip>
cout << fixed << setprecision(2) << 3.14159;      // 3.14
cout << setw(10) << setfill('*') << 42;            // ********42
cout << scientific << setprecision(1) << 123.456;  // 1.2e+02
```

`setprecision`, `setfill` = persistants · `setw` = prochain affichage seulement

---

## Opérateur ternaire

```cpp
result = condition ? valeur_si_vrai : valeur_si_faux;
```

---

## Arrays (Tableaux purs)

```cpp
int arr[] = {1, 2, 3, 4, 5};
int size = sizeof(arr) / sizeof(arr[0]);  // = 5
int* p = arr + 2;                         // p pointe sur arr[2] (valeur 3)
```
⚠️ **Aucun contrôle de dépassement en C++**.

---

## Classes et POO (`.h` vs `.cpp`)

```cpp
// ==== Fichier Interface (Point.h) ====
class Point {
private: 
    int x, y;             // Données encapsulées

public:
    Point();              // Prototype Constructeur par défaut
    Point(int x, int y);  // Prototype Constructeur avec paramètres
    void setX(int nx);    // Setter
    int getX();           // Getter
};                        // ⚠️ POINT VIRGULE A LA FIN DE CLASS !

// ==== Fichier Implémentation (Point.cpp) ====
// :: = Opérateur de résolution de portée
Point::Point() : x(0), y(0) {}  // Liste d'initialisation (Recommandé ! ✅)

Point::Point(int x_val, int y_val) : x(x_val), y(y_val) {}

void Point::setX(int nx) { 
    if (nx > 0) x = nx;   // Protection/Logique métier
}

int Point::getX() { return x; }
```

---

## Les Énumérations (Enums)

Améliorent la lisibilité et restreignent les variables à un pool limité.

```cpp
enum State { IDLE, RUNNING, ERROR }; // Internement: 0, 1, 2
State current_state = RUNNING;

if (current_state == RUNNING) {      // Fonctionne comme des entiers typés
    // ...
}
```

---

## Opérateurs d'incrémentation (Pré/Post)

```cpp
int a = 1, b = 1;
int x = ++a;   // PRE : a devient 2, puis x s'assigne 2. (x=2)
int y = b++;   // POST : y s'assigne 1, puis b devient 2. (y=1)
```
