# =====================================================================
# MODULE 06 - Une FONCTION en assembleur, appelée depuis le C
#             somme(long a, long b)  ->  a + b
#             (x86-64, Linux, syntaxe Intel)
# =====================================================================
# Ici, PAS de _start ! Ce n'est plus l'assembleur qui démarre le
# programme : c'est le C (via sa fonction main) qui DÉMARRE, puis qui
# APPELLE notre fonction `somme`. Notre travail est seulement d'écrire
# le corps de cette fonction.
#
# La CONVENTION D'APPEL System V AMD64 (la "règle du jeu" sous Linux)
# dit OÙ trouver les arguments et OÙ déposer le résultat :
#   - 1er argument entier  -> dans le registre rdi   (ici : a)
#   - 2e  argument entier  -> dans le registre rsi   (ici : b)
#   - valeur de RETOUR     -> dans le registre rax
#
# Pour que le C puisse "voir" et appeler cette fonction, on la rend
# PUBLIQUE avec la directive  .global somme  (sans ça, le nom resterait
# privé au fichier et l'éditeur de liens ne le trouverait pas).
#
# Assembler + lier + lancer (le C fournit main, gcc fait tout) :
#     gcc main.c somme.s -o prog
#     ./prog          # affiche : 7 + 5 = 12
#
# 🗺️ CHEMINEMENT DE LA FONCTION (rdi/rsi -> rax) :
#   1. À l'entrée, le C a déjà mis  a dans rdi  et  b dans rsi.
#   2. On copie a (rdi) dans rax.
#   3. On AJOUTE b (rsi) à rax  ->  rax contient maintenant a + b.
#   4. ret : on rend la main au C. Le C lira le résultat dans rax.

.intel_syntax noprefix

.text
.global somme            # rend le nom "somme" VISIBLE par le C (et par gcc)

somme:                   # début de la fonction (l'étiquette = son nom)
    mov rax, rdi         # (2) rax = a   (a est arrivé dans rdi)
    add rax, rsi         # (3) rax = rax + b = a + b   (b est arrivé dans rsi)
    ret                  # (4) retour au C ; le résultat est dans rax

# Petite formalité technique (pas besoin de comprendre maintenant) : on
# indique à l'éditeur de liens qu'on n'a pas besoin d'une pile exécutable.
# Ça évite juste un avertissement de gcc/ld. À garder tel quel.
.section .note.GNU-stack, "", @progbits
