# Module 06 — La STL : `std::map`, `std::set` et les algorithmes

Depuis le module 02, tu connais déjà `std::vector` (une liste qui grandit toute seule).
Eh bien `std::vector` fait partie d'une grande famille : la **STL**. Dans ce module, on
découvre deux nouveaux conteneurs très utiles (`std::map` et `std::set`) et des
**algorithmes** tout prêts pour trier et chercher (`std::sort`, `std::find`).

> Fichiers du module : `map_set.cpp` (un annuaire `nom -> âge` avec `std::map`, et une
> déduplication avec `std::set`) et `algorithmes.cpp` (trier un `std::vector` avec
> `std::sort`, puis y chercher avec `std::find`). Lis le README, puis compile et lance.

---

## 1. C'est quoi la STL ? Une grande boîte à outils

**STL** veut dire **S**tandard **T**emplate **L**ibrary : la **bibliothèque standard de
modèles**. C'est une **énorme boîte à outils** livrée *avec* le C++, remplie de pièces
prêtes à l'emploi. Tu n'as **rien à réécrire** : tu prends l'outil et tu t'en sers.

Cette boîte contient surtout deux choses :

- des **conteneurs** : des « boîtes » pour ranger plusieurs valeurs. Tu connais déjà
  `std::vector`. On ajoute aujourd'hui `std::map` et `std::set`.
- des **algorithmes** : des actions toutes faites à appliquer sur ces boîtes, comme
  **trier** (`std::sort`) ou **chercher** (`std::find`).

> 💡 Analogie : la STL, c'est la caisse à outils du bricoleur. Le `std::vector`, le
> `std::map`, le `std::set` sont des **rangements** (tiroirs, casiers…). `std::sort` et
> `std::find` sont des **outils** (une perceuse, un mètre…) qu'on applique au rangement.

---

## 2. `std::map` : un dictionnaire clé → valeur (comme un annuaire)

Un `std::map` associe une **clé** à une **valeur**. Comme un **annuaire** : tu cherches un
**nom** (la clé) et tu obtiens un **numéro** (la valeur). Ici, on fera un annuaire
`nom -> âge`.

```cpp
#include <map>
std::map<std::string, int> ages;   // clé = std::string (nom), valeur = int (âge)
ages["Alice"] = 30;                 // on range : la clé "Alice" vaut 30
ages["Bob"]   = 25;
std::cout << ages["Alice"];         // on relit avec la clé -> affiche 30
```

Entre les `< >` on écrit **deux types** : d'abord le type de la **clé**, puis le type de la
**valeur**. On range et on relit avec les **crochets `[ ]`** en donnant la clé.

> 💬 C'est **exactement** l'idée du `dict` de Python : `ages = {"Alice": 30}` puis
> `ages["Alice"]`. La seule différence : en C++ on précise les types entre `< >`.

---

## 3. `std::set` : un ensemble SANS doublons

Un `std::set` est une **collection sans doublons** : si tu ajoutes deux fois la même
valeur, elle n'est rangée **qu'une seule fois**. Parfait pour **dédupliquer** une liste.

```cpp
#include <set>
std::set<std::string> fruits;
fruits.insert("pomme");
fruits.insert("poire");
fruits.insert("pomme");   // déjà présent : IGNORÉ, pas de doublon
// fruits contient : pomme, poire  (2 éléments, pas 3)
```

On ajoute un élément avec `.insert(...)`. Bonus : un `std::set` garde ses éléments
**triés** automatiquement.

> 💬 C'est le `set` de Python : `fruits = set()` puis `fruits.add("pomme")`. Même idée,
> mêmes super-pouvoirs (pas de doublon).

---

## 4. Parcourir un conteneur : la boucle range-for

Pour parcourir n'importe quel conteneur de la STL, on utilise la **boucle range-for** (vue
au module 02). Elle se lit « **pour chaque** élément **dans** le conteneur ».

