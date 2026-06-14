# Module 08 (avancé) — La Programmation Orientée Objet (POO)

Jusqu'ici, tu rangeais tes données dans des variables, des listes et des dictionnaires, et
tes actions dans des fonctions. La **Programmation Orientée Objet** (POO) propose de
**regrouper les données ET les actions qui vont ensemble** dans un même « paquet » : l'objet.

C'est un module **avancé** : prends ton temps. La POO devient évidente avec une bonne
analogie, et c'est tout l'objet de cette théorie.

> 🧠 Lis cette théorie en entier **avant** d'ouvrir les fichiers `.py`. Les deux scripts du
> module sont : `classes.py` (définir et utiliser une classe) et `heritage.py` (réutiliser
> et spécialiser une classe avec l'héritage).

---

## 1. L'idée centrale : le plan (classe) et l'exemplaire (objet)

Imagine un **plan de construction** de maison. Le plan, à lui seul, n'est pas une maison :
c'est une **description** de ce qu'est une maison (elle a des murs, une porte, un toit) et de
ce qu'on peut y faire (ouvrir la porte, allumer la lumière).

- La **CLASSE**, c'est le **plan / le moule**. On l'écrit **une seule fois**.
- L'**OBJET** (aussi appelé **instance**), c'est un **exemplaire fabriqué** à partir du plan.
  Avec un même plan, on peut construire **autant de maisons qu'on veut**, chacune avec ses
  propres caractéristiques (l'une est bleue, l'autre rouge).

```
   CLASSE (le plan)                OBJETS (les exemplaires)
   ┌──────────────┐               🏠 maison_alice (bleue)
   │   Maison     │  ──fabrique──▶ 🏠 maison_bob   (rouge)
   └──────────────┘               🏠 maison_chloe (verte)
```

Autre analogie : la classe est le **moule à gâteau**, les objets sont les **gâteaux** qui en
sortent. Le moule décrit la forme ; chaque gâteau est un objet bien réel.

---

## 2. Le vocabulaire de la POO

Quatre mots à retenir. On les illustre avec une classe `Chien`.

| Mot | C'est quoi | Exemple |
|-----|------------|---------|
| **Classe** | le plan, le modèle | `class Chien:` |
| **Objet** (instance) | un exemplaire créé depuis la classe | `Chien("Rex", 3)` |
| **Attribut** | une **donnée** rangée dans l'objet | `rex.nom`, `rex.age` |
| **Méthode** | une **action** que l'objet sait faire | `rex.aboyer()` |

Retiens la distinction clé :
- **Attribut = donnée** (un nom, un âge, un solde…). C'est une variable qui vit **dans** l'objet.
- **Méthode = action** (aboyer, déposer de l'argent…). C'est une fonction qui vit **dans** l'objet.

---

## 3. `__init__` : le constructeur (la chaîne de montage)

Quand on fabrique un objet, il faut le **mettre en place** : lui donner son nom, son âge,
son solde de départ… C'est le rôle d'une méthode spéciale appelée **`__init__`** (deux
underscores avant et après — on prononce souvent « dunder init »).

`__init__` est le **constructeur** : Python l'appelle **automatiquement** au moment où tu
crées un objet. C'est la « chaîne de montage » qui prépare l'exemplaire.

```python
class Chien:
    def __init__(self, nom, age):   # appelé automatiquement à la création
        self.nom = nom              # on range le nom DANS l'objet
        self.age = age              # on range l'âge DANS l'objet

rex = Chien("Rex", 3)              # ICI Python appelle __init__ tout seul
```

> 💡 Tu n'appelles jamais `__init__` toi-même. Tu écris `Chien("Rex", 3)` et Python s'en
> charge en coulisses.

---

## 4. `self` : « l'objet courant »

Tu as remarqué le mot **`self`** partout. C'est **le mot le plus déroutant** de la POO au
début, alors prenons le temps.

`self` représente **l'objet en train d'être manipulé** — *celui-ci, précisément*. Comme
une classe sert à fabriquer **plusieurs** objets, il faut bien un mot pour dire « MOI,
l'exemplaire courant », par opposition aux autres.

- `self.nom = nom` veut dire : « range le nom **dans cet objet-ci** ».
- Quand tu écris `rex.aboyer()`, Python traduit en `aboyer(rex)` : il passe `rex` comme
  `self`. C'est pour ça que `self` est **toujours le premier paramètre** d'une méthode.

```python
class Chien:
    def __init__(self, nom):
        self.nom = nom

    def aboyer(self):                      # self = l'objet qui appelle la méthode
        print(f"{self.nom} dit : Wouf !")  # on lit le nom DE CET objet

rex = Chien("Rex")
rex.aboyer()        # Rex dit : Wouf !  (ici self vaut rex)
```

> 💡 `self` n'est pas un mot-clé magique, c'est juste une **convention** de nom. Tout le
> monde l'écrit `self`, garde-le toujours.

---

## 5. `__str__` : un affichage lisible

Si tu fais `print(rex)` sans rien préparer, Python affiche un truc moche comme
`<__main__.Chien object at 0x7f...>`. Pas très parlant !

La méthode spéciale **`__str__`** te laisse décider **comment l'objet s'affiche** quand on le
`print()`. Elle doit **renvoyer un texte** (`return "..."`).

```python
class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom}, chien de {self.age} ans"

rex = Chien("Rex", 3)
print(rex)          # Rex, chien de 3 ans   (grâce à __str__)
```

---

## 6. L'héritage : réutiliser et spécialiser

Souvent, plusieurs classes se **ressemblent**. Un `Chien` et un `Chat` sont tous les deux
des `Animal` : ils ont un nom, un âge, ils mangent… mais ils ne font pas le même cri.

Plutôt que de tout réécrire, l'**héritage** permet à une **classe fille** de **réutiliser**
le code d'une **classe mère**, et d'**ajouter ou changer** ce qui lui est propre.

```
            Animal  (classe MÈRE : nom, age, manger)
             /   \
          Chien   Chat   (classes FILLES : leur propre cri)
```

```python
class Animal:                       # classe MÈRE
    def __init__(self, nom):
        self.nom = nom
    def crier(self):
        print(f"{self.nom} fait un bruit.")

class Chien(Animal):                # Chien HÉRITE de Animal (entre parenthèses)
    def crier(self):                # on REDÉFINIT la méthode (on la spécialise)
        print(f"{self.nom} dit : Wouf !")
```

`Chien` récupère gratuitement le `__init__` et l'attribut `nom` d'`Animal`, mais
**redéfinit** `crier()` à sa façon. C'est ce qu'on appelle **redéfinir** (ou *surcharger*) une
méthode.

### `super()` : appeler la version de la mère

Parfois, la fille veut **compléter** le travail de la mère sans tout refaire. `super()` veut
dire « la classe mère » : il sert à appeler la méthode de la mère **puis** ajouter sa touche.

```python
class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom)    # on laisse Animal s'occuper du nom
        self.race = race         # puis on ajoute ce qui est propre au chien
```

---

## 7. L'encapsulation : le préfixe `_`

En POO, on aime **protéger** certaines données pour qu'on n'y touche pas n'importe comment
depuis l'extérieur (ex : le solde d'un compte ne doit changer **qu'**en passant par
`deposer()` / `retirer()`). C'est l'**encapsulation**.

En Python, il n'y a pas de vrai « privé » comme dans d'autres langages. On utilise une
**convention** : un attribut dont le nom commence par un **underscore `_`** signale « ceci
est interne, ne le modifie pas directement de l'extérieur ».

```python
self._solde = 0     # le _ dit : "n'y touche pas directement, passe par les méthodes"
```

> 💡 C'est une **politesse entre développeurs**, pas un cadenas. Python te laisse techniquement
> y accéder, mais le `_` te dit clairement « tu ne devrais pas ».

---

## 8. Pour ceux qui ont vu le C++ ou le Go

Si tu as croisé ces langages ailleurs dans le dépôt, voici les ponts :

- **C++ :** le `__init__` de Python correspond au **constructeur** C++ ; `self` correspond au
  pointeur **`this`**. Grande différence : en C++ tu as les mots-clés `public` / `private`
  pour vraiment cacher des données. Python n'a pas ça : il se contente de la **convention `_`**.
- **Go :** Go n'a **pas de classes** ni d'héritage classique ; il combine des `struct`
  (les données) et des **méthodes** rattachées avec un *receiver* (`func (c Chien) Crier()`)
  — ce *receiver* joue le rôle de `self`. La réutilisation passe par la **composition** (on
  imbrique des structs) plutôt que par l'héritage. En Go, la visibilité dépend de la
  **majuscule** du nom (`Nom` exporté, `nom` privé) là où Python utilise le `_`.

Conclusion : l'**idée** (regrouper données + actions) est universelle ; chaque langage a sa
syntaxe et ses règles de visibilité.

---

## ▶️ À toi de jouer

```bash
python3 python/automatisation/08_poo/classes.py
python3 python/automatisation/08_poo/heritage.py
```

Lis les deux fichiers, puis **modifie-les** : ajoute un attribut, crée une nouvelle méthode,
invente une troisième classe fille avec son propre cri.

➡️ Retour au sommaire du parcours : [`README.md`](../README.md).
