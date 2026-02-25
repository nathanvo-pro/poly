# ✅ Quiz / QCM — Informatique OOP (INFOH2001)

> Quiz avec questions à choix multiples pour réviser chaque chapitre.
> Cliquez sur **💡 Solution** pour vérifier votre réponse et voir l'explication.

---

##  Cours 1 : De Python à C++

### Question 1.1 : Quelle est la différence fondamentale d'exécution entre Python et C++ ?
- [ ] A) C++ est un langage compilé en code machine avant l'exécution, tandis que Python est interprété ligne par ligne.
- [ ] B) C++ est interprété par le processeur directement, Python est compilé dans un navigateur Web.
- [ ] C) Les deux sont interprétés, mais C++ utilise une machine virtuelle plus performante de bas niveau.
- [ ] D) Python nécessite un linker lors de la compilation, C++ non.

<details>
<summary>💡 Solution</summary>

**Réponse A**. C++ est un langage compilé. Le code source est d'abord traduit entièrement en fichier objet par le compilateur (comme g++), puis lié pour former un exécutable natif. Python est lu et exécuté par un interpréteur à la volée, ce qui le rend généralement plus lent.
</details>

### Question 1.2 : Pourquoi C++ est-il souvent qualifié de langage favorisant « l'informatique verte » comparativement à Python ?
- [ ] A) Car il dispose d'un module `<eco>` natif réduisant la consommation de l'écran.
- [ ] B) Parce que sa syntaxe est plus concise, réduisant la taille des fichiers sur le disque dur.
- [ ] C) Étant compilé et très proche de la machine, il exécute les calculs beaucoup plus rapidement, consommant ainsi moins de cycles CPU et donc moins d'électricité pour la même tâche.
- [ ] D) Il exige des variables statiques qui ne varient pas en tension électrique.

<details>
<summary>💡 Solution</summary>

**Réponse C**. La rapidité d'exécution du C++ (due à sa compilation réseau bas niveau) fait qu'il sollicite le processeur beaucoup moins longtemps que Python pour la même charge de travail, réduisant ainsi la consommation d'énergie (informatique verte).
</details>

### Question 1.3 : Quelles sont les deux étapes majeures successives pour transformer du code `.cpp` en un exécutable autonome ?
- [ ] A) Interprétation puis Garbage Collection.
- [ ] B) Compilation (génère les fichiers objets `.o`) puis Linkage/Édition de liens (combine les objets avec les bibliothèques).
- [ ] C) Debugging puis Run JIT.
- [ ] D) Parsing puis Assembleur dynamique.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le flux classique : le compilateur traduit d'abord chaque `.cpp` en un `.o` (code objet/machine rudimentaire), puis le Linker rassemble tout cela ainsi que les bibliothèques standards pour forger l'exécutable final.
</details>

### Question 1.4 : En C++, à quoi sert précisément l'instruction `return 0;` placée à la fin de la fonction `main()` ?
- [ ] A) À réinitialiser les boucles de l'ordinateur à zéro.
- [ ] B) C'est un code qui indique le nombre d'erreurs détectées (ici zéro).
- [ ] C) Elle signale au système d'exploitation que le programme s'est exécuté avec succès, sans erreur.
- [ ] D) Elle libère toute la mémoire RAM manuellement.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Par convention stricte des OS (Linux/Windows), un programme qui se termine et renvoie la valeur entière `0` dit "Tout s'est parfaitement déroulé". Une valeur différente de zéro signale généralement un code d'erreur ou d'anomalie.
</details>

### Question 1.5 : Quel sera le résultat de l'instruction C++ suivante concernant les types : `int a = 5; std::string b = "hello"; a + b;` ?
- [ ] A) Une erreur fatale de compilation empêchant la création de l'exécutable.
- [ ] B) Une erreur détectée uniquement lors de l'exécution (Runtime Error), comme en Python.
- [ ] C) L'affichage de "5hello" dans la console car C++ concatène dynamiquement.
- [ ] D) Le plantage silencieux du compilateur.

<details>
<summary>💡 Solution</summary>

**Réponse A**. C++ est un langage à « typage statique ». Il détecte d'office l'incompatibilité de type entre un `int` et un `std::string` avant même l'exécution, pendant la stricte phase de compilation.
</details>

