/* =====================================================================
 * MODULE 06 - Le programme C qui appelle notre fonction ASSEMBLEUR
 * =====================================================================
 * C'est le C qui fournit le POINT D'ENTRÉE du programme : la fonction
 * main. Depuis main, on appelle `somme`, qui est écrite en assembleur
 * dans le fichier somme.s. Le C n'a pas besoin de savoir COMMENT somme
 * est faite : il lui suffit de connaître son PROTOTYPE (son nom, ses
 * arguments et ce qu'elle renvoie).
 *
 * Compiler (= assembler) + lier + lancer, en une seule commande gcc :
 *     gcc main.c somme.s -o prog
 *     ./prog          // affiche : 7 + 5 = 12
 *
 * gcc s'occupe de TOUT : il compile main.c, assemble somme.s, puis
 * relie les deux ensemble pour produire l'exécutable "prog".
 */

#include <stdio.h>   /* pour printf */

/* PROTOTYPE : on PROMET au C qu'il existe quelque part une fonction
 * nommée "somme" qui prend deux long et renvoie un long. Le corps de
 * cette fonction est ailleurs (dans somme.s). */
long somme(long a, long b);

int main(void)
{
    long a = 7;
    long b = 5;

    /* Appel de la fonction assembleur. Sous le capot :
     *   - le C met a dans rdi et b dans rsi (convention System V AMD64),
     *   - notre code asm calcule a + b et le laisse dans rax,
     *   - le C récupère rax ici, dans la variable resultat. */
    long resultat = somme(a, b);

    printf("%ld + %ld = %ld\n", a, b, resultat);   /* affiche : 7 + 5 = 12 */

    return 0;
}
