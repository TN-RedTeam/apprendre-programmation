#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 04 : exceptions & fichiers

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.
"""


def division_sure(a, b):
    """Renvoie a / b, ou None si b vaut 0 (au lieu de planter).
    Ex : division_sure(10, 2) -> 5.0
         division_sure(10, 0) -> None
    """
    # TODO : utilise try / except ZeroDivisionError
    ...


def convertir_entier(texte):
    """Convertit `texte` en entier, ou renvoie None si ce n'est pas un nombre.
    Ex : convertir_entier("42")  -> 42
         convertir_entier("abc") -> None
    """
    # TODO : try / except ValueError autour de int(...)
    ...


def ecrire_puis_lire(chemin, contenu):
    """Écrit `contenu` dans le fichier `chemin`, puis relit et renvoie ce qu'il contient.
    Ex : ecrire_puis_lire("/tmp/x.txt", "salut") -> "salut"
    Utilise `with open(...)` en mode "w" puis "r", avec encoding="utf-8".
    """
    # TODO : deux blocs with open(...)
    ...


def compter_lignes(chemin):
    """Renvoie le nombre de lignes du fichier `chemin`.
    Si le fichier n'existe pas, renvoie 0 (sans planter).
    """
    # TODO : try / except FileNotFoundError ; lis les lignes et compte-les
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
    print("--- Vérification — module 04 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("division_sure(10, 2)", lambda: division_sure(10, 2), 5.0)
    essai("division_sure(10, 0)", lambda: division_sure(10, 0), None)
    essai("convertir_entier('42')", lambda: convertir_entier("42"), 42)
    essai("convertir_entier('abc')", lambda: convertir_entier("abc"), None)

    # Exercices fichiers : on travaille dans un dossier temporaire
    dossier = tempfile.mkdtemp()
    chemin = os.path.join(dossier, "test.txt")
    essai("ecrire_puis_lire(...)", lambda: ecrire_puis_lire(chemin, "salut"), "salut")

    chemin3 = os.path.join(dossier, "trois.txt")
    with open(chemin3, "w", encoding="utf-8") as f:
        f.write("a\nb\nc\n")
    essai("compter_lignes(3 lignes)", lambda: compter_lignes(chemin3), 3)
    essai("compter_lignes(inexistant)", lambda: compter_lignes(os.path.join(dossier, "nope.txt")), 0)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