### Question 1.6 : En C++, quelle est la plage de mémoire approximative d'un type `double` standart (flottant double précision) ?
- [ ] A) 4 octets, 7 chiffres significatifs.
- [ ] B) 1 octet, valeur absolue binaire.
- [ ] C) 8 octets, procurant environ 15 chiffres de précision significative.
- [ ] D) Dynamique, elle s'adapte à la taille de la RAM disponible.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le type `double` occupe généralement 8 bytes (64 bits) selon le standard IEEE 754, ce qui garantit environ 15-17 chiffres significatifs décimaux très précis.
</details>

### Question 1.7 : Que représente le caractère invisible d'échappement `\0` communément utilisé en bas niveau dans le monde du C/C++ ?
- [ ] A) L'équivalent du `None` de Python.
- [ ] B) Un saut de ligne de format Linux absolu.
- [ ] C) Le « caractère nul », qui indique mécaniquement la stricte fin d'une chaîne de caractères (C-string).
- [ ] D) L'adresse mémoire de base zéro du pointeur RAM.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le fameux caractère nul `\0` (code ASCII 0) est la sentinelle indispensable utilisée par toutes les fonctions traditionnelles C (`strlen`, `cout`) pour comprendre où se termine la lecture d'une chaîne `char[]`.
</details>

### Question 1.8 : Quelle est la conséquence grave et très courante du code suivant en C++ : `if (i = 5) { cout << "ok"; }` ?
- [ ] A) Il n'y a aucun problème, si $i$ valait $5$ avant, ok s'affiche.
- [ ] B) Piège classique ! C'est une affectation (et non une comparaison `==`). La variable $i$ devient $5$, et la condition évalue l'entier $5$ comme "vrai", imprimant "ok" systématiquement.
- [ ] C) La compilation échoue obligatoirement car le compilateur interdit l'affectation dans le if.
- [ ] D) C'est une fonction ternaire silencieuse provoquant une fuite de mémoire (Memory Leak).

<details>
<summary>💡 Solution</summary>

**Réponse B**. L'erreur fatale du débutant. En C++, `1 =` est l'assignation. Pour comparer, il faut `==`. Comme $5 \neq 0$, la condition est perçue comme `true`, ruinant ainsi la logique du test de façon silencieuse.
</details>

### Question 1.9 : Si l'on écrit un `switch(x)` en omettant délibérément l'instruction `break;` à la fin d'un `case 1:`, que se passe-t-il lorsque `x = 1` ?
- [ ] A) Le programme renvoie une exception et se termine.
- [ ] B) Rien, la fin du bloc `case` équivaut nativement à un arrêt de lecture.
- [ ] C) Phénomène de "Fall-through" : le programme va exécuter le `case 1`, puis va "tomber" et continuer d'exécuter bêtement les instructions du `case 2` en dessous, etc.
- [ ] D) Le premier `case` de la balise est relu en boucle infinie pure.

<details>
<summary>💡 Solution</summary>

**Réponse C**. C'est le "Fall-Through" ! En C++, le `case` sert juste d'étiquette d'entrée (entry-point). Sans l'interrupteur `break;`, l'exécution ne quitte pas le `switch` et "coule" dans le code de tous les cas suivants.
</details>

### Question 1.10 : À l'intérieur d'une instruction conditionnelle `if`, quelle est la valeur logique (booléenne) concédée par défaut à l'entier "0" (zéro) ?
- [ ] A) `true` (Vrai).
- [ ] B) `false` (Faux).
- [ ] C) Exponentielle relative.
- [ ] D) Non-définie (Undefined Behavior).

<details>
<summary>💡 Solution</summary>

**Réponse B**. En C++, n'importe quelle valeur algébrique numérique non nulle ($1, 5, -8, 100$) est interprétée purement comme `true`. **Seul `0` (zéro) est stictement synonyme de `false`**.
</details>

### Question 1.11 : Quelle boucle C++ est la seule à garantir abstraitement de toujours s'exécuter ***au moins une fois***, peu importe la condition de définition ?
- [ ] A) La boucle `for(;;) `.
- [ ] B) La boucle `while` stricte.
- [ ] C) La boucle `do...while`.
- [ ] D) La boucle inconditionnelle `goto`.

