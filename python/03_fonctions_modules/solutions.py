#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 03 : fonctions & modules

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""


def salutation(nom, politesse="Bonjour"):
    """Salutation avec politesse par défaut."""
    return f"{politesse} {nom} !"


def moyenne(*notes):
    """Moyenne d'un nombre variable de notes (0 si aucune)."""
    if not notes:                       # tuple vide → "si aucune note"
        return 0                        # on évite la division par zéro
    return sum(notes) / len(notes)      # somme / nombre d'éléments


def applique(fonction, liste):
    """Applique une fonction à chaque élément."""
    return [fonction(x) for x in liste]   # compréhension : appelle fonction(x) pour chaque x


def compter_mots(phrase):
    """Nombre de mots (séparés par des espaces)."""
    return len(phrase.split())          # split() → liste de mots, len() → combien


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
    print("--- Vérification — module 03 (solutions) ---")
    res = [
        _check("salutation('Ada')", salutation("Ada"), "Bonjour Ada !"),
        _check("salutation('Ada','Salut')", salutation("Ada", "Salut"), "Salut Ada !"),
        _check("moyenne(10, 20)", moyenne(10, 20), 15.0),
        _check("moyenne()", moyenne(), 0),
        _check("applique(x2, [1,2,3])", applique(lambda x: x * 2, [1, 2, 3]), [2, 4, 6]),
        _check("compter_mots('le chat dort')", compter_mots("le chat dort"), 3),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
