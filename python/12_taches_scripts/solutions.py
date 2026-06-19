#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 12 : scripts réutilisables (argparse)

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""

import argparse


def construire_parseur():
    """Parseur avec --source (obligatoire) et --destination (défaut)."""
    parseur = argparse.ArgumentParser(description="Sauvegarde un dossier")
    parseur.add_argument("--source", required=True, help="Dossier à sauvegarder")
    parseur.add_argument("--destination", default="sauvegardes", help="Où copier")
    return parseur


def nom_archive(source, date):
    """Nom d'archive : <source>_<date>.zip."""
    return f"{source}_{date}.zip"


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
    print("--- Vérification — module 12 (solutions) ---")
    p = construire_parseur()
    res = [
        _check("destination par défaut", p.parse_args(["--source", "docs"]).destination, "sauvegardes"),
        _check("source lue", p.parse_args(["--source", "docs", "--destination", "sav"]).source, "docs"),
        _check("nom_archive('docs','2026-06-19')", nom_archive("docs", "2026-06-19"), "docs_2026-06-19.zip"),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
