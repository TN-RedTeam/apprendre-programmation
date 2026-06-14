# Module 09 (avancé) — Concurrence et parallélisme

Jusqu'ici, tes scripts faisaient **une seule chose à la fois**, dans l'ordre, de haut en
bas. Mais parfois, attendre une chose après l'autre fait perdre énormément de temps.
Ce module t'apprend à faire **plusieurs choses « en même temps »** quand c'est utile.

C'est un module **avancé** : prends ton temps. L'idée est simple avec une bonne analogie,
mais le vocabulaire (threads, asyncio, GIL…) peut faire peur au début. On va tout démonter.

> 🧠 Lis cette théorie en entier **avant** d'ouvrir les fichiers `.py`. Les deux scripts du
> module sont : `threads.py` (lancer des tâches d'attente en parallèle avec un
> `ThreadPoolExecutor`) et `async_demo.py` (la même idée avec `asyncio` et `async`/`await`).

---

## 1. Le problème : attendre, c'est perdre du temps

Imagine que tu dois **télécharger 10 pages web**. Chaque téléchargement prend 1 seconde,
mais pendant cette seconde, **ton ordinateur ne fait rien** : il attend que le serveur
réponde, comme toi tu attends que l'eau bout.

- **À la file (séquentiel)** : tu télécharges la page 1, tu attends 1 s, puis la page 2,
  tu attends 1 s… Au total **10 secondes**. Tu passes ton temps à attendre.
- **En même temps (concurrent)** : tu lances les 10 téléchargements **d'un coup**, puis tu
  attends que tous reviennent. Comme ils attendent **en parallèle**, le total est proche de
  **1 seconde**. Dix fois plus rapide !

Analogie de la **cuisine** : pour préparer un repas, tu ne restes pas planté devant la
casserole pendant qu'elle chauffe. Tu mets l'eau à bouillir, **et pendant ce temps** tu
coupes les légumes. Tu **occupes les temps morts**. C'est exactement ça, la concurrence.

---

## 2. Deux familles de tâches (la distinction la PLUS importante)

Avant de choisir un outil, il faut savoir **quel type de travail** tu veux accélérer. Il y
en a deux, et ils ne s'accélèrent **pas de la même façon**.

| Type de tâche | Ce qu'elle fait | Exemples | Bon outil |
|---------------|-----------------|----------|-----------|
| **Tâche d'attente** (I/O) | elle **attend** quelque chose d'extérieur | télécharger une page, lire un gros fichier, interroger une base | **threads** ou **asyncio** |
| **Tâche de calcul** (CPU) | elle **fait travailler le processeur** sans arrêt | calculer des millions d'opérations, compresser une image | **multiprocessing** |

- **Tâche d'attente (I/O = Input/Output)** : le programme **patiente** (réseau, disque…).
  Pendant qu'une tâche attend, on peut en faire avancer une autre. C'est le cas idéal pour
  les **threads** et **asyncio**.
- **Tâche de calcul (CPU)** : le programme **calcule sans relâche**. Là, il n'y a pas de
  temps mort à occuper : pour aller plus vite, il faut **plusieurs processeurs** qui calculent
  vraiment en parallèle → c'est le rôle de **multiprocessing** (voir §6).

> 💡 La question à te poser **avant tout** : « est-ce que ma tâche **attend** beaucoup, ou
> est-ce qu'elle **calcule** beaucoup ? ». La réponse décide de l'outil.

---

## 3. Le GIL, expliqué très simplement

