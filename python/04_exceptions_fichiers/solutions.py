#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 04 : exceptions & fichiers

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""


def division_sure(a, b):
    """a / b, ou None si division par zéro."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def convertir_entier(texte):
    """Convertit en int, ou None si impossible."""
    try:
        return int(texte)
    except ValueError:
        return None


def ecrire_puis_lire(chemin, contenu):
    """Écrit puis relit un fichier."""
    with open(chemin, "w", encoding="utf-8") as f:   # "w" = écriture (écrase)
        f.write(contenu)
    with open(chemin, "r", encoding="utf-8") as f:   # "r" = lecture
        return f.read()


def compter_lignes(chemin):
    """Nombre de lignes, 0 si le fichier n'existe pas."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return len(f.readlines())     # readlines() → liste des lignes
    except FileNotFoundError:
        return 0


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
    print("--- Vérification — module 04 (solutions) ---")
    dossier = tempfile.mkdtemp()
    chemin = os.path.join(dossier, "test.txt")
    chemin3 = os.path.join(dossier, "trois.txt")
    with open(chemin3, "w", encoding="utf-8") as f:
        f.write("a\nb\nc\n")

    res = [
        _check("division_sure(10, 2)", division_sure(10, 2), 5.0),
        _check("division_sure(10, 0)", division_sure(10, 0), None),
        _check("convertir_entier('42')", convertir_entier("42"), 42),
        _check("convertir_entier('abc')", convertir_entier("abc"), None),
        _check("ecrire_puis_lire(...)", ecrire_puis_lire(chemin, "salut"), "salut"),
        _check("compter_lignes(3 lignes)", compter_lignes(chemin3), 3),
        _check("compter_lignes(inexistant)", compter_lignes(os.path.join(dossier, "nope.txt")), 0),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
