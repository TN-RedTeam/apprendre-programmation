/*
 * MODULE 02 - Une liste qui grandit : std::vector
 * ===============================================
 * Illustre les notions du README : créer un std::vector, ajouter des éléments
 * avec .push_back(), connaître sa taille avec .size(), accéder par index,
 * le parcourir avec une "range-based for", puis calculer somme et moyenne.
 *
 * Compiler puis lancer :
 *     g++ -Wall cpp/02_conteneurs_chaines/vecteurs.cpp -o vecteurs && ./vecteurs
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce qui se passe, dans l'ordre) :
 *   1. On crée un vector VIDE de notes.
 *   2. On y ajoute 4 notes une par une avec .push_back().
 *   3. On affiche combien il y en a (.size()) et la 1re (accès par index).
 *   4. On le parcourt avec une range-based for pour TOUT afficher.
 *   5. On reparcourt en ADDITIONNANT chaque note -> la somme.
 *   6. On divise la somme par le nombre de notes -> la moyenne.
 *   7. On affiche somme et moyenne, puis le programme se termine.
 */

#include <iostream>   // pour std::cout (afficher)
#include <vector>     // pour le type std::vector (une liste qui grandit)

int main() {

    // 1. CRÉER un vector VIDE de nombres entiers.
    //    Entre < > : le TYPE des éléments qu'il contiendra (ici des int).
    std::vector<int> notes;

    // 2. AJOUTER des éléments à la fin avec .push_back().
    //    (Équivalent du .append() de Python.) Le vector grandit tout seul.
    notes.push_back(12);
    notes.push_back(15);
    notes.push_back(9);
    notes.push_back(18);

    // 3. TAILLE avec .size() et ACCÈS PAR INDEX avec [ ] (on compte dès 0).
    std::cout << "Nombre de notes : " << notes.size() << std::endl;   // 4
    std::cout << "Premiere note   : " << notes[0]     << std::endl;   // 12

    // 4. PARCOURIR avec une "range-based for" : "pour chaque note dans notes".
    //    À chaque tour, 'note' prend la valeur de l'élément suivant.
    std::cout << "Toutes les notes :";
    for (int note : notes) {
        std::cout << " " << note;
    }
    std::cout << std::endl;

    // 5. CALCULER LA SOMME : on additionne chaque note dans un total.
    int somme = 0;
    for (int note : notes) {
        somme = somme + note;   // ou : somme += note;
    }

    // 6. CALCULER LA MOYENNE = somme / nombre de notes.
    //    On convertit en double pour garder les décimales (sinon division entière).
    double moyenne = static_cast<double>(somme) / notes.size();

    // 7. AFFICHER les résultats.
    std::cout << "Somme   : " << somme   << std::endl;   // 54
    std::cout << "Moyenne : " << moyenne << std::endl;   // 13.5

    return 0;   // succès
}
