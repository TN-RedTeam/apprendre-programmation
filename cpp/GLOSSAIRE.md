# 📖 Glossaire — les mots du C++ expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours ? Cherche-le ici. Les termes
sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**Compilation** — L'étape qui **traduit** ton fichier `.cpp` (lisible par les humains) en
un **exécutable** (langage machine) que l'ordinateur peut lancer. On la déclenche avec le
compilateur `g++`. Tant qu'il y a une erreur, le programme ne se construit pas.

**Compilateur** — Le programme qui fait la compilation. Ici on utilise **`g++`**.

**Conteneur** — Un outil de la bibliothèque standard qui **range plusieurs valeurs**
ensemble. `std::vector` (une liste) et `std::string` (une suite de caractères) sont des
conteneurs. Comme une boîte de rangement avec des cases.

**Exécutable** — Le fichier produit par la compilation, que l'ordinateur peut lancer
directement (ex : `./mon_prog`). C'est le résultat « machine » de ton code.

**Fonction** — Un bloc de code nommé et réutilisable. On la *définit* avec son type de
retour (`int additionner(int a, int b) { ... }`), on l'*appelle* par son nom. Comme une
recette qu'on peut refaire à volonté.

**`#include <iostream>`** — Une ligne en haut du fichier qui **ouvre une boîte à outils**
(ici `iostream`, pour les entrées/sorties). Sans elle, `std::cout` et `std::cin` sont
inconnus. `#include <string>` ouvre les textes, `#include <vector>` ouvre les listes.

**main** — La fonction de **départ** : quand on lance le programme, l'exécution commence
par `int main()`. Elle finit par `return 0;` (0 = tout s'est bien passé).

**namespace** (espace de noms) — Un « tiroir » qui regroupe des outils sous un nom commun
pour éviter les confusions. La bibliothèque standard vit dans le tiroir **`std`**, d'où le
`std::` devant `cout`, `string`, `vector`… (`::` veut dire « va chercher dedans »).

**range-based for** (boucle « pour chaque ») — Une boucle très lisible qui parcourt **tous
les éléments** d'un conteneur, un par un : `for (int n : notes) { ... }` se lit « pour
chaque `n` dans `notes` ». C'est l'équivalent du `for x in liste:` de Python.

**Référence** (`&`) — Un **surnom** qui désigne directement une variable existante, sans la
recopier. Écrire `for (const std::string& s : v)` évite de copier chaque texte à chaque
tour. Notion vue plus en détail plus tard ; pour des nombres simples, on peut s'en passer.

**STL** (*Standard Template Library*) — La grande **bibliothèque standard** du C++ : une
collection d'outils tout prêts (conteneurs comme `std::vector`, algorithmes, `std::string`…).
Plutôt que tout réécrire, on réutilise ces briques fiables.

**`std::`** — Le préfixe qui signifie « cet outil vient du namespace `std` » (la bibliothèque
standard). On le garde **explicite** dans ce parcours (`std::cout`, `std::string`) : c'est
plus clair pour débuter que de cacher le `std::` avec `using namespace std;`.

**`std::cin`** — L'entrée standard : **lit** ce que l'utilisateur tape au clavier, avec
l'opérateur `>>` (`std::cin >> age;`). Équivaut au `input()` de Python.

**`std::cout`** — La sortie standard : **affiche** du texte à l'écran, avec l'opérateur `<<`
(`std::cout << "Bonjour" << std::endl;`). Équivaut au `print()` de Python.

**`std::string`** — Le vrai type **texte** du C++ : une suite de caractères (`"bonjour"`).
On peut le coller avec `+`, mesurer sa longueur avec `.size()`, en extraire un morceau avec
`.substr()`. Bien plus pratique que les tableaux de `char` du C. Nécessite `#include <string>`.

**`std::vector`** — Un **tableau dynamique** : une liste ordonnée de valeurs du même type
qui **grandit toute seule** (avec `.push_back()`). Contrairement au tableau brut du C (taille
fixe), il s'adapte et connaît sa taille (`.size()`). Nécessite `#include <vector>`.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi
[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe.
