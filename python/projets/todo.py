"""
MINI-PROJET - Liste de tâches (to-do) persistante en ligne de commande
======================================================================
Une vraie petite "to-do list" dans ton terminal : tu peux AJOUTER des tâches,
les LISTER, en marquer comme FAITES, et en SUPPRIMER. Tout est SAUVEGARDÉ dans
un fichier JSON, donc ta liste te suit d'un lancement à l'autre.

C'est le grand frère du carnet de contacts : même structure (sous-commandes
argparse + sauvegarde JSON), mais avec une notion d'ÉTAT (fait / à faire).

Il réutilise :
   - module 02 : listes et dictionnaires (une tâche = {"texte": ..., "fait": ...}) ;
   - module 04 : lire/écrire un fichier JSON ;
   - module 12 : argparse avec des SOUS-COMMANDES.

Exemples de lancement :
   python3 python/projets/todo.py ajouter --texte "Acheter du pain"
   python3 python/projets/todo.py ajouter --texte "Réviser Python"
   python3 python/projets/todo.py lister
   python3 python/projets/todo.py terminer --numero 1
   python3 python/projets/todo.py supprimer --numero 2
   python3 python/projets/todo.py --help

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : argparse, json, pathlib.
   2. CHEMIN     : où ranger le fichier "taches.json".
   3. FONCTIONS  : charger / sauvegarder / ajouter / lister / terminer / supprimer.
   4. creer_parseur() : définit les sous-commandes et leurs options.
   5. main()     : lit la commande tapée et appelle la bonne fonction.
   6. __main__   : lance main() quand on exécute le fichier.
"""

import argparse
import json
from pathlib import Path


# Le fichier de données, rangé dans "exemples/" À CÔTÉ de ce script
# (dossier ignoré par git : tes tâches ne seront pas commitées).
FICHIER_TACHES = Path(__file__).parent / "exemples" / "taches.json"


def charger():
    """Lit le fichier JSON et renvoie la LISTE des tâches (ou une liste vide)."""
    if not FICHIER_TACHES.exists():       # au tout premier lancement, pas de fichier
        return []
    with open(FICHIER_TACHES, "r", encoding="utf-8") as f:
        return json.load(f)               # texte JSON → liste de dictionnaires


def sauvegarder(taches):
    """Écrit la liste des tâches dans le fichier JSON (crée le dossier au besoin)."""
    FICHIER_TACHES.parent.mkdir(parents=True, exist_ok=True)
    with open(FICHIER_TACHES, "w", encoding="utf-8") as f:
        # indent=2 → fichier lisible ; ensure_ascii=False → garde les accents.
        json.dump(taches, f, indent=2, ensure_ascii=False)


def ajouter(texte):
    """Ajoute une nouvelle tâche (au départ : NON faite), puis sauvegarde."""
    taches = charger()
    # Une tâche est un dictionnaire avec son texte et son état "fait".
    taches.append({"texte": texte, "fait": False})
    sauvegarder(taches)
    print(f"[+] Tâche ajoutée : {texte}")


def lister():
    """Affiche toutes les tâches, numérotées, avec une case [ ] ou [x]."""
    taches = charger()
    if not taches:                        # liste vide → message d'accueil
        print("Aucune tâche. Ajoute-en une avec : todo.py ajouter --texte \"...\"")
        return

    print(f"--- {len(taches)} tâche(s) ---")
    # enumerate(..., start=1) donne un numéro lisible (1, 2, 3...) à chaque tâche.
    for numero, tache in enumerate(taches, start=1):
        # Un ternaire (module COMPRENDRE_LE_CODE) : "[x]" si faite, sinon "[ ]".
        case = "[x]" if tache["fait"] else "[ ]"
        print(f"{numero}. {case} {tache['texte']}")


def terminer(numero):
    """Marque la tâche n°`numero` comme faite, puis sauvegarde."""
    taches = charger()

    # L'utilisateur compte à partir de 1, mais les listes commencent à l'index 0.
    # On vérifie d'abord que le numéro est valide pour éviter un plantage (IndexError).
    if numero < 1 or numero > len(taches):
        print(f"Numéro invalide : {numero} (il y a {len(taches)} tâche(s)).")
        return

    taches[numero - 1]["fait"] = True     # -1 : convertir le numéro humain en index
    sauvegarder(taches)
    print(f"[✓] Tâche {numero} terminée : {taches[numero - 1]['texte']}")


def supprimer(numero):
    """Supprime la tâche n°`numero`, puis sauvegarde."""
    taches = charger()
    if numero < 1 or numero > len(taches):
        print(f"Numéro invalide : {numero} (il y a {len(taches)} tâche(s)).")
        return

    # .pop(index) retire l'élément à cette position ET le renvoie : pratique
    # pour afficher ce qu'on vient d'enlever.
    enlevee = taches.pop(numero - 1)
    sauvegarder(taches)
    print(f"[-] Tâche supprimée : {enlevee['texte']}")


def creer_parseur():
    """Définit les sous-commandes (ajouter, lister, terminer, supprimer)."""
    parseur = argparse.ArgumentParser(description="Une liste de tâches en ligne de commande.")
    sous = parseur.add_subparsers(dest="commande", required=True)

    p_ajouter = sous.add_parser("ajouter", help="Ajouter une tâche")
    p_ajouter.add_argument("--texte", required=True, help="Le texte de la tâche")

    sous.add_parser("lister", help="Afficher toutes les tâches")

    p_terminer = sous.add_parser("terminer", help="Marquer une tâche comme faite")
    # type=int : le numéro doit être un entier (argparse convertit et vérifie).
    p_terminer.add_argument("--numero", type=int, required=True, help="Numéro de la tâche")

    p_supprimer = sous.add_parser("supprimer", help="Supprimer une tâche")
    p_supprimer.add_argument("--numero", type=int, required=True, help="Numéro de la tâche")

    return parseur


def main():
    """Lit la commande tapée et appelle la fonction correspondante."""
    args = creer_parseur().parse_args()

    if args.commande == "ajouter":
        ajouter(args.texte)
    elif args.commande == "lister":
        lister()
    elif args.commande == "terminer":
        terminer(args.numero)
    elif args.commande == "supprimer":
        supprimer(args.numero)


if __name__ == "__main__":
    main()
