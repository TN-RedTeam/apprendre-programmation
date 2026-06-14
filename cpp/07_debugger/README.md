# Module 07 — Débugger : trouver et corriger les bugs en C++

Un bug, ce n'est **pas un échec** : c'est une piste. En C++, deux moments te
parlent : le **compilateur** (qui refuse de traduire ton code tant qu'il y a une
faute) et le **plantage à l'exécution** (le fameux *segmentation fault*). Dans ce
module, on apprend à **lire** ces messages, à reconnaître les erreurs les plus
fréquentes, et à utiliser **gdb**, le débogueur qui exécute ton programme **pas à
pas**.

> Fichier du module : `demo_gdb.cpp` — un petit programme **correct et commenté**,
> parfait pour s'entraîner à le parcourir sous gdb. Lis le README, puis compile-le
> et lance-le.

---

## 1. D'abord, compile avec `-g` et `-Wall`

Deux options à mettre **dès maintenant**, pour toujours :

```bash
g++ -g -Wall -std=c++17 mon_programme.cpp -o mon_programme
```

- **`-Wall`** = *Warn all* : le compilateur t'affiche **tous les avertissements**
  (variable non utilisée, oubli d'initialisation…). Un *warning* n'empêche pas de
  compiler, mais c'est **très souvent** le signe d'un futur bug. **Lis-les.**
- **`-g`** = ajoute les **symboles de débogage** dans l'exécutable. Sans `-g`, gdb
  ne peut pas te montrer tes noms de variables ni tes numéros de ligne. **Obligatoire
  pour débugger.**

---

## 2. Lire un message d'erreur du COMPILATEUR (souvent long en C++)

En C++, les erreurs de compilation peuvent être **très longues** (surtout avec la
STL : des dizaines de lignes pour une seule faute). Pas de panique : **l'essentiel
est presque toujours sur la PREMIÈRE ligne d'erreur**.

Exemple — on a oublié un `;` :

```
mon_programme.cpp:5:24: error: expected ';' before 'return'
    5 |     std::cout << "Salut"
      |                        ^
      |                        ;
```

> 🔑 **La règle d'or : repère la PREMIÈRE ligne contenant `error:`.**

- Le **`error:`** te donne *quel* problème (`expected ';'` → il manque un
  point-virgule).
- Le début te donne *où* : `mon_programme.cpp:5:24` = **fichier**, **ligne 5**,
  colonne 24. Le petit `^` pointe l'endroit exact.

Astuce : corrige **la première erreur**, recompile, recommence. Une seule faute en
provoque souvent **dix autres** en cascade : la première réparée, les autres
disparaissent.

---

## 3. Les erreurs FRÉQUENTES en C++ (cause → solution)

| Erreur | Ce qui se passe | Symptôme | Solution |
|--------|-----------------|----------|----------|
| **Segmentation fault** | tu **déréférences un `nullptr`** (`*p` alors que `p` ne pointe sur rien) | le programme **plante** : `Segmentation fault (core dumped)` | vérifie `if (p != nullptr)` **avant** d'utiliser `*p` |
| **Accès hors limites d'un `std::vector`** | `v[10]` alors que `v` a moins de 11 éléments | comportement **imprévisible** (lit n'importe où, ne plante PAS toujours) | utilise **`v.at(10)`** : lève `std::out_of_range` au lieu de planter silencieusement |
| **Variable non initialisée** | `int total;` puis `total += x;` sans avoir mis `0` | résultat **aléatoire** (la variable contient « ce qui traînait » en mémoire) | **initialise toujours** : `int total = 0;` |
| **Oubli d'un `#include`** | tu utilises `std::vector` sans `#include <vector>` | erreur **compilateur** : `'vector' is not a member of 'std'` | ajoute le bon `#include` en haut du fichier |

> 💬 Côté Python, `v[10]` lèverait toujours un `IndexError` bien visible. En C++,
> `v[10]` ne vérifie **rien** par rapport à la vitesse : c'est pour ça que `.at()`
> existe, pour avoir un garde-fou. Pendant l'apprentissage, **préfère `.at()`**.

### Le danger du `nullptr` (le plus courant)

```cpp
int* p = nullptr;   // p ne pointe sur RIEN
std::cout << *p;    // 💥 Segmentation fault : on lit une adresse interdite
```

➡️ Un pointeur, c'est une **adresse mémoire**. `nullptr` veut dire « adresse vide ».
Déréférencer (`*p`) une adresse vide, c'est demander à lire une case qui n'existe
pas : le système coupe le programme (*segfault*). **Toujours vérifier avant.**

---

## 4. L'ESSENTIEL DE GDB : exécuter ton programme pas à pas

