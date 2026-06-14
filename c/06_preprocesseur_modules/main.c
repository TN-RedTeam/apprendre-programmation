/*
 * MODULE 06 - Préprocesseur (#define, #include) et plusieurs fichiers
 * ==================================================================
 * Ce programme principal n'écrit AUCUN calcul lui-même : il se sert des
 * fonctions et de la constante PI rangées dans calculs.h / calculs.c.
 * C'est tout l'intérêt de séparer son code : main.c "orchestre", la
 * boîte à outils "calcule".
 *
 * ⚠️ Comme le code est dans DEUX fichiers (.c), on les compile ENSEMBLE.
 * Compiler puis lancer (DEPUIS LA RACINE du dépôt) :
 *     gcc -Wall c/06_preprocesseur_modules/main.c c/06_preprocesseur_modules/calculs.c -o prog
 *     ./prog
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE  : <stdio.h> (printf, système) + "calculs.h" (le nôtre).
 *    2. PRÉPROCESSEUR : AVANT la compilation, #include colle le contenu des
 *                       .h, et PI est remplacé par 3.14159 partout.
 *    3. APPELS   : on utilise additionner / maximum / aire_disque, dont le
 *                  CODE vit dans calculs.c (compilé avec ce fichier).
 *    4. AFFICHER : printf montre les résultats.
 *    5. FIN      : return 0 (tout s'est bien passé).
 */

#include <stdio.h>     // chevrons <> = bibliothèque SYSTÈME (printf...)
#include "calculs.h"   // guillemets "" = NOTRE fichier (à côté de main.c)

int main(void) {

    // (3) On appelle des fonctions dont le code est dans calculs.c.
    int somme = additionner(7, 5);
    int plus_grand = maximum(7, 5);

    // PI vient du #define de calculs.h : ici, le préprocesseur a déjà
    // remplacé "PI" par 3.14159 avant même la compilation.
    double aire = aire_disque(2.0);

    // (4) On affiche les résultats.
    printf("--- Module 06 : plusieurs fichiers ensemble ---\n");
    printf("additionner(7, 5) = %d\n", somme);
    printf("maximum(7, 5)     = %d\n", plus_grand);
    printf("PI vaut %.5f\n", PI);
    printf("aire_disque(2.0)  = %.5f\n", aire);

    return 0;   // (5)
}
