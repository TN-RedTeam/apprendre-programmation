/*
 * MODULE 06 - Les ALGORITHMES de la STL : std::sort (trier) et std::find (chercher)
 * =================================================================================
 * La boîte à outils <algorithm> contient des actions toutes faites à appliquer sur
 * un conteneur. Ici, sur un std::vector d'entiers :
 *   - std::sort  : range les éléments du plus petit au plus grand.
 *   - std::find  : cherche une valeur et dit si elle est présente.
 * Les deux travaillent sur une PLAGE décrite par begin() (début) et end() (après la fin).
 *
 * Compiler puis lancer (depuis la racine du dépôt) :
 *     g++ -std=c++17 -Wall cpp/06_stl/algorithmes.cpp -o algorithmes
 *     ./algorithmes
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE   : iostream (affichage), vector (la liste), algorithm (sort + find).
 *    2. CRÉER     : un std::vector<int> avec des nombres en désordre.
 *    3. AFFICHER  : on montre la liste de départ (désordonnée).
 *    4. TRIER     : std::sort(v.begin(), v.end()) range les nombres dans l'ordre.
 *    5. AFFICHER  : on remontre la liste, maintenant triée.
 *    6. CHERCHER  : std::find cherche une valeur ; on teste != end() pour savoir si trouvé.
 *    7. FIN       : retour 0.
 */

#include <iostream>   // std::cout
#include <vector>     // std::vector (la liste qui grandit)
#include <algorithm>  // std::sort et std::find

int main() {
    // (2) Une liste de nombres EN DÉSORDRE.
    std::vector<int> nombres = {5, 2, 8, 1, 9, 3};

    // (3) On affiche la liste de départ.
    std::cout << "Liste de depart : ";
    for (int n : nombres) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // (4) On TRIE la liste. std::sort prend la PLAGE à trier : du début (begin())
    //     jusqu'à juste après la fin (end()). Il range du plus petit au plus grand.
    std::sort(nombres.begin(), nombres.end());

    // (5) On réaffiche : la liste est maintenant TRIÉE.
    std::cout << "Liste triee   : ";
    for (int n : nombres) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // (6) On CHERCHE une valeur avec std::find. Il renvoie un itérateur (un « doigt »)
    //     sur l'élément trouvé, ou end() s'il n'a RIEN trouvé.
    int cherche = 8;
    auto it = std::find(nombres.begin(), nombres.end(), cherche);
    if (it != nombres.end()) {
        // it != end() => la valeur est bien dans la liste.
        std::cout << "La valeur " << cherche << " est dans la liste." << std::endl;
    } else {
        std::cout << "La valeur " << cherche << " est absente." << std::endl;
    }

    // On refait une recherche, cette fois avec une valeur ABSENTE, pour voir l'autre cas.
    int absent = 42;
    auto it2 = std::find(nombres.begin(), nombres.end(), absent);
    if (it2 != nombres.end()) {
        std::cout << "La valeur " << absent << " est dans la liste." << std::endl;
    } else {
        std::cout << "La valeur " << absent << " est absente." << std::endl;
    }

    return 0;   // (7)
}
