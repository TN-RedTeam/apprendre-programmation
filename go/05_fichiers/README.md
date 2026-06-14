# Module 05 — Lire & écrire des fichiers

Jusqu'ici, nos programmes affichaient tout à l'écran et **oubliaient tout** en se fermant.
Dans ce module, on apprend à **garder** des informations : écrire dans un **fichier** sur le
disque, puis le **relire** plus tard.

> Fichiers du module : `ecrire.go` (écrit quelques lignes dans un fichier) et `lire.go`
> (relit ce fichier ligne par ligne et l'affiche).
> ⚠️ Chaque fichier a son propre `func main` : on les lance **séparément** avec `go run`.

---

## 1. Écrire d'un coup : `os.WriteFile`

La façon la plus simple d'écrire un fichier, c'est de tout donner **en une seule fois** :

```go
contenu := "première ligne\ndeuxième ligne\n"
err := os.WriteFile("exemples/notes.txt", []byte(contenu), 0644)
```

Trois choses à comprendre :

- **`"exemples/notes.txt"`** : le *chemin* du fichier (où l'écrire).
- **`[]byte(contenu)`** : un fichier ne stocke pas du « texte », mais des **octets** (`byte`).
  On *convertit* donc notre texte avec `[]byte(...)`. C'est une formule à recopier telle quelle.
- **`0644`** : les *permissions* du fichier (qui a le droit de lire/écrire). `0644` = « moi je
  peux lire et écrire, les autres peuvent seulement lire ». Une valeur standard à recopier.

Et **comme toute opération qui peut échouer** (disque plein, dossier manquant…), `os.WriteFile`
renvoie une `error`. On la teste **tout de suite**, avec le réflexe du module 04 :

```go
if err != nil {
    fmt.Println("Erreur :", err)
    return
}
```

---

## 2. Lire d'un coup : `os.ReadFile`

Symétrique de l'écriture : `os.ReadFile` lit **tout** le fichier en une fois.

```go
donnees, err := os.ReadFile("exemples/notes.txt")
if err != nil { ... }
fmt.Println(string(donnees))   // octets -> texte avec string(...)
```

Là encore, le fichier arrive sous forme d'**octets** (`[]byte`). On reconvertit en texte avec
`string(...)` (l'opération inverse de `[]byte(...)`).

> 💡 `ReadFile` est parfait pour un **petit** fichier. Mais s'il est énorme, tout charger en
> mémoire d'un coup est lourd. D'où la méthode suivante.

---

## 3. Lire **ligne par ligne** : `os.Open` + `bufio.NewScanner`

Pour lire un fichier **morceau par morceau** (ici, ligne par ligne), on procède en deux temps :

```go
fichier, err := os.Open("exemples/notes.txt")   // 1. ouvrir (ne lit rien encore)
if err != nil { ... }
defer fichier.Close()                            // 2. refermer à la fin, quoi qu'il arrive

scanner := bufio.NewScanner(fichier)             // 3. un "lecteur de lignes"
for scanner.Scan() {                             // 4. tant qu'il y a une ligne...
    ligne := scanner.Text()                      //    ...on la récupère (sans le \n)
    fmt.Println(ligne)
}
```

- **`os.Open`** ouvre le fichier en lecture (il **renvoie une `error`** : et si le fichier
  n'existe pas ?). On teste donc `if err != nil`.
- **`defer fichier.Close()`** : `defer` veut dire « fais ça **plus tard**, juste avant de
  quitter la fonction ». Très pratique pour **ne jamais oublier de refermer** le fichier.
- **`bufio.NewScanner`** crée un objet qui sait découper le fichier ; par défaut, **par lignes**.
- **`scanner.Scan()`** avance d'une ligne et renvoie `true` tant qu'il en reste ;
  **`scanner.Text()`** donne le texte de la ligne courante.

---

## 🆚 Comparaison avec Python

En Python, lire un fichier ligne par ligne est très court :

```python
with open("exemples/notes.txt") as f:   # 'with' referme tout seul
    for ligne in f:
        print(ligne.rstrip())
```

En Go, c'est un peu **plus verbeux** (ouvrir, `defer Close`, scanner, tester l'erreur), mais
chaque étape est **explicite** : tu vois exactement quand le fichier s'ouvre, se ferme, et
comment une erreur est gérée. Le `defer fichier.Close()` joue le rôle du `with` de Python.

---

## ▶️ À toi de jouer

⚠️ **Lance les commandes DEPUIS LA RACINE du dépôt** (le dossier qui contient `go/`). Le chemin
`exemples/notes.txt` est *relatif* à l'endroit d'où tu lances : il sera donc créé à la racine.

```bash
# 1. D'abord écrire le fichier (crée exemples/notes.txt) :
go run go/05_fichiers/ecrire.go

# 2. Ensuite le relire ligne par ligne :
go run go/05_fichiers/lire.go
```

`lire.go` doit afficher **exactement** ce que `ecrire.go` vient d'écrire. Si tu lances `lire.go`
**avant** `ecrire.go`, le fichier n'existe pas encore : le programme te le dit proprement
(grâce au `if err != nil`).

> 🧹 Le dossier `exemples/` est **généré** par le programme et **ignoré par git** (il n'a pas à
> être versionné). Tu peux le supprimer sans crainte : `rm -rf exemples`.

Essaie ensuite de **modifier** `ecrire.go` (ajoute des lignes, change le texte) puis relance les
deux commandes : tu verras le nouveau contenu ressortir.

➡️ La suite du parcours arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe Go en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots de Go expliqués simplement.
