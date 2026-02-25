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

### Question 2.12 : Le marqueur spécial et flagrant `std::string::npos` (notamment retourné par la recherche `string.find("texte")`) signifie intrinsèquement :
- [ ] A) Que la sémantique de la séquence textuelle que l'on recherche bêtement n'a " Pas Été Trouvée " (No Position).
- [ ] B) the in THE
- [ ] C) Un pur dépassement asymptotique.
- [ ] D) Qu'il y a eu The bête au

<details>
<summary>💡 Solution</summary>

**Réponse A**. C'est le concept de "Non-Position". L'algorithme a ratissé l'ensemble de la string sans l'apercevoir.
</details>

### Question 2.13 : Du coté de la Console, `cin` et `cout` ...
- [ ] A) Bêtes The 
- [ ] B) `cin` est une instance de `istream` (Flux D'Entrée). `cout` est un `ostream` (Flux De Sortie).
- [ ] C) la from
- [ ] D) in THE Asymètre

<details>
<summary>💡 Solution</summary>

**Réponse B**. i pour Input, o pour Output. `cin` absorbe les entrées du flux et `cout` propulse les sorties au terminal.
</details>

### Question 2.14 : Le `ostringstream` ...
- [ ] A) C'est une technique magique qui permet de " CONSTRUIRE " en concaténant des données variées à l'intérieur d'une string formatée sans même afficher à la console.
- [ ] B) In au Bêtes 
- [ ] C) asymètre from the 
- [ ] D) from The In

<details>
<summary>💡 Solution</summary>

**Réponse A**. `std::ostringstream` is building strings. Cela évite le grand fatras de `+` ou les formattages complexes à la C-style, tout en bénéficiant de `.str()` à la fin pour récupérer la chaîne globale.
</details>

### Question 2.15 : Côté Architecture de l'application, en C++ la `struct` ...
- [ ] A) The 
- [ ] B) in The 
- [ ] C) stocke THE ses variables de `Façon CONTIGUË` en " Mémoire " (RAM).
- [ ] D) The from

<details>
<summary>💡 Solution</summary>

**Réponse C**. La structure garantit que tous les champs variables alloués qu'elle porte existent en bloc direct contigu l'un après l'autre à son adresse physique pure RAM.
</details>

---

## Cours 3 : Hiérarchie mémoire, Arrays avancés et Introduction à la POO

### Question 3.1 : Quelle est la hiérarchie des vitesses d'accès typique de la mémoire ?
- [ ] A) bête
- [ ] B) " **Registres** " (< 1 ns), puis " **Cache L1/L2/L3** " (1-20 ns), then " **RAM** " (~ 50 ns), then " **Storage SSD** " (> 10 000ns).
- [ ] C) la The In
- [ ] D) the The

<details>
<summary>💡 Solution</summary>

**Réponse B**. La pyramide hiérarchique memory memory.
</details>

### Question 3.2 : Quelle est la "Règle d'Or en optimisation" face à l'arbre BMD ?
- [ ] A) " **Eviter Les Accès Disque (I/O) au profit de la RAM.** " Charger les data une seule fois en RAM Array (1000x plus rapide !).
- [ ] B) IN THE
- [ ] C) Bêtes 
- [ ] D) au

<details>
<summary>💡 Solution</summary>

**Réponse A**. L'IO (Entrée et Sorties asymétriques sur le disque) constituent un inévitable goulot d'étranglement fatal. Un vecteur en mémoire sera exploré massivement plus vite.
</details>

### Question 3.3 : Quel est le danger majeur de l'Array en natif C++ ?
- [ ] A) Bêtes In
- [ ] B) The 
- [ ] C) " Le C++ n'effectue JAMAIS la moindre Vérification des limites (Bounds Checking). " L'Accès à un index qui est au-delà provoque un **comportement indéfini** (le pur `Segfault` ou de Memory Corruption ).
- [ ] D) asymètre

<details>
<summary>💡 Solution</summary>

**Réponse C**. "No bounds Checking in C++". L'accès à une case pure hors taille lira la mémoire suivante de la machine non affiliée sans prévenir.
</details>

### Question 3.4 : Qu'est-ce qu'un pointer ?
- [ ] A) from asymétrique
- [ ] B) " **Une Variable qui contient une Adresse Mémoire** " au lieu d'une bête valeur primitive.
- [ ] C) la THE Bêtes
- [ ] D) Inbête from

<details>
<summary>💡 Solution</summary>

**Réponse B**. Un pointeur pointe sur la localisation unique (l'adresse absolue RAM) là où le programme ou le SE stocke physiquement la pure data.
</details>

### Question 3.5 : the In The IN The of `Dereference` The 
- [ ] A) L'Opérateur de *Déréférencement* `*` Returns The VALUE pointed asymètre in The.
- [ ] B) In The From
- [ ] C) in the from
- [ ] D) of THE from Inéluctablement Asymètre IN Bêtes

