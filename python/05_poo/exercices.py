#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 05 : la POO (classes)

  1. Complète chaque classe (remplace les `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.
"""


class Rectangle:
    """Un rectangle défini par sa largeur et sa hauteur.

    Doit fournir :
      - __init__(self, largeur, hauteur)  → range les deux dans l'objet
      - aire(self)        → largeur * hauteur
      - perimetre(self)   → 2 * (largeur + hauteur)
    """

    def __init__(self, largeur, hauteur):
        # TODO : range largeur et hauteur dans self
        ...

    def aire(self):
        # TODO
        ...

    def perimetre(self):
        # TODO
        ...


class Carre(Rectangle):
    """Un carré EST un rectangle dont les deux côtés sont égaux.

    __init__(self, cote) doit appeler le constructeur du parent (super())
    avec le même côté pour la largeur ET la hauteur.
    """

    def __init__(self, cote):
        # TODO : utilise super().__init__(...)
        ...


class CompteBancaire:
    """Un compte avec un solde.

      - __init__(self, solde=0)
      - deposer(self, montant)   → augmente le solde
      - retirer(self, montant)   → diminue le solde, MAIS refuse (ne fait rien)
                                    si le montant dépasse le solde
    """

    def __init__(self, solde=0):
        # TODO
        ...

    def deposer(self, montant):
        # TODO
        ...

    def retirer(self, montant):
        # TODO : vérifie d'abord que le solde est suffisant
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
    print("--- Vérification — module 05 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("Rectangle(3,4).aire()", lambda: Rectangle(3, 4).aire(), 12)
    essai("Rectangle(3,4).perimetre()", lambda: Rectangle(3, 4).perimetre(), 14)
    essai("Carre(5).aire()", lambda: Carre(5).aire(), 25)
    essai("Carre(5).perimetre()", lambda: Carre(5).perimetre(), 20)

    def scenario_compte():
        c = CompteBancaire(100)
        c.deposer(50)        # 150
        c.retirer(200)       # refusé → reste 150
        c.retirer(30)        # 120
        return c.solde

    essai("CompteBancaire scénario", scenario_compte, 120)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
