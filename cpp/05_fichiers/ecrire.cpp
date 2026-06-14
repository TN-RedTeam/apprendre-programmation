/*
 * MODULE 05 - Écrire dans un fichier avec std::ofstream
 * =====================================================
 * On ouvre (ou on crée) un fichier, puis on y écrit quelques lignes avec <<,
 * exactement comme on écrirait avec std::cout. Le fichier se referme tout seul
 * à la fin (RAII).
 *
 * Anti-pollution : le fichier est rangé dans le sous-dossier "exemples/",
 * que l'on crée au besoin avec std::filesystem. À LANCER DEPUIS LA RACINE du dépôt.
 *
 * Compiler puis lancer (depuis la racine, -std=c++17 requis pour <filesystem>) :
 *     g++ -Wall -std=c++17 cpp/05_fichiers/ecrire.cpp -o ecrire
 *     ./ecrire
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE   : iostream (affichage), fstream (fichiers), filesystem (dossier).
 *    2. DOSSIER   : créer "exemples/" s'il n'existe pas encore.
 *    3. OUVRIR    : un std::ofstream sur "exemples/notes.txt".
 *    4. VÉRIFIER  : .is_open() — sinon on prévient et on s'arrête.
 *    5. ÉCRIRE    : quelques lignes avec << (comme std::cout).
 *    6. FIN       : le fichier se referme automatiquement (RAII).
 */

#include <iostream>     // std::cout
#include <fstream>      // std::ofstream (flux pour écrire dans un fichier)
#include <filesystem>   // std::filesystem::create_directories

int main() {
    // (2) On crée le sous-dossier "exemples/" s'il n'existe pas déjà.
    //     S'il existe, cette ligne ne fait rien de mal.
    std::filesystem::create_directories("exemples");

    // (3) On ouvre (ou on crée) le fichier en ÉCRITURE.
    //     S'il existait déjà, son ancien contenu est remplacé.
    std::ofstream fichier("exemples/notes.txt");

    // (4) Réflexe de prudence : a-t-on bien réussi à ouvrir le fichier ?
    if (!fichier.is_open()) {
        std::cout << "Erreur : impossible de creer le fichier." << std::endl;
        return 1;   // on s'arrête proprement avec un code d'erreur
    }

    // (5) On écrit dans le fichier avec <<, comme avec std::cout.
    //     Chaque std::endl passe à la ligne suivante dans le fichier.
    fichier << "Bonjour, ceci est ma premiere note." << std::endl;
    fichier << "Le C++ sait ecrire dans des fichiers." << std::endl;
    fichier << "Et chaque ligne est ecrite avec <<." << std::endl;

    // On confirme à l'écran que c'est fait.
    std::cout << "3 lignes ecrites dans exemples/notes.txt" << std::endl;

    // (6) Pas besoin de fermer le fichier nous-mêmes : quand 'fichier' disparaît
    //     ici (fin de main), il est fermé automatiquement (RAII).
    return 0;
}
