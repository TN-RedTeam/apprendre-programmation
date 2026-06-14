# Module 06 — INTERFAÇAGE avec le C (convention d'appel System V AMD64)

Dans tous les modules précédents, ton programme **démarrait tout seul** grâce à l'étiquette
`_start`, et tu **liais** avec `ld`. Ce module change de point de vue : cette fois, on
n'écrit **pas** un programme autonome. On écrit une **FONCTION** en assembleur, et c'est un
programme **en C** qui l'appelle.

C'est exactement ce qui se passe « pour de vrai » : quand une partie d'un logiciel doit aller
très vite, on l'écrit parfois en assembleur, et le reste (en C) **l'appelle** comme n'importe
quelle autre fonction.

> Fichiers du module : [`somme.s`](./somme.s) (la fonction `somme` écrite en assembleur),
> [`main.c`](./main.c) (le programme C qui l'appelle). Tout est commenté presque ligne par
> ligne.

---

## 1. Pourquoi faire coopérer C et assembleur ?

- Le **C** est pratique pour écrire la **structure** d'un programme (boucles, affichage,
  organisation…), et il s'occupe de pleins de détails à ta place.
- L'**assembleur** permet d'écrire des morceaux **ultra-précis et rapides**, au plus près du
  processeur.

L'idée : laisser le C piloter, et lui confier une **fonction écrite en assembleur** pour une
tâche précise. Encore faut-il que les deux **se mettent d'accord** sur la façon de se passer
les arguments et le résultat. Ce « contrat » a un nom.

---

## 2. La CONVENTION D'APPEL System V AMD64

Sur Linux 64 bits, le C et l'assembleur respectent la même règle du jeu, appelée la
**convention d'appel System V AMD64**. Elle dit **où** une fonction trouve ses arguments et
**où** elle dépose son résultat :

| Élément | Où il se trouve |
|---------|-----------------|
| 1er argument entier | `rdi` |
| 2e argument entier  | `rsi` |
| 3e argument entier  | `rdx` |
| 4e argument entier  | `rcx` |
| (5e, 6e…)           | `r8`, `r9` |
| **valeur de retour** | `rax` |

> 🔑 À retenir pour ce module : pour `somme(a, b)`, le C met **`a` dans `rdi`** et **`b` dans
> `rsi`** *avant* d'appeler la fonction. Notre code asm fait le calcul et **laisse le résultat
> dans `rax`** : le C ira l'y chercher tout seul.

C'est joliment cohérent avec ce que tu connais déjà : aux modules précédents, `rdi`, `rsi`,
`rdx` servaient à passer les **arguments d'un appel système**. Ici, ce sont les **arguments
d'une fonction** — même esprit, même ordre.

---

## 3. Rendre la fonction VISIBLE par le C : `.global`

Par défaut, un nom défini dans un fichier `.s` reste **privé** à ce fichier. Pour que le C (et
l'éditeur de liens) puisse retrouver notre fonction, il faut la déclarer **publique** :

```asm
.global somme       # le nom "somme" devient visible de l'extérieur
somme:              # ...voici la fonction
    ...
    ret             # retour à l'appelant (le C)
```

Et surtout : **PAS de `_start` !** Le point d'entrée du programme est fourni par le **C** (sa
fonction `main`). Si on remettait un `_start`, on entrerait en conflit avec celui que le C
apporte déjà. Notre fichier asm ne contient donc **que la fonction**, qui se termine par
`ret` (et non par un `exit`).

---

## 4. Côté C : le PROTOTYPE

Le programme C n'a pas besoin de connaître le **contenu** de la fonction. Il lui suffit de sa
**signature** (le *prototype*) : son nom, ses paramètres et son type de retour.

```c
long somme(long, long);   // "je promets qu'une fonction somme existe quelque part"
```

Le corps, lui, est dans `somme.s`. C'est l'**éditeur de liens** qui fera le raccord entre la
*promesse* (le prototype en C) et la *réalité* (le code en assembleur).

---

## 5. Tout assembler et lier d'un coup avec `gcc`

Bonne nouvelle : pas besoin de lancer `as` puis `ld` à la main. L'outil **`gcc`** sait faire
toute la chaîne tout seul : il **compile** le C, **assemble** le `.s`, puis **lie** le tout en
un seul exécutable.

```bash
gcc main.c somme.s -o prog
```

- `main.c` → gcc le compile,
- `somme.s` → gcc l'assemble,
- `-o prog` → nom de l'exécutable produit,
- gcc relie automatiquement les deux ensemble.

---

## ▶️ À toi de jouer

Depuis la **racine du dépôt** :

```bash
gcc -Wall asm/06_interfacage_c/main.c asm/06_interfacage_c/somme.s -o /tmp/p && /tmp/p
```

Tu dois voir s'afficher :

```
7 + 5 = 12
```

Ensuite, **expérimente** :

- change les valeurs `a` et `b` dans `main.c` et relance ;
- dans `somme.s`, remplace `add rax, rsi` par `sub rax, rsi` : tu viens d'écrire une fonction
  **soustraction** ! (pense à renommer si tu veux que ce soit clair) ;
- ajoute un **3e argument** : il arrivera dans `rdx` (revois le tableau de la section 2).

➡️ La suite du parcours arrivera dans le même style.

📎 Besoin d'un rappel rapide ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
