#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 14 : les bibliothèques

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""

import importlib.util


def est_disponible(nom_module):
    """True si le module est importable."""
    return importlib.util.find_spec(nom_module) is not None   # None = introuvable


def ligne_requirement(nom, version):
    """Ligne requirements.txt avec version figée."""
    return f"{nom}=={version}"


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
    print("--- Vérification — module 14 (solutions) ---")
    res = [
        _check("est_disponible('json')", est_disponible("json"), True),
        _check("est_disponible('xyz_introuvable')", est_disponible("module_qui_nexiste_pas_xyz"), False),
        _check("ligne_requirement('requests','2.31.0')", ligne_requirement("requests", "2.31.0"), "requests==2.31.0"),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
