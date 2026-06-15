# 🃏 Aide-mémoire Rust (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle de Rust. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `01_les_bases`, `02_propriete`…

> 🧠 Rappels de fond : les variables sont **immuables par défaut** (`mut` pour modifier),
> chaque instruction se termine par **`;`**, les blocs sont entre **accolades `{ }`**, et
> il faut **compiler** avant de pouvoir exécuter.

---

## Compiler et lancer

```bash
# rustc : un fichier -> un exécutable
rustc programme.rs -o programme   # compile programme.rs -> exécutable "programme"
./programme                        # lance l'exécutable

# cargo : l'outil de projet (recommandé pour les vrais projets)
cargo new mon_projet   # crée un projet
cargo run              # compile PUIS lance
cargo check            # vérifie que ça compile, SANS produire l'exécutable (rapide)
```

## Structure type d'un programme

```rust
use std::collections::HashMap;   // 1. importer les outils dont on a besoin

fn additionner(a: i32, b: i32) -> i32 {   // 2. fonctions (avant OU après main)
    a + b   // dernière ligne SANS ';' = valeur renvoyée
}

fn main() {            // 3. main : le point de départ obligatoire
    // ... ton code ...
}
```

## Variables : immuables par défaut

```rust
let age = 30;           // immuable : on ne peut PAS la réassigner
let mut compteur = 0;   // 'mut' : on a le droit de la modifier
compteur += 1;
const TVA: f64 = 0.20;  // constante (EN MAJUSCULES, type obligatoire)
```

## Types de base

```rust
let age: i32 = 30;          // entier signé (i8/i16/i32/i64)
let n: u32 = 5;             // entier NON signé (positif : u8/u16/u32/u64)
let taille: f64 = 1.68;     // nombre à virgule (f32/f64)
let initiale: char = 'A';   // UN caractère, entre apostrophes simples ' '
let actif: bool = true;     // booléen : true / false
let prenom: &str = "Alice"; // texte fixe (tranche de chaîne)
```

> Le type est souvent **deviné** : `let x = 5;` suffit. On l'écrit après `:` si besoin.

## Afficher : println!

```rust
println!("Bonjour !");                 // texte simple
println!("Age : {}", age);             // chaque {} remplacé dans l'ordre
println!("{} a {} ans", prenom, age);  // plusieurs valeurs
println!("{:?}", liste);               // {:?} = affichage "debug" (Vec, struct…)
```

## Ownership & emprunts (le cœur de Rust)

```rust
let a = String::from("salut");
let b = a;            // MOVE : 'a' n'est plus utilisable (b possède la donnée)

fn lire(s: &String) {}        // EMPRUNT immuable : on regarde sans posséder
fn modifier(s: &mut String) {} // EMPRUNT mutable : on a le droit de modifier
lire(&a);                      // on prête avec &
modifier(&mut a);              // on prête en écriture avec &mut
```

> Règle : **un seul** emprunt mutable `&mut` à la fois, OU plusieurs `&` immuables. Jamais les deux.

## Conditions (if est une expression)

```rust
if note >= 16 {
    println!("Tres bien");
} else if note >= 10 {        // 'else if', pas 'elif'
    println!("Recu");
} else {
    println!("A retravailler");
}

let message = if reussi { "gagne" } else { "perdu" };  // if renvoie une valeur
```

## Boucles

```rust
for i in 0..3 { println!("{}", i); }   // 0, 1, 2 (le 3 est EXCLU)
for x in &liste { println!("{}", x); } // parcourir en EMPRUNTANT

let mut n = 0;
while n < 5 { n += 1; }                 // tant que la condition est vraie

loop { if fini { break; } }             // boucle infinie, on en sort avec 'break'
```

## Fonctions

```rust
fn additionner(a: i32, b: i32) -> i32 {  // paramètres typés, -> type de retour
    a + b                                 // pas de ';' = valeur renvoyée
}
fn saluer() {                             // sans '->' : ne renvoie rien
    println!("Bonjour !");
}
```

## struct, enum, match

```rust
struct Personne { nom: String, age: u32 }   // regrouper des champs
let p = Personne { nom: String::from("Alice"), age: 30 };
println!("{}", p.nom);                       // accès par '.'

enum Statut { AFaire, Terminee }             // un choix parmi des cas

match statut {                               // réagir selon le cas (exhaustif)
    Statut::AFaire   => println!("[ ]"),
    Statut::Terminee => println!("[x]"),
}
```

## Collections

```rust
let mut v: Vec<i32> = Vec::new();   // liste qui grandit
v.push(10); v.push(20);             // ajouter
v[0];                               // accès par indice
v.len();                            // longueur

let mut s = String::from("Salut");  // texte modifiable
s.push_str(" toi");                 // concaténer

use std::collections::HashMap;
let mut annuaire: HashMap<String, i32> = HashMap::new();
annuaire.insert(String::from("Alice"), 30);   // clé -> valeur
annuaire.get("Alice");                          // renvoie un Option
```

## Option & Result (+ l'opérateur ?)

```rust
// Option<T> : une valeur peut MANQUER
let trouve: Option<i32> = liste.iter().find(|&&x| x > 10).copied();
match trouve { Some(v) => /* ... */, None => /* ... */ }

// Result<T, E> : une opération peut ÉCHOUER
fn parser(txt: &str) -> Result<i32, std::num::ParseIntError> {
    let n: i32 = txt.parse()?;   // '?' : si Err, renvoie l'erreur tout de suite
    Ok(n)                        // sinon on renvoie Ok(...)
}

panic!("message");   // arrêt immédiat du programme (à éviter en vrai code)
```

## Traits & génériques

```rust
trait Descriptible {                    // un CONTRAT (capacités attendues)
    fn decrire(&self) -> String;
}
impl Descriptible for Personne {        // un type "signe" le contrat
    fn decrire(&self) -> String { format!("{}", self.nom) }
}

fn plus_grand<T: PartialOrd>(a: T, b: T) -> T {   // <T> = code "à trous"
    if a > b { a } else { b }
}
```

## Closures & itérateurs

```rust
let doubler = |x: i32| x * 2;     // mini-fonction sur place (|params| corps)

let total: i32 = (1..=5)
    .filter(|x| x % 2 == 0)        // garde les pairs
    .map(|x| x * 10)               // transforme chacun
    .sum();                        // additionne (collect() pour faire un Vec)
```

## Threads (concurrence)

```rust
use std::thread;
let h = thread::spawn(|| {        // lance un fil parallèle
    println!("dans le thread");
});
h.join().unwrap();                // ATTENDRE la fin du thread

use std::sync::{Arc, Mutex};      // partager une donnée entre threads, en sûreté
let donnee = Arc::new(Mutex::new(0));
*donnee.lock().unwrap() += 1;     // .lock() pour accéder, en exclusivité
```

---

➡️ Voir aussi : [GLOSSAIRE.md](./GLOSSAIRE.md) pour le sens des mots de Rust.
