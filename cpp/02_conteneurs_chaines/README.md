# Module 02 — Conteneurs & chaînes : `std::string` et `std::vector`

Jusqu'ici, une variable rangeait **une seule** valeur (`int age = 30;`). Mais souvent on
veut manipuler **du texte entier** (une phrase, un nom) ou **une collection de valeurs**
(une liste de notes, de prénoms…). Le C++ propose deux outils tout prêts pour ça :
**`std::string`** (le texte) et **`std::vector`** (la liste qui grandit).

> Fichiers du module : `chaines.cpp` (manipuler du texte) et `vecteurs.cpp` (une liste de
> nombres). Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. `std::string` : un vrai type de texte

Tu l'as déjà croisé au module 01 pour stocker un mot. Mais un `std::string` sait faire
**bien plus** que retenir du texte : on peut le **coller**, mesurer sa **longueur**, en
extraire un **morceau**, le parcourir **caractère par caractère**.

Pour l'utiliser, on ajoute en haut du fichier :

```cpp
#include <string>
```

### Concaténer (coller) avec `+`

L'opérateur `+` **assemble** deux textes bout à bout :

```cpp
std::string prenom = "Ada";
std::string nom    = "Lovelace";
std::string complet = prenom + " " + nom;   // "Ada Lovelace"
```

> 🆚 En C, coller deux textes était pénible (`strcat`, gestion de la mémoire…). En C++,
> un simple `+` suffit.

### Connaître la longueur avec `.size()`

```cpp
std::string mot = "Bonjour";
std::cout << mot.size() << std::endl;   // 7 (le nombre de caractères)
```

> `.size()` se lit « la taille de `mot` ». Le `.` veut dire « demande à cet objet… ».
> `.length()` fait exactement la même chose.

### Extraire un morceau avec `.substr()`

`.substr(début, combien)` renvoie une **sous-chaîne** : on part de la position `début`
(⚠️ on compte **à partir de 0**) et on prend `combien` caractères.

```cpp
std::string mot = "Bonjour";
std::cout << mot.substr(0, 3) << std::endl;   // "Bon" (3 lettres depuis la position 0)
std::cout << mot.substr(3)    << std::endl;   // "jour" (de la position 3 jusqu'à la fin)
```

### Accéder à un caractère et parcourir le texte

Comme une liste, chaque caractère a une **position** (un *index*) commençant à `0`. On y
accède avec `[ ]` :

```cpp
std::string mot = "Bonjour";
std::cout << mot[0] << std::endl;   // 'B' (le premier caractère)
```

Pour parcourir **tous** les caractères, on peut utiliser une boucle `for` classique avec
`.size()`, ou la boucle « range-based for » (voir plus bas) :

```cpp
for (char c : mot) {              // "pour chaque caractère c de mot"
    std::cout << c << "-";        // B-o-n-j-o-u-r-
}
```

---

## 2. `std::vector` : un tableau qui grandit tout seul

Un **`std::vector`** est une **liste ordonnée** de valeurs du **même type** (comme la
`list` de Python). C'est l'équivalent moderne du tableau, en bien plus pratique.

Pour l'utiliser, on ajoute en haut du fichier :

```cpp
#include <vector>
```

On déclare un vector en précisant **le type des éléments** qu'il contiendra, entre
chevrons `< >` :

```cpp
std::vector<int> notes;          // une liste (vide) de nombres entiers
std::vector<std::string> noms;   // une liste de textes
```

### `.push_back()` : ajouter un élément à la fin

```cpp
std::vector<int> notes;
notes.push_back(12);   // notes contient maintenant : [12]
notes.push_back(15);   // [12, 15]
notes.push_back(9);    // [12, 15, 9]
```

> `.push_back(x)` se lit « pousse `x` à la fin ». C'est l'équivalent du `.append()` de Python.

### `.size()` : combien d'éléments ?

```cpp
std::cout << notes.size() << std::endl;   // 3
```

### Accès par index avec `[ ]`

Chaque élément a une **position** commençant à `0` :

```cpp
std::cout << notes[0] << std::endl;   // 12 (le premier)
std::cout << notes[2] << std::endl;   // 9  (le troisième)
```

### Parcourir avec la boucle « range-based for »

Pour visiter **chaque** élément, le C++ offre une boucle très lisible, la **range-based
for** (« for sur une plage de valeurs ») :

```cpp
for (int note : notes) {              // "pour chaque note dans notes"
    std::cout << note << std::endl;   // affiche chaque élément à tour de rôle
}
```

Ça se lit presque comme du français : **« pour chaque `note` parmi `notes` »**. C'est
l'équivalent direct du `for fruit in liste:` de Python. À chaque tour, la variable `note`
prend la valeur de l'élément suivant.

> 💡 La forme `for (int note : notes)` recopie chaque élément dans `note`. Pour les types
> volumineux on écrira plus tard `for (const std::string& s : v)` (avec `&`, une
> *référence*) pour éviter la copie — voir le **glossaire**. Pour des `int`, la copie est
> sans importance.

---

## 3. 🆚 La grande différence avec les tableaux bruts du C

En C (et en C++ « bas niveau »), on a aussi les **tableaux bruts** :

```c
int notes[3];   // un tableau de 3 entiers... et c'est figé : TOUJOURS 3, pas un de plus.
```

Le problème : sa **taille est fixée** à la création. Si tu veux ajouter une 4ᵉ note, tu
ne peux pas — il faut tout recommencer avec un tableau plus grand. Le tableau ne connaît
même pas sa propre taille.

Le **`std::vector` règle tout ça** :

| | Tableau brut du C (`int t[3]`) | `std::vector<int>` |
|--|--------------------------------|--------------------|
| Taille | **fixe**, choisie à la création | **dynamique** : grandit tout seul |
| Ajouter un élément | impossible (taille figée) | `.push_back(x)` |
| Connaître sa taille | non (à toi de la retenir) | `.size()` |
| Sécurité | aucune vérification | méthodes plus sûres |

➡️ **Règle simple pour débuter : utilise `std::vector`.** Il grandit quand tu en as
besoin et se souvient de sa taille. On garde les tableaux bruts pour plus tard.

---

## ▶️ À toi de jouer

```bash
# Manipuler du texte (std::string)
g++ -Wall cpp/02_conteneurs_chaines/chaines.cpp -o chaines && ./chaines

# Une liste de nombres (std::vector) : somme et moyenne
g++ -Wall cpp/02_conteneurs_chaines/vecteurs.cpp -o vecteurs && ./vecteurs
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : ajoute des éléments au
vector, change le texte, calcule un maximum…

➡️ La suite du parcours (objets & classes, fichiers…) arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