<details>
<summary>💡 Solution</summary>

**Réponse C**. La conception du `do { ... } while(condition);` fait que la condition est formellement évaluée à la fin, *APRÈS* le premier tour de roue du corps de l'instruction !
</details>

### Question 1.12 : Sous C++, quel est l'exact rôle purement syntaxique de l'indentation (les espaces invisibles en début de ligne de code) ?
- [ ] A) Elle définit rigoureusement l'appartenance des portées (scopes) comme le fait Python.
- [ ] B) Elle autorise la désactivation du point-virgule de fin de fonction.
- [ ] C) Strictement aucun rôle au niveau compilation. Elle ne sert qu'à la lisibilité oculaire du développeur.
- [ ] D) L'indentation gère le niveau d'optimisation (O3).

<details>
<summary>💡 Solution</summary>

**Réponse C**. En C++, c'est le combo `{}` (accolades) asymétrique pure qui définit les blocs et la portée, et le `;` (point-virgule) pour les fins d'instructions. Les espaces/tabulations sont totalement ignorés par g++.
</details>

### Question 1.13 : Concernant la scope (portée locale des variables absolues), si je déclare `int x = 42;` entre les accolades pures d'un bloc `if`, quel est son statut à la sortie du bloc en question ?
- [ ] A) Sa valeur passe définitivement à zéro.
- [ ] B) La variable est instantanément détruite de la pile par le C++. Tenter de l'utiliser provoquera une Erreur de Compilation.
- [ ] C) Elle existe encore dans le scope global principal.
- [ ] D) Elle reste sous forme de pointeur orphelin. 

<details>
<summary>💡 Solution</summary>

**Réponse B**. Les variables en C++ sont limitées formellement à la portée de leurs propres accolades (scope). À la fermeture de l'accolade d'un bloc `if`, `x` est effacé de la mémoire. 
</details>

### Question 1.14 : Si l'on effectue la boucle `for (int i = 5; i < 5; i++)`, que fait le compilateur ou le programme C++ en exécution ?
- [ ] A) La boucle est ignorée (zéro itération).
- [ ] B) Elle plante.
- [ ] C) Elle dérive vers l'infini car la borne $5$ engendre un overflow.
- [ ] D) i va de 5 à 4 cycliquement.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'ordinateur teste `i < 5` (est-ce que $5 < 5$ ?). $False$. La boucle est directement avortée.
</details>

### Question 1.15 : Quelle est la grande force de l'instruction `std::endl` comparativement au simple retour chariot `\n` ?
- [ ] A) Elle compile en assembleur natif de 32 bits.
- [ ] B) Elle insère un caractère invisible EOF.
- [ ] C) `std::endl` a un double effet : saut de ligne ET FORCER le Vidage (Flush) complet du Tampon (Buffer) de sortie.
- [ ] D) Elle efface et rafraichit totalement la console terminal.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le "flushing" du stream `cout` assure que vos impressions console sont instantanément visibles et validées sans attendre de remplir le buffer de la machine.
</details>

---

##  Cours 2 : File I/O, Strings, Structs & Fonctions

### Question 2.1 : À quelle classe standard faites-vous appel pour extraire dynamiquement des données de texte contenues à l'intérieur d'un fichier sauvegardé sur le disque ?
- [ ] A) `ofstream`
- [ ] B) `ifstream`
- [ ] C) `scanf`
- [ ] D) `filelib`

<details>
<summary>💡 Solution</summary>

**Réponse B**. `ifstream` (Input File Stream). Permet d'ouvrir un flux de communication depuis le fichier texte vers l'application C++. 
</details>

### Question 2.2 : Pour quelle raison capitale de stabilité devez-vous toujours spécifier la commande `fic.close()` à la fin d'un travail sur un fichier nommé `fic` ?
- [ ] A) `close()` force la machine à vider le cache des buffers résiduels pour sécuriser les octets sur le disque dur réel, et libère le fichier débloquant l'utilisation par un autre programme (OS Thread).
- [ ] B) C'est juste facultatif, l'OS ferme les fichiers tout seul en C++.
- [ ] C) Sans le `close()`, le fichier est physiquement supprimé de la corbeille.
- [ ] D) Le compilateur refuse la compilation si le texte de l'instruction `close()` est absent.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Sans `close()`, les tampons mémoire ne se vident pas toujours causant des pertes (loss) partielles du fichier texte, et le programme maintient un statut de "verrou" (locked format) dans l'explorateur Windows/Linux.
</details>

