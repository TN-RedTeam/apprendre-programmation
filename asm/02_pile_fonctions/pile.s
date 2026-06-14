# ============================================================================
#  pile.s — Sauvegarder puis restaurer une valeur avec push / pop
# ----------------------------------------------------------------------------
#  Ce que fait ce programme :
#    1. Il met 42 dans rax (la valeur qu'on veut PROTÉGER).
#    2. Il SAUVEGARDE rax sur la pile avec 'push'.
#    3. Il ÉCRASE volontairement rax avec 99 (comme si on réutilisait rax).
#    4. Il RESTAURE l'ancienne valeur depuis la pile avec 'pop'  ->  rax = 42.
#    5. Il quitte en renvoyant rax (42) comme CODE DE SORTIE.
#
#  But : montrer que push + pop ramènent la valeur INTACTE (pile = LIFO).
#
#  CODE DE SORTIE ATTENDU : 42   (visible avec  echo $?)
#
#  Pour l'assembler, le lier et le lancer :
#    as asm/02_pile_fonctions/pile.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
# ============================================================================

.intel_syntax noprefix      # Syntaxe Intel (plus lisible pour débuter).

.section .text
.global _start              # _start = point de départ du programme.

_start:
    # --- 1. On place la valeur à protéger. ----------------------------------
    mov rax, 42           # rax = 42 : la valeur précieuse qu'on veut garder.

    # --- 2. SAUVEGARDE : on pose rax sur le dessus de la pile. --------------
    push rax              # 'push' POSE le contenu de rax sur la pile (sommet).

    # --- 3. On écrase rax (comme si on devait réutiliser ce registre). ------
    mov rax, 99           # rax = 99 : la valeur 42 semble perdue... mais non !

    # --- 4. RESTAURE : on reprend le sommet de la pile dans rax. ------------
    pop rax               # 'pop' RETIRE le sommet (42) et le remet dans rax.
                          # rax revaut 42 : la sauvegarde a fonctionné.

    # --- 5. EXIT : quitter en renvoyant rax (42) comme code de sortie. ------
    mov rdi, rax          # rdi = 42 -> ce sera le code de sortie.
    mov rax, 60           # rax = 60 : service "exit".
    syscall               # On quitte. Le code de sortie vaudra 42.
