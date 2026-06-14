# Module 09 (avancé) — Les SMART POINTERS & le RAII : la mémoire en toute sécurité

Souviens-toi du module 04 : pour fabriquer un objet via un pointeur, on écrivait `new`, et
on devait penser à écrire `delete` plus tard pour **libérer** la mémoire. Ça marche… tant
qu'on n'oublie **jamais** le `delete`. Et là est le piège : dès qu'un programme grandit,
oublier un `delete` devient très facile — et chaque oubli laisse de la mémoire occupée
**pour rien**.

Les **smart pointers** (« pointeurs intelligents ») règlent ce problème une fois pour
toutes : ils **libèrent la mémoire automatiquement** pour toi. Plus de `delete` à ne pas
oublier. C'est la façon **moderne** et **sûre** de gérer la mémoire en C++.

> Fichiers du module : `unique_ptr.cpp` (un objet avec **un seul propriétaire**, libéré
> tout seul) et `shared_ptr.cpp` (un objet **partagé** entre plusieurs pointeurs, libéré
> seulement quand le dernier disparaît). Lis ce README, puis compile et lance (voir en bas).

---

## 1. Le PROBLÈME : `new`/`delete` à la main, c'est risqué

Avec `new`, **tu** demandes de la mémoire. Avec `delete`, **tu** dois la rendre :

```cpp
Chien* rex = new Chien();   // je réserve de la mémoire pour un Chien
rex->aboyer();
delete rex;                 // … et je dois penser à la rendre. Si j'oublie : FUITE
```

L'analogie : c'est comme **emprunter un livre à la bibliothèque**. Tant que tu le rends
(`delete`), tout va bien. Mais si tu **oublies de le rendre**, le livre reste « pris » et
personne d'autre ne peut l'utiliser. En informatique, ce livre jamais rendu s'appelle une
**fuite mémoire** (*memory leak*) : de la mémoire occupée que plus personne ne libérera.

Et c'est pire qu'il n'y paraît : si une erreur survient **entre** le `new` et le `delete`
(une exception, un `return` anticipé…), le `delete` n'est **jamais** atteint. Compter sur
l'humain pour ne jamais oublier, c'est compter sur une catastrophe.

---

## 2. La SOLUTION : le RAII, « ranger tout seul en partant »

Le C++ a une idée très puissante au nom barbare : le **RAII**
(*Resource Acquisition Is Initialization*). Derrière ce sigle, une règle toute simple :

> **Une ressource (mémoire, fichier…) est liée à un objet. Quand cet objet sort de portée,
> sa ressource est libérée automatiquement.**

« Sortir de portée », c'est tout simplement **arriver à la fin du bloc `{ }`** où l'objet a
été créé. À ce moment-là, le C++ appelle **automatiquement** le **destructeur** de l'objet
(le `~NomDeClasse` vu au module 04) — et c'est lui qui range.

L'analogie : une **lumière à détecteur de présence**. Tu entres dans la pièce, la lumière
s'allume ; tu sors, elle s'éteint **toute seule**. Tu n'as **rien** à éteindre. Le RAII,
c'est ça pour la mémoire : tu n'as rien à libérer, ça se fait en partant.

> 💡 Tu connais **déjà** le RAII sans le savoir ! Au module 05, `std::ofstream` fermait le
> fichier **tout seul** à la fin du bloc. Même principe : la ressource (le fichier) est
> libérée quand l'objet sort de portée.

---

## 3. `std::unique_ptr` : UN SEUL propriétaire

Le premier smart pointer, `std::unique_ptr`, applique le RAII à un objet créé sur le tas :
il en est le **propriétaire unique**, et le libère tout seul en sortant de portée.

On le crée avec **`std::make_unique`** (et il faut `#include <memory>`) :

```cpp
#include <memory>

std::unique_ptr<Chien> rex = std::make_unique<Chien>();  // je crée un Chien possédé
rex->aboyer();          // on l'utilise comme un pointeur normal : la flèche ->
// ... pas de delete ! À la fin du bloc, rex est détruit et libère le Chien tout seul
```

