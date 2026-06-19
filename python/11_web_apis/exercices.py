#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 11 : web & APIs (traiter une réponse JSON)

Pas besoin d'Internet ici : on s'entraîne à TRAITER une réponse d'API,
qui arrive presque toujours sous forme de JSON (du texte structuré).

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.
"""

import json


def extraire_temperature(reponse_texte):
    """`reponse_texte` est une chaîne JSON, ex. '{"ville": "Paris", "temperature": 18}'.
    Renvoie la valeur de "temperature" (un nombre).
    Indice : json.loads(texte) transforme le TEXTE JSON en dict Python.
    """
    # TODO : json.loads puis accède à la clé
    ...


def noms_des_resultats(reponse):
    """`reponse` est DÉJÀ un dict, de la forme :
        {"results": [{"name": "Ada"}, {"name": "Bob"}]}
    Renvoie la liste des noms : ["Ada", "Bob"].
    """
    # TODO : parcours reponse["results"] et récupère chaque "name"
    ...


def statut_ok(code):
    """Renvoie True si `code` est un code HTTP de succès (entre 200 et 299 inclus).
    Ex : statut_ok(200) -> True ; statut_ok(404) -> False
    """
    # TODO
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
    print("--- Vérification — module 11 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("extraire_temperature(...)",
          lambda: extraire_temperature('{"ville": "Paris", "temperature": 18}'), 18)
    essai("noms_des_resultats(...)",
          lambda: noms_des_resultats({"results": [{"name": "Ada"}, {"name": "Bob"}]}), ["Ada", "Bob"])
    essai("statut_ok(200)", lambda: statut_ok(200), True)
    essai("statut_ok(404)", lambda: statut_ok(404), False)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
