/*
 * PROJET CAPSTONE - Gestionnaire de taches (to-do list)
 * =====================================================
 * Un mini-projet qui COMBINE plusieurs modules du parcours :
 *   - Module 03 (classes & objets)  : une classe Tache (description + faite/pas faite)
 *   - Module 02 (std::vector)       : une liste de Tache qui grandit toute seule
 *   - Module 05 (fichiers)          : sauvegarde/chargement avec std::ofstream/std::ifstream
 *   - Module 06 (STL, en bonus)     : std::filesystem pour creer le dossier exemples/
 *
 * C'est l'idee d'un "capstone" : au lieu d'illustrer UNE notion, on assemble
 * plusieurs briques apprises separement pour fabriquer un vrai petit outil.
 *
 * NON INTERACTIF : le programme ne pose AUCUNE question. Il ajoute des taches
 * d'exemple, en marque une comme faite, sauvegarde dans un fichier, puis
 * RECHARGE depuis ce fichier et affiche le resultat. Tu peux donc juste le
 * lancer et regarder ce qui se passe.
 *
 * ANTI-POLLUTION : tout est ecrit dans un sous-dossier "exemples/" (cree
 * automatiquement). Tu peux le supprimer apres coup, ca ne touche a rien.
 *
 * Compiler puis lancer (DEPUIS LA RACINE du depot, et il FAUT -std=c++17
 * a cause de std::filesystem) :
 *     g++ -std=c++17 -Wall cpp/projets/gestionnaire_taches.cpp -o gestionnaire
 *     ./gestionnaire
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes etapes, dans l'ordre) :
 *    1. PREPARER  : on cree le dossier "exemples/" s'il n'existe pas.
 *    2. REMPLIR   : on cree une liste (std::vector<Tache>) et on ajoute 3 taches.
 *    3. MARQUER   : on marque la tache numero 2 comme FAITE.
 *    4. AFFICHER  : on affiche la liste en memoire.
 *    5. SAUVEGARDER : on ecrit la liste dans "exemples/taches.txt".
 *    6. RECHARGER : on repart d'une liste VIDE et on la remplit depuis le fichier.
 *    7. AFFICHER  : on affiche la liste rechargee -> elle est identique. 🎉
 */

#include <iostream>     // std::cout (afficher)
#include <fstream>      // std::ofstream / std::ifstream (ecrire / lire un fichier)
#include <string>       // std::string (le texte des taches)
#include <vector>       // std::vector (la liste de taches qui grandit)
#include <filesystem>   // std::filesystem (creer le dossier exemples/) -> besoin de -std=c++17

// =====================================================================
// LA CLASSE (module 03) : une Tache, c'est une description + un etat
// (faite ou pas). On garde les attributs PRIVES et on expose des
// methodes PUBLIC : c'est l'encapsulation.
// =====================================================================
class Tache {
private:
    std::string description;   // ce qu'il y a a faire
    bool faite;                // true = terminee, false = encore a faire

public:
    // CONSTRUCTEUR : a la creation, une tache n'est PAS faite par defaut.
    // Le "= false" donne une valeur par defaut au 2e parametre : on peut
    // donc ecrire Tache("...") sans preciser l'etat.
    Tache(std::string desc, bool estFaite = false) {
        description = desc;
        faite = estFaite;
    }

    // METHODE : marquer la tache comme terminee.
    void marquerFaite() {
        faite = true;
    }

    // ACCESSEURS (on dit aussi "getters") : des portes pour LIRE les
    // attributs prives depuis l'exterieur, sans pouvoir les casser.
    // Le "const" a la fin promet que la methode ne modifie pas l'objet.
    std::string getDescription() const {
        return description;
    }
    bool estFaite() const {
        return faite;
    }

    // METHODE : afficher joliment la tache. [x] = faite, [ ] = a faire.
    void afficher() const {
        std::cout << "  [" << (faite ? "x" : " ") << "] " << description << std::endl;
    }
};