### Question 2.3 : Quel est l'atout de la classe moderne orientée objet `std::string` en rapport avec la désuète chaine format C (`char[]`) ?
- [ ] A) Elle permet des calculs algébriques `string` $\times$ `string`.
- [ ] B) Elle réduit l'allocation de la RAM par 10 purement.
- [ ] C) `std::string` encapsule dynamiquement sa taille et s'assure toute seule d'éviter les infâmes "buffer overflows" mortels, nous affranchissant de manipuler manuellement de dangereux marqueurs comme `\0`.
- [ ] D) Elle est rétrocompatible avec les calculateurs FORTRAN.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le système très haut-niveau et souple `std::string` gère sa mémoire dynamiquement interne, ce qui est extrêmement résistant aux failles de sécurité de la `strcpy` ou `strlen` en C natif.
</details>

### Question 2.4 : La puissante commande `sscanf(line, "%d,%d", &n_id, &l_id);` est destinée fondamentalement à :
- [ ] A) Récupérer (extraire) des données formatées complexes depuis une base contenant un C String existant en mémoire, en parsant la syntaxe.
- [ ] B) Transformer une String C++ en fichier .CSV.
- [ ] C) Faire une requête serveur réseau SQL basique.
- [ ] D) Scroller les lignes du terminal actif de Linux.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Formidable outil C "String Scan Formatted". Il absorbe un string plat de caractère et en extrait les entonnoirs mathématiques purs `%d` dans des variables adresses passées numériquement `&var`.
</details>

### Question 2.5 : L'objectif structurel fondamental d'une définition `struct` en programmation C/C++ est :
- [ ] A) D'initialiser une fonction mère.
- [ ] B) De créer de vos propres mains de nouveaux « TYPES » composites sur mesure de données (Data) ; cela afin de regrouper unitairement un paquet de variables "champs" hétérogènes (de types variés) intrinsèquement corrélées sémantiquement.
- [ ] C) D'ouvrir un lien HTML vers une feuille CSS.
- [ ] D) D'implémenter les balises graphiques d'un vecteur Matrix OpenGL.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le principe central de la structure : Regrouper dans une "seule boîte" ce qui va logiquement ensemble. L'exemple est un `struct Patient { int age; string name; float height; };`.
</details>

### Question 2.6 : La méthode sûre en C++ utilisée et préconisée pour effectuer un cast de la valeur d'une variable type `double d = 3.14;` formatée manuellement vers un type standard `int` est :
- [ ] A) `int n = (int)d;`
- [ ] B) `int n = int::cast(d);`
- [ ] C) `int n = static_cast<int>(d);`
- [ ] D) `int n = Dynamic_Cast_Format(d);`

<details>
<summary>💡 Solution</summary>

**Réponse C**. L'outil robuste absolu et explicite du compilateur en C++ : `static_cast<nouveau_type>(variable_a_caster)`. Il vérifie la validité des formats (Types Safety) là ou le cast old school de C style `(int)x` laissait passer de graves absurdités invisibles.
</details>

### Question 2.7 : Concernant le passage rigoureux des paramètres d'une fonction, que désigne le très célèbre concept informatique conventionnel « Passage par Valeur » ?
- [ ] A) La fonction compte la masse en hexadécimal pur de la signature de son prototype virtuel.
- [ ] B) Un principe essentiel qui veut que la fonction C++ redevable effectue inéluctablement un clone furtif et local (une pure COPIE parfaite) de la variable d'origine afin de travailler de façon cloîtrée sans perturber l'original.
- [ ] C) La transmission unilatérale de l'adresse RAM du programme en 64 bits de la fonction originelle.
- [ ] D) Une faille d'injection mémoire.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Quand vous faites `fonction(x)`, `x` fait preuve d'un "Pass by Value". Les valeurs pures de $x$ se dupliquent temporairement et se font piéger pour les opérations dans la scope de la fonction hôte. L'original $x$ restera intact à son retour au `main()`.
</details>

