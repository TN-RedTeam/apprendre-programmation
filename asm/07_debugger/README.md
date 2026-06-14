# Module 07 — Débugger l'assembleur avec gdb (voir les registres pas à pas)

En Python, quand tu ne comprends pas ce qui se passe, tu mets des `print(...)` un peu
partout pour « voir » les valeurs. En **assembleur**, c'est beaucoup plus dur : afficher
ne serait-ce qu'un nombre demande tout un travail (un appel système `write`, une
conversion en texte…). Tu ne peux donc **pas** semer des `print()` à chaque ligne.

Heureusement, il existe un outil fait exactement pour ça : le **débogueur** (`gdb`). Avec
lui, tu peux **arrêter** le programme, **avancer d'une seule instruction à la fois**, et
**regarder le contenu des registres** à chaque étape. C'est, en assembleur, l'outil le
plus **essentiel** pour comprendre ce qui se passe vraiment dans la machine.

> Fichier du module : [`demo_debug.s`](./demo_debug.s) — un petit programme qui enchaîne
> quelques calculs puis quitte avec un code de sortie connu (**12**). Il est conçu pour
> être exploré pas à pas sous gdb.

---

## 1. Assembler AVEC les infos de debug : `as -g`

Pour que gdb puisse t'afficher tes lignes de code (et pas seulement des adresses), il faut
ajouter l'option **`-g`** au moment d'assembler. C'est elle qui glisse dans le fichier les
**informations de débogage** (numéros de ligne, noms…).

```bash
as -g asm/07_debugger/demo_debug.s -o /tmp/d.o     # -g = on garde les infos de debug
ld /tmp/d.o -o /tmp/d                               # on lie comme d'habitude
```

> 💡 Sans `-g`, le programme marche pareil, mais gdb t'affichera des adresses mémoire
> brutes au lieu de tes jolies lignes commentées. Avec `-g`, c'est bien plus confortable.

---

## 2. L'ESSENTIEL de gdb pour l'assembleur (en mots simples)

On lance gdb sur notre exécutable, puis on tape des **commandes** une par une :

```bash
gdb /tmp/d        # on démarre gdb sur notre programme
```

| Commande | En mots simples |
|----------|-----------------|
| `break _start` | **Pose un point d'arrêt** sur `_start` : le programme s'arrêtera là. |
| `run`          | **Lance** le programme (il s'arrête au premier point d'arrêt). |
| `stepi`        | **Exécute UNE seule instruction**, puis s'arrête à nouveau. (raccourci : `si`) |
| `info registers rax` | **Montre le contenu** du registre `rax`. (raccourci : `i r rax`) |
| `info registers` | Montre **tous** les registres d'un coup. (raccourci : `i r`) |
| `x/4xb &label` | **Examine la mémoire** : ici 4 octets (`b`) en hexadécimal (`x`) à l'adresse de `label`. |
| `continue`     | **Repart** jusqu'au prochain arrêt (ou la fin). (raccourci : `c`) |
| `quit`         | **Quitte** gdb. (raccourci : `q`) |

