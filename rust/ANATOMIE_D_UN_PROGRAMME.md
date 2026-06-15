# 🧭 Anatomie d'un programme Rust : dans quel ordre écrire son code ?

Beaucoup de débutants savent écrire des lignes de Rust, mais ne savent pas **dans quel
ordre les ranger** pour former un programme complet et propre. Ce guide explique le
**cheminement logique** d'un programme Rust, du début à la fin.

> 📌 À lire après les modules [`00_demarrer`](./00_demarrer/) et
> [`01_les_bases`](./01_les_bases/), puis à garder sous la main comme aide-mémoire.
> C'est le cousin, côté Rust, du guide C `c/ANATOMIE_D_UN_PROGRAMME.md`.

---

## 1. La règle d'or : une chose doit EXISTER avant qu'on l'utilise

Comme partout, le compilateur a besoin de **connaître** un nom (variable, fonction, type)
avant que tu t'en serves.

> Bonne nouvelle pour qui vient du C : en Rust, **l'ordre des fonctions n'a pas d'importance**.
> Tu peux appeler une fonction définie **plus bas** que `main` — Rust « voit » tout le fichier.
> Donc **pas de prototypes** à écrire (contrairement au C) !

```rust
fn main() {
    saluer();             // ← on appelle saluer AVANT qu'elle soit définie : c'est OK en Rust
}

fn saluer() {             // définie plus bas, pas de problème
    println!("Bonjour !");
}
```

La règle reste vraie à l'**intérieur** d'une fonction : une variable doit être créée (`let`)
**avant** la ligne qui l'utilise. Là, on lit bien de haut en bas.

---

## 2. Le SQUELETTE STANDARD d'un programme Rust

Presque tous les programmes Rust bien écrits suivent **ce même ordre**, de haut en bas :

```rust
//                                                          ┐
//  Description du programme : à quoi il sert,              │  (0) COMMENTAIRE D'EN-TÊTE
//  comment le compiler et le lancer.                       │      (facultatif mais conseillé)
//                                                          ┘

use std::collections::HashMap;                           // ┐  (1) LES 'use' (imports)
                                                         //  ┘     (les boîtes à outils)

const TVA: f64 = 0.20;                                   // ┐  (2) CONSTANTES
const TAILLE_MAX: usize = 100;                           // ┘     (valeurs fixes, EN MAJUSCULES)

struct Personne {                                        // ┐  (3) STRUCTS / ENUMS
    nom: String,                                         //  │     (tes types de données)
    age: u32,                                            //  │
}                                                        //  │
enum Statut { AFaire, Terminee }                         // ┘

fn additionner(a: i32, b: i32) -> i32 {                  // ┐  (4) FONCTIONS
    a + b                                                //  │     (avant OU après main,
}                                                        //  ┘      l'ordre est libre)

fn main() {                                              // ┐  (5) LA FONCTION main()
    let somme = additionner(2, 3);                       //  │     (le POINT D'ENTRÉE :
    println!("2 + 3 = {}", somme);                       //  │      le programme DÉMARRE ici
}                                                        // ┘
```

### Pourquoi cet ordre, partie par partie

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 0 | **Commentaire d'en-tête** | La 1re chose qu'on lit : « ce programme sert à… ». Facultatif, mais bien utile. |
| 1 | **`use`** | On **importe les boîtes à outils** avant de s'en servir : `use std::collections::HashMap;` donne accès à `HashMap`. (Beaucoup de choses, comme `println!` ou `Vec`, sont déjà dispo sans `use`.) |
| 2 | **constantes (`const`)** | Les réglages fixes, regroupés en haut pour les changer facilement. Par convention, on les écrit `EN_MAJUSCULES` et leur type est obligatoire. |
| 3 | **`struct` / `enum`** | On **définit ses propres types** (les « moules » de données) avant les fonctions qui les manipulent. |
| 4 | **Fonctions** | Le **vrai code** des fonctions. En Rust, l'ordre est libre : on les place souvent **après** `main()` pour lire d'abord le déroulé général, puis les détails. Pas de prototypes nécessaires. |
| 5 | **`main()`** | Le **chef d'orchestre** : c'est le **point d'entrée**, l'endroit où le programme commence vraiment. Il appelle les fonctions dans le bon ordre. |

> 💡 **Différence majeure avec le C.** En C, il faut **annoncer** une fonction (un *prototype*)
> en haut si elle est appelée avant d'être définie. En Rust, **rien de tout ça** : le
> compilateur lit tout le fichier, donc l'ordre des fonctions est libre.

> 🧠 **Variante fréquente.** Certains regroupent les méthodes d'un type dans un bloc `impl`
> juste après la `struct` correspondante. C'est très lisible : la donnée et ses opérations
> côte à côte.

---

## 3. Le cycle en Rust : écrire → COMPILER → corriger → lancer

C'est LA grande différence avec Python. En Python, tu écris `script.py` et tu le lances
directement. En Rust, il y a une étape de plus : la **compilation**.

```
   programme.rs   ──[ rustc ]──►   programme (exécutable)   ──►   ./programme
   (ton code)      COMPILATION      (langage machine)             EXÉCUTION
```

