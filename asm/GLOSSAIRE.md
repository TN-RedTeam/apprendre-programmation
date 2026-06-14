# 📖 Glossaire ASSEMBLEUR (expliqué simplement)

Les mots qui reviennent souvent, expliqués avec des mots de tous les jours. À garder ouvert
à côté de toi pendant que tu lis les modules.

---

**Registre**
Une petite « case » de mémoire ultra-rapide **à l'intérieur du processeur**. Le processeur
ne sait calculer qu'avec ces cases. Exemples : `rax`, `rdi`, `rsi`, `rdx`, `rsp`.

**Instruction**
Un **ordre élémentaire** donné au processeur (`mov`, `add`, `jmp`…). Une ligne d'assembleur
= (presque) une instruction. C'est l'unité de base de ce que fait la machine.

**Mémoire**
La grande zone de stockage de l'ordinateur (la RAM), **en dehors** du processeur. Plus vaste
que les registres, mais plus lente d'accès. La pile vit dans la mémoire.

**Pile (stack)**
Une zone de la mémoire organisée comme une **pile d'assiettes** : on pose une valeur sur le
dessus, on reprend celle du dessus. Règle **LIFO** : *Last In, First Out* (dernier posé,
premier repris). Sert à sauvegarder des valeurs et à mémoriser où revenir après un `call`.

**`rsp` (stack pointer)**
Le **pointeur de pile** : un registre qui **indique en permanence le sommet** de la pile
(la dernière valeur posée). Mis à jour automatiquement par `push`, `pop`, `call` et `ret`.

**`push` / `pop`**
`push valeur` **pose** une valeur sur le dessus de la pile. `pop registre` **retire** la
valeur du dessus et la met dans le registre. Ils vont par paire pour sauvegarder/restaurer.

**Label (étiquette)**
Un **nom posé sur un endroit du code**, suivi de `:` (par exemple `boucle:` ou `fin:`). Les
sauts et les `call` s'en servent comme **destination**. C'est un point de repère.

**Saut (jump)**
Le fait d'**aller à un autre endroit du code** au lieu de continuer ligne par ligne.
`jmp etiquette` saute **toujours** vers cette étiquette.

**Saut conditionnel**
Un saut qui ne se fait **que si une condition est vraie**, juste après un `cmp`. Exemples :
`jl` (si plus petit), `jg` (si plus grand), `je` (si égal), `jne` (si différent).

**`cmp`**
L'instruction qui **compare deux valeurs** sans rien modifier. Elle prépare le terrain pour
le saut conditionnel qui suit (qui décidera où aller selon le résultat).

**Syscall (appel système)**
Une **demande de service au système Linux** (afficher du texte, quitter…). On met le numéro
du service dans `rax`, les arguments dans `rdi`/`rsi`/`rdx`, puis on déclenche avec
`syscall`. Exemples : `write` (n° 1), `exit` (n° 60).

**`_start`**
L'**étiquette du point d'entrée** : l'endroit où le programme **commence** à s'exécuter. On
la rend visible avec `.global _start` pour que l'éditeur de liens (`ld`) la trouve.

**Assemblage vs édition de liens**
- **Assemblage** (`as`) : transforme ton fichier source `.s` en un **fichier objet** `.o`
  (presque du langage machine).
- **Édition de liens** (`ld`) : transforme le `.o` en un **exécutable** réellement lançable.

**Code de sortie**
Le **nombre que le programme renvoie en quittant** (via `exit`, valeur dans `rdi`). Va de
**0 à 255** ; par convention `0` = tout s'est bien passé. On le lit avec `echo $?`, et on
s'en sert dans ce parcours pour « voir » le résultat d'un calcul.
