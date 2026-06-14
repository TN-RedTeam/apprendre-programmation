"""
MODULE 08 (avancé) - Définir et utiliser une CLASSE
===================================================
Ce script illustre les notions du README :
classe (le plan), objet (l'exemplaire), __init__ (le constructeur),
self (l'objet courant), attributs (données) et méthodes (actions).

Exemple choisi : un CompteBancaire, parce qu'il regroupe naturellement
des DONNÉES (le solde) et des ACTIONS (déposer, retirer).

Lance-le :  python3 python/automatisation/08_poo/classes.py
"""

# ─────────────────────────────────────────────
# 1. DÉFINIR UNE CLASSE (le plan / le moule)
# ─────────────────────────────────────────────
# 'class' = "définir un plan". On l'écrit UNE seule fois, puis on fabrique
# autant d'objets (exemplaires) qu'on veut à partir de ce plan.
class CompteBancaire:
    """Un compte en banque : un titulaire et un solde, qu'on peut faire évoluer."""

    # __init__ = le CONSTRUCTEUR. Python l'appelle AUTOMATIQUEMENT chaque fois
    # qu'on crée un objet. Son rôle : mettre l'objet en place (lui donner ses
    # données de départ).
    #   self           = l'objet courant ("MOI, cet exemplaire-ci")
    #   titulaire/depot = les informations qu'on fournit à la création
    def __init__(self, titulaire, depot_initial):
        # self.titulaire = on RANGE le titulaire DANS cet objet (un ATTRIBUT).
        self.titulaire = titulaire
        # self._solde : le '_' au début signale "donnée interne, n'y touche pas
        # directement de l'extérieur ; passe par les méthodes". C'est la
        # convention d'ENCAPSULATION (une politesse entre développeurs).
        self._solde = depot_initial

    # Une MÉTHODE = une ACTION que l'objet sait faire. C'est une fonction
    # définie DANS la classe, dont le 1er paramètre est toujours 'self'.
    def deposer(self, montant):
        """Ajoute de l'argent sur le compte."""
        self._solde += montant     # on modifie le solde DE CET objet
        print(f"+{montant} € déposés. Nouveau solde : {self._solde} €")

    def retirer(self, montant):
        """Retire de l'argent, si le solde est suffisant."""
        # On VÉRIFIE avant d'agir : c'est tout l'intérêt de passer par une méthode
        # plutôt que de modifier le solde n'importe comment depuis l'extérieur.
        if montant > self._solde:
            print(f"❌ Retrait refusé : il manque {montant - self._solde} €.")
        else:
            self._solde -= montant
            print(f"-{montant} € retirés. Nouveau solde : {self._solde} €")

    def afficher_solde(self):
        """Affiche le solde actuel du compte."""
        # self.titulaire et self._solde lisent les données DE CET objet précis.
        print(f"💰 Solde de {self.titulaire} : {self._solde} €")


# ─────────────────────────────────────────────
# 2. CRÉER DES OBJETS (des exemplaires du plan)
# ─────────────────────────────────────────────
# Écrire CompteBancaire(...) FABRIQUE un objet : Python appelle __init__ tout
# seul avec les valeurs entre parenthèses. On range l'objet créé dans une variable.
compte_alice = CompteBancaire("Alice", 100)   # déclenche __init__("Alice", 100)
compte_bob = CompteBancaire("Bob", 50)        # un AUTRE objet, indépendant

# Les deux objets sortent du MÊME plan, mais chacun a SES propres données :
compte_alice.afficher_solde()    # 💰 Solde de Alice : 100 €
compte_bob.afficher_solde()      # 💰 Solde de Bob : 50 €


# ─────────────────────────────────────────────
# 3. UTILISER LES MÉTHODES (faire agir les objets)
# ─────────────────────────────────────────────
# objet.methode() : Python passe l'objet en tant que 'self' à la méthode.
# Ainsi compte_alice.deposer(40) agit sur le solde D'ALICE, pas celui de Bob.
compte_alice.deposer(40)         # +40 € → 140 €
compte_alice.retirer(200)        # refusé : il manque 60 €
compte_alice.retirer(30)         # -30 € → 110 €

# Bob est resté intact : preuve que chaque objet a sa propre "boîte de données".
compte_bob.afficher_solde()      # 💰 Solde de Bob : 50 €


# ─────────────────────────────────────────────
# 4. LIRE UN ATTRIBUT DIRECTEMENT
# ─────────────────────────────────────────────
# On peut lire un attribut "public" (sans _) directement avec objet.attribut.
print(f"Le titulaire du premier compte est : {compte_alice.titulaire}")
