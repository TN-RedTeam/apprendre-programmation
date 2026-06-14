# 🧭 Anatomie d'un programme C++ : dans quel ordre écrire son code ?

Beaucoup de débutants savent écrire des lignes de C++, mais ne savent pas **dans quel
ordre les ranger** pour former un programme complet et propre. Ce guide explique le
**cheminement logique** d'un programme `.cpp`, du début à la fin.

> 📌 À lire après les modules [`00_demarrer`](./00_demarrer/) et
> [`01_les_bases`](./01_les_bases/), et à garder sous la main comme aide-mémoire.

---

## 1. LA règle d'or : le C++ se lit de HAUT en BAS

C'est le point le plus important, et la cause n°1 des bugs de débutant.

> Le compilateur lit ton fichier **de haut en bas**, comme tu lis une page. **Une chose
> doit être déclarée AVANT qu'on l'utilise.**

Tu ne peux pas verser le café dans une tasse que tu n'as pas encore sortie du placard.
En code, c'est pareil : tu ne peux pas utiliser une fonction, une classe ou un outil
(`std::cout`…) **avant** de l'avoir déclaré/inclus plus haut. Si tu appelles une fonction
qui est écrite **plus bas** que `main()`, le compilateur râle : « il ne la connaît pas
encore ».

---

## 2. Le squelette standard d'un programme C++

Presque tous les programmes C++ bien écrits suivent **ce même ordre**, de haut en bas :

```cpp
// (1) LES #include : on ouvre les boîtes à outils
#include <iostream>      // pour std::cout, std::cin
#include <string>        // pour std::string

// (2) CONSTANTES / DÉCLARATIONS : les réglages fixes, regroupés en haut
const double TVA = 0.20;             // une constante (valeur qui ne change pas)
const int    AGE_MAJORITE = 18;

// (3) DÉFINITIONS de classes et de fonctions : on les ÉCRIT ici,
//     elles ne s'exécutent PAS encore.
class Personne {
public:
    std::string nom;
    int age;

    bool estMajeure() {              // une méthode (action de l'objet)
        return age >= AGE_MAJORITE;
    }
};

double prixTTC(double prixHT) {       // une fonction réutilisable
    return prixHT * (1 + TVA);
}

// (4) LA FONCTION main() : le point d'entrée, le chef d'orchestre.
//     C'est ICI que tout DÉMARRE et qu'on appelle les classes/fonctions.
int main() {
    Personne p;
    p.nom = "Sami";
    p.age = 20;

    std::cout << p.nom << " majeur ? " << p.estMajeure() << std::endl;
    std::cout << "Prix TTC : " << prixTTC(100.0) << std::endl;

    return 0;   // 0 = « tout s'est bien passé »
}
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 1 | **`#include`** | On **ouvre les caisses à outils** avant de s'en servir. `#include <iostream>` apporte `std::cout`/`std::cin`. Sans ça, le compilateur ne connaît pas ces outils. |
| 2 | **Constantes / déclarations** | Les réglages fixes (`const`), regroupés en haut pour les retrouver et les changer facilement. Par convention, on les écrit `EN_MAJUSCULES`. |
| 3 | **Définitions (classes & fonctions)** | On **définit** les modèles (classes) et les actions réutilisables (fonctions). ⚠️ Définir ≠ exécuter : le code d'une fonction ne tourne que lorsqu'on l'**appelle**. Elles doivent être écrites **avant** d'être utilisées dans `main()`. |
| 4 | **`main()`** | Le **point d'entrée** du programme et le **chef d'orchestre** : il crée les objets et appelle les fonctions dans le bon ordre. On le met **tout en bas**, après tout ce dont il a besoin. |

> 💡 « Définir une fonction/classe » = écrire la recette. « L'appeler/l'utiliser » =
> cuisiner le plat. On écrit toutes les recettes en haut, puis on cuisine dans `main()`.

> 🧩 **Astuce pour les plus grands projets :** quand un fichier devient gros, on **sépare**
> le code en deux fichiers (comme en C) : un fichier d'en-tête **`.h`** (les *déclarations* :
> « telle classe et telle fonction existent ») et un fichier **`.cpp`** (les *définitions* :
> leur vrai contenu). Les autres fichiers font alors `#include "monfichier.h"` pour y avoir
> accès. Au début, garde tout dans un seul `.cpp` : c'est plus simple.

---

## 3. Le cycle de travail : écrire → COMPILER → corriger → lancer

Contrairement à Python (qui se lance directement), le C++ doit être **compilé** avant de
tourner. Le va-et-vient est :

