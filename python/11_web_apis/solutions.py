#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 11 : web & APIs

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""

import json


def extraire_temperature(reponse_texte):
    """Lit le JSON et renvoie la température."""
    donnees = json.loads(reponse_texte)   # texte JSON → dict Python
    return donnees["temperature"]


def noms_des_resultats(reponse):
    """Liste des noms dans reponse["results"]."""
    return [item["name"] for item in reponse["results"]]


def statut_ok(code):
    """Succès HTTP = code de la famille 2xx."""
    return 200 <= code <= 299


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
    print("--- Vérification — module 11 (solutions) ---")
    res = [
        _check("extraire_temperature(...)",
               extraire_temperature('{"ville": "Paris", "temperature": 18}'), 18),
        _check("noms_des_resultats(...)",
               noms_des_resultats({"results": [{"name": "Ada"}, {"name": "Bob"}]}), ["Ada", "Bob"]),
        _check("statut_ok(200)", statut_ok(200), True),
        _check("statut_ok(404)", statut_ok(404), False),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
