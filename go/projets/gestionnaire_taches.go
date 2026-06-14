/*
 * PROJET CAPSTONE - Gestionnaire de TÂCHES persistant (JSON)
 * =========================================================
 * Premier "vrai" mini-projet du parcours Go : il ne montre pas UNE notion,
 * il en COMBINE plusieurs pour fabriquer un petit outil complet.
 *
 * 🧩 MODULES COMBINÉS (ce qu'on réutilise des fondations)
 *   - Module 02 (collections) : un SLICE []Tache, parcouru avec range.
 *   - Module 03 (structs)     : un struct Tache (Description + Faite).
 *   - Module 04 (erreurs)     : le réflexe "if err != nil" partout.
 *   - Module 05 (fichiers)    : os.MkdirAll, os.WriteFile, os.ReadFile.
 *   - Nouveauté du projet      : encoding/json pour SAUVEGARDER / RECHARGER.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 *    Il est NON INTERACTIF : il déroule un scénario tout seul (aucune saisie).
 * Lancer DEPUIS LA RACINE du dépôt :
 *     go run go/projets/gestionnaire_taches.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer le sous-dossier "exemples/" s'il manque (anti-pollution).
 *   2. Partir d'une liste de tâches VIDE, puis y AJOUTER des tâches d'exemple.
 *   3. MARQUER une tâche comme faite.
 *   4. AFFICHER la liste en mémoire.
 *   5. SAUVEGARDER la liste dans un fichier JSON (avec test d'erreur).
 *   6. RECHARGER la liste depuis ce fichier (dans une variable NEUVE).
 *   7. AFFICHER la liste rechargée pour prouver que la persistance marche.
 */

package main

import (
	"encoding/json" // transformer nos structs <-> texte JSON
	"fmt"           // boîte à outils d'affichage (Println, Printf)
	"os"            // boîte à outils "système" : fichiers, dossiers...
)

// Chemin du fichier où l'on range les tâches. Une constante = on l'écrit une
// seule fois, on la réutilise partout (sauvegarde ET rechargement).
const fichierTaches = "exemples/taches.json"

// Le MODÈLE d'une tâche : deux champs liés regroupés sous un type "Tache".
// Les balises `json:"..."` disent à encoding/json comment NOMMER les champs
// dans le fichier (en minuscules, plus joli).
type Tache struct {
	Description string `json:"description"` // ce qu'il y a à faire (du texte)
	Faite       bool   `json:"faite"`       // vrai = terminée, faux = à faire
}

// ajouter : prend la liste actuelle + une description, et renvoie une NOUVELLE
// liste avec la tâche en plus. append agrandit le slice tout seul (module 02).
func ajouter(taches []Tache, description string) []Tache {
	nouvelle := Tache{Description: description, Faite: false} // neuve = pas faite
	return append(taches, nouvelle)
}

// marquer : passe la tâche numéro "index" à Faite = true.
// On prend un *pointeur* (&taches) car on veut MODIFIER le slice d'origine.
func marquer(taches []Tache, index int) {
	// On vérifie d'abord que l'index existe vraiment (sinon : plantage).
	if index < 0 || index >= len(taches) {
		fmt.Println("Index hors limites, rien marqué :", index)
		return
	}
	taches[index].Faite = true // on coche la case
}

// afficher : parcourt le slice et imprime chaque tâche joliment.
func afficher(taches []Tache) {
	fmt.Println("--- Ma liste de tâches ---")
	if len(taches) == 0 { // cas particulier : liste vide
		fmt.Println("(aucune tâche)")
		return
	}
	// range donne l'INDICE (i) et la VALEUR (t) de chaque élément.
	for i, t := range taches {
		coche := "[ ]" // case vide par défaut
		if t.Faite {   // si la tâche est faite...
			coche = "[x]" // ...on dessine une croix
		}
		fmt.Printf("%d. %s %s\n", i, coche, t.Description)
	}
}

// sauvegarder : transforme le slice en JSON et l'écrit dans un fichier.
// Renvoie une error : l'appelant pourra la tester (réflexe module 04).
func sauvegarder(taches []Tache, chemin string) error {
	// json.MarshalIndent transforme nos données en texte JSON LISIBLE
	// (indenté de 2 espaces). Il renvoie les octets + une éventuelle erreur.
	donnees, err := json.MarshalIndent(taches, "", "  ")
	if err != nil {
		return err // on remonte l'erreur telle quelle
	}
	// On écrit ces octets dans le fichier (0644 = permissions standard).
	return os.WriteFile(chemin, donnees, 0644)
}

// charger : lit le fichier JSON et reconstruit le slice []Tache.
func charger(chemin string) ([]Tache, error) {
	// 1. Lire tout le fichier d'un coup -> des octets.
	donnees, err := os.ReadFile(chemin)
	if err != nil {
		return nil, err // fichier introuvable / illisible : on remonte l'erreur
	}
	// 2. Décoder le JSON DANS une variable de type []Tache.
	var taches []Tache
	if err := json.Unmarshal(donnees, &taches); err != nil {
		return nil, err // JSON abîmé : on remonte l'erreur
	}
	return taches, nil // tout va bien : on renvoie la liste + pas d'erreur
}

func main() {

	// 1. CRÉER le dossier "exemples/" s'il manque (anti-pollution du dépôt).
	if err := os.MkdirAll("exemples", 0755); err != nil {
		fmt.Println("Erreur en créant le dossier :", err)
		return
	}

	// 2. PARTIR d'une liste VIDE puis AJOUTER des tâches d'exemple.
	//    ajouter renvoie une nouvelle liste : on réaffecte à chaque fois.
	var taches []Tache
	taches = ajouter(taches, "Apprendre les structs en Go")
	taches = ajouter(taches, "Lire un fichier JSON")
	taches = ajouter(taches, "Arroser les plantes")

	// 3. MARQUER la première tâche (index 0) comme faite.
	marquer(taches, 0)

	// 4. AFFICHER la liste telle qu'elle est EN MÉMOIRE.
	fmt.Println("AVANT sauvegarde :")
	afficher(taches)

	// 5. SAUVEGARDER en JSON, en testant l'erreur tout de suite.
	if err := sauvegarder(taches, fichierTaches); err != nil {
		fmt.Println("Erreur à la sauvegarde :", err)
		return
	}
	fmt.Println("\nSauvegardé dans", fichierTaches)

	// 6. RECHARGER depuis le fichier dans une variable NEUVE (rechargees).
	//    Si la persistance marche, elle doit contenir la même chose.
	rechargees, err := charger(fichierTaches)
	if err != nil {
		fmt.Println("Erreur au chargement :", err)
		return
	}

	// 7. AFFICHER la liste rechargée : preuve que tout a bien été persisté.
	fmt.Println("\nAPRÈS rechargement depuis le fichier :")
	afficher(rechargees)
}