<details>
<summary>💡 Solution</summary>

**Réponse A**. *p = Value. En utilisant l'astérisque de déréférence (sur le pointeur mémoire pur the p), vous pouvez subtilement extraire sa valeur hébergée.
</details>

### Question 3.6 : THE `new` permet...
- [ ] A) IN 
- [ ] B) of The
- [ ] C) L'Instruction `new` permet de **ALLOUER DYNAMIQUEMENT** la Mémoire dans the the Heap (Le tas).
- [ ] D) Asymétriquement IN in THE The Bêtes

<details>
<summary>💡 Solution</summary>

**Réponse C**. Allocation du Heap dynamique pure in Memory C++ the $new$.
</details>

### Question 3.7 : THE from Of the Asymétriquement THE of the In Bêtes
- [ ] A) " **Chaque Appel à `new` Doit inéluctablement Avoir SON `delete` correspondant** " (Pour in the Free la Memory the).
- [ ] B) The in THE From
- [ ] C) IN 
- [ ] D) Asymètre the

<details>
<summary>💡 Solution</summary>

**Réponse A**. The $new\dots{}delete$ The The $new[]\dots{}delete[]$. Bêtes The In IN from Memory from
</details>

### Question 3.8 : Qu'est ce qu'un `Memory Leak` ?
- [ ] A) Une "Fuite de Mémoire" the arrive quand le PROGRAM THE oublie the in `Free (delete)` la Memory in the. La RAM sature.
- [ ] B) The In Bêtes the 
- [ ] C) THE from
- [ ] D) of Asymètre IN

<details>
<summary>💡 Solution</summary>

**Réponse A**. In C++ $leak$ = asymètre In no The $delete$. 
</details>

### Question 3.9 : Le Constructor in The OOP
- [ ] A) Bêtes In asymètre
- [ ] B) " le `Constructor` " is The Function in The that is " **Called Automatically at Object's Creation (Instantiation ) To Initialize the State (Data)** ".
- [ ] C) la THE
- [ ] D) bête the

<details>
<summary>💡 Solution</summary>

**Réponse B**. IN constructor from The Object.
</details>

### Question 3.10 : Bêtes in `Encapsulation` ...
- [ ] A) Bêtes 
- [ ] B) Of The
- [ ] C) L'`Encapsulation` in OOP is " **Data The Hiding** " = (`Private Attributes` The = Data , In `Public Methods (Getters/Setters )` = the Access).
- [ ] D) THE In

<details>
<summary>💡 Solution</summary>

**Réponse C**. IN asymètre from Encap = Data hiding the In (Private attributes).
</details>

### Question 3.11 : Le `this` pointer ...
- [ ] A) Le " `this` pointer " in The is The " Pointer to the In Current `OBJECT` " the asymétriquement the it is acting on.
- [ ] B) bête 
- [ ] C) la
- [ ] D) the

<details>
<summary>💡 Solution</summary>

**Réponse A**. $this$ pointer = The object In the asymètre Address. 
</details>

### Question 3.12 : Le `Destructor` from The Asymètre 
- [ ] A) The `Destructors (\~Classname)` the are " `Called Automatically` " when an `Object Is Destroyed` to Cleanup The any Memory au the In The allocated. 
- [ ] B) In 
- [ ] C) in The
- [ ] D) l'

<details>
<summary>💡 Solution</summary>

**Réponse A**. "called on The In Memory bêtes From The destroy. The $~$.
</details>

### Question 3.13 : `Reference` the in C++
- [ ] A) The 
- [ ] B) `References` `&` The la create `an Alias` (another Name for the same Variable). It allows " `Pass By Reference` ". This avoids copying and permits modification of the original.
- [ ] C) from
- [ ] D) the

<details>
<summary>💡 Solution</summary>

**Réponse B**. THE the Pass By Reference (no The In copy ). Modify original. 
</details>

### Question 3.14 : `Pass by Const Reference`
- [ ] A) `const Type&` `Combines The Performance` The with `Safety`. it `avoids copy` The (Fast ) and `prevents modifying` the (Safe). au
- [ ] B) of 
- [ ] C) in THE
- [ ] D) The

<details>
<summary>💡 Solution</summary>

**Réponse A**. the The const Reference $\implies$ Fast (No Copy ) and Safe In (Const In). The
</details>

### Question 3.15 : Which of these is WRONG regarding memory areas?
- [ ] A) The Stack provides large, dynamic memory blocks managed carefully by the user using 'new'.
- [ ] B) The Stack is automatically managed via the scope of variables inside functions.
- [ ] C) The Heap allows for massive memory capacity for the lifetime of the program until explicitly freed.
- [ ] D) Accessing memory via references generally uses standard pointer logic underneath for abstraction without syntax clutter.

<details>
<summary>💡 Solution</summary>

**Réponse A**. Stack memory provides small, statically managed, extremely fast memory buffers. The user uses the 'new' tool onto the mighty Heap area instead !
</details>
