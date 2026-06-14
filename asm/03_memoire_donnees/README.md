# Module 03 — La mémoire et les données (sections, adressage, tableaux)

Jusqu'ici, tu calculais **uniquement dans les registres** (les petites cases du processeur).
Mais les registres sont **peu nombreux**. Pour ranger **beaucoup** de valeurs, il faut la
**mémoire**. Dans ce module, tu apprends à **déclarer des données**, à **lire et écrire en
mémoire**, et à parcourir un **tableau**.

> Fichiers du module : [`donnees.s`](./donnees.s) (déclarer et lire des valeurs en mémoire)
> et [`tableau.s`](./tableau.s) (parcourir un tableau et calculer sa somme). Tout est
> commenté presque ligne par ligne.

---

## 1. Les SECTIONS de données : `.data` et `.bss`

Un programme range ses données dans des **sections** (des zones séparées de la mémoire).
Deux nous intéressent ici :

| Section | À quoi elle sert |
|---------|------------------|
| `.data` | les données **initialisées** : tu donnes une **valeur de départ** (ex. `42`). |
| `.bss`  | la mémoire **réservée** mais **non initialisée** : tu réserves de la place vide. |

> 💡 Pourquoi deux sections ? Mettre `42` dans `.data` veut dire « réserve une case **et**
> écris `42` dedans ». Réserver une case dans `.bss` veut dire juste « garde-moi de la place,
> je la remplirai plus tard ». La `.bss` ne prend pas de place dans le fichier exécutable (on
> ne stocke pas des zéros), c'est plus économique pour de grandes zones vides.

Et bien sûr, le **code** (les instructions) vit dans la section `.text`, comme tu l'as déjà
vu dans les modules précédents.

---

## 2. DÉCLARER des données : `.byte`, `.word`, `.quad`, `.ascii`

Dans `.data`, on pose une **étiquette** (un nom) puis une **directive** qui dit la **taille**
de la donnée et sa **valeur** :

| Directive | Taille | Ce qu'elle déclare |
|-----------|--------|--------------------|
| `.byte`  | 1 octet (8 bits)   | un tout petit nombre (0 à 255) |
| `.word`  | 2 octets (16 bits) | un nombre moyen |
| `.quad`  | 8 octets (64 bits) | un grand nombre (la taille d'un registre comme `rax`) |
| `.ascii` | 1 octet par lettre | du **texte** (suite de caractères) |

```asm
.section .data
mon_nombre:  .quad 42          # une case de 8 octets contenant 42.
petit:       .byte 7           # une case de 1 octet contenant 7.
message:     .ascii "Salut"    # 5 octets : 'S','a','l','u','t'.
```

> 💡 On utilise surtout `.quad` dans ce parcours, car **8 octets = la taille d'un registre**
> 64 bits (`rax`, `rdi`…). Une valeur `.quad` rentre donc **pile** dans un registre.

---

## 3. L'ADRESSAGE : lire et écrire en mémoire

Une **étiquette** dans `.data`, c'est en réalité une **adresse** : le « numéro de la case »
en mémoire. Pour travailler avec, il y a deux opérations très différentes :

### a) Lire/écrire la **valeur** rangée à une adresse : les crochets `[ ]`

Les crochets veulent dire « **le contenu de la case** située à cette adresse » :

```asm
mov rax, [mon_nombre]    # rax = la VALEUR rangée dans 'mon_nombre' (= 42).
mov [mon_nombre], rbx    # écrit le contenu de rbx DANS la case 'mon_nombre'.
```

> 🔑 Retiens bien : `mov rax, mon_nombre` (sans crochets) mettrait l'**adresse**, alors que
> `mov rax, [mon_nombre]` (avec crochets) met la **valeur** rangée à cette adresse. C'est la
> différence entre « la maison » et « ce qu'il y a **dans** la maison ».

### b) Charger une **adresse** dans un registre : `lea`

`lea` (*Load Effective Address* = « charge l'adresse effective ») met **l'adresse** (le
numéro de case), pas la valeur :

```asm
lea rbx, [mon_tableau]   # rbx = l'ADRESSE du début de 'mon_tableau'.
```

Une fois l'adresse dans `rbx`, on peut lire la valeur avec `mov rax, [rbx]`.

---

## 4. Un TABLEAU en mémoire : des cases CONTIGUËS

Un **tableau** est juste une **suite de cases collées les unes aux autres** (contiguës) en
mémoire. Si chaque case fait 8 octets (`.quad`), elles se suivent comme ça :

```
adresse :   +0        +8        +16       +24       +32
          +---------+---------+---------+---------+---------+
valeur :  |   10    |   20    |   30    |   40    |   50    |
          +---------+---------+---------+---------+---------+
index  :      0         1         2         3         4
```

Pour atteindre l'élément numéro `index`, on calcule son adresse ainsi :

```
adresse_element = adresse_du_debut + index * taille_d_un_element
```

Avec des `.quad` (8 octets), l'élément `2` est à `début + 2*8 = début + 16`.

### Lire un élément avec `[base + index*8]`

L'assembleur sait faire ce calcul d'adresse **tout seul**, directement dans les crochets :

```asm
lea rbx, [mon_tableau]      # rbx = adresse du début du tableau.
mov rcx, 2                  # rcx = l'index voulu (ici, l'élément n°2).
mov rax, [rbx + rcx*8]      # rax = la valeur de l'élément n°2 (= 30).
```

`[rbx + rcx*8]` se lit : « la case située à l'adresse `rbx`, décalée de `rcx` fois 8 octets ».
Pour **parcourir** tout le tableau, il suffit de faire **augmenter l'index** dans une boucle
(comme au module 01) et de relire `[rbx + rcx*8]` à chaque tour. C'est exactement ce que fait
[`tableau.s`](./tableau.s).

---

## ▶️ À toi de jouer

```bash
# donnees.s : lit deux valeurs en mémoire, les additionne -> exit=42
as asm/03_memoire_donnees/donnees.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"

# tableau.s : additionne les 5 cases du tableau (10+20+30+40+50) -> exit=150
as asm/03_memoire_donnees/tableau.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
```

Lis les deux fichiers, puis **modifie-les** : dans `donnees.s`, change les valeurs déclarées
dans `.data` et recalcule le résultat attendu. Dans `tableau.s`, ajoute une case au tableau
(et augmente le nombre de tours de boucle) : la somme changera en conséquence.

➡️ La suite du parcours (chaînes de caractères, affichage de nombres…) arrivera dans le
même style.

📎 Besoin d'un rappel rapide ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
