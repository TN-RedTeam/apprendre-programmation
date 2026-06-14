# Module 02 — La pile et les fonctions (sous-programmes)

Tu sais maintenant **calculer** et **faire des boucles**. On va apprendre deux choses qui
vont ensemble : **la pile** (une zone mémoire spéciale) et les **fonctions** (des petits
morceaux de programme réutilisables qu'on peut **appeler**).

> Fichiers du module : [`pile.s`](./pile.s) (démontre `push`/`pop`) et
> [`fonction.s`](./fonction.s) (définit et appelle une fonction). Tout est commenté
> presque ligne par ligne.

---

## 1. LA PILE (the stack) : une « pile d'assiettes »

Imagine une **pile d'assiettes** dans un placard :

- Tu **poses** une assiette **sur le dessus** de la pile.
- Pour en **retirer** une, tu prends **celle du dessus** (la dernière posée).

La **pile** (en anglais *the stack*) est une **zone de la mémoire** qui fonctionne
exactement comme ça. On dit qu'elle est **LIFO** : *Last In, First Out* —
**dernier arrivé, premier sorti**. La dernière valeur posée est la première reprise.

Deux instructions servent à manipuler la pile :

| Instruction | Ce qu'elle fait (en mots simples) |
|-------------|------------------------------------|
| `push valeur` | **pose** une valeur sur le dessus de la pile |
| `pop registre` | **retire** la valeur du dessus et la met dans le registre |

Un registre spécial, **`rsp`** (*stack pointer* = « pointeur de pile »), **pointe toujours
vers le sommet** de la pile (l'assiette du dessus). Tu n'as pas besoin de le gérer toi-même :
`push` et `pop` le mettent à jour automatiquement.

```asm
push rax        # pose le contenu de rax sur la pile
pop  rbx        # retire le sommet de la pile et le met dans rbx
```

> 💡 **À quoi ça sert ?** Surtout à **sauvegarder une valeur** pour la **récupérer plus
> tard**, par exemple quand on doit réutiliser un registre entre-temps. On `push` avant, on
> `pop` après : la valeur revient intacte. C'est ce que montre [`pile.s`](./pile.s).

---

## 2. Les SOUS-PROGRAMMES : `call` et `ret`

Un **sous-programme** (ou **fonction**) est un **bout de code qu'on peut appeler** depuis
plusieurs endroits, au lieu de le réécrire à chaque fois. Deux instructions le permettent :

| Instruction | Ce qu'elle fait |
|-------------|-----------------|
| `call etiquette` | **saute** vers l'étiquette **ET** mémorise sur la pile **où revenir** |
| `ret` | **revient** à l'endroit juste après le `call` |

C'est là que la pile devient indispensable : quand tu fais `call additionner`, le processeur
**pose discrètement sur la pile l'adresse de retour** (la ligne d'après le `call`). Quand la
fonction fait `ret`, il **reprend cette adresse sur la pile** et y retourne. Magique, mais
logique : c'est juste un `push` puis un `pop` cachés !

```asm
    call additionner   # saute dans 'additionner', en notant où revenir
    # ... on revient ICI après le 'ret' ...

additionner:           # début de la fonction
    add rax, rdi       # ... le travail de la fonction ...
    ret                # revient juste après le 'call'
```

---

## 3. Convention simple : arguments et résultat

Pour qu'une fonction soit utile, il faut lui **donner des valeurs** (les **arguments**) et
**récupérer son résultat**. On adopte une convention simple, la même que Linux :

- On **passe les arguments dans des registres** : `rdi` = 1er argument, `rsi` = 2e argument.
- La fonction **range son résultat dans `rax`**.

C'est exactement ce que fait [`fonction.s`](./fonction.s) : on met `7` dans `rdi` et `5`
dans `rsi`, on appelle `additionner`, et on récupère **12** dans `rax`.

---

## ▶️ À toi de jouer

```bash
# pile.s : sauvegarde/restaure une valeur avec push/pop -> exit=42
as asm/02_pile_fonctions/pile.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"

# fonction.s : appelle 'additionner' (7 + 5) avec call -> exit=12
as asm/02_pile_fonctions/fonction.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
```

Lis les deux fichiers, puis **modifie-les** : dans `fonction.s`, change les valeurs de `rdi`
et `rsi` (par exemple `10` et `20`, tu devrais lire `exit=30`). Dans `pile.s`, change la
valeur sauvegardée et vérifie qu'elle revient bien intacte après le `pop`.

➡️ La suite du parcours (chaînes de caractères, affichage de nombres…) arrivera dans le
même style.

📎 Besoin d'un rappel rapide ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
