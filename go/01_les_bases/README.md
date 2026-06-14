# Module 01 — Les bases du Go

Les mêmes briques fondamentales que dans tout langage (variables, conditions, boucles,
fonctions), mais à la **façon de Go** : un typage **statique** (chaque variable a un type),
souvent **deviné automatiquement**, et une syntaxe **épurée** (pas de point-virgule visible,
pas de parenthèses autour des conditions).

> Fichiers du module : `bases.go` (les briques) et `mini_calculatrice.go` (un mini-projet).

> ⚠️ **Important — deux fichiers, deux `func main`.** `bases.go` et `mini_calculatrice.go`
> sont dans le **même dossier** et déclarent **chacun** `package main` et `func main`. C'est
> OK **à condition de les lancer SÉPARÉMENT**, un seul fichier à la fois :
> ```bash
> go run go/01_les_bases/bases.go              # lance UNIQUEMENT bases.go
> go run go/01_les_bases/mini_calculatrice.go  # lance UNIQUEMENT la calculatrice
> ```
> (On ne crée pas de fichier `go.mod` : inutile pour lancer un seul fichier avec `go run`.)

---

## 1. Variables et types

En Go, il y a **deux façons** de créer une variable :

```go
var age int = 30   // forme longue : "var", le nom, le TYPE (int), la valeur
age2 := 30         // forme courte : Go DEVINE le type tout seul (ici : int)
```

La forme courte **`:=`** est la plus utilisée : elle crée une variable **et** lui donne une
valeur, en laissant Go deviner le type. (Elle ne marche qu'**à l'intérieur** d'une fonction.)

Les **types de base** à connaître :

| Type | Sert à | Exemple |
|------|--------|---------|
| `int` | nombre entier | `42` |
| `float64` | nombre à virgule (décimal) | `3.14` |
| `string` | du texte (entre guillemets `"`) | `"salut"` |
| `bool` | vrai / faux | `true`, `false` |

> 💡 Contrairement au C, Go a un **vrai type booléen** : `bool`, avec `true` et `false`.

> ⚠️ Go est strict : une variable **déclarée mais jamais utilisée** provoque une **erreur de
> compilation**. Pareil pour un `import` inutile. Ça garde le code propre.

---

## 2. Afficher avec `fmt`

Deux outils principaux dans le paquet `fmt` :

### `fmt.Println` — simple, ajoute un retour à la ligne

```go
fmt.Println("Age :", age)   // affiche les valeurs séparées par une espace + saut de ligne
```

### `fmt.Printf` — contrôle précis avec des « verbes de format »

Comme le `printf` du C : tu places un **verbe** commençant par `%`, et tu donnes la valeur
après la virgule. **Attention : `Printf` n'ajoute PAS de saut de ligne**, il faut mettre `\n`.

```go
fmt.Printf("Age : %d ans\n", age)        // %d = un entier
fmt.Printf("Taille : %.2f m\n", taille)  // %f = un décimal ; .2 = 2 chiffres après la virgule
fmt.Printf("Nom : %s\n", "Sam")          // %s = une chaîne de caractères (string)
```

| Verbe | Type affiché |
|-------|--------------|
| `%d` | entier (`int`) |
| `%f` | décimal (`float64`) |
| `%s` | chaîne de caractères (`string`) |
| `%t` | booléen (`bool`) |

---

## 3. Conditions : `if` / `else if` / `else`

```go
note := 12
if note >= 16 {              // PAS de parenthèses autour de la condition…
    fmt.Println("Tres bien")
} else if note >= 10 {       // …mais les accolades { } sont OBLIGATOIRES
    fmt.Println("Recu")
} else {
    fmt.Println("A retravailler")
}
```

Différences notables : en Go la condition est **sans parenthèses** `( )`, mais les accolades
`{ }` sont **toujours obligatoires** (même pour une seule ligne). Les comparaisons sont les
mêmes qu'ailleurs : `==`, `!=`, `<`, `>`, `<=`, `>=`, et les opérateurs logiques `&&` (ET),
`||` (OU), `!` (NON).

---

## 4. Boucles : Go n'a QUE `for`

Surprise : **Go n'a pas de `while`** ! Le mot-clé `for` fait tout, sous **3 formes** :

```go
// Forme 1 : la boucle "classique" (début ; condition ; pas) — comme le for du C.
for i := 0; i < 3; i++ {        // i++ veut dire "i = i + 1"
    fmt.Println("Tour", i)      // affiche 0, 1, 2
}

// Forme 2 : "for" avec seulement une condition = le "while" des autres langages.
compteur := 0
for compteur < 3 {              // tant que la condition est vraie
    fmt.Println("compteur =", compteur)
    compteur++                  // sans ça, boucle infinie !
}

// Forme 3 : "for" tout seul = boucle infinie, qu'on arrête avec "break".
n := 0
for {                           // pas de condition = tourne sans fin…
    if n == 2 {
        break                   // …jusqu'à ce que "break" la stoppe
    }
    fmt.Println("n =", n)
    n++
}
```

Une seule structure à retenir, trois usages : voilà la **simplicité** revendiquée par Go.

---

## 5. Fonctions : `func nom(params) typeDeRetour`

```go
// 'func' déclare une fonction. (a int, b int) = deux paramètres entiers.
// Le 'int' APRÈS les parenthèses = le type de la valeur RENVOYÉE.
func additionner(a int, b int) int {
    return a + b   // 'return' renvoie le résultat
}

// Une fonction qui ne renvoie rien n'indique aucun type de retour :
func saluer() {
    fmt.Println("Bonjour !")
}
```

> 💡 En Go, l'ordre n'a pas d'importance : tu peux appeler une fonction définie **plus bas**
> dans le fichier (contrairement au C qui exige qu'elle soit connue avant).

---

## ▶️ À toi de jouer

⚠️ On lance les fichiers **un par un** (chacun a son propre `func main`) :

```bash
# Le fichier des briques de base
go run go/01_les_bases/bases.go

# Le mini-projet calculatrice (tape l'opération puis deux nombres)
go run go/01_les_bases/mini_calculatrice.go
```

Lis les deux fichiers, puis **modifie-les** et **relance** : ajoute une opération, change les
conditions, crée ta propre fonction.

➡️ La suite du parcours (slices, maps, structures…) arrivera dans le même style.
