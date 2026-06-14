// =============================================================================
//  Module 09 — shared_ptr.cpp
//  std::shared_ptr : propriété PARTAGÉE avec un COMPTEUR de références.
//  L'objet n'est détruit que quand le DERNIER partage disparaît.
//  Compiler :  g++ -std=c++17 -Wall cpp/09_smart_pointers/shared_ptr.cpp -o shared_ptr
//  Lancer   :  ./shared_ptr
// =============================================================================
//
//  🗺️ CHEMINEMENT DU PROGRAMME
//  ---------------------------------------------------------------------------
//   1. On crée un Chien partagé avec 'proprietaire1' .... compteur = 1
//   2. 'proprietaire2 = proprietaire1' : on PARTAGE ...... compteur = 2
//   3. On affiche use_count() (= nombre de partages actuels)
//   4. On entre dans un bloc { } et on crée un 3e partage . compteur = 3
//   5. On sort du bloc : le 3e partage disparaît .......... compteur = 2
//   6. Fin du main : proprietaire1 et proprietaire2 partent .. compteur = 0
//      -> SEULEMENT MAINTENANT le Chien est détruit (le DERNIER est parti)
//  ---------------------------------------------------------------------------

#include <iostream>   // pour std::cout
#include <memory>     // INDISPENSABLE pour std::shared_ptr et std::make_shared
#include <string>     // pour std::string

// Même Chien qu'avant : son destructeur affiche un message, pour qu'on VOIE
// l'instant précis où l'objet est enfin libéré.
class Chien {
private:
    std::string nom;

public:
    Chien(std::string n) {
        nom = n;
        std::cout << "[CONSTRUCTEUR] Le chien " << nom << " vient de naitre." << std::endl;
    }

    ~Chien() {
        std::cout << "[DESTRUCTEUR]  Le chien " << nom << " est libere (memoire rendue)." << std::endl;
    }

    void aboyer() {
        std::cout << nom << " fait : Wouf !" << std::endl;
    }
};

int main() {
    std::cout << "--- Debut du programme ---" << std::endl;

    // ÉTAPE 1 : on crée le Chien avec un std::shared_ptr, via std::make_shared.
    // Pour l'instant, un seul propriétaire -> le compteur vaut 1.
    std::shared_ptr<Chien> proprietaire1 = std::make_shared<Chien>("Medor");
    std::cout << "Apres proprietaire1   -> use_count = " << proprietaire1.use_count() << std::endl;

    // ÉTAPE 2 : on COPIE le shared_ptr. Les deux pointent vers le MÊME chien.
    // Ce n'est PAS un deuxième chien : c'est le même, partagé -> compteur = 2.
    std::shared_ptr<Chien> proprietaire2 = proprietaire1;
    std::cout << "Apres proprietaire2   -> use_count = " << proprietaire2.use_count() << std::endl;

    // ÉTAPE 3 : on l'utilise. Peu importe par quel propriétaire : c'est le même chien.
    proprietaire2->aboyer();

    // ÉTAPE 4+5 : un 3e partage, mais limité à un bloc { }.
    {
        std::shared_ptr<Chien> proprietaire3 = proprietaire1;   // partage de plus
        std::cout << "Dans le bloc (3 partages) -> use_count = "
                  << proprietaire1.use_count() << std::endl;     // -> 3
    }   // <-- proprietaire3 sort de portée : un partage en moins -> compteur redescend

    std::cout << "Apres le bloc         -> use_count = " << proprietaire1.use_count() << std::endl;  // -> 2

    std::cout << "--- Fin du main : le chien n'est PAS encore libere ! ---" << std::endl;
    return 0;
}   // <-- ÉTAPE 6 : proprietaire1 ET proprietaire2 sortent de portée.
    //     Le compteur tombe à 0 -> le DERNIER partage est parti -> le chien
    //     est enfin détruit. (Tu verras le message [DESTRUCTEUR] ici, à la toute fin.)
