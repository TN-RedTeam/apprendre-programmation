# Module 03 — Les structs et les méthodes

Jusqu'ici, une variable retenait **une seule information** (un nom, un âge), et un slice ou une
map regroupaient **plusieurs valeurs du même genre**. Mais comment décrire un **objet du monde
réel** qui possède **plusieurs informations DIFFÉRENTES** liées entre elles — une personne (un
nom *et* un âge), un rectangle (une largeur *et* une hauteur) ? C'est le rôle des **structs**.
Et pour leur donner des **comportements** (calculer, modifier…), on leur attache des
**méthodes**.

> Fichiers du module : `structs.go` (regrouper des champs) et `methodes.go` (attacher des
> comportements).

> ⚠️ **Important — deux fichiers, deux `func main`.** `structs.go` et `methodes.go` sont dans
> le **même dossier** et déclarent **chacun** `package main` et `func main`. C'est OK **à
> condition de les lancer SÉPARÉMENT**, un seul fichier à la fois :
> ```bash
> go run go/03_structs_methodes/structs.go    # lance UNIQUEMENT structs.go
> go run go/03_structs_methodes/methodes.go   # lance UNIQUEMENT methodes.go
> ```
> (On ne crée pas de fichier `go.mod` : inutile pour lancer un seul fichier avec `go run`.)

---

## 1. Les STRUCTS : regrouper des champs sous un même type

Un **struct** (prononce « strocte », pour *structure*) te permet de **regrouper plusieurs
informations liées** sous **un seul type que tu inventes**.

> 🪪 **Analogie : la fiche d'identité.** Une carte d'identité, ce n'est pas une seule donnée :
> c'est un nom **+** un prénom **+** une date de naissance **+** une photo, le tout sur **une
> même carte**. Un struct, c'est exactement ça : un **modèle de fiche** que tu remplis ensuite.

On déclare d'abord le **modèle** (le type), avec le mot-clé `type` :

```go
// On invente un nouveau type "Personne" qui regroupe deux CHAMPS.
type Personne struct {
    Nom string   // un champ "Nom", de type string
    Age int      // un champ "Age", de type int
}
```

`type Personne struct { ... }` se lit : « je crée un nouveau type appelé `Personne`, c'est une
structure qui contient un `Nom` (texte) et un `Age` (entier) ».

### Créer une instance (remplir une fiche)

Une fois le modèle défini, on peut fabriquer autant de **fiches** (on dit des **instances**)
que l'on veut :

```go
// On crée une instance en nommant chaque champ : c'est le plus clair.
p := Personne{Nom: "Sam", Age: 30}
```

### Accéder et modifier les champs avec le point `.`

Pour lire ou changer un champ, on écrit le nom de la variable, **un point `.`**, puis le nom
du champ :

```go
fmt.Println(p.Nom)   // LIRE : affiche "Sam"
p.Age = 31           // MODIFIER : Sam vient d'avoir un an
```

> 💡 **Struct vs Python.** En Python, on utiliserait souvent une **classe** (`class Personne:`)
> avec un `__init__`. En Go, pas de classe : on décrit juste les **champs** dans un `struct`,
> et le point `.` (`p.Nom`) fonctionne comme en Python (`p.nom`).

---

## 2. Les MÉTHODES : attacher un comportement à un type

Un struct **range des données**. Mais souvent on veut aussi des **actions** liées à ces
données : un `Rectangle` sait calculer son **aire**, un `CompteEnBancaire` sait **déposer** de
l'argent… Pour ça, Go propose les **méthodes** : ce sont des **fonctions attachées à un type**.

> 🛠️ **Analogie.** Une fonction « libre » est comme un outil posé dans un tiroir : utilisable
> sur n'importe quoi. Une **méthode** est comme un bouton **collé sur l'objet** lui-même : le
> bouton « calculer l'aire » est directement sur le rectangle.

### Le récepteur : ce qui « colle » la fonction au type

Une méthode ressemble à une fonction, avec **un petit bloc en plus, AVANT le nom** : le
**récepteur**. C'est lui qui dit « cette fonction appartient à ce type ».

