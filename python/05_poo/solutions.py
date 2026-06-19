#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 05 : la POO

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""


class Rectangle:
    """Rectangle (largeur, hauteur)."""

    def __init__(self, largeur, hauteur):
        self.largeur = largeur          # on RANGE les données dans l'objet (self)
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)


class Carre(Rectangle):
    """Carré : un rectangle aux côtés égaux."""

    def __init__(self, cote):
        super().__init__(cote, cote)    # réutilise le constructeur du parent (même côté ×2)
        # aire() et perimetre() sont HÉRITÉS de Rectangle : rien à réécrire.


class CompteBancaire:
    """Compte avec solde, dépôt et retrait sécurisé."""

    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:        # garde : on refuse si insuffisant
            return                      # on quitte sans rien changer
        self.solde -= montant


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
    print("--- Vérification — module 05 (solutions) ---")
    c = CompteBancaire(100)
    c.deposer(50)
    c.retirer(200)
    c.retirer(30)
    res = [
        _check("Rectangle(3,4).aire()", Rectangle(3, 4).aire(), 12),
        _check("Rectangle(3,4).perimetre()", Rectangle(3, 4).perimetre(), 14),
        _check("Carre(5).aire()", Carre(5).aire(), 25),
        _check("Carre(5).perimetre()", Carre(5).perimetre(), 20),
        _check("CompteBancaire scénario", c.solde, 120),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
