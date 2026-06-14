# ============================================================================
#  tableau.s — Déclarer un tableau, le parcourir et calculer sa somme
# ----------------------------------------------------------------------------
#  Ce que fait ce programme :
#    Il déclare un tableau de 5 entiers (.quad) en mémoire : 10, 20, 30, 40, 50.
#    Il le PARCOURT en boucle, en lisant chaque case avec [base + index*8],
#    il ADDITIONNE toutes les valeurs (10+20+30+40+50 = 150),
#    puis quitte en renvoyant la somme (150) comme CODE DE SORTIE.
#
#  Rappels essentiels :
#    - un tableau = des cases CONTIGUËS en mémoire (collées les unes aux autres) ;
#    - chaque .quad fait 8 octets, donc l'élément n°index est à  début + index*8 ;
#    - [rbx + rcx*8]  =  la VALEUR de la case n°rcx du tableau qui débute en rbx.
#
#  🗺️ CHEMINEMENT DU PROGRAMME (le déroulé, étape par étape) :
#    1. DONNÉES : en .data, le tableau 'nombres' = [10, 20, 30, 40, 50].
#    2. INIT    : rbx = adresse du début du tableau (via 'lea') ;
#                 rax = 0 (la somme, qui partira de zéro) ;
#                 rcx = 0 (l'index courant, qui partira de la 1re case).
#    3. BOUCLE  : tant que rcx < 5 :
#                   - lire la case n°rcx :   valeur = [rbx + rcx*8] ;
#                   - l'ajouter à la somme : rax = rax + valeur ;
#                   - passer à la case suivante : rcx = rcx + 1.
#    4. EXIT    : on quitte en renvoyant rax (la somme = 150) comme code de sortie.
#
#  CODE DE SORTIE ATTENDU : 150   (visible avec  echo $?)
#
#  Pour l'assembler, le lier et le lancer :
#    as asm/03_memoire_donnees/tableau.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
# ============================================================================

.intel_syntax noprefix      # Syntaxe Intel (plus lisible pour débuter).

# --- 1. DONNÉES : le tableau, 5 cases de 8 octets, collées en mémoire. -------
.section .data
nombres:    .quad 10, 20, 30, 40, 50   # 5 entiers contigus : index 0,1,2,3,4.

.section .text
.global _start              # _start = point de départ du programme.

_start:
    # --- 2. INIT : on prépare l'adresse, la somme et l'index. ---------------
    lea rbx, [nombres]    # rbx = ADRESSE du début du tableau (pas sa valeur !).
    mov rax, 0            # rax = 0 : la somme commence à zéro.
    mov rcx, 0            # rcx = 0 : l'index commence à la 1re case (index 0).

    # --- 3. BOUCLE : on parcourt les 5 cases. -------------------------------
boucle:
    cmp rcx, 5            # compare l'index à 5 (le nombre de cases).
    jge fin              # si rcx >= 5, on a tout parcouru -> on sort.

    add rax, [rbx + rcx*8] # rax = rax + valeur de la case n°rcx.
    #   [rbx + rcx*8] = "la case à l'adresse rbx, décalée de rcx fois 8 octets".
    #   Donc on lit successivement 10, puis 20, puis 30, puis 40, puis 50.

    inc rcx              # rcx = rcx + 1 : on passe à la case suivante.
    jmp boucle           # on retourne au début de la boucle.

fin:
    # --- 4. EXIT : quitter en renvoyant rax (la somme = 150). ---------------
    mov rdi, rax          # rdi = 150 -> ce sera le code de sortie.
    mov rax, 60           # rax = 60 : service "exit".
    syscall               # On quitte. Le code de sortie vaudra 150.
