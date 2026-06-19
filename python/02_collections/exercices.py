#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 02 : les collections (listes, dicts, tuples, sets)

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py (à voir APRÈS avoir essayé).
"""


def deuxieme_element(liste):
    """Renvoie le DEUXIÈME élément d'une liste.
    Ex : deuxieme_element(["a", "b", "c"]) -> "b"
    Rappel : le premier élément est à l'index 0.
    """
    # TODO : utilise l'indexation [ ]
    ...


def compter_occurrences(liste, valeur):
    """Renvoie combien de fois `valeur` apparaît dans `liste`.
    Ex : compter_occurrences([1, 2, 2, 3, 2], 2) -> 3
    """
    # TODO : une boucle for + un compteur (ou la méthode .count)
    ...


def sans_doublons_tries(liste):
    """Renvoie la liste des valeurs DISTINCTES, triées par ordre croissant.
    Ex : sans_doublons_tries([3, 1, 2, 3, 1]) -> [1, 2, 3]
    Indice : un set enlève les doublons, sorted() trie.
    """
    # TODO
    ...


def inverser_dictionnaire(d):
    """Échange clés et valeurs d'un dictionnaire.
    Ex : inverser_dictionnaire({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    (On suppose que les valeurs sont uniques.)
    """
    # TODO : parcours d.items() et construis un nouveau dict
    ...


def total_panier(panier):
    """`panier` est un dict {produit: prix}. Renvoie la somme des prix.
    Ex : total_panier({"pain": 1.2, "lait": 0.8}) -> 2.0
    """
    # TODO : additionne les VALEURS du dictionnaire
    ...


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 02 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("deuxieme_element(['a','b','c'])", lambda: deuxieme_element(["a", "b", "c"]), "b")
    essai("compter_occurrences([1,2,2,3,2], 2)", lambda: compter_occurrences([1, 2, 2, 3, 2], 2), 3)
    essai("sans_doublons_tries([3,1,2,3,1])", lambda: sans_doublons_tries([3, 1, 2, 3, 1]), [1, 2, 3])
    essai("inverser_dictionnaire({'a':1,'b':2})", lambda: inverser_dictionnaire({"a": 1, "b": 2}), {1: "a", 2: "b"})
    essai("total_panier({'pain':1.2,'lait':0.8})", lambda: total_panier({"pain": 1.2, "lait": 0.8}), 2.0)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
