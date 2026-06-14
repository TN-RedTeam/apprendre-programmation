/*
 * pointeurs_fonctions.c — une fonction a une ADRESSE, donc on peut la ranger dans
 * un POINTEUR, l'appeler plus tard, en faire un TABLEAU, ou la passer en ARGUMENT
 * (un "callback").
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME
 *   1. On définit de petites fonctions : additionner(), soustraire(), multiplier().
 *   2. ÉTAPE A : on crée UN pointeur de fonction 'op'. On le fait pointer vers
 *      additionner() et on appelle ; puis vers soustraire() et on rappelle.
 *      => même ligne d'appel, comportement différent.
 *   3. ÉTAPE B : on range ces fonctions dans un TABLEAU de pointeurs de fonctions
 *      et on le parcourt EN BOUCLE pour toutes les appeler.
 *   4. ÉTAPE C : on appelle appliquer(), une fonction qui reçoit un CALLBACK
 *      (une fonction en argument) et l'exécute. On lui confie tantôt l'une,
 *      tantôt l'autre.
 *   5. ÉTAPE D (cas réel) : on trie un tableau avec qsort() en lui FOURNISSANT
 *      notre fonction de comparaison — le callback "de la vraie vie".
 *
 *   Compiler puis lancer :
 *       gcc -Wall c/09_pointeurs_fonctions/pointeurs_fonctions.c -o pointeurs_fonctions && ./pointeurs_fonctions
 */

#include <stdio.h>    /* pour printf */
#include <stdlib.h>   /* pour qsort  */

/* -------------------------------------------------------------------------
 * Nos petites fonctions. Chacune prend deux int et renvoie un int.
 * Elles ont donc TOUTES la même "forme" : (int, int) -> int.
 * C'est ce qui nous permettra de les ranger dans le même pointeur / tableau.
 * ----------------------------------------------------------------------- */

int additionner(int a, int b) { return a + b; }   /* a + b */
int soustraire(int a, int b)  { return a - b; }   /* a - b */
int multiplier(int a, int b)  { return a * b; }   /* a * b */

/*
 * appliquer() : reçoit deux nombres ET une FONCTION à exécuter dessus.
 * Ce 3ᵉ paramètre 'callback' est un POINTEUR DE FONCTION :
 *   int (*callback)(int, int)  se lit "callback pointe vers une fonction (int,int) -> int".
 * appliquer() ne sait pas à l'avance ce qu'elle va faire : c'est l'APPELANT qui décide,
 * en lui passant telle ou telle fonction.
 */
int appliquer(int a, int b, int (*callback)(int, int))
{
    return callback(a, b);   /* on "rappelle" la fonction qu'on nous a confiée */
}

/*
 * comparer_ints() : le callback IMPOSÉ par qsort().
 * qsort sait trier, mais c'est À NOUS de dire comment COMPARER deux éléments.
 * Signature imposée : reçoit deux pointeurs génériques (const void *).
 *   - on les reconvertit en (const int *) puis on lit la valeur avec '*' ;
 *   - on renvoie <0, 0 ou >0 selon l'ordre voulu.
 */
int comparer_ints(const void *a, const void *b)
{
    int x = *(const int *)a;   /* "va voir" l'entier pointé par a */
    int y = *(const int *)b;   /* "va voir" l'entier pointé par b */
    return x - y;              /* <0 : x avant y | 0 : égaux | >0 : x après y */
}

int main(void)
{
    /* =====================================================================
     * ÉTAPE A — un pointeur de fonction qu'on fait pointer vers l'une puis l'autre
     * ===================================================================== */
    printf("--- ETAPE A : un pointeur de fonction ---\n");

    /* On déclare 'op' : un pointeur vers une fonction (int,int) -> int.
     * Les parenthèses autour de *op sont OBLIGATOIRES. */
    int (*op)(int, int);

    op = additionner;          /* on note le "numéro" de additionner (PAS de parenthèses) */
    printf("op = additionner ; op(2, 3) = %d\n", op(2, 3));   /* 5 */

    op = soustraire;           /* on change le "numéro" noté... */
    printf("op = soustraire  ; op(2, 3) = %d\n", op(2, 3));   /* -1 : MEME ligne, autre resultat ! */

    /* =====================================================================
     * ÉTAPE B — un TABLEAU de pointeurs de fonctions, parcouru en boucle
     * ===================================================================== */
    printf("\n--- ETAPE B : un tableau de pointeurs de fonctions ---\n");

    /* Un "répertoire" d'opérations : chaque case est une fonction (int,int) -> int. */
    int (*operations[])(int, int) = { additionner, soustraire, multiplier };
    const char *noms[] = { "additionner", "soustraire ", "multiplier " };

    /* Nombre d'entrées du tableau, calculé automatiquement. */
    int nb = (int)(sizeof(operations) / sizeof(operations[0]));

    for (int i = 0; i < nb; i++) {
        /* operations[i](10, 3) : on appelle l'opération rangée à la case i. */
        printf("operations[%d] (%s) -> %d\n", i, noms[i], operations[i](10, 3));
    }

    /* =====================================================================
     * ÉTAPE C — passer une fonction EN ARGUMENT (callback)
     * ===================================================================== */
    printf("\n--- ETAPE C : un callback passe en argument ---\n");

    /* On CONFIE une fonction à appliquer() ; elle la rappellera pour nous. */
    printf("appliquer(6, 2, additionner) = %d\n", appliquer(6, 2, additionner));  /* 8 */
    printf("appliquer(6, 2, soustraire)  = %d\n", appliquer(6, 2, soustraire));   /* 4 */
    printf("appliquer(6, 2, multiplier)  = %d\n", appliquer(6, 2, multiplier));   /* 12 */

    /* =====================================================================
     * ÉTAPE D — le callback "de la vraie vie" : qsort()
     * ===================================================================== */
    printf("\n--- ETAPE D : qsort avec notre fonction de comparaison ---\n");

    int t[] = { 5, 2, 9, 1, 7, 3 };
    int n = (int)(sizeof(t) / sizeof(t[0]));

    printf("avant tri  : ");
    for (int i = 0; i < n; i++) printf("%d ", t[i]);
    printf("\n");

    /* On donne à qsort : le tableau, son nombre d'elements, la taille d'un element,
     * et NOTRE callback de comparaison. qsort fait le reste. */
    qsort(t, n, sizeof(int), comparer_ints);

    printf("apres tri  : ");
    for (int i = 0; i < n; i++) printf("%d ", t[i]);
    printf("\n");

    return 0;   /* tout s'est bien passe */
}