### Question 2.8 : À quelle étape intervient formellement le principe philosophique crucial et de bon sens d'hygiène logicielle (SRP) « Single Responsibility Principle » lors de l'écriture d'une fonction C++ ?
- [ ] A) Lors du placement des espaces.
- [ ] B) Il gère les responsabilités des threads virtuels CPU.
- [ ] C) Quand Github commite l'édition des codes.
- [ ] D) Il impose pragmatiquement la sagesse que chaque sous-fonction codée de manière individuelle doit formellement adresser inéluctablement une « et d'une SEULE et unique pure Tâche de résolution » globale de votre projet.

<details>
<summary>💡 Solution</summary>

**Réponse D**. "Une Fonction = Une Tâche". On n'écrit pas de fonctions monolithiques immenses qui calculent l'âge du candidat, impriment le mot de passe, envoient l'email et nettoient les registres Windows. 
</details>

### Question 2.9 : Il existe une dualité fine en C++ entre les extractions via `getline(fic, line)` ou par l'opérateur flèche à base de chevrons formel `fic >> mot;`. La faille du chevron sur le fichier est que :
- [ ] A) Il divise toutes les chaines extraites par le quotient binaire absolu Zéro.
- [ ] B) L'opérateur de flux classique `>>` parse et avale des blocs, mais s'arrête devant un banal caractère Espace `" "`, là où `getline` englobe sans pitié toute la largeur de ligne jusqu'au `\n`.
- [ ] C) Il ne compile purement plus sur Windows 11.
- [ ] D) Il n'accepte qu'un maximum charnière formel strict de 8 mots (256 bits).

<details>
<summary>💡 Solution</summary>

**Réponse B**. L'opérateur classique s'arrête aux espacements. Si vous avez un fichier nommant `Jean Michel`, `fic >> prenom` récupèrera unitairement la partie pure `Jean`.
</details>

### Question 2.10 : Les modes flux `std::ios::app`, apposés formellement en conjonction avec un flux type `ofstream`, s'utilisent précisément dans de quel but ?
- [ ] A) Fabriquer au sein du terminal une pure "Apple Application" binaire.
- [ ] B) Imposer un filtre audio.
- [ ] C) Ajouter des informations textuelles à la **Toute Fin** du fichier physique sans procéder à l'anéantissement ("Overwrite") irrémédiable des données y figurant à l'origine absolue.  
- [ ] D) Analyser les virus.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le terme est le raccourci global du terme inéluctable anglophone : "Append" (ajouter au bout/à la queue).
</details>

### Question 2.11 : À quelle subtile manipulation de terminal sert la fonction formelle pure du `#include <iomanip>` appelé `setprecision(n)` en conjonction direct du flux standard `cout` ?
- [ ] A) Bloquer avec rigueur l'étalage intime et la pure quantité d'affichage total du "Nombre de Chiffres Significatifs" accordé (ou après une virgule `fixed`) pour retenir purement une donnée de type `double`.
- [ ] B) Calibrer la vitesse pure du rafraichissement écran en MHz stricts.
- [ ] C) De calculer avec des variables asymétriques inéluctables pures les conditions formelles asymètres.
- [ ] D) Réduire purement les erreurs d'arrondi de l'IEEE 754 de dans In.

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'IO Manipulator est l'assistant inéluctable du console out. `setprecision(3)` formelle impose au nombre le format $1.23$.
</details>

### Question 2.12 : Le marqueur spécial `std::string::npos` (retourné par `string.find("texte")`) signifie :
- [ ] A) Que la séquence textuelle n'a pas été trouvée (No Position).
- [ ] B) Que la chaîne a dépassé la limite de taille autorisée.
- [ ] C) Que la recherche s'est arrêtée au premier espace.
- [ ] D) Une erreur de pointeur nul.

<details>
<summary>💡 Solution</summary>

**Réponse A**. C'est le concept de "Non-Position". L'algorithme a ratissé l'ensemble de la string sans trouver la sous-chaîne. `npos` est la valeur maximale possible pour le type de taille.
</details>

### Question 2.13 : Concernant la console, que sont `cin` et `cout` ?
- [ ] A) Des mots-clés réservés pour la compilation.
- [ ] B) `cin` est une instance de `istream` (Flux d'Entrée) et `cout` est un `ostream` (Flux de Sortie).
- [ ] C) Des variables globales de type int.
- [ ] D) Des pointeurs vers des fichiers physiques.

