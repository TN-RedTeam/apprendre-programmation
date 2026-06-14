# Module 09 (AVANCÉ) — Pointeurs de fonctions & callbacks

Tu sais déjà qu'une **variable** a une adresse (module 03). Surprise : une **fonction** aussi !
Et comme tout ce qui a une adresse, on peut la ranger dans un **pointeur**. Ça ouvre une porte
géniale : **passer une fonction à une autre fonction**, comme on passe un nombre. On appelle ça
un **callback**. On y va doucement, avec des analogies, comme d'habitude.

> Fichier du module : `pointeurs_fonctions.c` (un pointeur qu'on fait pointer vers différentes
> fonctions, un **tableau** de pointeurs de fonctions parcouru en boucle, et une fonction qui
> reçoit un **callback**). On **compile** puis on **lance** (voir en bas).

---

## 1. Une fonction a une ADRESSE, elle aussi

Au module 03, tu as appris qu'une variable vit **quelque part** en mémoire, à une **adresse**.
Eh bien le **code** d'une fonction est lui aussi rangé en mémoire : la fonction a donc, elle
aussi, une **adresse** — l'endroit où commencent ses instructions.

📞 **Analogie : un numéro de téléphone.** Une fonction, c'est comme un **contact** que tu peux
appeler. Le **numéro de téléphone**, c'est son adresse. Si tu **notes ce numéro** sur un papier,
tu pourras appeler ce contact **plus tard**, sans avoir à le connaître à l'avance.

En C, le **nom d'une fonction** (sans les parenthèses) vaut déjà son **adresse** — exactement
comme le nom d'un tableau valait l'adresse de sa première case (module 03) :

```c
int additionner(int a, int b) { return a + b; }

additionner       // l'ADRESSE de la fonction (le "numéro de téléphone")
additionner(2, 3) // l'APPEL de la fonction (on téléphone : ça renvoie 5)
```

---

## 2. Un POINTEUR DE FONCTION : ranger ce « numéro »

Puisqu'une fonction a une adresse, on peut la stocker dans un **pointeur de fonction** : une
variable qui retient **quelle fonction appeler**.

📝 **Analogie :** le papier où tu **notes le numéro** d'un contact. Le papier n'est pas le
contact ; il **indique** lequel appeler. Plus tard, tu lis le papier et tu téléphones.

La syntaxe surprend au début. Pour pointer vers une fonction qui prend `(int, int)` et renvoie
un `int`, on écrit :

```c
int (*op)(int, int);   // 'op' est un pointeur vers une fonction (int,int) -> int
```

À décortiquer calmement :
- `int`            → le **type de retour** de la fonction pointée ;
- `(*op)`          → `op` est un **pointeur** (les parenthèses sont **obligatoires**) ;
- `(int, int)`     → les **paramètres** de la fonction pointée.

> ⚠️ Les parenthèses autour de `*op` sont **essentielles**. Sans elles, `int *op(int, int)`
> voudrait dire « une **fonction** qui renvoie un `int *` » — pas du tout la même chose !

On le fait ensuite **pointer** vers une vraie fonction, juste avec son nom :

```c
op = additionner;   // 'op' note le "numéro" de additionner (pas de parenthèses !)
```

---

## 3. APPELER la fonction via le pointeur

Une fois le pointeur réglé, on l'appelle **comme une fonction normale** :

```c
int (*op)(int, int) = additionner;

int r = op(2, 3);    // on "téléphone" au contact noté dans op -> 5
```

🚶 **Analogie :** tu lis le numéro sur le papier (`op`) et tu **passes l'appel** (`op(2, 3)`).
Le plus beau : il suffit de **changer le numéro noté** pour appeler quelqu'un d'autre, **sans
changer** la ligne qui téléphone :

```c
op = soustraire;     // on note un autre "numéro"
r = op(2, 3);        // même ligne d'appel... mais ça donne -1 maintenant !
```

> 💡 Tu peux aussi écrire `(*op)(2, 3)` pour bien montrer le déréférencement. Les deux
> écritures marchent ; `op(2, 3)` est la plus courante et la plus lisible.

---

## 4. Un TABLEAU de pointeurs de fonctions

Comme n'importe quel type, on peut faire un **tableau** de pointeurs de fonctions. Très pratique
pour ranger des opérations et les **parcourir en boucle**.

📇 **Analogie : un répertoire téléphonique.** Une liste de numéros : tu prends l'entrée 0, tu
appelles ; l'entrée 1, tu appelles… Ici, chaque « entrée » est une opération.

