# ============================================================================
#  demo_debug.s — Un petit programme FAIT POUR être exploré pas à pas sous gdb
# ----------------------------------------------------------------------------
#  Ce programme ne fait rien d'impressionnant : il enchaîne quelques calculs
#  simples dans des registres, puis quitte avec un CODE DE SORTIE connu.
#  Son but n'est pas le résultat, mais de te donner un terrain de jeu idéal
#  pour APPRENDRE À OBSERVER les registres au débogueur (gdb).
#
#  🗺️ CHEMINEMENT DU PROGRAMME (suis-le avec gdb, une instruction à la fois) :
#     1. rax = 10              (on met 10 dans rax)
#     2. rax = rax + 5  -> 15  (on ajoute 5)
#     3. rbx = 3               (on met 3 dans rbx, un autre registre)
#     4. rax = rax - rbx -> 12 (on soustrait rbx de rax)
#     5. on copie rax dans rdi (le futur code de sortie : 12)
#     6. on quitte (exit) en renvoyant 12
#
#  Pour l'assembler AVEC LES INFOS DE DEBUG (-g), le lier, le lancer :
#    as -g asm/07_debugger/demo_debug.s -o /tmp/d.o && ld /tmp/d.o -o /tmp/d && /tmp/d ; echo "exit=$?"
#
#  CODE DE SORTIE ATTENDU : 12
# ============================================================================

.intel_syntax noprefix      # Syntaxe Intel (plus lisible pour débuter).

.section .text
.global _start              # _start = point de départ du programme.

_start:
    # --- Étape 1 : on remplit un premier registre. --------------------------
    mov rax, 10           # rax = 10   (on MET la valeur 10 dans rax).

    # --- Étape 2 : on additionne. -------------------------------------------
    add rax, 5            # rax = rax + 5  ->  rax vaut maintenant 15.

    # --- Étape 3 : on utilise un deuxième registre. -------------------------
    mov rbx, 3            # rbx = 3    (un autre registre, pour varier).

    # --- Étape 4 : on soustrait un registre à un autre. ---------------------
    sub rax, rbx          # rax = rax - rbx  ->  15 - 3 = 12.

    # --- Étape 5 : on prépare la sortie. ------------------------------------
    mov rdi, rax          # rdi = rax : le code de sortie sera notre résultat (12).
    mov rax, 60           # rax = 60 : service "exit" (quitter).

    # --- Étape 6 : on quitte. -----------------------------------------------
    syscall               # On quitte. Le code de sortie vaudra 12.
