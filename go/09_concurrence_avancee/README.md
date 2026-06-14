# Module avancé 09 — La concurrence avancée : `select` & worker pool

Au module 06, tu as appris à lancer des tâches « à côté » (**goroutines**), à les attendre
(**`sync.WaitGroup`**) et à les faire communiquer par des **channels** (les « tuyaux »). Ici on
monte d'un cran avec deux outils que les programmes Go sérieux utilisent tout le temps :
**`select`** (attendre sur plusieurs tuyaux à la fois) et le motif **worker pool** (une équipe
de travailleurs qui se partage une pile de tâches).

> Fichiers du module : `select.go` (choisir le premier channel prêt, + un timeout) et
> `worker_pool.go` (N travailleurs traitent M tâches).
> ⚠️ Chaque fichier a son propre `package main` et son propre `func main`, dans le **même
> dossier** : on les lance **séparément** avec `go run` (pas de `go.mod` ici, c'est voulu).

---

## 1. `select` : surveiller PLUSIEURS tuyaux à la fois

Avec un channel simple, `v := <-ch` attend **un seul** tuyau. Mais souvent on aimerait
surveiller **plusieurs** tuyaux **en même temps** et réagir au **premier** qui a quelque chose.
C'est exactement le rôle de **`select`** :

```go
select {
case v := <-ch1:
    // exécuté si ch1 est prêt en premier
case v := <-ch2:
    // exécuté si ch2 est prêt en premier
}
```

`select` **bloque** jusqu'à ce qu'**un** des cas soit prêt, puis exécute **ce cas-là** (et lui
seul). C'est comme un `switch`, mais au lieu de tester des valeurs, il **attend des channels**.

> 🏦 **Analogie : les guichets de banque.** Tu es devant **deux guichets** et tu ne sais pas
> lequel se libérera d'abord. Tu surveilles les **deux** et tu fonces vers **celui qui t'appelle
> en premier**. `select`, c'est ça : plusieurs guichets surveillés, on sert le premier prêt.

---

## 2. `select` + `time.After` : poser un TIMEOUT

Et si **aucun** tuyau ne répond ? On ne veut pas attendre **pour toujours**. La fonction
**`time.After(d)`** renvoie un **channel** qui « sonne » (envoie une valeur) après la durée `d`.
En l'ajoutant comme un cas du `select`, on obtient un **délai maximum** :

```go
select {
case v := <-ch:
    fmt.Println("reçu :", v)
case <-time.After(100 * time.Millisecond):
    fmt.Println("timeout : trop long, on abandonne")
}
```

Si `ch` répond avant 100 ms, c'est le premier cas. Sinon, la minuterie « sonne » et c'est le
cas timeout qui gagne. **Plus jamais d'attente infinie.**

> ⏱️ **Analogie.** Tu attends un ami au café, mais tu te dis « si dans 10 minutes il n'est pas
> là, je commande sans lui ». Le `time.After`, c'est ton réveil de 10 minutes.

C'est ce que montre **`select.go`** : une course gagnée par le tuyau le plus rapide, puis un
timeout déclenché face à un tuyau trop lent. La sortie est **déterministe** (les durées sont
choisies pour que le résultat soit toujours le même).

---

## 3. Le motif WORKER POOL (« pool de travailleurs »)

Imagine une **pile de tâches** à traiter et une **équipe** pour s'en occuper. Plutôt qu'un seul
travailleur qui fait tout, on en met **plusieurs** qui **se partagent la pile** : ça va plus
vite, et personne ne traite deux fois la même tâche.

Les briques, toutes déjà connues du module 06 :

- un channel **`jobs`** = la **pile de tickets** à faire ;
- **N goroutines** « travailleuses » (les **workers**) qui **piochent** dans `jobs` ;
- un channel **`resultats`** où chaque worker **dépose** ce qu'il a produit ;
- un **`sync.WaitGroup`** pour **attendre** que **tous** les workers aient fini.

> 🎫 **Analogie : l'équipe au support.** Une pile de tickets clients (`jobs`). Trois agents
> (workers) prennent chacun un ticket, le traitent, en reprennent un autre… jusqu'à ce que la
> pile soit vide. Les réponses finies vont dans un bac (`resultats`). Le channel garantit que
> **deux agents ne prennent jamais le même ticket**.

### Le squelette du motif

```go
jobs := make(chan int, nbJobs)
resultats := make(chan int, nbJobs)
var wg sync.WaitGroup

// 1) démarrer N workers
for id := 1; id <= nbWorkers; id++ {
    wg.Add(1)
    go worker(id, jobs, resultats, &wg) // chacun pioche dans jobs, écrit dans resultats
}

// 2) envoyer les tâches, puis fermer jobs
for n := 1; n <= nbJobs; n++ { jobs <- n }
close(jobs)                 // "plus de tickets" -> les workers s'arrêteront

// 3) fermer resultats QUAND tous les workers ont fini
go func() { wg.Wait(); close(resultats) }()

// 4) collecter
for r := range resultats { /* ... */ }
```

Le point délicat (point 3) : c'est une **goroutine séparée** qui attend la fin des workers
(`wg.Wait()`) **puis** ferme `resultats`. Sans elle, le `for ... range resultats` attendrait
**pour toujours** un tuyau jamais fermé.

C'est ce que montre **`worker_pool.go`** : 3 workers élèvent au carré les nombres 1 à 9, et on
collecte la **somme des carrés**. Quel que soit l'ordre où les workers piochent, la somme est
**toujours 285** (1+4+9+…+81). Résultat **déterministe**.

---

## 🆚 Lien avec le module 06

| Module 06 | Module 09 (ici) |
|-----------|-----------------|
| Attendre **un** channel (`<-ch`) | Attendre **plusieurs** channels (`select`) |
| Une goroutine fait une tâche | **N** goroutines se **partagent** M tâches |
| `WaitGroup` pour attendre la fin | `WaitGroup` pour fermer `resultats` au bon moment |
| Pas de limite de temps | **Timeout** avec `time.After` |

Rien de magique : on **assemble** les briques de base (goroutines, channels, `WaitGroup`) pour
fabriquer des motifs plus puissants.

---

## ▶️ À toi de jouer

⚠️ Les deux fichiers ont **chacun** leur `package main` et leur `func main`, dans le **même
dossier**. On ne peut donc **pas** lancer le dossier entier : on les lance **séparément**, en
nommant le fichier. (Pas de `go.mod` ici, c'est volontaire : on reste sur de simples fichiers.)

Lance les commandes **DEPUIS LA RACINE** du dépôt (le dossier qui contient `go/`) :

```bash
# select : choisir le premier channel prêt, puis un timeout :
go run go/09_concurrence_avancee/select.go

# worker pool : 3 workers traitent 9 jobs, somme des carrés = 285 :
go run go/09_concurrence_avancee/worker_pool.go
```

La sortie est **déterministe** : relance plusieurs fois, tu obtiendras toujours le même total.
(Dans `worker_pool.go`, l'**ordre des lignes** des workers peut varier d'une fois à l'autre —
c'est normal, ils travaillent en parallèle — mais la **somme finale** ne change jamais.)

> 🧪 **Expériences.**
> - Dans `select.go`, mets le timeout à `400 * time.Millisecond` (au lieu de 100) : cette fois
>   le tuyau « trainard » (300 ms) répond **avant** le réveil, et c'est lui qui gagne.
> - Dans `worker_pool.go`, change `nbWorkers` (1, 5, 9…) : la somme reste **285**, seul le
>   partage du travail change.

➡️ D'autres modules avancés arriveront dans le même style.

## 📎 Ressources

- [`../06_concurrence/`](../06_concurrence/) — les bases : goroutines, `WaitGroup`, channels.
- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe Go en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots de Go expliqués simplement.
