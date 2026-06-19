#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 01 : les bases

Corrigé commenté des exercices de exercices.py.
Lance-le pour vérifier que tout passe au vert :   python3 solutions.py
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


def somme_jusqua(n):
    """Somme des entiers de 1 à n inclus."""
    total = 0
    for i in range(1, n + 1):     # range(1, n+1) → 1, 2, ..., n  (n+1 est exclu)
        total += i                # total = total + i
    return total
    # Variante experte : return sum(range(1, n + 1))


def est_pair(n):
    """True si n est pair."""
    return n % 2 == 0             # le reste de la division par 2 vaut 0 → pair


def fizzbuzz(n):
    """Renvoie Fizz / Buzz / FizzBuzz / le nombre, pour un n donné."""
    if n % 3 == 0 and n % 5 == 0:   # cas le PLUS précis testé en premier
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)               # str() convertit le nombre en texte


def compte_a_rebours(depart):
    """Liste décroissante de depart à 1."""
    resultat = []
    compteur = depart
    while compteur > 0:             # tant que positif
        resultat.append(compteur)
        compteur -= 1               # IMPORTANT : faire avancer vers la fin
    return resultat
    # Variante : return list(range(depart, 0, -1))


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification (identique à exercices.py)
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 01 (solutions) ---")
    res = [
        _check("somme_jusqua(5)", somme_jusqua(5), 15),
        _check("somme_jusqua(1)", somme_jusqua(1), 1),
        _check("est_pair(4)", est_pair(4), True),
        _check("est_pair(7)", est_pair(7), False),
        _check("fizzbuzz(15)", fizzbuzz(15), "FizzBuzz"),
        _check("fizzbuzz(9)", fizzbuzz(9), "Fizz"),
        _check("fizzbuzz(10)", fizzbuzz(10), "Buzz"),
        _check("fizzbuzz(7)", fizzbuzz(7), "7"),
        _check("compte_a_rebours(3)", compte_a_rebours(3), [3, 2, 1]),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