> 🔑 Les deux commandes que tu utiliseras le plus : **`stepi`** (avancer d'un cran) et
> **`info registers rax`** (regarder un registre). C'est ça, « voir » l'assembleur tourner.

> ℹ️ Petit détail rassurant : gdb affiche souvent la ligne que tu vas exécuter **ensuite**.
> Donc, après un `stepi`, le registre montre le résultat de l'instruction **précédente**,
> et la ligne affichée est la **prochaine** à venir.

---

## 3. Une SESSION gdb d'exemple, pas à pas

Voici une vraie session sur `demo_debug.s`. On suit le 🗺️ CHEMINEMENT décrit en tête du
fichier `.s` : `rax = 10`, puis `+5` (→ 15), puis on met `rbx = 3`, puis `rax - rbx` (→ 12).

```text
(gdb) break _start
Breakpoint 1 at 0x401000: file asm/07_debugger/demo_debug.s, line 30.

(gdb) run
Breakpoint 1, _start () at asm/07_debugger/demo_debug.s:30
30          mov rax, 10           # on s'arrête JUSTE AVANT cette instruction

(gdb) info registers rax
rax            0x0                 0            # rax vaut encore 0 (rien fait)

(gdb) stepi                                     # on exécute  mov rax, 10
33          add rax, 5

(gdb) info registers rax
rax            0xa                 10           # rax = 10  (0xa en hexadécimal)

(gdb) stepi                                     # on exécute  add rax, 5
36          mov rbx, 3

(gdb) info registers rax
rax            0xf                 15           # rax = 15  (0xf)  ->  le +5 a marché !

(gdb) stepi                                     # on exécute  mov rbx, 3
39          sub rax, rbx

(gdb) info registers rax rbx
rax            0xf                 15
rbx            0x3                 3            # rbx = 3, prêt pour la soustraction

(gdb) stepi                                     # on exécute  sub rax, rbx
42          mov rdi, rax

(gdb) info registers rax
rax            0xc                 12           # rax = 12  ->  le calcul est juste ! 🎉

(gdb) continue                                  # on laisse finir le programme
[Inferior 1 (process ...) exited with code 014]   # 014 = 12 en octal -> code de sortie 12

(gdb) quit
```

> 💡 La colonne du milieu est en **hexadécimal** (`0xa` = 10, `0xf` = 15, `0xc` = 12), la
> colonne de droite donne la valeur en **décimal** (plus lisible). Suivre `rax` passer de
> 10 à 15 puis à 12, c'est littéralement **voir le programme penser**.

---

## 4. Les PIÈGES fréquents en assembleur (et comment gdb les démasque)

L'assembleur ne te tient pas la main : une petite erreur ne provoque pas un joli message,
mais un **résultat faux** ou un **« segmentation fault »** (le programme plante brutalement).
Le réflexe est toujours le même : **avance avec `stepi` et regarde les registres** jusqu'à
trouver l'instruction qui ne fait pas ce que tu crois.

| Piège fréquent | Ce qui se passe | Comment gdb t'aide |
|----------------|-----------------|--------------------|
| **Oubli de mettre `rdx` = 0 avant `div`** | `div` utilise `rdx:rax` ensemble ; si `rdx` traîne une vieille valeur, la division est fausse (ou plante en *divide error*). | Avant le `div`, fais `i r rdx` : si `rdx` n'est pas 0, tu as trouvé. Ajoute `xor rdx, rdx` (ou `mov rdx, 0`) avant. |
| **Mauvais numéro de syscall** | Tu voulais `write` (1) mais `rax` contient autre chose : le système fait un service inattendu, ou rien. | Juste avant le `syscall`, fais `i r rax` : le numéro est-il bien celui voulu (1 = write, 60 = exit) ? |
| **Mauvaise taille passée à `write`** | Tu mets dans `rdx` (la longueur) un nombre trop grand/trop petit : texte tronqué ou caractères en trop. | `i r rdx` avant le `syscall` : la longueur correspond-elle vraiment à ton texte ? |
| **Adresse invalide → segmentation fault** | Tu lis/écris à une adresse qui n'existe pas (mauvais `lea`, pointeur jamais initialisé). | `run`, gdb s'arrête PILE sur l'instruction fautive. Regarde le registre d'adresse avec `i r` : vaut-il `0x0` ou une valeur absurde ? |

> 🧭 Méthode universelle : **« où ça plante ? »** (gdb s'arrête sur la ligne) puis
> **« qu'y a-t-il dans les registres à ce moment-là ? »** (`info registers`). Avec ces deux
> questions, on trouve presque tous les bugs en assembleur.

---

## ▶️ À toi de jouer

Assemble (avec `-g`), lie, lance — le code de sortie doit valoir **12** :

```bash
as -g asm/07_debugger/demo_debug.s -o /tmp/d.o && ld /tmp/d.o -o /tmp/d && /tmp/d ; echo "exit=$?"
```

Puis explore-le sous gdb en rejouant la session de la section 3 :

```bash
gdb /tmp/d
```

Tape les commandes une à une (`break _start`, `run`, `stepi`, `info registers rax`…) et
regarde `rax` évoluer. Pour t'amuser : **change** un nombre dans `demo_debug.s` (par exemple
`add rax, 5` → `add rax, 50`), ré-assemble, et **devine** le nouveau code de sortie AVANT de
le vérifier au débogueur.

➡️ Tu sais maintenant « voir » l'assembleur tourner. La suite du parcours arrivera dans le
même style.

📎 Besoin d'un rappel rapide ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
