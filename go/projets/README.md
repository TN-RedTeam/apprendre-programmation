# 🛠️ Projets — mettre les modules bout à bout

Tu as digéré les modules `00` à `07` ? Bravo. Place maintenant aux **projets capstone** :
des petits programmes complets qui ne montrent pas UNE notion isolée, mais qui en
**combinent plusieurs** pour fabriquer un vrai petit outil. C'est l'étape la plus
importante : c'est en assemblant les briques qu'on devient autonome.

> Chaque fichier commence par un bloc **« 🗺️ CHEMINEMENT DU PROGRAMME »** qui résume
> ses étapes : lis-le en premier pour comprendre la logique avant de plonger dans le code.

## Les projets

| Projet | Ce qu'il fait | Modules combinés |
|--------|---------------|------------------|
| [`gestionnaire_taches.go`](./gestionnaire_taches.go) | Une liste de tâches **persistante** : on ajoute des tâches, on en marque une faite, on **sauvegarde en JSON**, puis on **recharge** depuis le fichier | 02 (slices) · 03 (structs) · 04 (erreurs) · 05 (fichiers) · `encoding/json` |

## Lancer le projet

À lancer **DEPUIS LA RACINE du dépôt** (sinon le chemin `exemples/` tombe à côté) :

```bash
go run go/projets/gestionnaire_taches.go
```

Le programme est **non interactif** : il déroule un scénario tout seul (ajoute des
tâches d'exemple, en coche une, sauvegarde, recharge, affiche). Tu dois voir la liste
**rechargée depuis le fichier** s'afficher à la fin.

> 💡 Le fichier produit (`exemples/taches.json`) est créé dans un sous-dossier
> `exemples/` : tu peux relancer et expérimenter sans polluer le dépôt.

## Et ensuite ?

Le meilleur exercice : **modifie le scénario** de `main` (ajoute tes propres tâches,
marque-en d'autres), ou tente d'écrire une fonction `supprimer`. C'est comme ça qu'on
apprend pour de bon. 🚀
