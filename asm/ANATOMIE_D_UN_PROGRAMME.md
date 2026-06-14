# 🧭 Anatomie d'un programme assembleur : dans quel ordre l'écrire ?

Tu sais peut-être déjà taper quelques instructions (`mov`, `add`, `syscall`), mais une
question revient sans cesse chez les débutants : **dans quel ordre ranger tout ça** pour
former un programme complet qui s'assemble, se lie et se lance sans planter ? Ce guide
explique le **squelette standard** d'un programme assembleur x86-64 (syntaxe Intel,
outils `as`/`ld`), section par section, et **pourquoi** cet ordre.

> 📌 À lire après le module [`00_demarrer`](./00_demarrer/), et à garder sous la main comme
> aide-mémoire. Pour l'essentiel ultra-condensé, vois aussi [`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md).

---

## 1. LA règle d'or : le processeur exécute de HAUT en BAS

C'est le point le plus important.

> Le processeur exécute les instructions **une par une, de haut en bas**, comme tu lis une
> page… **SAUF** quand un **saut** (`jmp`, `jl`, `jne`…) ou un **appel** (`call`) lui dit
> d'aller ailleurs.

Imagine un doigt qui descend ligne après ligne dans la section `.text`. La plupart du
temps il avance tout droit. Mais un `jmp etiquette` **déplace le doigt** d'un coup vers
l'étiquette indiquée, et un `call` part exécuter un sous-programme puis **revient** juste
après. Tant qu'il n'y a ni saut ni appel, **l'ordre d'écriture = l'ordre d'exécution.**

> ⚠️ Conséquence cruciale : le processeur **ne s'arrête pas tout seul** en bas du fichier.
> Si tu oublies de quitter (voir §2, point 5), il continue sur ce qui suit en mémoire et…
> **plante**. On y revient.

---

## 2. Le squelette standard d'un programme

Presque tous les programmes assembleur bien rangés suivent **ce même ordre**, de haut en
bas. Voici un exemple complet et commenté (il affiche `Bonjour` puis quitte) :

