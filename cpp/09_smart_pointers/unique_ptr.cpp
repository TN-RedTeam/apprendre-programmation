// =============================================================================
//  Module 09 — unique_ptr.cpp
//  std::unique_ptr : UN SEUL propriétaire, libération AUTOMATIQUE (RAII).
//  Compiler :  g++ -std=c++17 -Wall cpp/09_smart_pointers/unique_ptr.cpp -o unique_ptr
//  Lancer   :  ./unique_ptr
// =============================================================================

#include <iostream>   // pour std::cout (afficher)
#include <memory>     // INDISPENSABLE pour les smart pointers (std::unique_ptr, make_unique)
#include <string>     // pour std::string (le nom du chien)

// -----------------------------------------------------------------------------
// Une petite classe Chien. Le point important ici, c'est son DESTRUCTEUR :
// il affiche un message. Comme ça, on VOIT de nos yeux à quel moment exact
// l'objet est détruit (= sa mémoire libérée).
// -----------------------------------------------------------------------------
class Chien {
private:
    std::string nom;   // chaque chien a un nom

public:
    // Constructeur : appelé quand on CRÉE le chien. Il affiche un message.
    Chien(std::string n) {
        nom = n;
        std::cout << "[CONSTRUCTEUR] Le chien " << nom << " vient de naitre." << std::endl;
    }

    // Destructeur : appelé AUTOMATIQUEMENT quand le chien est détruit.
    // C'est lui qui prouve la libération automatique : on n'écrit aucun delete !
    ~Chien() {
        std::cout << "[DESTRUCTEUR]  Le chien " << nom << " est libere (memoire rendue)." << std::endl;
    }

    void aboyer() {
        std::cout << nom << " fait : Wouf !" << std::endl;
    }
};

int main() {
    std::cout << "--- Debut du programme ---" << std::endl;

    {   // On ouvre un bloc { } pour bien voir le RAII : tout ce qui est créé
        //  dedans sera libéré quand on arrive à l'accolade fermante } du bloc.

        // On crée un Chien possédé par un std::unique_ptr, via std::make_unique.
        // 'rex' est le PROPRIÉTAIRE UNIQUE de ce chien.
        std::unique_ptr<Chien> rex = std::make_unique<Chien>("Rex");

        // On utilise l'objet exactement comme un pointeur normal : avec la flèche ->
        rex->aboyer();

        std::cout << "(on arrive bientot a la fin du bloc...)" << std::endl;

    }   // <-- ICI : 'rex' sort de portée. Le DESTRUCTEUR du Chien est appelé
        //          TOUT SEUL. Aucun delete écrit nulle part : c'est le RAII.

    std::cout << "--- Fin du programme (le chien etait deja libere) ---" << std::endl;
    return 0;
}