<details>
<summary>💡 Solution</summary>

**Réponse B**. "i" pour Input, "o" pour Output. `cin` absorbe les entrées du clavier et `cout` propulse les sorties vers le terminal.
</details>

### Question 2.14 : Quel est l'intérêt principal de `std::ostringstream` ?
- [ ] A) Il permet de construire une chaîne formattée en mémoire sans l'afficher immédiatement à l'écran, agissant comme un tampon.
- [ ] B) Il convertit automatiquement du texte en binaire brut.
- [ ] C) Il chiffre les données avant leur envoi sur le réseau.
- [ ] D) Il crée une copie asynchrone du flux standard.

<details>
<summary>💡 Solution</summary>

**Réponse A**. `std::ostringstream` sert à "bâtir" des chaînes complexes en utilisant l'opérateur `<<` (comme on le ferait avec `cout`), puis on extrait le résultat final avec l'appel `.str()`.
</details>

### Question 2.15 : Côté architecture de l'application, en C++ une `struct`...
- [ ] A) Contient uniquement des fonctions.
- [ ] B) Alloue automatiquement ses attributs sur le Heap.
- [ ] C) Stocke physiquement ses variables attributs de façon contiguë (les unes à la suite des autres) en mémoire RAM.
- [ ] D) Ne peut contenir que des types de données primitifs.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Dans une structure, l'agencement mémoire garantit que toutes ses données sont rassemblées dans un bloc contigu direct.
</details>

---

## Cours 3 : Hiérarchie mémoire, Arrays avancés et Introduction à la POO

### Question 3.1 : Quelle est la hiérarchie classique des vitesses d'accès à la mémoire dans un ordinateur, du plus rapide au plus lent ?
- [ ] A) Cache L1, RAM, Registres, Disque Dur.
- [ ] B) Registres, Cache L1/L2/L3, RAM, Stockage (SSD/HDD).
- [ ] C) RAM, Cache L3, Registres, SSD.
- [ ] D) Registres, RAM, ROM, Disque Dur.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Les registres du processeur sont les plus rapides (< 1 ns), suivis par les différents niveaux de mémoire cache (1-20 ns), puis la RAM (~ 50-100 ns), et enfin le stockage persistant comme les SSD qui sont des milliers de fois plus lents.
</details>

### Question 3.2 : Quelle est la règle d'or en optimisation de performance concernant les accès aux données ?
- [ ] A) Privilégier systématiquement les accès disque (I/O) pour économiser la RAM.
- [ ] B) Utiliser des variables globales pour tout le programme.
- [ ] C) Minimiser les accès au disque dur (I/O) en chargeant unitairement de gros blocs en RAM.
- [ ] D) Ne jamais utiliser le cache L1.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Les opérations d'entrée/sortie (I/O) sur un disque sont un très gros goulot d'étranglement. Il faut privilégier le travail en mémoire vive (RAM) avec des structures de données contiguës (comme les tableaux/vectors).
</details>

### Question 3.3 : Quel est le principal danger des tableaux statiques natifs (built-in arrays) en C++ ?
- [ ] A) Ils sont très lents à allouer.
- [ ] B) Le C++ ne fait aucune vérification de dépassement de limite (Bounds Checking), ce qui peut causer des accès mémoire indéfinis (Segfault) ou de la corruption de données.
- [ ] C) Ils ne peuvent stocker que des entiers.
- [ ] D) Ils nécessitent une commande `delete[]` même s'ils sont déclarés sur la pile (Stack).

<details>
<summary>💡 Solution</summary>

**Réponse B**. Si vous déclarez `int tab[5];` et accédez à `tab[10]`, le C++ lira ou écrira la mémoire à cette adresse sans erreur de compilation, ce qui peut écraser d'autres variables et causer un crash brutal silencieux.
</details>