```cpp
for (const std::string& fruit : fruits) {     // pour chaque fruit dans l'ensemble
    std::cout << fruit << std::endl;
}
```

Pour un `std::map`, chaque élément est une **paire** clé/valeur. On y accède avec `.first`
(la clé) et `.second` (la valeur). En C++17, on peut « déballer » la paire d'un coup :

```cpp
for (const auto& [nom, age] : ages) {         // nom = la clé, age = la valeur
    std::cout << nom << " a " << age << " ans" << std::endl;
}
```

> 💬 `const auto& [nom, age]` ressemble au `for nom, age in ages.items():` de Python.
> Le `auto` veut dire « devine le type tout seul ».

---

## 5. Les algorithmes de `<algorithm>` : `std::sort` et `std::find`

Les **algorithmes** sont des actions toutes faites. On les trouve dans la boîte
`#include <algorithm>`. Ils travaillent presque toujours sur une **plage** d'éléments
décrite par deux repères : `begin()` (le **début**) et `end()` (**après** le dernier).

> 💬 Ces deux repères s'appellent des **itérateurs** : pense à un **doigt** qui pointe un
> élément. `begin()` = le doigt sur le premier élément ; `end()` = le doigt juste **après**
> le dernier (une sentinelle qui veut dire « c'est fini »). Tu n'as pas besoin de les
> manipuler à la main ici : tu donnes juste `v.begin()` et `v.end()` aux algorithmes.

### Trier : `std::sort`

```cpp
std::vector<int> v = {5, 2, 8, 1};
std::sort(v.begin(), v.end());   // range v du plus petit au plus grand : 1, 2, 5, 8
```

### Chercher : `std::find`

```cpp
auto it = std::find(v.begin(), v.end(), 8);   // cherche la valeur 8
if (it != v.end()) {                           // trouvé si on n'est PAS arrivé à la fin
    std::cout << "Trouve !" << std::endl;
}
```

`std::find` renvoie un **itérateur** (un doigt) sur l'élément trouvé. S'il n'a **rien
trouvé**, il renvoie `end()` : c'est pour ça qu'on compare avec `!= v.end()` pour savoir si
la recherche a réussi.

> 💬 En Python tu écrirais `v.sort()` et `if 8 in v:`. En C++, c'est un peu plus explicite
> (on donne `begin()`/`end()`), mais l'idée est la même.

---

## 6. 🆚 Récapitulatif Python ↔ C++

| Tu veux… | Python | C++ (STL) |
|----------|--------|-----------|
| Un dictionnaire | `d = {}` ; `d["a"] = 1` | `std::map<std::string,int> d;` ; `d["a"] = 1;` |
| Un ensemble | `s = set()` ; `s.add(x)` | `std::set<int> s;` ; `s.insert(x);` |
| Trier une liste | `v.sort()` | `std::sort(v.begin(), v.end());` |
| Chercher | `if x in v:` | `std::find(v.begin(), v.end(), x) != v.end()` |
| Parcourir | `for x in v:` | `for (auto& x : v)` |

---

## ▶️ À toi de jouer

Depuis la **racine du dépôt** (le dossier qui contient `cpp/`) :

```bash
# 1. map + set : un annuaire et une déduplication
g++ -std=c++17 -Wall cpp/06_stl/map_set.cpp -o map_set && ./map_set

# 2. algorithmes : trier puis chercher dans un std::vector
g++ -std=c++17 -Wall cpp/06_stl/algorithmes.cpp -o algorithmes && ./algorithmes
```

> Le `-std=c++17` active la version moderne du langage (utile, entre autres, pour le
> « déballage » `auto& [nom, age]` du `std::map`).

Ensuite, **modifie** : ajoute des gens dans l'annuaire, mets des doublons dans le `set`
pour voir qu'ils disparaissent, ou change la valeur cherchée par `std::find` pour une qui
n'existe pas et observe le message « pas trouvé ».

➡️ La suite du parcours arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
