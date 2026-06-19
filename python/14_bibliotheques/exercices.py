#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 14 : les bibliothèques

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.
"""

import importlib.util


def est_disponible(nom_module):
    """Renvoie True si le module `nom_module` est installé/importable, False sinon.
    Ex : est_disponible("json") -> True   (stdlib, toujours là)
         est_disponible("module_qui_nexiste_pas_xyz") -> False
    Indice : importlib.util.find_spec(nom) renvoie None si le module est introuvable.
    """
    # TODO
    ...


def ligne_requirement(nom, version):
    """Construit une ligne de requirements.txt qui FIGE la version (avec ==).
    Ex : ligne_requirement("requests", "2.31.0") -> "requests==2.31.0"
    """
    # TODO : une f-string avec ==
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
    print("--- Vérification — module 14 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("est_disponible('json')", lambda: est_disponible("json"), True)
    essai("est_disponible('xyz_introuvable')", lambda: est_disponible("module_qui_nexiste_pas_xyz"), False)
    essai("ligne_requirement('requests','2.31.0')",
          lambda: ligne_requirement("requests", "2.31.0"), "requests==2.31.0")

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
