#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 10 : fichiers & dossiers

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""

from pathlib import Path
import json


def lister_noms(dossier):
    """Noms triés du contenu d'un dossier."""
    return sorted(element.name for element in Path(dossier).iterdir())


def compter_par_extension(dossier):
    """Compte les fichiers par extension."""
    compteur = {}
    for element in Path(dossier).iterdir():
        if element.is_file():                     # on ignore les sous-dossiers
            ext = element.suffix                  # ".txt", ".csv", ...
            compteur[ext] = compteur.get(ext, 0) + 1   # +1, ou 1 si jamais vu
    return compteur


def sauver_puis_charger_json(chemin, donnees):
    """Écrit un dict en JSON puis le relit."""
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f)        # dict Python → texte JSON dans le fichier
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)          # texte JSON → dict Python


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification
# ════════════════════════════════════════════════════════════════════
import tempfile
import os


def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 10 (solutions) ---")
    dossier = tempfile.mkdtemp()
    for nom_fichier in ["a.txt", "b.txt", "c.csv"]:
        Path(dossier, nom_fichier).write_text("x", encoding="utf-8")
    chemin_json = os.path.join(dossier, "data.json")

    res = [
        _check("lister_noms(...)", lister_noms(dossier), ["a.txt", "b.txt", "c.csv"]),
        _check("compter_par_extension(...)", compter_par_extension(dossier), {".txt": 2, ".csv": 1}),
        _check("sauver_puis_charger_json(...)", sauver_puis_charger_json(chemin_json, {"a": 1}), {"a": 1}),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
