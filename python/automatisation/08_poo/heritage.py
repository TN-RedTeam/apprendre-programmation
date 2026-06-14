"""
MODULE 08 (avancé) - L'HÉRITAGE
===============================
Ce script illustre les notions du README :
classe MÈRE et classes FILLES, redéfinition d'une méthode, super()
(appeler la version de la mère) et __str__ (affichage lisible).

╔══════════════════════════════════════════════════════════════════════╗
║ 🗺️  CHEMINEMENT DU SCRIPT                                             ║
║                                                                      ║
║ 1. On définit une classe MÈRE  : Animal (nom, age, manger, crier).   ║
║ 2. On définit deux classes FILLES : Chien et Chat, qui HÉRITENT      ║
║    d'Animal et REDÉFINISSENT le cri à leur façon.                    ║
║    - Chien ajoute un attribut (race) via super().__init__(...).      ║
║ 3. On ajoute __str__ pour un affichage lisible avec print(objet).    ║
║ 4. On crée des objets et on les fait agir : on voit que le code      ║
║    commun (manger) est réutilisé, et que le cri est spécialisé.      ║
╚══════════════════════════════════════════════════════════════════════╝

Lance-le :  python3 python/automatisation/08_poo/heritage.py
"""

# ─────────────────────────────────────────────
# 1. LA CLASSE MÈRE (le tronc commun)
# ─────────────────────────────────────────────
# Animal regroupe ce que TOUS les animaux ont en commun. Les classes filles
# vont en hériter pour ne pas réécrire ce code.
class Animal:
    """Classe mère : tout animal a un nom, un âge, mange et émet un cri."""

    def __init__(self, nom, age):
        self.nom = nom        # attribut commun à tous les animaux
        self.age = age        # idem

    def manger(self):
        """Action commune : tous les animaux mangent pareil ici."""
        print(f"{self.nom} mange. 🍽️")

    def crier(self):
        """Cri générique. Les filles vont le REDÉFINIR (chacune son cri)."""
        print(f"{self.nom} fait un bruit.")

    # __str__ décide COMMENT l'objet s'affiche avec print(). Il RENVOIE un texte.
    # Hérité par les filles, donc print(chien) et print(chat) marcheront aussi.
    def __str__(self):
        return f"{self.nom}, {self.age} ans"


# ─────────────────────────────────────────────
# 2. PREMIÈRE CLASSE FILLE : Chien
# ─────────────────────────────────────────────
# 'class Chien(Animal)' : les parenthèses signifient "Chien HÉRITE d'Animal".
# Chien récupère gratuitement __init__, manger, crier et __str__.
class Chien(Animal):
    """Classe fille : un chien EST un animal, avec en plus une race et son cri."""

    def __init__(self, nom, age, race):
        # super() = "la classe mère". On lui laisse remplir nom et age...
        super().__init__(nom, age)
        # ... puis on AJOUTE ce qui est propre au chien.
        self.race = race

    # On REDÉFINIT crier() : la version du chien remplace celle d'Animal.
    def crier(self):
        print(f"{self.nom} dit : Wouf ! 🐶")


# ─────────────────────────────────────────────
# 3. DEUXIÈME CLASSE FILLE : Chat
# ─────────────────────────────────────────────
class Chat(Animal):
    """Classe fille : un chat EST un animal, avec son propre cri."""

    # Pas de __init__ ici : Chat réutilise tel quel celui d'Animal (nom, age).
    def crier(self):
        print(f"{self.nom} dit : Miaou ! 🐱")


# ─────────────────────────────────────────────
# 4. ON CRÉE ET ON UTILISE LES OBJETS
# ─────────────────────────────────────────────
rex = Chien("Rex", 3, "Labrador")    # déclenche le __init__ de Chien (puis super)
felix = Chat("Félix", 5)             # déclenche le __init__ hérité d'Animal

# print(objet) déclenche __str__ (hérité d'Animal par les deux filles).
print(rex)      # Rex, 3 ans
print(felix)    # Félix, 5 ans

# manger() vient de la MÈRE : code réutilisé, écrit une seule fois.
rex.manger()    # Rex mange. 🍽️
felix.manger()  # Félix mange. 🍽️

# crier() est SPÉCIALISÉ dans chaque fille : chacun fait son propre cri.
rex.crier()     # Rex dit : Wouf ! 🐶
felix.crier()   # Félix dit : Miaou ! 🐱

# L'attribut ajouté par la fille Chien est bien disponible :
print(f"{rex.nom} est un {rex.race}.")   # Rex est un Labrador.
