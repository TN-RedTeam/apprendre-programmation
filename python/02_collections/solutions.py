#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 02 : les collections

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
⚠️ À consulter APRÈS avoir essayé exercices.py par toi-même.
"""


def deuxieme_element(liste):
    """Deuxième élément : index 1 (le premier est à l'index 0)."""
    return liste[1]


def compter_occurrences(liste, valeur):
    """Compte les apparitions de `valeur`."""
    total = 0
    for element in liste:
        if element == valeur:
            total += 1
    return total
    # Variante : return liste.count(valeur)


def sans_doublons_tries(liste):
    """Valeurs distinctes, triées."""
    return sorted(set(liste))     # set() retire les doublons, sorted() trie et renvoie une liste


def inverser_dictionnaire(d):
    """Échange clés et valeurs."""
    inverse = {}
    for cle, valeur in d.items():     # .items() donne (clé, valeur)
        inverse[valeur] = cle         # la valeur devient la clé, et inversement
    return inverse
    # Variante : return {v: k for k, v in d.items()}


def total_panier(panier):
    """Somme des prix (les valeurs du dict)."""
    return sum(panier.values())       # .values() donne toutes les valeurs


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 02 (solutions) ---")
    res = [
        _check("deuxieme_element", deuxieme_element(["a", "b", "c"]), "b"),
        _check("compter_occurrences", compter_occurrences([1, 2, 2, 3, 2], 2), 3),
        _check("sans_doublons_tries", sans_doublons_tries([3, 1, 2, 3, 1]), [1, 2, 3]),
        _check("inverser_dictionnaire", inverser_dictionnaire({"a": 1, "b": 2}), {1: "a", 2: "b"}),
        _check("total_panier", total_panier({"pain": 1.2, "lait": 0.8}), 2.0),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