Tu vas vite entendre parler du **GIL** (*Global Interpreter Lock*, « le verrou global de
l'interpréteur »). C'est une particularité de Python qu'il faut connaître.

Imagine que Python, c'est **une cuisine avec un seul micro** (un seul micro pour parler) :
même s'il y a plusieurs cuisiniers (les threads), **un seul peut parler à la fois**. Le GIL,
c'est ce micro unique : il garantit qu'**un seul thread exécute du code Python à un instant
donné**.

Conséquence très concrète :

- Pour les **tâches d'attente**, ce n'est **pas grave** : quand un thread attend le réseau,
  il **lâche le micro**, un autre thread peut avancer. Les threads sont donc **efficaces**
  pour l'I/O. 👍
- Pour les **calculs lourds**, c'est **bloquant** : les threads ne calculent jamais
  vraiment en même temps (ils se passent le micro chacun leur tour), donc ça **n'accélère
  pas** le CPU. Pour ça, il faut **multiprocessing**, qui ouvre **plusieurs cuisines
  séparées** (plusieurs processus, donc plusieurs micros). 👍

> 💡 Retiens la phrase magique : **threads/asyncio pour ce qui ATTEND, multiprocessing pour
> ce qui CALCULE.** Le GIL est la raison de cette règle.

---

## 4. La façon la plus simple : `ThreadPoolExecutor`

Le module `threading` permet de créer des threads à la main, mais c'est un peu verbeux. La
manière **la plus simple et la plus recommandée** aujourd'hui passe par
`concurrent.futures.ThreadPoolExecutor`.

Un *executor* (« exécuteur ») est comme un **chef d'équipe** : tu lui donnes une liste de
tâches, il les distribue à une **équipe d'ouvriers (les threads)** et te ramène les résultats.

```python
from concurrent.futures import ThreadPoolExecutor

def telecharger(page):
    # ... une tâche qui attend (réseau) ...
    return f"contenu de {page}"

pages = ["page1", "page2", "page3"]

# 'with' ouvre l'équipe puis la referme proprement à la fin (très important).
with ThreadPoolExecutor() as executor:
    # .map applique 'telecharger' à CHAQUE page, EN PARALLÈLE,
    # et renvoie les résultats DANS L'ORDRE des pages d'entrée.
    resultats = list(executor.map(telecharger, pages))

print(resultats)   # ['contenu de page1', 'contenu de page2', 'contenu de page3']
```

Deux points qui rassurent les débutants :

- **`with ... as executor`** : c'est le même `with` que pour ouvrir un fichier. Il garantit
  que l'équipe est **bien refermée** à la fin (pas de thread oublié qui traîne).
- **`executor.map(fonction, liste)`** : renvoie les résultats **dans l'ordre de la liste
  d'entrée**, même si les tâches finissent dans le désordre. C'est ce qui rend le résultat
  **déterministe** (toujours le même) — pratique pour les tests.

➡️ C'est exactement ce que montre **`threads.py`**.

---

## 5. `asyncio` : `async` / `await` (une autre façon d'attendre)

`asyncio` est une **autre approche** pour les tâches d'attente. L'idée est la même
(occuper les temps morts), mais au lieu d'une équipe de threads, **un seul thread** jongle
très vite entre plusieurs tâches, comme **un seul serveur de restaurant** qui s'occupe de
plusieurs tables : il prend la commande d'une table, et pendant que la cuisine prépare, il va
servir une autre table. Personne n'attend pour rien.

Deux mots-clés nouveaux :

- **`async def`** : déclare une **coroutine**, une fonction « spéciale » qui sait se mettre
  en pause sans bloquer les autres.
- **`await`** : « ici je vais **attendre** quelque chose ; pendant ce temps, laisse les
  autres tâches avancer ». C'est le moment où le serveur va s'occuper d'une autre table.

```python
import asyncio

async def telecharger(page):
    await asyncio.sleep(1)        # simule une attente (réseau), SANS bloquer les autres
    return f"contenu de {page}"

async def main():
    # asyncio.gather LANCE plusieurs coroutines EN MÊME TEMPS
    # et attend qu'elles soient TOUTES finies. Résultats dans l'ordre donné.
    resultats = await asyncio.gather(
        telecharger("page1"),
        telecharger("page2"),
        telecharger("page3"),
    )
    print(resultats)

asyncio.run(main())               # asyncio.run() démarre tout et s'arrête à la fin
```

Points de repère :

- **`asyncio.sleep()`** (et non `time.sleep()`) : c'est l'attente « polie » qui laisse les
  autres avancer. Dans la vraie vie, ce serait une requête réseau asynchrone.
- **`asyncio.gather(...)`** : lance plusieurs coroutines **en parallèle** et renvoie leurs
  résultats **dans l'ordre** où tu les as listées (encore une fois : déterministe).
- **`asyncio.run(main())`** : le point d'entrée. Il démarre la « boucle » d'asyncio, exécute
  `main()`, **puis s'arrête proprement**.

➡️ C'est exactement ce que montre **`async_demo.py`**.

---

## 6. Et pour les calculs lourds ? `multiprocessing` (en une phrase)

Pour un travail qui **calcule sans arrêt** (et non qui attend), threads et asyncio
n'aident pas à cause du GIL : utilise alors **`multiprocessing`** (ou
`concurrent.futures.ProcessPoolExecutor`), qui lance **plusieurs processus** capables de
calculer **vraiment en même temps** sur plusieurs cœurs du processeur.

---

## 7. Lequel choisir ? (le résumé)

| Ta situation | Choisis |
|--------------|---------|
| Beaucoup de tâches qui **attendent** (réseau, fichiers), code simple | **`ThreadPoolExecutor`** |
| Beaucoup de tâches qui **attendent**, et tu veux du moderne / très nombreux | **`asyncio`** |
| Du **calcul intensif** qui sature le processeur | **`multiprocessing`** |
| Une seule tâche, rien à attendre | reste **séquentiel**, c'est très bien |

> 💡 En cas de doute, commence **séquentiel**. N'ajoute de la concurrence **que** si ton
> programme est lent **parce qu'il attend**. La concurrence ajoute de la complexité : elle
> doit servir à quelque chose.

---

## ▶️ À toi de jouer

```bash
python3 python/automatisation/09_concurrence/threads.py
python3 python/automatisation/09_concurrence/async_demo.py
```

Lis les deux fichiers, puis **modifie-les** : ajoute des tâches, change les durées, et
compare le temps séquentiel au temps parallèle affiché. Essaie de prédire le total **avant**
de lancer.

➡️ Retour au sommaire du parcours : [`README.md`](../README.md).