Le cycle complet ressemble à ceci :

```
   1. ÉCRIRE        2. COMPILER          3. CORRIGER          4. LANCER
   le .rs           avec rustc           les erreurs          l'exécutable
   ──────           ──────────           ───────────          ──────────
   ton éditeur      rustc prog.rs        rustc se plaint ?    ./prog
                    -o prog              tu corriges et
                                         tu re-compiles
```

```bash
# 1. Compiler le fichier source en un exécutable nommé "programme"
rustc rust/00_demarrer/premier_programme.rs -o programme

# 2. Lancer l'exécutable créé
./programme
```

> 💡 Les messages d'erreur de Rust sont **parmi les meilleurs au monde** : ils pointent la
> ligne, expliquent le problème en clair, et proposent souvent la correction. Lis-les, c'est
> ton meilleur allié de débutant (voir le module [`07_debugger`](./07_debugger/)).

> ⚠️ **Important :** si tu modifies ton `.rs`, tu dois **re-compiler** avant de relancer.
> Sinon tu exécutes l'ancienne version ! (En Python, pas besoin : il relit le fichier
> à chaque lancement.) Avec `cargo run`, la recompilation est automatique.

---

## 4. Le rôle spécial de `fn main()`

Dans tout programme Rust, **l'exécution commence par la fonction `main()`** — jamais ailleurs.
C'est le **point d'entrée** imposé par le langage : peu importe où `main()` est écrit dans
le fichier, c'est toujours par là que ça démarre.

```rust
fn main() {
    // ... tout le déroulé du programme ...
}
```

Deux choses à retenir :

- **Pas de type de retour** par défaut : contrairement au C (`int main`), `fn main()` ne
  renvoie rien d'office (on peut renvoyer un `Result` pour les programmes avancés).
- **Pas de `return 0;`** : on ne rend rien au système dans le cas simple.

> 🧠 `fn main()` : les parenthèses vides veulent dire « cette fonction ne reçoit aucune
> information ». (Plus tard, tu liras les arguments de la ligne de commande avec
> `std::env::args()` — mais pas besoin pour débuter.)

---

## 5. La logique INTERNE : entrée → traitement → sortie

À l'intérieur de `main()` (ou d'une fonction), le code suit presque toujours **3 phases**,
dans cet ordre :

```
   1. ENTRÉE              2. TRAITEMENT              3. SORTIE
   (je récupère           (je calcule, je décide,    (j'affiche ou
    les données)           je transforme)             j'enregistre)
   ──────────             ───────────────            ──────────
   let x = ...            if / else                   println!(...)
   .read_line(...)        for / while / loop          eprintln!(...) (erreurs)
   args()                 match, calculs, appels      write!(...) (fichier)
```

Exemple complet et correct des 3 phases :

```rust
fn main() {
    // 1. ENTRÉE : je récupère une donnée (ici fixée pour l'exemple)
    let age: i32 = 16;

    // 2. TRAITEMENT : je décide en fonction de la donnée
    let annees_restantes = 18 - age;

    // 3. SORTIE : j'affiche le résultat
    if age >= 18 {
        println!("Tu es majeur.");
    } else {
        println!("Encore {} an(s) avant la majorite.", annees_restantes);
    }
}
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

---

## 6. Comment lire un programme Rust complexe qu'on découvre

Quand un programme te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va directement à `main()`.** C'est le **point de départ** réel : il montre
   l'enchaînement principal des grandes étapes. (Inutile de t'attarder d'abord sur les
   `use`, les `struct` ou les fonctions : ce ne sont que des préparatifs.)
2. **Suis les appels de fonctions** depuis `main()`. Quand tu vois `additionner(2, 3)`,
   va lire la fonction `fn additionner(...)` pour comprendre ce qu'elle fait.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes), puis seulement après, plonge dans chaque fonction.

> C'est comme une table des matières : `main()` te donne les titres de chapitres, puis tu
> ouvres les chapitres qui t'intéressent (les fonctions définies plus bas).

---

## 7. Récapitulatif visuel

```
┌─────────────────────────────────────────────────┐
│ 0. // Commentaire   : à quoi sert le programme   │
│ 1. use std::...     : les boites a outils        │  ← on prépare
│ 2. const CONST      : les réglages fixes         │
├─────────────────────────────────────────────────┤
│ 3. struct / enum    : tes propres types          │  ← on outille
│ 4. fn ... { }       : les fonctions (ordre libre) │
├─────────────────────────────────────────────────┤
│ 5. fn main() {                                   │
│        entrée  ->  traitement  ->  sortie        │  ← on EXÉCUTE
│    }                                              │    (ça démarre ICI)
└─────────────────────────────────────────────────┘
   (le compilateur lit tout le fichier ; on COMPILE
    avec rustc, PUIS on lance l'exécutable)
```

➡️ Garde ce modèle en tête pour démarrer tes propres programmes du bon pied, et reviens-y
dès qu'un programme te semble en désordre. Sous la main aussi :
l'[`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md) et le [`GLOSSAIRE.md`](./GLOSSAIRE.md).
