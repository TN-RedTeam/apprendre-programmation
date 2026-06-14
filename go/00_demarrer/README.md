# Module 00 — Démarrer en Go : lancer son premier programme

Avant d'écrire beaucoup de code, comprenons **la structure minimale** d'un programme Go et
**comment le lancer**. Ce module est court : un premier programme à exécuter à la fin.

---

## 1. Compiler, mais sans s'en rendre compte

L'ordinateur ne comprend pas directement le texte que tu écris (`fmt.Println(...)`). Comme en
C, il faut une étape de **traduction en langage machine** appelée **compilation**.

La grande différence avec le C, c'est que Go peut faire **tout en une seule commande** :

```
   premier_programme.go   ──[ go run ]──►   compilation + exécution   ──►   ça tourne
   (TON code, lisible)      automatique      (Go s'occupe de tout)
```

> 📌 Conséquence importante (comme en C) : si ton code contient une faute, **Go refuse de
> compiler** et t'affiche une erreur. Rien ne s'exécute tant que ça ne compile pas. C'est
> normal et utile : beaucoup d'erreurs sont attrapées *avant* l'exécution.

---

## 2. La structure minimale d'un programme Go

Voici le plus petit programme Go utile, décortiqué :

```go
package main          // (1) ce programme est un programme "principal" (lançable)

import "fmt"          // (2) on importe la boîte à outils d'affichage (fmt)

func main() {         // (3) func main : le POINT DE DÉPART du programme
    fmt.Println("Bonjour")  // (4) afficher du texte (Println = "print line")
}
```

1. **`package main`** : en Go, le code est rangé en *paquets* (*packages*). Le paquet spécial
   `main` indique : « ceci est un programme **exécutable** » (et non une bibliothèque). Tout
   programme lançable commence par `package main`.
2. **`import "fmt"`** : charge le paquet `fmt` (*format*), qui contient les outils d'affichage
   comme `Println`. C'est l'équivalent d'un `import` en Python.
3. **`func main()`** : **tout programme Go démarre par la fonction `main`.** C'est le point
   d'entrée. Les accolades `{ }` délimitent son contenu.
4. **`fmt.Println(...)`** : affiche du texte **suivi d'un retour à la ligne automatique**
   (`Println` = *print line*). Pas besoin de `\n` à la fin : c'est inclus.

> 💬 Les commentaires en Go s'écrivent `// sur une ligne` ou `/* sur plusieurs lignes */`.
> Le compilateur les ignore : ils sont là pour les humains.

> ⚠️ Go est **strict** : si tu importes un paquet **sans l'utiliser** (ou déclares une variable
> jamais utilisée), il **refuse de compiler**. Ça force un code propre.

---

## 3. Lancer le programme

Une fois le fichier `premier_programme.go` écrit, **une seule commande** suffit :

```bash
go run go/00_demarrer/premier_programme.go
```

`go run` **compile puis exécute** d'un coup. Pas d'exécutable à gérer, pas de `./`.

> Pour fabriquer un vrai fichier exécutable à garder, on utiliserait `go build` (voir le
> [README du parcours](../README.md)). Pour apprendre, `go run` suffit.

---

## ▶️ À toi de jouer

Lance le programme de ce module :

```bash
go run go/00_demarrer/premier_programme.go
```

Lis ensuite [`premier_programme.go`](./premier_programme.go) (tout est commenté), puis
**modifie le texte** et **relance** pour voir le changement. (Avec `go run`, pas besoin de
« recompiler » à la main : c'est automatique à chaque lancement.)

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