L'analogie : `unique_ptr`, c'est un **billet de concert nominatif**. Il y a **un seul**
propriétaire à la fois. Tu ne peux pas en faire deux copies (ce serait deux personnes avec
le même billet) — mais tu peux le **transmettre** à quelqu'un d'autre (on dit *déplacer*).

- ✅ **Avantage** : zéro `delete` à écrire, donc **zéro fuite** possible par oubli.
- 🔒 **Règle** : un seul propriétaire. C'est le bon choix **par défaut**, le plus courant.

---

## 4. `std::shared_ptr` : propriété PARTAGÉE (avec un compteur)

Parfois, **plusieurs** parties du programme ont besoin de partager le **même** objet, et on
ne sait pas laquelle finira en dernier. C'est le rôle de **`std::shared_ptr`** : la
**propriété partagée**.

Comment savoir quand libérer ? Le `shared_ptr` tient un **compteur de références**
(*reference count*) : combien de pointeurs partagent l'objet en ce moment. À chaque nouveau
partage, le compteur **monte** ; à chaque partage qui disparaît, il **descend**. Quand il
tombe à **zéro** — donc quand le **dernier** propriétaire s'en va — l'objet est libéré.

On le crée avec **`std::make_shared`**, et on lit le compteur avec **`.use_count()`** :

```cpp
#include <memory>

std::shared_ptr<Chien> a = std::make_shared<Chien>();  // compteur = 1
std::shared_ptr<Chien> b = a;        // b PARTAGE le même Chien -> compteur = 2
std::cout << a.use_count() << std::endl;   // affiche 2
// quand a ET b ont disparu, compteur = 0 -> le Chien est enfin libéré
```

L'analogie : un **document partagé** entre collègues. Tant qu'au moins une personne l'a
encore ouvert, on le garde. Quand **la dernière** personne le ferme, on peut le ranger
pour de bon. Le compteur, c'est « combien de personnes l'ont ouvert ».

---

## 5. 🆚 Lequel choisir ?

| | `std::unique_ptr` | `std::shared_ptr` |
|--|-------------------|-------------------|
| Propriété | **un seul** propriétaire | **plusieurs**, partagée |
| On le crée avec | `std::make_unique` | `std::make_shared` |
| Compteur de références | non (inutile) | oui (`.use_count()`) |
| Coût | très léger | un peu plus lourd (le compteur) |
| Quand l'utiliser | **par défaut** | quand un objet doit vraiment être **partagé** |

> 💬 **Conseil de pro** : préfère **toujours** les smart pointers aux `new`/`delete` bruts.
> Commence par `std::unique_ptr` (le plus simple et le moins cher) ; ne passe à
> `std::shared_ptr` que si tu as **réellement** besoin de partager la propriété. Les `new`
> et `delete` à la main, tu n'en auras presque plus jamais besoin.

---

## ▶️ À toi de jouer

Depuis la **racine du dépôt** (le dossier qui contient `cpp/`) :

```bash
# 1. unique_ptr : un seul propriétaire, libération automatique en fin de bloc
g++ -std=c++17 -Wall cpp/09_smart_pointers/unique_ptr.cpp -o unique_ptr && ./unique_ptr

# 2. shared_ptr : propriété partagée, le compteur use_count() et la libération au dernier
g++ -std=c++17 -Wall cpp/09_smart_pointers/shared_ptr.cpp -o shared_ptr && ./shared_ptr
```

Observe bien le **destructeur** qui s'affiche : tu verras **précisément** à quel moment
l'objet est libéré — sans que tu aies écrit un seul `delete`. Ensuite, **modifie** :
mets le `shared_ptr` `b` dans un bloc `{ }` à lui et regarde le compteur **redescendre**
quand on sort du bloc.

➡️ D'autres modules avancés viendront dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
