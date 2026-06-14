/*
 * calculs.c — le VRAI CODE des fonctions annoncées dans calculs.h.
 * ===============================================================
 * Le .h est la carte de visite (les promesses) ; le .c les TIENT.
 * On inclut notre propre .h pour que le compilateur vérifie que le code
 * correspond bien aux prototypes (mêmes noms, mêmes types).
 *
 * Note : ce fichier ne contient PAS de main(). C'est normal : ce n'est
 * pas un programme à lancer seul, c'est une "boîte à outils" qu'on
 * compile AVEC main.c (voir la commande dans main.c et le README).
 */

#include "calculs.h"   // guillemets "" = NOTRE fichier (pas une lib système)

/* Additionne deux entiers. */
int additionner(int a, int b) {
    return a + b;
}

/* Renvoie le plus grand des deux. */
int maximum(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

/* Aire d'un disque = PI x rayon x rayon. PI vient du #define du .h. */
double aire_disque(double rayon) {
    return PI * rayon * rayon;
}
