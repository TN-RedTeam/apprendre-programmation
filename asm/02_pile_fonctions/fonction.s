# ============================================================================
#  fonction.s — Définir et appeler une fonction avec call / ret
# ----------------------------------------------------------------------------
#  Ce que fait ce programme :
#    Il appelle une petite fonction 'additionner' qui fait rdi + rsi,
#    avec rdi = 7 et rsi = 5. Le résultat (12) revient dans rax.
#    Puis il quitte en renvoyant 12 comme CODE DE SORTIE.
#
#  Convention (la même que Linux) :
#    - arguments dans rdi (1er) et rsi (2e),
#    - résultat dans rax.
#
#  🗺️ CHEMINEMENT DU PROGRAMME (le déroulé, étape par étape) :
#    1. INIT     : on met les arguments  rdi = 7  et  rsi = 5.
#    2. CALL     : 'call additionner' saute dans la fonction
#                  ET mémorise sur la pile OÙ revenir (la ligne d'après).
#    3. FONCTION : dans 'additionner', on calcule rax = rdi + rsi  (= 12),
#                  puis 'ret' REVIENT juste après le 'call'.
#    4. EXIT     : on quitte en renvoyant rax (12) comme code de sortie.
#
#  CODE DE SORTIE ATTENDU : 12   (visible avec  echo $?)
#
#  Pour l'assembler, le lier et le lancer :
#    as asm/02_pile_fonctions/fonction.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
# ============================================================================

.intel_syntax noprefix      # Syntaxe Intel (plus lisible pour débuter).

.section .text
.global _start              # _start = point de départ du programme.

_start:
    # --- 1. INIT : on prépare les arguments de la fonction. -----------------
    mov rdi, 7            # rdi = 7 : 1er argument.
    mov rsi, 5            # rsi = 5 : 2e argument.

    # --- 2. CALL : on appelle la fonction. ----------------------------------
    call additionner      # saute dans 'additionner' ET note où revenir (pile).
    # <-- on REVIENT ICI après le 'ret'. rax contient maintenant 12.

    # --- 4. EXIT : quitter en renvoyant rax (12) comme code de sortie. ------
    mov rdi, rax          # rdi = 12 -> ce sera le code de sortie.
    mov rax, 60           # rax = 60 : service "exit".
    syscall               # On quitte. Le code de sortie vaudra 12.

# ----------------------------------------------------------------------------
#  3. LA FONCTION 'additionner'
#     Entrée : rdi (1er nombre), rsi (2e nombre).
#     Sortie : rax = rdi + rsi.
# ----------------------------------------------------------------------------
additionner:
    mov rax, rdi          # rax = rdi   (on copie le 1er argument dans rax).
    add rax, rsi          # rax = rax + rsi  ->  rax = 7 + 5 = 12.
    ret                   # REVIENT juste après le 'call' (reprend l'adresse sur la pile).
