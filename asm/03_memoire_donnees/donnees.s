# ============================================================================
#  donnees.s — Déclarer des données en mémoire, les lire et calculer
# ----------------------------------------------------------------------------
#  Ce que fait ce programme :
#    Il déclare deux nombres dans la section .data (15 et 27),
#    les LIT depuis la mémoire vers des registres,
#    les additionne (15 + 27 = 42),
#    puis quitte en renvoyant 42 comme CODE DE SORTIE.
#
#  Rappel essentiel :
#    - une étiquette (ex. 'premier') est une ADRESSE en mémoire ;
#    - [etiquette] (avec crochets) = la VALEUR rangée à cette adresse.
#
#  🗺️ CHEMINEMENT DU PROGRAMME (le déroulé, étape par étape) :
#    1. DONNÉES : en .data, on a réservé deux cases : premier=15, second=27.
#    2. LIRE    : on charge ces valeurs en registres (rax=15, rbx=27).
#    3. CALCUL  : on additionne  ->  rax = 15 + 27 = 42.
#    4. EXIT    : on quitte en renvoyant rax (42) comme code de sortie.
#
#  CODE DE SORTIE ATTENDU : 42   (visible avec  echo $?)
#
#  Pour l'assembler, le lier et le lancer :
#    as asm/03_memoire_donnees/donnees.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
# ============================================================================

.intel_syntax noprefix      # Syntaxe Intel (plus lisible pour débuter).

# --- 1. DONNÉES : la section .data contient des valeurs INITIALISÉES. --------
.section .data
premier:    .quad 15        # une case de 8 octets contenant 15.
second:     .quad 27        # une case de 8 octets contenant 27.

# --- Le code, lui, vit dans la section .text. --------------------------------
.section .text
.global _start              # _start = point de départ du programme.

_start:
    # --- 2. LIRE : on copie les VALEURS de la mémoire vers des registres. ----
    mov rax, [premier]    # rax = la valeur rangée dans 'premier'  (= 15).
    mov rbx, [second]     # rbx = la valeur rangée dans 'second'   (= 27).
    #   ⚠️ Les crochets sont importants : sans eux on aurait copié l'ADRESSE,
    #      pas la valeur. Avec [ ], on lit bien le CONTENU de la case.

    # --- 3. CALCUL : on additionne les deux valeurs. ------------------------
    add rax, rbx          # rax = rax + rbx  ->  rax = 15 + 27 = 42.

    # --- 4. EXIT : quitter en renvoyant rax (42) comme code de sortie. ------
    mov rdi, rax          # rdi = 42 -> ce sera le code de sortie.
    mov rax, 60           # rax = 60 : service "exit".
    syscall               # On quitte. Le code de sortie vaudra 42.