```go
// (r Rectangle) = le RÉCEPTEUR : "cette méthode s'applique à un Rectangle qu'on appelle r".
func (r Rectangle) Aire() float64 {
    return r.Largeur * r.Hauteur   // on accède aux champs de r avec le point, comme avant
}
```

On l'appelle alors **sur l'objet**, avec le point `.` (comme un champ, mais avec des
parenthèses) :

```go
rect := Rectangle{Largeur: 4, Hauteur: 3}
fmt.Println(rect.Aire())   // affiche 12 — on a appuyé sur le "bouton" Aire du rectangle
```

> 💡 **Méthode vs Python.** Le `r` du récepteur joue exactement le rôle du `self` de Python.
> En Python : `def aire(self): return self.largeur * self.hauteur`. En Go, on déclare ce
> « self » **entre les parenthèses du récepteur**, et on choisit son nom (souvent une lettre).

### Récepteur VALEUR vs récepteur POINTEUR : copie ou vrai objet ?

C'est le point **le plus important** du module. Il existe **deux sortes** de récepteurs :

```go
func (r Rectangle) Aire() float64 { ... }       // récepteur VALEUR : reçoit une COPIE
func (r *Rectangle) Doubler() { ... }           // récepteur POINTEUR : reçoit le VRAI objet
```

- **Récepteur valeur `(r Rectangle)`** : la méthode reçoit une **photocopie** de l'objet. Elle
  peut la **lire** sans souci, mais si elle modifie cette copie, **l'original ne change pas**.
  Parfait pour **juste calculer/lire** (comme `Aire`).

- **Récepteur pointeur `(r *Rectangle)`** : le petit **`*`** signifie « le **vrai** objet, pas
  une copie ». La méthode travaille **directement sur l'original** : si elle modifie un champ,
  **le changement reste** après l'appel. Obligatoire dès qu'on veut **MODIFIER** l'objet.

> 🪪 **Analogie.** Récepteur valeur = on te donne une **photocopie** de la fiche : tu peux
> gribouiller dessus, l'originale reste intacte. Récepteur pointeur = on te donne **la fiche
> originale** : ce que tu écris dessus, ça compte pour de vrai.

> 💡 Bonne nouvelle : pour **appeler** une méthode à récepteur pointeur, tu écris la même chose
> que d'habitude (`rect.Doubler()`). Go ajoute le `&` (« prends l'adresse ») tout seul. Tu n'as
> qu'à mettre le `*` **dans la définition** de la méthode.

---

## 3. Go n'a pas de classes (et c'est voulu)

Si tu connais Java, C++ ou Python, tu as l'habitude des **classes** qui réunissent données
**et** comportements au même endroit. **Go n'a pas de classes.** À la place, il sépare :

| | Langages à classes (Python, Java…) | Go |
|--|------------------------------------|----|
| Les données | attributs **dans** la classe | champs d'un **`struct`** |
| Les comportements | méthodes **dans** la classe | fonctions avec un **récepteur** |
| Le « moi » courant | `self` / `this` | le **récepteur** (`r`, `p`…) |
| Héritage | oui | **non** (Go préfère la *composition*) |

En clair : un `struct` + des méthodes te donnent **l'essentiel** d'un objet, mais de façon
**plus simple** et plus explicite. C'est la philosophie habituelle de Go.

---

## ▶️ À toi de jouer

⚠️ On lance les fichiers **un par un** (chacun a son propre `func main`) :

```bash
# Le fichier sur les structs (regrouper des champs)
go run go/03_structs_methodes/structs.go

# Le fichier sur les méthodes (récepteur valeur vs pointeur)
go run go/03_structs_methodes/methodes.go
```

Lis les deux fichiers, puis **modifie-les** et **relance** : ajoute un champ au struct, crée
une nouvelle instance, écris une méthode `Perimetre()`, transforme une méthode de lecture en
méthode qui modifie (récepteur pointeur).

➡️ La suite du parcours (gestion des erreurs, petits projets…) arrivera dans le même style. En
attendant, garde sous la main l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
