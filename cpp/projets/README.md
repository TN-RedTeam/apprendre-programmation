# 🛠️ Projets C++ — assembler ce que tu as appris

Une fois les modules `00` à `07` digérés, place aux **projets « capstone »** : des
programmes complets qui **combinent plusieurs notions** au lieu d'en illustrer une seule.
C'est l'étape la plus importante, celle où on devient autonome : on prend des briques
apprises séparément et on construit un vrai petit outil.

> Chaque programme commence par un bloc **« 🗺️ CHEMINEMENT DU PROGRAMME »** qui résume
> ses étapes : lis-le en premier pour comprendre la logique avant de plonger dans le code.

## Les projets

| Projet | Ce qu'il fait | Modules combinés |
|--------|---------------|------------------|
| [`gestionnaire_taches.cpp`](./gestionnaire_taches.cpp) | Une mini liste de tâches (to-do) : ajoute des tâches, en marque une faite, **sauvegarde dans un fichier**, puis **recharge** depuis ce fichier et affiche | 03 (classe `Tache`), 02 (`std::vector`), 05 (fichiers `std::ofstream`/`std::ifstream`), 06 (`std::filesystem`) |

### Le gestionnaire de tâches en détail

- Une **classe `Tache`** (module 03) : une description + un état *faite / pas faite*,
  attributs **privés** et méthodes **publiques** (encapsulation).
- Une **liste qui grandit** `std::vector<Tache>` (module 02) pour stocker les tâches.
- La **sauvegarde et le chargement** dans un fichier (module 05) : une tâche par ligne,
  au format `etat|description`, avec `std::ofstream` (écrire) et `std::ifstream` (lire).
- **`std::filesystem`** (module 06) pour créer le sous-dossier `exemples/` automatiquement.

Le programme est **non interactif** : il ne pose aucune question. Tu le lances, et il
ajoute des tâches d'exemple, en marque une faite, sauvegarde, recharge depuis le fichier,
puis affiche le résultat (identique à l'original : la preuve que ça a marché 🎉).

## Compiler et lancer

⚠️ Lance la commande **DEPUIS LA RACINE du dépôt**. Il faut **`-std=c++17`**
(obligatoire ici à cause de `std::filesystem`).

```bash
g++ -std=c++17 -Wall cpp/projets/gestionnaire_taches.cpp -o gestionnaire
./gestionnaire
```

> 💡 **Anti-pollution :** le fichier produit (`exemples/taches.txt`) est créé dans un
> sous-dossier `exemples/`. Tu peux expérimenter sans risque, et tout supprimer ensuite
> avec `rm -rf exemples`.

## Et ensuite ?

Le meilleur exercice : **fais évoluer ce projet**. Par exemple, ajoute une méthode pour
*supprimer* une tâche, ou un *compteur* de tâches restantes. C'est en bricolant un vrai
programme qu'on apprend pour de bon. 🚀
