#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 12 : scripts réutilisables (argparse)

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.
"""

import argparse


def construire_parseur():
    """Renvoie un ArgumentParser configuré ainsi :
      - un argument OBLIGATOIRE  --source
      - un argument FACULTATIF   --destination, avec la valeur par défaut "sauvegardes"
    (Ne pas appeler parse_args ici : juste construire et renvoyer le parseur.)
    """
    # TODO :
    #   parseur = argparse.ArgumentParser(...)
    #   parseur.add_argument("--source", required=True)
    #   parseur.add_argument("--destination", default="sauvegardes")
    #   return parseur
    ...


def nom_archive(source, date):
    """Renvoie le nom d'archive au format "<source>_<date>.zip".
    Ex : nom_archive("docs", "2026-06-19") -> "docs_2026-06-19.zip"
    """
    # TODO : une f-string
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
    print("--- Vérification — module 12 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    def dest_par_defaut():
        p = construire_parseur()
        return p.parse_args(["--source", "docs"]).destination

    def source_lue():
        p = construire_parseur()
        return p.parse_args(["--source", "docs", "--destination", "sav"]).source

    essai("destination par défaut", dest_par_defaut, "sauvegardes")
    essai("source lue", source_lue, "docs")
    essai("nom_archive('docs','2026-06-19')", lambda: nom_archive("docs", "2026-06-19"), "docs_2026-06-19.zip")

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
