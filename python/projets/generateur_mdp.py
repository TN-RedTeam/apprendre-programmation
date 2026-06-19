"""
MINI-PROJET - Générateur de mots de passe solides
==================================================
Un outil en ligne de commande qui fabrique des mots de passe aléatoires, avec
des options : longueur, présence de chiffres, de symboles, et nombre de mots de
passe à générer d'un coup.

Il réutilise :
   - module 01/02 : construire du texte, des listes ;
   - module 12    : argparse (les options en ligne de commande).

⭐ POINT IMPORTANT (sécurité) : pour un mot de passe, on N'UTILISE PAS le module
   'random'. On utilise 'secrets', conçu spécialement pour le hasard
   "cryptographique" (imprévisible). 'random' est très bien pour un jeu ou une
   simulation, mais ses tirages sont PRÉVISIBLES par un attaquant — donc à
   proscrire pour tout ce qui touche à la sécurité. Retenir cette distinction
   te place déjà au-dessus de beaucoup de débutants.

Exemples de lancement :
   python3 python/projets/generateur_mdp.py
   python3 python/projets/generateur_mdp.py --longueur 24 --symboles
   python3 python/projets/generateur_mdp.py --longueur 12 --sans-chiffres --nombre 5
   python3 python/projets/generateur_mdp.py --help

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : secrets (hasard sûr), string (lettres/chiffres tout prêts), argparse.
   2. construire_alphabet() : assemble l'ensemble des caractères autorisés.
   3. generer()  : tire au hasard, caractère par caractère, le mot de passe.
   4. creer_parseur() : déclare les options (--longueur, --symboles, ...).
   5. PROGRAMME (main + __main__) : lit les options et affiche le(s) mot(s) de passe.
   (Pour comprendre : commence par lire main() puis le bloc __main__ en bas.)
"""

# ─────────────────────────────────────────────
# 1. IMPORTS (tout est dans la bibliothèque standard : rien à installer)
# ─────────────────────────────────────────────

# secrets = le module pour un hasard SÛR (mots de passe, jetons...).
import secrets

# string = des constantes pratiques contenant des familles de caractères :
#   string.ascii_letters = "abc...XYZ" (toutes les lettres min + maj)
#   string.digits        = "0123456789"
#   string.punctuation   = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
import string

# argparse = pour lire les options tapées au terminal.
import argparse


# ─────────────────────────────────────────────
# 2. CONSTRUIRE L'ENSEMBLE DES CARACTÈRES AUTORISÉS
# ─────────────────────────────────────────────
def construire_alphabet(avec_chiffres: bool, avec_symboles: bool) -> str:
    """Renvoie une grande chaîne contenant TOUS les caractères utilisables.
    On part des lettres, puis on AJOUTE (concaténation avec +) chiffres et
    symboles selon les options demandées.
    """
    # Les lettres sont toujours incluses : c'est la base.
    alphabet = string.ascii_letters          # "abc...XYZ"

    if avec_chiffres:                         # si l'option chiffres est active
        alphabet += string.digits            # on colle "0123456789" à la suite

    if avec_symboles:                         # si l'option symboles est active
        alphabet += string.punctuation       # on colle les symboles

    return alphabet


# ─────────────────────────────────────────────
# 3. GÉNÉRER UN MOT DE PASSE
# ─────────────────────────────────────────────
def generer(longueur: int, avec_chiffres: bool = True, avec_symboles: bool = False) -> str:
    """Fabrique UN mot de passe aléatoire de `longueur` caractères."""
    alphabet = construire_alphabet(avec_chiffres, avec_symboles)

    # secrets.choice(alphabet) tire UN caractère au hasard (de façon sûre).
    # On répète l'opération `longueur` fois grâce à une compréhension, puis
    # "".join(...) recolle tous ces caractères en une seule chaîne.
    #   - le "_" signifie "variable de boucle dont on n'a pas besoin"
    #   - "".join(...) avec séparateur vide = on colle sans rien entre les lettres
    return "".join(secrets.choice(alphabet) for _ in range(longueur))


# ─────────────────────────────────────────────
# 4. DÉCLARER LES OPTIONS (argparse)
# ─────────────────────────────────────────────
def creer_parseur() -> argparse.ArgumentParser:
    """Définit les options de la ligne de commande."""
    parseur = argparse.ArgumentParser(description="Génère des mots de passe solides.")

    # --longueur attend un ENTIER (type=int). Par défaut 16 si non fourni.
    parseur.add_argument("--longueur", type=int, default=16,
                         help="Longueur du mot de passe (défaut : 16)")

    # action="store_true" = c'est un INTERRUPTEUR (un drapeau) : présent → True,
    # absent → False. Pas besoin de lui donner une valeur.
    parseur.add_argument("--symboles", action="store_true",
                         help="Inclure des symboles (!@#$...)")

    # --sans-chiffres : drapeau pour EXCLURE les chiffres. argparse range
    # automatiquement "--sans-chiffres" dans l'attribut args.sans_chiffres
    # (le tiret devient un underscore).
    parseur.add_argument("--sans-chiffres", action="store_true",
                         help="Exclure les chiffres")

    parseur.add_argument("--nombre", type=int, default=1,
                         help="Combien de mots de passe générer (défaut : 1)")

    return parseur


# ─────────────────────────────────────────────
# 5. PROGRAMME PRINCIPAL
# ─────────────────────────────────────────────
def main():
    """Lit les options et affiche le ou les mots de passe demandés."""
    args = creer_parseur().parse_args()

    # Petite vérification de bon sens : une longueur trop courte n'a aucun intérêt.
    if args.longueur < 4:
        print("⚠️  Choisis une longueur d'au moins 4 caractères.")
        return

    # On génère autant de mots de passe que demandé.
    for _ in range(args.nombre):
        mdp = generer(
            longueur=args.longueur,
            # avec_chiffres = l'INVERSE de --sans-chiffres :
            #   si --sans-chiffres est False, on VEUT des chiffres → True.
            avec_chiffres=not args.sans_chiffres,
            avec_symboles=args.symboles,
        )
        print(mdp)


if __name__ == "__main__":
    main()