```c
int (*operations[])(int, int) = { additionner, soustraire, multiplier };

for (int i = 0; i < 3; i++) {
    int r = operations[i](10, 3);   // on appelle l'opération numéro i
    printf("%d\n", r);              // 13, puis 7, puis 30
}
```

Une seule boucle, et on enchaîne des comportements différents : c'est l'idée de la **table
d'opérations** (on remplace une longue suite de `if`/`else` par un simple tableau).

---

## 5. Le CALLBACK : passer une fonction EN ARGUMENT

Voici le cas qui change tout. Puisqu'un pointeur de fonction est une **valeur**, on peut le
passer **en argument** à une autre fonction. Cette fonction reçue, on l'appelle un **callback**
(« fonction de rappel »).

🗣️ **Analogie : « voici quoi faire quand… ».** Tu confies une tâche à quelqu'un en lui disant :
« voici **ce que tu feras** une fois arrivé ». Tu lui donnes des **instructions à rappeler plus
tard**. La fonction principale décide **quand** ; toi, tu décides **quoi**.

```c
// 'appliquer' reçoit deux nombres ET une fonction à exécuter dessus.
int appliquer(int a, int b, int (*callback)(int, int)) {
    return callback(a, b);   // elle "rappelle" la fonction qu'on lui a confiée
}

appliquer(6, 2, additionner);   // -> 8
appliquer(6, 2, soustraire);    // -> 4   (même fonction 'appliquer', comportement différent !)
```

La force du callback : `appliquer` ne sait **pas à l'avance** ce qu'elle va faire. C'est
**l'appelant** qui le décide en passant **telle ou telle** fonction. Le même code se comporte
différemment selon le callback fourni.

---

## 6. Cas d'usage réel : `qsort` et sa fonction de comparaison

Tu n'inventes pas les callbacks pour rien : la **bibliothèque standard** s'en sert déjà.
L'exemple le plus connu est **`qsort`** (de `<stdlib.h>`), qui trie un tableau de **n'importe
quoi**. Mais pour trier, il faut savoir **comparer deux éléments**… et seul **toi** sais comment
comparer **tes** données. Alors `qsort` te demande de lui **fournir** une fonction de comparaison :
un **callback**.

```c
// Callback imposé par qsort : compare deux éléments via des pointeurs génériques.
int comparer_ints(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return x - y;   // <0 si x avant y, 0 si égaux, >0 si x après y
}

int t[] = {5, 2, 9, 1};
qsort(t, 4, sizeof(int), comparer_ints);   // on CONFIE comparer_ints à qsort
// t vaut maintenant {1, 2, 5, 9}
```

> 💡 C'est exactement l'idée du callback : `qsort` sait **comment trier** (l'algorithme), toi tu
> fournis **comment comparer** (la règle). Chacun son rôle. Pour trier dans l'autre sens, il te
> suffit de fournir une **autre** fonction de comparaison — sans toucher à `qsort`.

---

## 7. Ce que fait `pointeurs_fonctions.c`

- il définit quelques petites fonctions : `additionner`, `soustraire`, `multiplier` ;
- il crée **un** pointeur de fonction, le fait pointer vers l'une **puis** l'autre, et appelle ;
- il construit un **tableau** de pointeurs de fonctions et le parcourt **en boucle** ;
- il définit `appliquer`, une fonction qui reçoit un **callback** et l'exécute ;
- en bonus, il montre `qsort` avec une fonction de comparaison (le callback « de la vraie vie »).

Le tout est commenté **presque ligne par ligne**, avec le « 🗺️ CHEMINEMENT DU PROGRAMME » en tête.

---

## ▶️ À toi de jouer

```bash
# Compiler puis lancer
gcc -Wall c/09_pointeurs_fonctions/pointeurs_fonctions.c -o pointeurs_fonctions && ./pointeurs_fonctions
```

**Expériences** pour bien comprendre :
- ajoute une fonction `diviser` et fais-la pointer/appeler comme les autres ;
- ajoute-la au **tableau** d'opérations (n'oublie pas d'ajuster la taille de la boucle) ;
- passe `multiplier` à `appliquer` et vérifie le résultat ;
- inverse l'ordre du tri en écrivant un `comparer_ints_decroissant` (renvoie `y - x`) et confie-le
  à `qsort` à la place.

➡️ Les pointeurs de fonctions sont partout : tri, gestion d'événements (« quand on clique,
appelle CETTE fonction »), tables de commandes… Dès que tu veux dire « voici **quoi faire**
quand le moment viendra », pense **callback**.
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
