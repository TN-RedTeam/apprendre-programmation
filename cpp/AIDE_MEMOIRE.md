# 🃏 Aide-mémoire C++ (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `01_les_bases`, `02_conteneurs_chaines`…

> ⚠️ En C++ : chaque instruction finit par un **`;`**, les blocs sont entre **`{ }`**, et on
> écrit `std::` devant les outils de la bibliothèque standard (`cout`, `cin`, `string`…).

---

## Compiler et lancer (g++)

```bash
g++ -Wall mon_fichier.cpp -o mon_prog   # compile (-Wall = montre tous les avertissements)
./mon_prog                              # lance l'exécutable produit
# En une ligne :
g++ -Wall mon_fichier.cpp -o mon_prog && ./mon_prog
```

## Structure type d'un programme

```cpp
#include <iostream>   // 1. les boîtes à outils (#include)
#include <string>

int additionner(int a, int b) {   // 2. les fonctions (AVANT main)
    return a + b;
}

int main() {                      // 3. main : le point de départ
    std::cout << "Bonjour" << std::endl;
    return 0;                     //    0 = tout s'est bien passé
}
```

## Afficher / lire

```cpp
std::cout << "Bonjour" << std::endl;        // afficher (endl = retour à la ligne)
std::cout << "Age : " << age << std::endl;  // enchaîner texte et variables avec <<
std::cin >> age;                            // lire un nombre tapé au clavier (pas de &)
std::getline(std::cin, ligne);              // lire une ligne ENTIÈRE de texte
```

## Variables et types

```cpp
int age = 30;             // int    : entier
double prix = 9.99;       // double : nombre à virgule
char lettre = 'A';        // char   : UN caractère, entre apostrophes ' '
std::string nom = "Lou";  // string : du texte, entre guillemets " "
bool actif = true;        // bool   : true (vrai) / false (faux)
```

## Opérateurs

```cpp
+  -  *  /        // addition, soustraction, multiplication, division
%                 // reste (modulo) : 7 % 2 == 1
==  !=            // égal / différent
<  >  <=  >=      // comparaisons
&&   ||   !       // ET / OU / NON logiques
```

## Conditions

```cpp
if (age >= 18) {
    std::cout << "Majeur" << std::endl;
} else if (age >= 13) {           // 'else if' (et non 'elif')
    std::cout << "Ado" << std::endl;
} else {
    std::cout << "Enfant" << std::endl;
}
```

## Boucles

```cpp
for (int i = 0; i < 5; i++) {           // (début ; condition ; pas) -> 0,1,2,3,4
    std::cout << i << std::endl;
}

while (x < 10) {                        // tant que la condition est vraie
    x++;                                // sinon : boucle infinie !
}

for (int note : notes) {                // range-for : "pour chaque note de notes"
    std::cout << note << std::endl;
}
```

## Fonctions

```cpp
// type_de_retour nom(paramètres typés) { ... }
int additionner(int a, int b) {
    return a + b;       // renvoie un résultat
}

void saluer() {         // void = ne renvoie rien
    std::cout << "Bonjour !" << std::endl;
}
```

## Chaînes (`std::string`) — `#include <string>`

```cpp
std::string s = "Bonjour";
std::string c = "Ada" + std::string(" ") + "Lovelace";  // concaténer avec +
s.size();                 // longueur (nombre de caractères)
s.substr(0, 3);           // sous-chaîne : "Bon" (depuis 0, 3 caractères)
s[0];                     // accès à un caractère par index (dès 0)
for (char ch : s) { ... } // parcourir caractère par caractère
```

## Listes (`std::vector`) — `#include <vector>`

```cpp
std::vector<int> notes;       // une liste (vide) d'entiers
notes.push_back(12);          // ajouter à la fin (comme .append() en Python)
notes.size();                 // nombre d'éléments
notes[0];                     // accès par index (dès 0)
for (int n : notes) { ... }   // parcourir avec une range-for
// 🆚 Contrairement au tableau brut du C (taille fixe), un vector grandit tout seul.
```

➡️ Voir aussi : [GLOSSAIRE.md](./GLOSSAIRE.md) pour les définitions.
