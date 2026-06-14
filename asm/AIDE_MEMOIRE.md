# 📎 Aide-mémoire ASSEMBLEUR (x86-64 Linux, syntaxe Intel)

Une page pour retrouver l'essentiel d'un coup d'œil. Tout est en syntaxe `.intel_syntax
noprefix`, avec les outils `as` et `ld`.

---

## ▶️ Assembler, lier, lancer

```bash
as monfichier.s -o /tmp/x.o      # 1. ASSEMBLER : .s -> .o (fichier objet)
ld /tmp/x.o -o /tmp/x            # 2. LIER       : .o -> exécutable
/tmp/x ; echo "exit=$?"          # 3. LANCER + lire le CODE DE SORTIE
```

En une seule ligne :

```bash
as monfichier.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
```

> `echo $?` affiche le **code de sortie** du dernier programme (0 à 255).

---

## 🧠 Registres principaux

| Registre | Rôle habituel |
|----------|---------------|
| `rax` | n° de l'appel système, et **résultat** des calculs / fonctions |
| `rdi` | 1er argument (syscall ou fonction), souvent le **code de sortie** |
| `rsi` | 2e argument |
| `rdx` | 3e argument |
| `rsp` | **pointeur de pile** : pointe le sommet de la pile (géré par push/pop/call/ret) |

---

## ⚙️ Instructions clés

| Instruction | Effet |
|-------------|-------|
| `mov A, B` | A reçoit B (copie B dans A) |
| `add A, B` | A = A + B |
| `sub A, B` | A = A - B |
| `cmp A, B` | compare A et B (ne modifie rien ; prépare un saut) |
| `jmp lbl` | saute vers `lbl` **toujours** |
| `jl lbl`  | saute si A **<** B (après un `cmp`) |
| `jne lbl` | saute si A **≠** B (après un `cmp`) |
| `push R`  | **pose** R sur la pile |
| `pop R`   | **retire** le sommet de la pile dans R |
| `call lbl`| saute vers `lbl` ET mémorise l'adresse de retour sur la pile |
| `ret`     | revient juste après le `call` |

> Autres sauts utiles : `je` (égal), `jg` (plus grand), `jle`, `jge`.

---

## 📞 Appels système (syscalls)

| Service | n° dans `rax` | Arguments | Rôle |
|---------|---------------|-----------|------|
| `write` | 1  | `rdi`=descripteur (1=écran), `rsi`=adresse texte, `rdx`=longueur | écrire du texte |
| `exit`  | 60 | `rdi`=code de sortie | quitter le programme |

```asm
mov rax, 60        # service exit
mov rdi, 0         # code de sortie 0
syscall            # déclenche l'appel système
```

---

## 🦴 Squelette d'un programme

```asm
.intel_syntax noprefix          # syntaxe Intel (lisible)

.section .data                  # (optionnel) données fixes : textes, nombres
message: .ascii "Bonjour\n"

.section .text                  # le code
.global _start                  # rend _start visible pour ld

_start:                         # point d'entrée du programme
    # ... ton code ici ...
    mov rax, 60                 # service exit
    mov rdi, 0                  # code de sortie
    syscall                     # quitte
```

---

## 🔎 Lire le résultat

```bash
/tmp/x ; echo $?     # affiche le code de sortie (utile pour "voir" un calcul)
```
