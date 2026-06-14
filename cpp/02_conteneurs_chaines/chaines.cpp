/*
 * MODULE 02 - Manipuler du texte avec std::string
 * ================================================
 * Illustre, dans l'ordre, les notions du README : concaténation avec +,
 * .size(), .substr(), accès par index et parcours caractère par caractère.
 *
 * Compiler puis lancer :
 *     g++ -Wall cpp/02_conteneurs_chaines/chaines.cpp -o chaines && ./chaines
 */

#include <iostream>   // pour std::cout (afficher)
#include <string>     // pour le type std::string (du texte)

int main() {

    // 1. CRÉER des chaînes (du texte, entre guillemets doubles).
    std::string prenom = "Ada";
    std::string nom    = "Lovelace";

    // 2. CONCATÉNER (coller) avec + : on assemble les textes bout à bout.
    //    On glisse un " " (une espace) entre les deux pour ne pas tout coller.
    std::string complet = prenom + " " + nom;
    std::cout << "Nom complet : " << complet << std::endl;   // Ada Lovelace

    // 3. LONGUEUR avec .size() : le nombre de caractères de la chaîne.
    //    Le '.' veut dire "demande à cet objet...". L'espace compte aussi !
    std::cout << "Longueur du nom complet : " << complet.size() << std::endl;   // 12

    // 4. EXTRAIRE un morceau avec .substr(debut, combien).
    //    Attention : on compte les positions À PARTIR DE 0.
    std::string mot = "Bonjour";
    std::cout << "mot.substr(0, 3) = " << mot.substr(0, 3) << std::endl;   // "Bon"
    std::cout << "mot.substr(3)    = " << mot.substr(3)    << std::endl;   // "jour"

    // 5. ACCÈS PAR INDEX avec [ ] : chaque caractère a une position (dès 0).
    std::cout << "Premier caractere de '" << mot << "' : " << mot[0] << std::endl;   // 'B'

    // 6. PARCOURIR caractère par caractère avec une "range-based for".
    //    Se lit : "pour chaque caractere c de mot".
    std::cout << "Lettre par lettre : ";
    for (char c : mot) {
        std::cout << c << "-";   // affiche B-o-n-j-o-u-r-
    }
    std::cout << std::endl;

    return 0;   // succès
}
