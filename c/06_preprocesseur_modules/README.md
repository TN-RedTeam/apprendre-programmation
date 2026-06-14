# Module 06 — Le préprocesseur et séparer son code en plusieurs fichiers

Jusqu'ici, chaque programme tenait dans **un seul fichier `.c`**. Ça va pour apprendre,
mais dans un vrai projet on a vite des **centaines** de fonctions : tout mettre dans un
seul fichier devient illisible. La solution : **ranger son code dans plusieurs fichiers**.
On va aussi découvrir le **préprocesseur**, ce petit assistant qui prépare ton code
**avant** la compilation (tu l'utilises déjà sans le savoir avec `#include` !).

> Fichiers du module : `calculs.h` (les déclarations, la « carte de visite »),
> `calculs.c` (le vrai code des fonctions) et `main.c` (le programme principal qui s'en
> sert). On les **compile ensemble** (voir en bas).

---

## 1. Le préprocesseur : un assistant qui agit AVANT la compilation

📋 **Analogie : un assistant qui prépare ton texte.** Avant que le compilateur ne traduise
ton code en langage machine, un premier programme appelé **préprocesseur** relit ton fichier
et applique toutes les lignes qui commencent par un **`#`** (les *directives*). Il fait du
**copier-coller** et des **remplacements de texte**, puis passe le résultat au compilateur.

```
   ton code .c  ──[ préprocesseur ]──►  code "préparé"  ──[ compilateur ]──►  exécutable
                  (#include, #define)     (texte gonflé)      (traduction)
```

Les deux directives à connaître commencent par `#` : **`#include`** et **`#define`**.

---

## 2. `#define` : donner un nom à une valeur

`#define` dit au préprocesseur : « **AVANT** de compiler, remplace partout tel mot par telle
valeur ». C'est un simple **remplacement de texte**.

```c
#define PI 3.14159
```

Partout où tu écris `PI` ensuite, le préprocesseur le remplace par `3.14159`. Avantages :

- **Lisible** : `PI` parle plus que `3.14159` perdu au milieu du code.
- **Un seul endroit à changer** : si un jour tu veux plus de précision, tu modifies la
  ligne `#define` et c'est répercuté partout.

> 🧠 **Convention :** les noms de `#define` s'écrivent en **MAJUSCULES** (`PI`, `TAILLE_MAX`),
> pour qu'on voie tout de suite que ce n'est pas une variable ordinaire.

---

## 3. `#include` : coller le contenu d'un autre fichier

`#include` colle (littéralement) le contenu d'un autre fichier à cet endroit. Il y a **deux
formes**, et la différence est importante :

| Écriture | Sens | Exemple |
|----------|------|---------|
| `#include <stdio.h>` | un fichier **SYSTÈME** (fourni avec le compilateur) | `<stdio.h>`, `<string.h>`, `<math.h>` |
| `#include "calculs.h"` | un fichier **À TOI** (à côté de ton code) | `"calculs.h"` |

> 🔑 **À retenir :** **chevrons `< >`** = bibliothèques du système ; **guillemets `" "`** =
> tes propres fichiers. Le compilateur ne les cherche pas au même endroit.

---

## 4. Pourquoi séparer en plusieurs fichiers ? `.h` et `.c`

💼 **Analogie : la carte de visite et l'atelier.** Quand on découpe un module, on le coupe
en deux :

- le **`.h`** (header / en-tête) = la **carte de visite** : il **annonce** ce qui existe
  (les noms des fonctions, leurs paramètres, le type renvoyé) et les `#define`. C'est ce que
  les autres fichiers ont besoin de **connaître**.
- le **`.c`** = l'**atelier** : il contient le **vrai code** des fonctions. C'est là que le
  travail se fait.

Ainsi, `main.c` n'a qu'à inclure `calculs.h` pour savoir **comment** appeler les fonctions,
sans avoir à connaître leur code. On peut changer l'atelier (`calculs.c`) sans toucher au
reste, tant que la carte de visite (`calculs.h`) ne change pas.

### La GARDE D'INCLUSION (dans chaque `.h`)

Un même `.h` peut finir inclus **deux fois** (directement et via un autre fichier). Sans
protection, on déclarerait deux fois les mêmes choses → **erreur**. On entoure donc tout le
`.h` d'une **garde** :

```c
#ifndef CALCULS_H   // SI le marqueur CALCULS_H n'existe pas encore...
#define CALCULS_H   // ...on le crée (donc la 1re fois seulement)...

/* ... déclarations et #define ... */

#endif              // fin du bloc
```

À la **2e** inclusion, `CALCULS_H` existe déjà : tout le bloc est **sauté**. Le nom du
marqueur est libre ; par convention, c'est le nom du fichier en MAJUSCULES (`CALCULS_H`).

---

## 5. Compiler PLUSIEURS fichiers ensemble

Notre code est maintenant dans **deux `.c`** (`main.c` et `calculs.c`). Il faut les donner
**tous les deux** à `gcc`, sur la même ligne :

```bash
gcc -Wall c/06_preprocesseur_modules/main.c c/06_preprocesseur_modules/calculs.c -o prog
```

> 💡 On ne met **PAS** le `.h` dans la commande : il est déjà « collé » par `#include`. On
> ne compile que les `.c`. Le résultat est **un seul** exécutable (`prog`) qui réunit tout.

### Petite mention : les bibliothèques (`-l...`)

Certaines bibliothèques système ont besoin d'être **liées** explicitement. La plus classique
est **`math.h`** (racine carrée, puissances…) : on ajoute **`-lm`** (l = *link*, m = *math*)
à la fin :

```bash
gcc -Wall mon_prog.c -o prog -lm   # nécessaire si tu utilises <math.h>
```

(Notre module n'en a pas besoin — c'est juste pour que tu saches que ça existe.)

---

## ▶️ À toi de jouer

```bash
# Compiler les DEUX fichiers .c ensemble, puis lancer (DEPUIS LA RACINE) :
gcc -Wall c/06_preprocesseur_modules/main.c c/06_preprocesseur_modules/calculs.c -o prog && ./prog
```

Tu dois voir s'afficher la somme, le maximum, la valeur de `PI` et l'aire d'un disque.
Ensuite **modifie** : change la valeur du `#define PI`, ajoute une nouvelle fonction (déclare-la
dans `calculs.h`, écris son code dans `calculs.c`, appelle-la dans `main.c`). Essaie aussi,
pour voir l'erreur, d'oublier `calculs.c` dans la commande de compilation : le compilateur se
plaindra qu'il ne trouve pas le code des fonctions.

➡️ La suite du parcours (projets plus complets…) arrivera dans le même style.
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