**gdb** (*GNU Debugger*) lance ton programme et te laisse **l'arrêter, l'avancer
ligne par ligne, et inspecter les variables**. C'est l'outil idéal quand un
programme plante sans que tu comprennes pourquoi.

D'abord, compile **avec `-g`**, puis lance gdb sur l'exécutable :

```bash
g++ -g -std=c++17 -Wall demo_gdb.cpp -o demo_gdb
gdb ./demo_gdb
```

Tu te retrouves dans une invite `(gdb)`. Voici les **7 commandes** à connaître :

| Commande | Raccourci | Ce qu'elle fait |
|----------|-----------|-----------------|
| `run` | `r` | **Lance** le programme |
| `break N` | `b N` | Met un **point d'arrêt** à la ligne N (le programme s'arrêtera là) |
| `bt` | — | *Backtrace* : la **pile des appels** — où es-tu et qui t'a appelé (génial après un plantage) |
| `next` | `n` | Exécute **la ligne suivante** (sans entrer dans les fonctions) |
| `print x` | `p x` | **Affiche** la valeur de la variable `x` |
| `continue` | `c` | **Reprend** jusqu'au prochain arrêt (ou la fin) |
| `quit` | `q` | **Quitte** gdb |

> 💬 C'est l'équivalent musclé des `print(...)` que tu ajoutais en Python : au lieu
> de modifier ton code pour afficher des valeurs, tu les inspectes « en direct ».

---

## 5. Exemple de session gdb (sur `demo_gdb.cpp`)

Voici à quoi ressemble une vraie séance. Tes saisies sont après le `(gdb)`.

```text
$ g++ -g -std=c++17 -Wall demo_gdb.cpp -o demo_gdb
$ gdb ./demo_gdb

(gdb) break moyenne          # on s'arrête à l'entrée de la fonction moyenne
Breakpoint 1 at 0x...: file demo_gdb.cpp, line 33.

(gdb) run                    # on lance le programme
Starting program: ./demo_gdb
Notes : 12 15 8 17 20

Breakpoint 1, moyenne (notes=...) at demo_gdb.cpp:33
33          int total = 0;

(gdb) next                   # on exécute la ligne courante, on passe à la suivante
34          for (int note : notes) {

(gdb) print total            # que vaut total à ce stade ?
$1 = 0

(gdb) continue               # on laisse tourner jusqu'au bout
Continuing.
Moyenne : 14.4
...
[Inferior 1 (process ...) exited normally]

(gdb) quit                   # on quitte gdb
```

Et si le programme **plantait** (segfault), la commande reine est **`bt`** : après
le crash, tape `bt` et gdb te montre **la ligne exacte** où ça a cassé, et toute la
chaîne des fonctions qui y a mené.

---

## 6. Anticiper les erreurs prévisibles avec `try / catch`

Certaines erreurs sont **prévisibles** (un index peut dépasser, un fichier peut
manquer). On les **attrape** pour réagir proprement, au lieu de planter. En C++, on
utilise `try / catch` (l'équivalent du `try / except` de Python).

```cpp
try {
    int x = notes.at(10);          // .at() lève std::out_of_range si 10 est hors limites
} catch (const std::out_of_range& e) {
    std::cout << "Index invalide : " << e.what() << std::endl;
}
```

- Dans le **`try`**, on met le code qui peut échouer.
- Le **`catch`** attrape l'exception (ici `std::out_of_range`, levée par `.at()`).
- **`e.what()`** donne le message d'explication de l'erreur.

C'est exactement ce que fait `demo_gdb.cpp` dans sa fonction `note_securisee`.

> 💬 `try { } catch (...)` ⇄ `try: ... except ...:` en Python. Même idée :
> prévoir l'erreur plutôt que de planter.

---

## ▶️ À toi de jouer

Depuis la **racine du dépôt** (le dossier qui contient `cpp/`) :

```bash
# Compiler AVEC -g et -Wall, puis lancer
g++ -g -std=c++17 -Wall cpp/07_debugger/demo_gdb.cpp -o demo_gdb && ./demo_gdb
```

Tu verras les notes, la moyenne, une lecture valide, puis une lecture **hors
limites** attrapée proprement par le `try/catch`.

Ensuite, **entraîne-toi sous gdb** (sans modifier le code) :

```bash
gdb ./demo_gdb
# puis tape, dans l'ordre :  break moyenne   →   run   →   next   →   print total   →   continue   →   quit
```

➡️ Avec la lecture des erreurs du compilateur + gdb + le `try/catch`, tu as tout ce
qu'il faut pour traquer les bugs C++. 💪

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
