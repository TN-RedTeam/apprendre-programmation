# 🦀 Apprendre le Rust — pour grands débutants

Le **Rust** est un langage moderne qui vise un objectif rare : être à la fois **rapide** et
**sûr**. Comme le C, il est **compilé** (traduit en langage machine, donc très performant et
proche de la machine). Mais contrairement au C, il garantit la **sécurité mémoire** — sans
**ramasse-miettes** (*garbage collector*) — grâce à une idée géniale, l'**ownership** (la
*propriété* des données), vérifiée **à la compilation**. Résultat : la vitesse du C, sans ses
plantages mémoire silencieux.

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, compile, lance, modifie.

---

## 🆚 Différences avec Python et avec C

C'est la grande nouveauté si tu viens de Python, et la grande tranquillité si tu viens du C.

| | Python | C | **Rust** |
|--|--------|---|----------|
| Exécution | *interprété* | **compilé** | **compilé** |
| Types | dynamiques (`x = 5`) | statiques (`int x = 5;`) | **statiques** (souvent *devinés* : `let x = 5;`) |
| Mémoire | *garbage collector* | **manuelle** (pointeurs, `malloc`/`free`) | **automatique ET sûre** grâce à l'*ownership*, vérifiée à la compilation |
| Erreurs mémoire | rares (GC) | fréquentes (segfault, fuites…) | **empêchées dès la compilation** |
| Vitesse | lente | très rapide | **très rapide** (comme le C) |
| Variables | modifiables par défaut | modifiables par défaut | **immuables par défaut** (`mut` pour modifier) |

En résumé :
- vs **Python** : Rust est **compilé** et **typé** (plus strict, mais plus rapide et plus sûr).
- vs **C** : Rust offre la **même vitesse**, mais la **sécurité mémoire est garantie par le
  compilateur** — fini les segfaults et les fuites mémoire silencieuses.

---

## 📚 Le parcours (fondations)

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Qu'est-ce que Rust, compiler/exécuter (`rustc`, `cargo`), `println!` |
| 1 | [`01_les_bases`](./01_les_bases/) | Variables (`let`/`let mut`), types, `if`/`else` (et `if` expression), boucles (`loop`/`while`/`for`), fonctions |
| 2 | [`02_propriete`](./02_propriete/) | L'**ownership** (LE cœur de Rust) : le *move*, l'emprunt immuable `&`, l'emprunt mutable `&mut` |
| 3 | [`03_structs_enums`](./03_structs_enums/) | Regrouper des données (`struct`), représenter des choix (`enum`), réagir avec `match`, gérer l'absence avec `Option<T>` |
| 4 | [`04_collections`](./04_collections/) | Les collections : `Vec<T>` (la liste), `String` (texte modifiable), `HashMap` (l'annuaire clé → valeur) |
| 5 | [`05_erreurs`](./05_erreurs/) | Gérer l'échec : `Result<T, E>` (`Ok`/`Err`), rappel `Option`, l'opérateur `?`, et `panic!` |
| 6 | [`06_traits_generics`](./06_traits_generics/) | Les `trait` (des *contrats* que des types respectent) et les **génériques** `<T>` (du code « à trous ») |
| 7 | [`07_debugger`](./07_debugger/) | Le compilateur, ton meilleur ami : lire ses messages, `cargo check`/`rustc`, `dbg!`, l'affichage `{:?}`, lire un `Result` |

### 🚀 Modules avancés

À faire **une fois les fondations solides**. Plus exigeants, mais passionnants.

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 8 | [`08_closures_iterateurs`](./08_closures_iterateurs/) | Les **closures** `\|x\| ...` (mini-fonctions sur place) et les **itérateurs** : enchaîner `map` / `filter` / `collect` / `sum` en style « pipeline » |
| 9 | [`09_concurrence`](./09_concurrence/) | La **concurrence** : lancer des **threads** (`thread::spawn`), communiquer par **channels** (`mpsc`), partager une donnée en sûreté avec `Arc<Mutex<>>` |

> 🎯 **Et après les fondations ?** Le dossier [`projets/`](./projets/) rassemble un
> **projet « capstone »** (un gestionnaire de tâches en mémoire) qui combine plusieurs
> modules (`struct` + `enum` + `Vec` + `Result` + itérateurs) pour construire un vrai petit
> outil. À faire une fois les bases acquises.

> 📎 **Ressources** (à garder sous la main) : le guide
> [`ANATOMIE_D_UN_PROGRAMME.md`](./ANATOMIE_D_UN_PROGRAMME.md) (dans quel ordre écrire son
> code : `use`, constantes, `struct`/`enum`, fonctions, `fn main`…), l'[`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md)
> (cheat-sheet d'une page) et le [`GLOSSAIRE.md`](./GLOSSAIRE.md) (les mots de Rust expliqués).

---

## ⚙️ Pré-requis : le compilateur Rust

Tu as besoin de **`rustc`** (le compilateur) et **`cargo`** (le gestionnaire de projet),
tous deux installés par l'outil officiel **`rustup`**. Vérifie s'ils sont déjà là :

```bash
rustc --version
cargo --version
```

Sinon, voir les instructions d'installation dans [`00_demarrer`](./00_demarrer/).

## ▶️ Compiler et lancer un programme

Deux manières de faire.

```bash
# a) Avec rustc (compilateur direct, pratique pour un seul fichier)
#    -o donne le NOM de l'exécutable à créer
rustc rust/00_demarrer/premier_programme.rs -o premier && ./premier

# b) Avec cargo (l'outil de projet, recommandé pour les vrais projets)
cargo new mon_projet   # crée un dossier prêt à l'emploi
cd mon_projet
cargo run              # compile PUIS lance, en une seule commande
```

> Dans ce parcours d'apprentissage, on utilise surtout `rustc` (un fichier = un programme),
> car c'est plus simple pour découvrir. `cargo` deviendra ton ami pour les vrais projets.

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).

## 🔐 Module sécurité (pentest)

Pour découvrir le rôle de ce langage en **sécurité informatique** — à usage
**strictement éducatif et autorisé** (tes propres systèmes, CTF, labs) — voir le
dossier [`pentest/`](./pentest/).
