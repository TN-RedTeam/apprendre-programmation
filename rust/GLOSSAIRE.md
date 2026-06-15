# 📖 Glossaire — les mots de Rust expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours de Rust ? Cherche-le ici. Les
termes sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**Argument** — La valeur concrète que tu donnes à une fonction quand tu l'appelles. Dans
`additionner(7, 5)`, `7` et `5` sont les arguments. (Côté définition, on parle de *paramètre*.)

**Cargo** — Le **gestionnaire de projet** de Rust : il crée des projets (`cargo new`), compile
et lance (`cargo run`), vérifie (`cargo check`) et gère les **dépendances** (les *crates*).
C'est l'outil de référence pour les vrais projets.

**Closure** — Une **mini-fonction sans nom**, écrite directement là où on en a besoin :
`|x| x * 2`. Les `|...|` remplacent les parenthèses des paramètres. Elle peut **capturer** des
variables de l'extérieur. Très utilisée avec les itérateurs.

**Compilateur** (`rustc`) — Le programme qui **traduit** ton code `.rs` en langage machine. En
Rust il est particulièrement bavard et bienveillant : il attrape beaucoup de bugs **avant**
l'exécution et explique en clair quoi corriger.

**Compilation** — L'étape de **traduction** du code source en exécutable. Spécificité de Rust
(comme le C) : tant que ça ne compile pas, rien ne tourne. C'est normal — et utile.

**Crate** — Une **bibliothèque** ou un **paquet** Rust : une boîte à outils réutilisable. La
*bibliothèque standard* (`std`) en est une ; les autres se récupèrent via Cargo.

**Emprunt** (*borrow*) — Le fait de **prêter** une donnée sans en transférer la propriété, avec
le `&`. Comme prêter un livre : l'autre peut le lire (`&`) ou le modifier (`&mut`), mais le
propriétaire reste le même. À la fin de l'emprunt, le propriétaire récupère sa donnée.

**Enum** (énumération) — Un type qui représente **un choix parmi plusieurs cas** :
`enum Statut { AFaire, Terminee }`. Une valeur de ce type est exactement **l'un** des cas. On
réagit dessus avec `match`.

**Fonction** (`fn`) — Un bloc de code nommé et réutilisable. On déclare le **type de chaque
paramètre** et, après `->`, le **type de retour**. La dernière expression sans `;` est la
valeur renvoyée.

**Génériques** (`<T>`) — Du code **« à trous »** qui marche pour **plusieurs types** à la fois.
Le `T` est un type qu'on remplit au moment de l'usage : `Vec<T>` devient `Vec<i32>`,
`Vec<String>`… On évite ainsi de réécrire la même fonction pour chaque type.

**Immuabilité** — En Rust, une variable est **immuable par défaut** : une fois créée, on ne
peut **pas** la réassigner. Il faut ajouter `mut` (`let mut x = 0;`) pour avoir le droit de la
modifier. C'est l'inverse de Python/C, et ça évite beaucoup de bugs.

**Lifetime** (*durée de vie*) — La **portée pendant laquelle un emprunt reste valide**. Le
compilateur la vérifie pour garantir qu'on n'utilise jamais une donnée déjà libérée. Notion
avancée : au début, le compilateur la déduit tout seul la plupart du temps.

**main** — La fonction de **départ** obligatoire : l'exécution du programme commence toujours
par `fn main()`. (Pas de `int` ni de `return 0` comme en C.)

**`match`** — Un aiguillage **exhaustif** : on traite **chaque** cas possible d'une valeur
(souvent un `enum`, un `Option` ou un `Result`). Le compilateur **refuse** de compiler si tu
oublies un cas — un garde-fou très précieux.

**Move** (déplacement) — Quand on assigne une donnée « lourde » (comme une `String`) à une
autre variable, Rust **transfère la propriété** : l'ancienne variable n'est plus utilisable.
Ça évite que deux variables croient posséder la même donnée.

**Option<T>** — Un type qui dit « il y a **peut-être** une valeur ». Soit `Some(v)` (il y a la
valeur `v`), soit `None` (rien). Rust **oblige** à traiter le cas `None` : fini les `null`
oubliés qui font planter.

**Ownership** (propriété) — **LA** notion centrale de Rust. Chaque donnée a **un seul
propriétaire** ; quand le propriétaire disparaît, la donnée est **libérée automatiquement**.
C'est ce qui rend Rust sûr en mémoire **sans garbage collector** et sans `free` manuel.

**panic!** — Un **arrêt immédiat** du programme quand une erreur irrécupérable survient (ou
qu'on l'a demandé avec `panic!("...")`). À réserver aux cas vraiment exceptionnels : pour les
erreurs normales, on préfère `Result`.

**Paramètre** — Le nom d'une entrée dans la *définition* d'une fonction :
`fn additionner(a: i32, b: i32)` → `a` et `b` sont des paramètres. (La valeur fournie à
l'appel est l'*argument*.)

**println!** — La « fonction » (en fait une **macro**, d'où le `!`) qui **affiche** du texte.
Chaque `{}` est remplacé, dans l'ordre, par une valeur donnée ensuite. `{:?}` donne un
affichage « debug ».

**Result<T, E>** — Un type qui dit « l'opération a **réussi ou échoué** ». Soit `Ok(v)` (succès
avec la valeur `v`), soit `Err(e)` (échec avec l'erreur `e`). L'échec est **visible dans le
type** : impossible de l'oublier.

**rustc** — Le **compilateur** Rust en ligne de commande : `rustc fichier.rs -o nom` produit
l'exécutable `nom`. Pratique pour un seul fichier (c'est ce qu'on utilise dans ce parcours).

**rustup** — L'**installateur officiel** de la chaîne d'outils Rust : il met en place `rustc`,
`cargo` et permet de les mettre à jour.

**struct** (structure) — Un modèle qui **regroupe plusieurs données** sous un même nom, comme
une fiche d'identité : `struct Personne { nom: String, age: u32 }`. On accède aux champs avec
le point : `p.nom`.

**Trait** — Un **contrat** : une liste de capacités qu'un type s'engage à fournir (« savoir se
décrire »). Tout type qui **implémente** (`impl`) le trait « a le permis ». C'est l'équivalent
Rust des *interfaces* d'autres langages.

**Type** — La nature d'une valeur. En Rust les types sont **statiques** (fixés à la
compilation) mais souvent **devinés** : `let x = 5;` suffit, le compilateur déduit `i32`.

**`unwrap()`** — Une méthode rapide qui **sort la valeur** d'un `Option`/`Result`… mais
**panique** si c'est `None`/`Err`. Pratique pour apprendre ou prototyper, à éviter en vrai code
(on préfère `match` ou `?`).

**Variable** — Une boîte étiquetée qui retient une valeur. On la crée avec `let`. **Immuable
par défaut** : ajoute `mut` pour pouvoir la modifier.

**`?` (point d'interrogation)** — Un raccourci sur un `Result` : si c'est `Ok(v)`, il sort `v` ;
si c'est `Err(e)`, il **arrête la fonction** et renvoie l'erreur tout de suite. Évite d'écrire
un `match` à chaque appel qui peut échouer.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi [AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md)
pour la syntaxe.
