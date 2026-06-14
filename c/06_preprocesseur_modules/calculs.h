/*
 * calculs.h — la "CARTE DE VISITE" de notre module de calculs.
 * ===========================================================
 * Un fichier .h (header = "en-tête") ne contient PAS le code des fonctions,
 * seulement leurs DÉCLARATIONS (les "prototypes") et nos #define.
 * C'est ce que les autres fichiers ont besoin de connaître pour s'en servir.
 * (Le vrai code, lui, est rangé dans calculs.c.)
 */

/* --- GARDE D'INCLUSION (à mettre dans tout fichier .h) -------------------
 * Si ce .h est inclus deux fois (ça arrive vite dans un vrai projet), on
 * risque de déclarer deux fois les mêmes choses -> erreur de compilation.
 * La garde évite ça :
 *   - #ifndef CALCULS_H  : "SI ce nom n'a PAS encore été défini..."
 *   - #define CALCULS_H  : "...alors on le définit (1re fois seulement)..."
 *   - ...le contenu...
 *   - #endif             : fin du bloc.
 * À la 2e inclusion, CALCULS_H existe déjà : tout le bloc est SAUTÉ.
 * CALCULS_H est juste un nom de marqueur (par convention : le nom du fichier
 * en MAJUSCULES, avec _ à la place du point).
 */
#ifndef CALCULS_H
#define CALCULS_H

/* --- Une CONSTANTE avec #define -----------------------------------------
 * #define dit au préprocesseur : "AVANT de compiler, remplace partout le
 * mot PI par 3.14159". PI n'est pas une variable, c'est un simple
 * remplacement de texte. Par convention, les #define sont en MAJUSCULES.
 */
#define PI 3.14159

/* --- Les PROTOTYPES de nos fonctions ------------------------------------
 * Un prototype = la "carte de visite" d'une fonction : son nom, ce qu'elle
 * reçoit, ce qu'elle renvoie. Pas de code ici, juste un point-virgule.
 * Grâce à ça, main.c sait comment appeler ces fonctions, même si leur code
 * est dans un AUTRE fichier (calculs.c).
 */

/* Renvoie la somme de deux entiers. */
int additionner(int a, int b);

/* Renvoie le plus grand des deux entiers. */
int maximum(int a, int b);

/* Renvoie l'aire d'un disque de rayon donné (utilise PI). */
double aire_disque(double rayon);

#endif /* CALCULS_H — fin de la garde d'inclusion */