// =====================================================================
// SAUVEGARDER (module 05) : on ecrit toute la liste dans un fichier.
// Format choisi, une tache par ligne : "etat|description"
// ou etat vaut 1 (faite) ou 0 (a faire). Le '|' separe les deux champs.
// On passe la liste par REFERENCE CONSTANTE (const &) : pas de copie,
// et la fonction promet de ne pas la modifier.
// =====================================================================
void sauvegarder(const std::vector<Tache>& taches, const std::string& chemin) {
    // On ouvre le fichier en ECRITURE. S'il existe deja, il est ecrase.
    std::ofstream fichier(chemin);
    if (!fichier.is_open()) {
        std::cout << "Erreur : impossible d'ecrire dans " << chemin << std::endl;
        return;
    }
    // Boucle range-for (module 02) : on parcourt chaque tache de la liste.
    for (const Tache& t : taches) {
        // (t.estFaite() ? 1 : 0) -> on ecrit 1 ou 0, puis '|', puis le texte.
        fichier << (t.estFaite() ? 1 : 0) << "|" << t.getDescription() << std::endl;
    }
    // Le fichier se referme tout seul ici (RAII).
    std::cout << "Sauvegarde effectuee dans " << chemin << std::endl;
}

// =====================================================================
// CHARGER (module 05) : on lit le fichier et on RECONSTRUIT une liste
// de Tache. On renvoie un std::vector<Tache> tout neuf.
// =====================================================================
std::vector<Tache> charger(const std::string& chemin) {
    std::vector<Tache> taches;          // on part d'une liste VIDE
    std::ifstream fichier(chemin);      // ouverture en LECTURE
    if (!fichier.is_open()) {
        std::cout << "Aucun fichier a charger (" << chemin << ")." << std::endl;
        return taches;                  // on renvoie la liste vide
    }

    std::string ligne;
    // On lit le fichier LIGNE PAR LIGNE (module 05).
    while (std::getline(fichier, ligne)) {
        if (ligne.empty()) continue;    // on saute les lignes vides par securite

        // On cherche le separateur '|' pour couper "etat" et "description".
        std::size_t pos = ligne.find('|');
        if (pos == std::string::npos) continue;  // ligne mal formee : on l'ignore

        // substr(debut, longueur) et substr(debut) decoupent la chaine.
        std::string etat = ligne.substr(0, pos);   // "1" ou "0"
        std::string desc = ligne.substr(pos + 1);  // tout ce qui suit le '|'

        bool faite = (etat == "1");     // on retransforme "1" -> true
        // On reconstruit une Tache et on l'ajoute a la liste (module 02).
        taches.push_back(Tache(desc, faite));
    }
    return taches;                      // RAII : le fichier se referme ici
}

// Petite fonction utilitaire pour afficher toute une liste de taches.
void afficherListe(const std::vector<Tache>& taches, const std::string& titre) {
    std::cout << titre << std::endl;
    if (taches.empty()) {
        std::cout << "  (liste vide)" << std::endl;
        return;
    }
    for (const Tache& t : taches) {
        t.afficher();
    }
}

int main() {
    // Chemin du fichier de sauvegarde, dans le sous-dossier exemples/.
    const std::string chemin = "exemples/taches.txt";

    // (1) PREPARER : on cree le dossier "exemples/" s'il n'existe pas deja.
    //     create_directories ne se plaint pas si le dossier existe deja.
    std::filesystem::create_directories("exemples");

    // (2) REMPLIR : une liste de taches qui grandit (std::vector, module 02).
    std::vector<Tache> maListe;
    maListe.push_back(Tache("Acheter du pain"));
    maListe.push_back(Tache("Reviser le module C++ sur les classes"));
    maListe.push_back(Tache("Arroser les plantes"));

    // (3) MARQUER : on marque la 2e tache comme faite.
    //     Attention : en C++ on compte a partir de 0, donc l'indice 1 = 2e tache.
    maListe[1].marquerFaite();

    // (4) AFFICHER la liste en memoire.
    afficherListe(maListe, "Ma liste de taches (en memoire) :");
    std::cout << std::endl;

    // (5) SAUVEGARDER dans le fichier.
    sauvegarder(maListe, chemin);
    std::cout << std::endl;

    // (6) RECHARGER : on repart de ZERO et on relit le fichier.
    //     C'est la preuve que la sauvegarde a vraiment fonctionne.
    std::vector<Tache> listeRechargee = charger(chemin);

    // (7) AFFICHER la liste rechargee : elle doit etre identique. 🎉
    afficherListe(listeRechargee, "Liste rechargee depuis le fichier :");

    return 0;   // succes
}
