// =============================================================================
//  Module 07 — DÉBUGGER : un petit programme à explorer (correct et instructif)
// =============================================================================
//
//  🗺️ CHEMINEMENT DU PROGRAMME
//  ---------------------------------------------------------------------------
//  1. On crée un std::vector<int> de notes (une liste de nombres).
//  2. moyenne(...)   : on additionne toutes les notes, puis on divise par le
//                      nombre de notes -> on renvoie la moyenne.
//  3. note_securisee(...) : on lit une note avec .at(index). Si l'index est HORS
//                      LIMITES, .at() lève une exception std::out_of_range qu'on
//                      ATTRAPE avec try/catch (au lieu de planter silencieusement).
//  4. Dans main(), on affiche les notes, la moyenne, une lecture VALIDE, puis on
//     provoque exprès une lecture HORS LIMITES pour montrer le try/catch.
//
//  Tout est CORRECT : le programme compile sans erreur ni warning et se termine
//  proprement. Le but n'est pas de planter, mais d'avoir un programme propre
//  à PARCOURIR PAS À PAS sous gdb (voir le README).
//
//  ▶️ Compiler AVEC les symboles de débogage (-g) et les avertissements (-Wall) :
//        g++ -g -std=c++17 -Wall cpp/07_debugger/demo_gdb.cpp -o demo_gdb
//        ./demo_gdb
// =============================================================================

#include <iostream>   // std::cout, std::endl  (afficher)
#include <vector>     // std::vector           (la liste qui grandit)
#include <stdexcept>  // std::out_of_range     (le type d'exception de .at())

// -----------------------------------------------------------------------------
// moyenne : additionne toutes les notes puis divise par leur nombre.
// On reçoit le vector par référence constante (const&) pour éviter de le copier.
// -----------------------------------------------------------------------------
double moyenne(const std::vector<int>& notes) {
    int total = 0;                         // on PART de 0 (variable bien initialisée !)
    for (int note : notes) {               // pour chaque note dans la liste
        total += note;                     // on l'ajoute au total
    }
    // total est un int, notes.size() aussi : on convertit en double pour avoir
    // une vraie division décimale (sinon 17 / 3 donnerait 5, pas 5.66...).
    return static_cast<double>(total) / notes.size();
}

// -----------------------------------------------------------------------------
// note_securisee : lit notes[index] avec .at(), qui VÉRIFIE les limites.
// Si l'index est trop grand, .at() lève std::out_of_range : on l'attrape ici.
// -----------------------------------------------------------------------------
int note_securisee(const std::vector<int>& notes, std::size_t index) {
    try {
        // .at(index) plante PROPREMENT (exception) si index est hors limites,
        // contrairement à notes[index] qui lit n'importe où en mémoire (danger).
        return notes.at(index);
    } catch (const std::out_of_range& e) {
        // On attrape l'erreur prévisible et on réagit calmement.
        std::cout << "  ⚠️  Index " << index << " hors limites : " << e.what() << std::endl;
        return -1;   // valeur « sentinelle » pour dire « pas de note valide »
    }
}

int main() {
    // 1) Nos données : 5 notes sur 20.
    std::vector<int> notes = {12, 15, 8, 17, 20};

    // 2) Affichage des notes (boucle range-for, vue au module 02).
    std::cout << "Notes : ";
    for (int note : notes) {
        std::cout << note << " ";
    }
    std::cout << std::endl;

    // 3) Moyenne.
    std::cout << "Moyenne : " << moyenne(notes) << std::endl;

    // 4) Une lecture VALIDE (index 2 existe : c'est la 3e note).
    std::cout << "Note a l'index 2 : " << note_securisee(notes, 2) << std::endl;

    // 5) Une lecture HORS LIMITES exprès (index 10 n'existe pas) :
    //    .at() lève std::out_of_range, que note_securisee ATTRAPE proprement.
    std::cout << "Note a l'index 10 : " << note_securisee(notes, 10) << std::endl;

    std::cout << "Programme termine proprement. ✅" << std::endl;
    return 0;
}
