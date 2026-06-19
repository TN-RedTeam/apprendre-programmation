#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 10 : fichiers & dossiers (pathlib, json)

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.
"""

from pathlib import Path
import json


def lister_noms(dossier):
    """Renvoie la liste TRIÉE des noms de fichiers/dossiers présents dans `dossier`.
    `dossier` est un chemin (str ou Path).
    Ex : si le dossier contient a.txt et b.txt -> ["a.txt", "b.txt"]
    Indice : Path(dossier).iterdir() ; l'attribut .name donne le nom court.
    """
    # TODO : parcours iterdir(), récupère .name, renvoie une liste triée
    ...


def compter_par_extension(dossier):
    """Renvoie un dict {extension: nombre} pour les fichiers de `dossier`.
    Ex : pour a.txt, b.txt, c.csv -> {".txt": 2, ".csv": 1}
    Indice : l'attribut .suffix d'un Path donne l'extension (ex. ".txt").
    """
    # TODO : utilise un dict et .get(ext, 0) + 1
    ...


def sauver_puis_charger_json(chemin, donnees):
    """Écrit `donnees` (un dict) en JSON dans `chemin`, puis le recharge et le renvoie.
    Ex : sauver_puis_charger_json("/tmp/x.json", {"a": 1}) -> {"a": 1}
    Indice : json.dump(obj, fichier) pour écrire, json.load(fichier) pour lire.
    """
    # TODO : un with open(..., "w") + json.dump, puis un with open(..., "r") + json.load
    ...


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification — NE PAS MODIFIER
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
    print("--- Vérification — module 10 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    # Prépare un dossier temporaire avec quelques fichiers
    dossier = tempfile.mkdtemp()
    for nom_fichier in ["a.txt", "b.txt", "c.csv"]:
        Path(dossier, nom_fichier).write_text("x", encoding="utf-8")

    essai("lister_noms(...)", lambda: lister_noms(dossier), ["a.txt", "b.txt", "c.csv"])
    essai("compter_par_extension(...)", lambda: compter_par_extension(dossier), {".txt": 2, ".csv": 1})

    chemin_json = os.path.join(dossier, "data.json")
    essai("sauver_puis_charger_json(...)", lambda: sauver_puis_charger_json(chemin_json, {"a": 1}), {"a": 1})

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