```asm
# (1) DIRECTIVE : on choisit la syntaxe Intel (plus lisible pour débuter).
.intel_syntax noprefix

# (2) SECTION .data : les données INITIALISÉES (qui ont déjà une valeur).
.section .data
message:
    .ascii "Bonjour\n"          # un texte fixe, prêt à être affiché

# (3) SECTION .bss : la mémoire RÉSERVÉE mais VIDE (des tampons à remplir).
.section .bss
    .lcomm tampon, 64           # réserve 64 octets vides (ex : pour lire au clavier)

# (4) SECTION .text : le CODE (les instructions à exécuter).
.section .text
.global _start                  # rend _start visible : c'est le POINT D'ENTRÉE
_start:
    # --- write(1, message, 8) : afficher le texte ---
    mov rax, 1                  # service 1 = write (écrire)
    mov rdi, 1                  # vers l'écran (sortie standard)
    lea rsi, [message]          # adresse du texte à afficher
    mov rdx, 8                  # nombre d'octets ("Bonjour\n" = 8)
    syscall                     # on demande à Linux d'écrire

    # (5) FIN OBLIGATOIRE : exit(0) : quitter proprement
    mov rax, 60                 # service 60 = exit (quitter)
    mov rdi, 0                  # code de sortie 0 = tout va bien
    syscall                     # le programme s'arrête ICI
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Rôle et pourquoi il est là |
|------|------|-----------------------------|
| 1 | **`.intel_syntax noprefix`** | Tout en haut : c'est une **consigne pour `as`**, pas une instruction. Elle dit « lis tout le fichier en syntaxe Intel ». Si elle manque, `as` lit en syntaxe AT&T et **tout est faux**. On la met en premier pour qu'elle s'applique au reste. |
| 2 | **`.section .data`** | Les **données déjà remplies** : textes, nombres fixes. C'est le « garde-manger » : on prépare les ingrédients **avant** de cuisiner. |
| 3 | **`.section .bss`** | La mémoire **réservée mais vide** : des **tampons** (zones de travail) qu'on remplira pendant l'exécution, par exemple ce qu'on lit au clavier. Vide au départ → elle n'alourdit pas le fichier exécutable. |
| 4 | **`.section .text`** + `.global _start` + `_start:` | Le **code** : les instructions exécutées. `.global _start` rend l'étiquette **visible** pour `ld`, et `_start:` marque l'**endroit où l'exécution commence** (le point d'entrée). |
| 5 | **Le syscall `exit`** | La **dernière chose** que fait le programme : dire « j'ai fini ». **Obligatoire** (sinon plantage, voir §1). |

> 💡 Pourquoi données AVANT code ? Parce que le code (`.text`) **utilise** les données
> (`.data`/`.bss`). On range d'abord les ingrédients dans le garde-manger, on cuisine
> ensuite. (Techniquement `as` accepte d'autres ordres, mais **celui-ci est le plus clair**
> et c'est celui qu'on garde dans tout le parcours.)

> 🔎 `.data` ou `.bss` peuvent être **absentes** si ton programme n'a pas de texte ni de
> tampon (ex : un programme qui ne fait que des calculs). La section `.text` et `_start`,
> elles, sont **toujours** là.

---

## 3. Le cycle de vie : écrire → ASSEMBLER → LIER → lancer

En Python, tu écris puis tu lances. En assembleur, il y a **deux étapes de traduction**
entre les deux :

```
   écrire           ASSEMBLER (as)        LIER (ld)            lancer
   ──────           ──────────────        ─────────            ──────
  hello.s   ───►   hello.o (objet)  ───►  hello (exécutable)  ───►  ./hello
  (ton texte)      (langage machine,      (programme complet,        (Linux
                    pas encore lançable)   lançable)                  l'exécute)
```

```bash
as  asm/00_demarrer/hello.s -o /tmp/p.o   # 1. ASSEMBLER : .s  -> .o
ld  /tmp/p.o            -o /tmp/p          # 2. LIER      : .o  -> exécutable
/tmp/p ; echo "code de sortie = $?"        # 3. LANCER, et voir le code de sortie
```

### Assembler ≠ compiler

- **Compiler** (C, etc.) : traduire un langage de **haut niveau** vers le langage machine.
  C'est un gros travail : le compilateur décide pour toi quelles instructions produire.
- **Assembler** : ta source est **déjà** quasiment du langage machine. L'outil `as` fait
  une traduction presque **mot à mot** (une ligne ≈ une instruction). D'où le nom
  **assemblage**, et pas compilation.

> 🔗 **Et `ld` (lier) ?** L'éditeur de liens assemble les morceaux (ici un seul `.o`),
> place le code en mémoire et **marque où est `_start`** pour que Linux sache par où
> commencer. Sans cette étape, le `.o` n'est **pas** lançable.

---

## 4. `_start` et l'obligation de quitter

### Le point d'entrée : `_start`

En C, tout commence à `main`. En assembleur **nu** (sans la bibliothèque C), tout commence
à l'étiquette **`_start`**. C'est l'endroit que `ld` marque comme « début de
l'exécution ». On la rend visible avec `.global _start` :

```asm
.global _start      # rend _start visible pour l'éditeur de liens
_start:             # ICI commence l'exécution
    ...
```

### Quitter est OBLIGATOIRE

Le processeur **ne devine pas** que ton programme est terminé. Après la dernière
instruction, il continue tout droit (règle d'or, §1) sur des octets qui ne sont pas du
code valide → **crash** (« segmentation fault »). La sortie propre se fait avec le syscall
`exit` :

```asm
mov rax, 60     # service exit (quitter)
mov rdi, 0      # code de sortie 0 = succès
syscall         # le programme s'arrête ICI, pour de bon
```

> 💡 Le **code de sortie** (`rdi`) est un petit nombre que le programme renvoie en partant.
> Par convention, `0` = tout va bien. On le voit avec `echo $?` après le lancement.

---

## 5. Registres et convention des syscalls (rappel)

Le processeur calcule dans des **registres** (des cases ultra-rapides en son sein). Les
principaux qu'on utilise :

| Registre | On s'en sert pour… |
|----------|---------------------|
| `rax` | le **numéro** du syscall, et les résultats de calculs |
| `rdi` | **1er** argument du syscall |
| `rsi` | **2e** argument du syscall |
| `rdx` | **3e** argument du syscall |

**La convention des appels système Linux**, à retenir une fois pour toutes :

```
   rax = QUEL service        (ex : 1 = write, 60 = exit)
   rdi = 1er argument        ┐
   rsi = 2e  argument        ├─ les détails du service
   rdx = 3e  argument        ┘
   syscall                   = on déclenche la demande
```

| Service | `rax` | `rdi` | `rsi` | `rdx` |
|---------|------|-------|-------|-------|
| `write` | 1 | où écrire (1 = écran) | adresse du texte | nb d'octets |
| `exit`  | 60 | code de sortie | — | — |

> On **prépare** d'abord les registres (les `mov`), **ensuite** on fait `syscall`. L'ordre
> des `mov` entre eux n'a pas d'importance, mais ils doivent **tous** être faits avant le
> `syscall`.

---

## 6. La logique INTERNE : 3 phases

À l'intérieur de `_start`, le déroulé suit presque toujours **3 phases**, dans cet ordre :

```
   1. PRÉPARER          2. CALCULER / BOUCLER       3. AFFICHER puis QUITTER
   (je remplis les      (mov / add / sub / cmp,     (write pour montrer,
    registres)           jmp / jl pour les boucles)  exit pour finir)
   ──────────          ─────────────────────       ────────────────────
   mov rax, ...         add / sub / imul            write (rax=1, syscall)
   mov rdi, ...         cmp + jmp/jl/jne            exit  (rax=60, syscall)
```

Garde cette trame en tête : **je prépare, je calcule, j'affiche/je quitte.** Si tu fais un
`syscall write` avant d'avoir préparé `rsi`/`rdx`, c'est qu'un bloc est mal placé.

---

## 7. Comment lire un programme asm qu'on découvre

Quand un fichier `.s` te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais
ainsi :

1. **Repère `_start`** (dans `.text`) : c'est le **vrai point de départ** de l'exécution.
   Ignore d'abord ce qu'il y a au-dessus dans `.data`/`.bss`.
2. **Descends ligne par ligne** depuis `_start`, comme le ferait le processeur.
3. **Quand tu vois un saut ou un appel, suis-le.** Un `jmp boucle` ? Va lire l'étiquette
   `boucle:`. Un `call afficher` ? Va lire le sous-programme `afficher:`, puis **reviens**
   après le `call` (le processeur, lui, revient grâce à `ret`).
4. **Reviens aux données seulement quand le code les utilise.** Tu vois
   `lea rsi, [message]` ? **Là** tu remontes voir ce que vaut `message` dans `.data`.

> C'est comme suivre un itinéraire : tu pars de `_start`, tu avances tout droit, et tu
> tournes uniquement aux panneaux (`jmp`, `call`).

---

## 8. Récapitulatif visuel

```
┌──────────────────────────────────────────────────────────┐
│ (1) .intel_syntax noprefix : consigne pour `as`           │  ← on règle
├──────────────────────────────────────────────────────────┤
│ (2) .section .data : données REMPLIES (textes, nombres)   │  ← on prépare
│ (3) .section .bss  : mémoire RÉSERVÉE vide (tampons)      │     les données
├──────────────────────────────────────────────────────────┤
│ (4) .section .text                                        │
│        .global _start   : on rend _start visible          │  ← on EXÉCUTE
│        _start:          : POINT D'ENTRÉE                   │
│            préparer -> calculer -> afficher (write)       │
│ (5)        exit (rax=60, syscall)  : QUITTER (obligatoire) │
└──────────────────────────────────────────────────────────┘
   (le processeur lit de haut en bas, sauf jmp / call)

   cycle :  écrire .s  ──as──►  .o  ──ld──►  exécutable  ──►  lancer
```

➡️ Pour mettre tout ça en pratique, (re)fais le module [`00_demarrer`](./00_demarrer/),
puis enchaîne sur [`01_les_bases`](./01_les_bases/) pour les registres et les sauts.