```
   écrire le .cpp  ──►  COMPILER (g++)  ──►  corriger les erreurs  ──►  lancer l'exécutable
        ▲                     │                      │
        └─────────────────────┴──────────────────────┘
             (on recommence tant qu'il y a des erreurs)
```

```bash
# Compiler le fichier source en un exécutable, puis le lancer
g++ -Wall mon_programme.cpp -o mon_programme && ./mon_programme
```

- `g++` = le compilateur ; `-Wall` = « montre-moi tous les avertissements » (très utile) ;
- `-o mon_programme` = nom de l'exécutable à créer ;
- `./mon_programme` = lancer l'exécutable obtenu.

> 💬 Si la compilation **échoue**, le programme n'est **pas** mis à jour : lis le message
> d'erreur (il indique souvent la ligne), corrige, et **recompile**. C'est normal d'y
> revenir plusieurs fois !

---

## 4. Le rôle de `main()` : le point d'entrée

```cpp
int main() {
    // ... ton programme ...
    return 0;
}
```

- **`main()` est le point d'entrée** : quand tu lances l'exécutable, l'ordinateur cherche
  `main()` et commence par là. **Tout part de `main()`.**
- Son type de retour est **`int`** : `main()` renvoie un nombre entier au système.
- **`return 0;`** signifie « le programme s'est terminé **sans erreur** ». Un autre nombre
  (ex. `return 1;`) signalerait un problème.

> Il n'y a qu'**un seul** `main()` par programme. Les classes et les fonctions, elles, sont
> juste « disponibles » : elles ne s'exécutent que lorsque `main()` (ou une autre fonction)
> les appelle.

---

## 5. La logique INTERNE : entrée → traitement → sortie

À l'intérieur de `main()` (ou d'une fonction), le code suit presque toujours **3 phases**,
dans cet ordre :

```
   1. ENTRÉE              2. TRAITEMENT             3. SORTIE
   (je récupère           (je calcule, je décide,   (j'affiche ou
    les données)           je transforme)            j'enregistre)
   ──────────             ───────────────          ──────────
   std::cin >> x;         if / else                 std::cout << ...
   std::getline(...)      for / while               écrire un fichier
   lire un fichier        calculs, fonctions        std::ofstream
   (std::ifstream)        appels de méthodes        (module 05)
```

Exemple complet des 3 phases :

```cpp
int main() {
    int age;
    std::cout << "Quel est ton age ? ";   // invite
    std::cin >> age;                       // 1. ENTRÉE : on lit au clavier

    bool majeur = (age >= 18);             // 2. TRAITEMENT : on décide

    if (majeur) {                          // 3. SORTIE : on affiche le résultat
        std::cout << "Tu es majeur." << std::endl;
    } else {
        std::cout << "Tu es mineur." << std::endl;
    }
    return 0;
}
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

> 📁 Pour lire/écrire des **fichiers** plutôt que le clavier/l'écran, c'est la même logique,
> avec `<fstream>` (`std::ifstream` pour lire, `std::ofstream` pour écrire) — voir le module
> [`05_fichiers`](./05_fichiers/).

---

## 6. Comment lire un programme C++ qu'on découvre

Quand un programme te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va directement à `main()`.** C'est le **point de départ** réel : il montre
   l'enchaînement principal du programme.
2. **Suis les appels** depuis `main()`. Quand tu vois `prixTTC(100.0)` ou `p.estMajeure()`,
   remonte lire la **fonction** `prixTTC` ou la **classe** `Personne` pour comprendre ce
   qu'elles font.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes de `main()`), puis seulement après, plonge dans chaque fonction/classe.

> C'est comme une table des matières : tu lis d'abord les titres de chapitres (le contenu de
> `main()`), puis tu ouvres les chapitres qui t'intéressent (les fonctions et les classes).

---

## 7. Récapitulatif visuel

```
┌─────────────────────────────────────────────┐
│ 1. #include <...>   : les boîtes à outils     │  ← on prépare
│ 2. const / déclar.  : les réglages fixes      │
├─────────────────────────────────────────────┤
│ 3. class ... { }    : on DÉFINIT les modèles  │  ← on outille
│    type fonction()  : on DÉFINIT les actions  │
├─────────────────────────────────────────────┤
│ 4. int main() {                               │
│        entrée  ->  traitement  ->  sortie     │  ← on EXÉCUTE
│        return 0;                              │
│    }                                          │
└─────────────────────────────────────────────┘
        (le compilateur lit de haut en bas)

    écrire  ──►  COMPILER (g++)  ──►  corriger  ──►  lancer
```

➡️ Garde ce squelette en tête pour démarrer tes propres programmes du bon pied, et n'oublie
pas : **on déclare avant d'utiliser, et tout démarre dans `main()`.**
