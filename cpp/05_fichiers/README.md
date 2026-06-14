# Module 05 — Lire et écrire des FICHIERS avec `<fstream>`

Jusqu'ici, tes programmes affichaient des choses à l'écran avec `std::cout` et lisaient
au clavier avec `std::cin`. Mais dès qu'ils s'arrêtaient, **tout était oublié**. Pour
**garder** des informations (un score, une liste de notes, un texte…), il faut les
**écrire dans un fichier** sur le disque. Et plus tard, on peut **relire** ce fichier.
C'est exactement ce que fait le module 05.

> Fichiers du module : `ecrire.cpp` (écrit quelques lignes dans un fichier) et `lire.cpp`
> (relit ce fichier et l'affiche ligne par ligne). Lance d'abord `ecrire`, puis `lire`.

---

## 1. L'analogie : un flux, c'est un tuyau

En C++, on parle de **flux** (*stream* en anglais). Imagine un **tuyau** par lequel
circulent des données.

- Tu connais déjà `std::cout` : un tuyau qui envoie du texte **vers l'écran**.
- Tu connais déjà `std::cin` : un tuyau qui amène du texte **depuis le clavier**.

Pour les fichiers, c'est **pareil**, sauf que le tuyau est branché sur un fichier :

- `std::ofstream` = **o**utput **f**ile **stream** = un tuyau qui envoie du texte **vers un
  fichier** (pour **écrire**). On s'en sert avec `<<`, **exactement comme `std::cout`**.
- `std::ifstream` = **i**nput **f**ile **stream** = un tuyau qui amène du texte **depuis un
  fichier** (pour **lire**).

Le `f` au milieu veut dire **file** (fichier). Tout vient de la boîte à outils
`#include <fstream>`.

```
   ÉCRIRE :   ton programme  ──[ std::ofstream  << ]──►  fichier sur le disque
   LIRE   :   fichier        ──[ std::ifstream  >> ]──►  ton programme
```

---

## 2. ÉCRIRE dans un fichier : `std::ofstream`

On crée un flux de sortie en lui donnant le **nom du fichier**. S'il n'existe pas, il est
**créé** ; s'il existe déjà, son contenu est **remplacé**.

```cpp
std::ofstream fichier("exemples/notes.txt");   // ouvre (ou crée) le fichier
fichier << "Bonjour !" << std::endl;           // on écrit avec <<, comme std::cout
fichier << "Deuxième ligne" << std::endl;
```

C'est tout : `<<` envoie le texte dans le tuyau, qui le dépose dans le fichier.

---

## 3. LIRE un fichier ligne par ligne : `std::ifstream` + `std::getline`

On crée un flux d'entrée avec le nom du fichier, puis on lit **ligne par ligne** avec
`std::getline`. C'est la façon la plus simple et la plus sûre de tout lire :

```cpp
std::ifstream fichier("exemples/notes.txt");
std::string ligne;
while (std::getline(fichier, ligne)) {   // lit une ligne ; s'arrête à la fin du fichier
    std::cout << ligne << std::endl;     // affiche la ligne lue
}
```

`std::getline(fichier, ligne)` met la prochaine ligne du fichier dans la variable
`ligne`. Quand il n'y a plus rien à lire, la condition du `while` devient **fausse** et
la boucle s'arrête toute seule.

---

## 4. Toujours vérifier : `.is_open()`

Et si le fichier **n'existe pas** (mauvais nom, mauvais dossier…) ? Le flux ne réussit pas
à l'ouvrir. On le **vérifie** avec `.is_open()`, qui répond `true` (ouvert) ou `false` :

```cpp
std::ifstream fichier("exemples/notes.txt");
if (!fichier.is_open()) {                       // le « ! » veut dire « PAS ouvert »
    std::cout << "Impossible d'ouvrir le fichier." << std::endl;
    return 1;                                    // on s'arrête proprement
}
```

C'est le réflexe de prudence : on **vérifie avant d'utiliser**.

---

## 5. Le fichier se referme TOUT SEUL (RAII)

En C, après avoir fini, il fallait penser à **fermer** le fichier soi-même
(`fclose(...)`). Si on oubliait, c'était une fuite.

En C++, c'est **automatique** : quand la variable flux (`fichier`) **disparaît** — par
exemple à la fin de la fonction `main`, quand on sort de ses accolades `{ }` — le fichier
est **fermé pour toi**. Ce mécanisme s'appelle le **RAII**.

> 💡 Analogie : c'est comme une porte à fermeture automatique. Tu entres, tu fais ce que
> tu as à faire, et la porte se referme seule derrière toi quand tu sors de la pièce. Pas
> besoin d'y penser.

---

## 6. 🆚 En C, c'était plus pénible

| | C | C++ |
|--|---|-----|
| Ouvrir pour écrire | `FILE* f = fopen("x.txt", "w");` | `std::ofstream f("x.txt");` |
| Écrire | `fprintf(f, "Age : %d\n", age);` | `f << "Age : " << age << std::endl;` |
| Lire une ligne | `fgets(buffer, 100, f);` (taille fixe à gérer) | `std::getline(f, ligne);` |
| Fermer | `fclose(f);` (à ne pas oublier !) | **automatique** (RAII) |

En C++, on écrit avec `<<` comme avec `std::cout`, on lit avec `std::getline` dans une
`std::string` qui s'agrandit toute seule, et on **n'oublie jamais de fermer** : c'est fait
pour nous.

---

## 7. ⚠️ Où le fichier est-il créé ? (anti-pollution)

Pour ne pas éparpiller des fichiers partout, ces programmes rangent leur fichier dans un
**sous-dossier `exemples/`** (chemin `exemples/notes.txt`). Le dossier est créé
automatiquement par `ecrire.cpp` grâce à :

```cpp
#include <filesystem>
std::filesystem::create_directories("exemples");   // crée le dossier s'il manque
```

> ⚠️ **Lance les programmes DEPUIS LA RACINE du dépôt** (le dossier qui contient `cpp/`).
> Le dossier `exemples/` sera donc créé à la racine. Il est **ignoré par git** : c'est du
> contenu jetable, tu peux le supprimer quand tu veux.

`std::filesystem` demande la version **C++17** du langage : c'est pourquoi on ajoute le
drapeau **`-std=c++17`** à la compilation (voir ci-dessous).

---

## ▶️ À toi de jouer

Depuis la **racine du dépôt** (le dossier qui contient `cpp/`) :

```bash
# 1. Écrire le fichier (crée le dossier exemples/ et exemples/notes.txt)
g++ -Wall -std=c++17 cpp/05_fichiers/ecrire.cpp -o ecrire && ./ecrire

# 2. Lire et afficher ce qu'on vient d'écrire
g++ -Wall -std=c++17 cpp/05_fichiers/lire.cpp -o lire && ./lire
```

> Le `-std=c++17` est nécessaire pour `std::filesystem` (création du dossier `exemples/`).

Ensuite, **modifie** les fichiers : ajoute des lignes dans `ecrire.cpp`, ou fais lire à
`lire.cpp` un fichier qui n'existe pas (change le nom) pour voir le message d'erreur de
`.is_open()` s'afficher.

➡️ La suite du parcours arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
