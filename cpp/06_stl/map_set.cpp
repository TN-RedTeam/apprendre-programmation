/*
 * MODULE 06 - La STL : std::map (annuaire clé->valeur) et std::set (sans doublons)
 * ================================================================================
 * Deux conteneurs de la grande boîte à outils du C++ (la STL) :
 *   - std::map : associe une CLÉ à une VALEUR, comme un annuaire nom -> âge.
 *   - std::set : une collection SANS DOUBLONS, parfaite pour dédupliquer une liste.
 * On les remplit, puis on les parcourt avec la boucle range-for.
 *
 * Compiler puis lancer (depuis la racine du dépôt) :
 *     g++ -std=c++17 -Wall cpp/06_stl/map_set.cpp -o map_set
 *     ./map_set
 */

#include <iostream>   // std::cout
#include <string>     // std::string (les noms, les fruits)
#include <map>        // std::map (le dictionnaire clé -> valeur)
#include <set>        // std::set (l'ensemble sans doublons)

int main() {
    // =========================================================================
    // PARTIE 1 : std::map, un annuaire nom -> âge
    // =========================================================================
    // Entre les < > : d'abord le type de la CLÉ (std::string), puis celui de la
    // VALEUR (int). Ici la clé est un nom, la valeur est un âge.
    std::map<std::string, int> ages;

    // On range des entrées avec les crochets [ ] : la clé entre [ ], la valeur après =.
    ages["Alice"] = 30;
    ages["Bob"]   = 25;
    ages["Chloe"] = 42;

    // On relit une valeur en donnant sa clé entre [ ] (comme en Python : ages["Alice"]).
    std::cout << "Annuaire (acces direct par cle) :" << std::endl;
    std::cout << "  Alice a " << ages["Alice"] << " ans" << std::endl;

    // On parcourt TOUT l'annuaire avec une boucle range-for.
    // Chaque élément est une PAIRE clé/valeur : en C++17 on la « déballe » en [nom, age].
    // (Bonus : un std::map garde ses clés triées, ici par ordre alphabétique.)
    std::cout << "Annuaire complet :" << std::endl;
    for (const auto& [nom, age] : ages) {
        std::cout << "  " << nom << " a " << age << " ans" << std::endl;
    }

    // =========================================================================
    // PARTIE 2 : std::set, dédupliquer une liste de fruits
    // =========================================================================
    // Un std::set ne garde JAMAIS deux fois la même valeur.
    std::set<std::string> fruits;

    // On ajoute des éléments avec .insert(...). On insère exprès des doublons.
    fruits.insert("pomme");
    fruits.insert("poire");
    fruits.insert("pomme");   // déjà présent : IGNORÉ
    fruits.insert("banane");
    fruits.insert("poire");   // déjà présent : IGNORÉ

    // Malgré 5 insertions, il ne reste que les valeurs UNIQUES. .size() les compte.
    std::cout << "\nFruits uniques (" << fruits.size() << " au total) :" << std::endl;

    // On parcourt l'ensemble avec range-for (un std::set est aussi trié tout seul).
    for (const std::string& fruit : fruits) {
        std::cout << "  - " << fruit << std::endl;
    }

    return 0;
}