### Question 3.4 : Qu'est-ce qu'un pointeur en C++ ?
- [ ] A) Une variable qui contient le type d'une autre variable.
- [ ] B) Une fonction spéciale utilisée pour naviguer dans un tableau.
- [ ] C) Une variable qui contient l'**adresse mémoire** d'une autre variable (ou d'un objet).
- [ ] D) Une référence inaltérable.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Un pointeur pointe physiquement sur la case mémoire (l'adresse RAM) où se trouve la véritable donnée. Par exemple `int* p = &var;`.
</details>

### Question 3.5 : Quel opérateur est utilisé pour extraire la valeur pointée par un pointeur (déréférencement) ?
- [ ] A) `&` (Esperluette)
- [ ] B) `*` (Astérisque)
- [ ] C) `->` (Flèche)
- [ ] D) `.` (Point)

<details>
<summary>💡 Solution</summary>

**Réponse B**. L'opérateur `*` (`*p`) permet d'accéder à la valeur stockée à l'adresse pointée. L'opérateur `&` sert à obtenir l'adresse d'une variable.
</details>

### Question 3.6 : En C++, à quoi sert l'instruction `new` ?
- [ ] A) À instancier un nouvel espace de travail dans l'IDE.
- [ ] B) À vider la mémoire tampon.
- [ ] C) À allouer dynamiquement de la mémoire sur le Tas (Heap) pendant l'exécution du programme.
- [ ] D) À déclarer une variable locale constante sur la Pile (Stack).

<details>
<summary>💡 Solution</summary>

**Réponse C**. `new` sollicite le système d'exploitation pour réserver un bloc de mémoire dynamique sur le Heap et retourne un pointeur vers cette adresse mémoire.
</details>

### Question 3.7 : Quelle est la règle stricte concernant l'utilisation de `new` pour éviter les fuites de mémoire ?
- [ ] A) Tout appel à `new` doit être strictement couplé à un appel ultérieur à `delete` (ou `delete[]`) pour libérer la mémoire.
- [ ] B) Le compilateur gère automatiquement la destruction via le Garbage Collector virtuel.
- [ ] C) Il faut allouer avec `new` et libérer avec `free()`.
- [ ] D) `new` ne s'utilise que pour les tableaux, pas pour les objets seuls.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Sans `delete`, la mémoire reste allouée et verrouillée même si le pointeur est détruit, créant une "fuite de mémoire" (Memory Leak) qui remplit la RAM.
</details>

### Question 3.8 : Qu'est-ce qu'une Fuite de Mémoire (Memory Leak) ?
- [ ] A) Un dépassement d'indice dans un tableau causant une réécriture accidentelle.
- [ ] B) Une situation où de la mémoire allouée dynamiquement sur le Heap n'est jamais libérée, saturant peu à peu la RAM du système.
- [ ] C) Un plantage de l'ordinateur causé par un pointeur nul.
- [ ] D) Une faille de sécurité permettant d'injecter du code dans la Pile (Stack).

<details>
<summary>💡 Solution</summary>

**Réponse B**. En C++, l'oubli scrupuleux de l'opérateur `delete` amène la mémoire de l'OS à saturer, obligeant parfois l'utilisateur à forcer la fermeture de son logiciel.
</details>

### Question 3.9 : En Programmation Orientée Objet (POO), qu'est-ce qu'un Constructeur ?
- [ ] A) Une fonction qui détruit l'objet à la fin de son cycle de vie.
- [ ] B) Une méthode globale permettant d'afficher l'état de la classe.
- [ ] C) Une méthode spéciale, portant le même nom que la classe, appelée automatiquement lors de l'instanciation (création) de l'objet pour initialiser ses attributs.
- [ ] D) Un fichier header `.h` qui déclare les variables de l'objet.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Le constructeur sert à préparer l'objet (allocation de mémoire interne, valeurs par défaut des attributs, etc.) dès l'instant où il naît en mémoire.
</details>

### Question 3.10 : Quel est l'objectif du principe d'Encapsulation en POO ?
- [ ] A) Rendre tous les attributs publics pour faciliter l'accès depuis le `main()`.
- [ ] B) Cacher les données internes (attributs privés) et fournir des méthodes publiques (Getters/Setters) pour les lire ou les modifier de manière sécurisée et contrôlée.
- [ ] C) Mettre plusieurs classes dans le même fichier `.cpp`.
- [ ] D) Compresser les données en mémoire vive.

<details>
<summary>💡 Solution</summary>

