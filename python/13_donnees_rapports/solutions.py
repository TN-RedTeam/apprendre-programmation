#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 13 : données & rapports

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
(En pandas : df["montant"].sum(), df.groupby("produit")["montant"].sum(),
 df[df["montant"] > seuil] — ici on le fait à la main pour comprendre.)
"""


def chiffre_affaires_total(ventes):
    """Somme de tous les montants."""
    return sum(vente["montant"] for vente in ventes)


def total_par_produit(ventes):
    """Total des montants regroupés par produit (un groupby manuel)."""
    totaux = {}
    for vente in ventes:
        produit = vente["produit"]
        totaux[produit] = totaux.get(produit, 0) + vente["montant"]
    return totaux


def grosses_ventes(ventes, seuil):
    """Ventes au-dessus du seuil."""
    return [vente for vente in ventes if vente["montant"] > seuil]


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
    print("--- Vérification — module 13 (solutions) ---")
    ventes = [
        {"produit": "pomme", "montant": 10},
        {"produit": "pomme", "montant": 5},
        {"produit": "poire", "montant": 3},
    ]
    res = [
        _check("chiffre_affaires_total", chiffre_affaires_total(ventes), 18),
        _check("total_par_produit", total_par_produit(ventes), {"pomme": 15, "poire": 3}),
        _check("grosses_ventes(>4)", grosses_ventes(ventes, 4),
               [{"produit": "pomme", "montant": 10}, {"produit": "pomme", "montant": 5}]),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
