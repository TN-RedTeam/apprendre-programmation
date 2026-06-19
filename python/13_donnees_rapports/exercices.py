#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 13 : données & rapports (le RAISONNEMENT, sans pandas)

pandas fait ça en une ligne, mais pour bien comprendre, on reproduit ici la
logique d'un rapport « à la main » avec des listes de dictionnaires.

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.

Format des données : une liste de ventes, chaque vente est un dict, ex.
    {"produit": "pomme", "montant": 10}
"""


def chiffre_affaires_total(ventes):
    """Renvoie la somme de tous les "montant".
    Ex : [{"montant": 10}, {"montant": 5}] -> 15
    """
    # TODO
    ...


def total_par_produit(ventes):
    """Renvoie un dict {produit: somme des montants de ce produit} (comme un groupby).
    Ex : [{"produit":"a","montant":10}, {"produit":"a","montant":5}, {"produit":"b","montant":3}]
         -> {"a": 15, "b": 3}
    """
    # TODO : parcours les ventes, accumule dans un dict avec .get(produit, 0)
    ...


def grosses_ventes(ventes, seuil):
    """Renvoie la liste des ventes dont le "montant" dépasse strictement `seuil`.
    Ex : grosses_ventes([{"montant":10},{"montant":3}], 5) -> [{"montant":10}]
    """
    # TODO : une compréhension de liste avec un filtre
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
    print("--- Vérification — module 13 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    ventes = [
        {"produit": "pomme", "montant": 10},
        {"produit": "pomme", "montant": 5},
        {"produit": "poire", "montant": 3},
    ]

    essai("chiffre_affaires_total", lambda: chiffre_affaires_total(ventes), 18)
    essai("total_par_produit", lambda: total_par_produit(ventes), {"pomme": 15, "poire": 3})
    essai("grosses_ventes(>4)", lambda: grosses_ventes(ventes, 4),
          [{"produit": "pomme", "montant": 10}, {"produit": "pomme", "montant": 5}])

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
