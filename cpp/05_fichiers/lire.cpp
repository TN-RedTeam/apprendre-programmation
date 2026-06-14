/*
 * MODULE 05 - Lire un fichier ligne par ligne avec std::ifstream + std::getline
 * =============================================================================
 * On ouvre un fichier en LECTURE, on vérifie qu'il existe bien (.is_open()),
 * puis on lit chaque ligne avec std::getline et on l'affiche. Le fichier se
 * referme tout seul à la fin (RAII).
 *
 * ⚠️ Lance d'abord ecrire.cpp pour créer exemples/notes.txt, et lance ce
 * programme DEPUIS LA RACINE du dépôt.
 *
 * Compiler puis lancer (depuis la racine) :
 *     g++ -Wall -std=c++17 cpp/05_fichiers/lire.cpp -o lire
 *     ./lire
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE   : iostream (affichage), fstream (fichiers), string (les lignes).
 *    2. OUVRIR    : un std::ifstream sur "exemples/notes.txt".
 *    3. VÉRIFIER  : .is_open() — si le fichier n'existe pas, on prévient et on s'arrête.
 *    4. LIRE      : boucle while + std::getline = une ligne à la fois jusqu'à la fin.
 *    5. AFFICHER  : chaque ligne lue est envoyée à std::cout.
 *    6. FIN       : le fichier se referme automatiquement (RAII).
 */

#include <iostream>   // std::cout
#include <fstream>    // std::ifstream (flux pour lire un fichier)
#include <string>     // std::string (pour stocker chaque ligne)

int main() {
    // (2) On ouvre le fichier en LECTURE.
    std::ifstream fichier("exemples/notes.txt");

    // (3) Le fichier existe-t-il et a-t-il pu être ouvert ?
    //     Le « ! » se lit « PAS » : ici « si le fichier n'est PAS ouvert ».
    if (!fichier.is_open()) {
        std::cout << "Impossible d'ouvrir exemples/notes.txt." << std::endl;
        std::cout << "As-tu lance ./ecrire d'abord, depuis la racine du depot ?" << std::endl;
        return 1;   // on s'arrête proprement avec un code d'erreur
    }

    // (4 + 5) On lit le fichier LIGNE PAR LIGNE.
    //     std::getline met la prochaine ligne dans 'ligne' et renvoie le flux.
    //     Quand il n'y a plus rien à lire, la condition devient fausse : on sort.
    std::string ligne;
    while (std::getline(fichier, ligne)) {
        std::cout << ligne << std::endl;   // on affiche la ligne qu'on vient de lire
    }

    // (6) Le fichier se referme automatiquement quand 'fichier' disparaît (RAII).
    return 0;
}