**Réponse B**. L'encapsulation (Data Hiding) protège les états internes de l'objet afin de garantir sa cohérence et d'empêcher le programme extérieur de corrompre des variables cruciales.
</details>

### Question 3.11 : À l'intérieur d'une classe, que représente le pointeur `this` ?
- [ ] A) Un pointeur vers la classe mère (héritage).
- [ ] B) Une référence globale au fichier source appelant.
- [ ] C) Un pointeur invisible et natif de la classe, qui pointe vers l'adresse mémoire de **l'objet (l'instance) courant** sur lequel la méthode a été appelée.
- [ ] D) Un mot clé équivalent à `nullptr`.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Par exemple `this->name = name;` permet de lever l'ambiguïté entre l'attribut de membre de cet objet précis `name` et le paramètre local `name` entrant dans la fonction.
</details>

### Question 3.12 : Quel est le rôle principal d'un Destructeur (ex: `~MyClass()`) ?
- [ ] A) Forcer la suppression de tous les fichiers annexes du programme sur le disque dur.
- [ ] B) Il est appelé automatiquement juste avant la destruction de l'objet, son rôle majeur est d'effectuer un grand nettoyage, notamment en libérant (delete) la mémoire dynamique allouée par l'objet durant sa vie.
- [ ] C) Remettre à zéro toutes les variables primitives de la pile.
- [ ] D) Il n'a aucun rôle en C++, c'est un héritage du langage C.

<details>
<summary>💡 Solution</summary>

**Réponse B**. C'est le nettoyeur officiel de l'objet pour éviter ces fameuses Memory Leaks quand ce dernier disparait de sa portée (scope).
</details>

### Question 3.13 : Qu'est-ce qu'une Référence `&` en C++ comparativement à un banal Pointeur ?
- [ ] A) C'est exactement la même chose à l'octet près.
- [ ] B) Une référence est un alias, un "autre nom" pour une variable existante. Elle ne peut pas être nulle (`nullptr`), ne peut pas être réaffectée à pointer ailleurs, et s'utilise avec une syntaxe plus simple (sans devoir utiliser `*` ou `->`).
- [ ] C) Les références sont bien plus lentes et volumineuses que les pointeurs.
- [ ] D) Les références ne servent que pour des constantes.

<details>
<summary>💡 Solution</summary>

**Réponse B**. Sous le capot, c'est très similaire, mais structurellement et syntaxiquement l'alias symbolique d'une Référence amène beaucoup de sécurité et de clarté dans le code (notamment pour le passage de paramètres).
</details>

### Question 3.14 : Pourquoi le passage par "Référence Constante" (ex: `const std::string& str`) est-il très souvent utilisé en C++ ?
- [ ] A) Pour obliger le programmeur à écrire plus de code de sécurisation mémoire.
- [ ] B) Pour optimiser la base de données.
- [ ] C) Cela combine la Performance et la Sécurité : on évite une coûteuse copie de la variable géante (performance), tout en interdisant à la fonction de modifier l'original par erreur (sécurité grâce au mot clé const).
- [ ] D) Les passages de valeurs sont interdits, c'est l'unique alternative qui compile.

<details>
<summary>💡 Solution</summary>

**Réponse C**. Très très courant en C++. On passe une lourde `std::string` ou un lourd `Object` sans le dupliquer et pour uniquement le lire.
</details>

### Question 3.15 : Laquelle de ces affirmations concernant l'allocation de mémoire est fausse ?
- [ ] A) La Pile (Stack) offre de larges blocs de mémoire dynamique gérée soigneusement par l'utilisateur avec `new`.
- [ ] B) La Pile (Stack) est gérée automatiquement via la portée (scope) des variables dans les fonctions.
- [ ] C) Le Tas (Heap) permet de stocker des données massives dont la durée de vie persiste jusqu'à appel explicite de libération.
- [ ] D) Dépasser la taille allouée de la pile provoque un plantage appelé Stack Overflow.

<details>
<summary>💡 Solution</summary>

**Réponse A**. La Pile (Stack) fournit des blocs fixes, petits et extrèmement rapides pour des variables locales, pas pour le mode dynamique manuel. L'utilisateur se sert de `new` pour viser le vaste Heap (Tas) !
</details>
