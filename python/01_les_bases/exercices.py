#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 01 : les bases (variables, conditions, boucles)

COMMENT T'ENTRAÎNER :
  1. Complète chaque fonction là où il y a "TODO" (remplace la ligne `...`).
  2. Lance ce fichier :   python3 exercices.py
  3. Chaque ✅ = réussi, chaque ❌ = à corriger. Objectif : tout en vert.
  4. Bloqué après un vrai essai ? Regarde solutions.py (mais essaie D'ABORD).
"""


def somme_jusqua(n):
    """Renvoie la somme de tous les entiers de 1 à n inclus.
    Ex : somme_jusqua(5) -> 15   (1 + 2 + 3 + 4 + 5)
    """
    # TODO : utilise une boucle for et range pour additionner
    ...


def est_pair(n):
    """Renvoie True si n est pair, False sinon.
    Indice : un nombre est pair si son reste dans la division par 2 vaut 0.
    """
    # TODO : utilise l'opérateur modulo %
    ...


def fizzbuzz(n):
    """Pour UN nombre n, renvoie (sous forme de texte) :
      - "FizzBuzz" si n est divisible par 3 ET par 5,
      - "Fizz"     si divisible par 3 seulement,
      - "Buzz"     si divisible par 5 seulement,
      - sinon le nombre lui-même converti en texte, ex. "7".
    """
    # TODO : attention à l'ORDRE des conditions (le cas le plus précis d'abord)
    ...


def compte_a_rebours(depart):
    """Renvoie une liste qui décompte de `depart` jusqu'à 1.
    Ex : compte_a_rebours(3) -> [3, 2, 1]
    """
    # TODO : une boucle while ou un range décroissant
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
    print("--- Vérification — module 01 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("somme_jusqua(5)", lambda: somme_jusqua(5), 15)
    essai("somme_jusqua(1)", lambda: somme_jusqua(1), 1)
    essai("est_pair(4)", lambda: est_pair(4), True)
    essai("est_pair(7)", lambda: est_pair(7), False)
    essai("fizzbuzz(15)", lambda: fizzbuzz(15), "FizzBuzz")
    essai("fizzbuzz(9)", lambda: fizzbuzz(9), "Fizz")
    essai("fizzbuzz(10)", lambda: fizzbuzz(10), "Buzz")
    essai("fizzbuzz(7)", lambda: fizzbuzz(7), "7")
    essai("compte_a_rebours(3)", lambda: compte_a_rebours(3), [3, 2, 1])

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
