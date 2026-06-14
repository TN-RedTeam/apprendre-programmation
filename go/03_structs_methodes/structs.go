/*
 * MODULE 03 - Les STRUCTS (regrouper des champs sous un même type) en Go
 * =====================================================================
 * Illustre, dans l'ordre, les notions du README : définir un struct (le
 * MODÈLE), créer des instances (les FICHES remplies), lire et modifier
 * les champs avec le point ".", et afficher le tout.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/03_structs_methodes/structs.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer une première instance de Personne (champs nommés).
 *   2. LIRE ses champs avec le point "." (p.Nom, p.Age).
 *   3. MODIFIER un champ (p.Age) et constater le changement.
 *   4. Créer une 2e instance pour montrer que chaque fiche est INDÉPENDANTE.
 *   5. Afficher une fiche complète proprement avec Printf.
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

// On déclare le MODÈLE de fiche : un nouveau type "Personne".
// type ... struct { } regroupe plusieurs CHAMPS liés sous un seul type.
// (On le met en dehors de main, au niveau du fichier : c'est l'usage.)
type Personne struct {
	Nom string // champ 1 : le nom, du texte
	Age int    // champ 2 : l'âge, un entier
}

func main() {

	// 1. CRÉER UNE INSTANCE : on remplit une fiche en nommant chaque champ.
	//    p est une variable de type Personne.
	p := Personne{Nom: "Sam", Age: 30}
	fmt.Println("Fiche creee :", p)

	// 2. LIRE les champs avec le point "." (nomDeLaVariable.NomDuChamp).
	fmt.Println("Nom :", p.Nom)
	fmt.Println("Age :", p.Age)

	// 3. MODIFIER un champ : on lui range une nouvelle valeur.
	p.Age = 31 // Sam vient d'avoir un an
	fmt.Println("Apres anniversaire, age :", p.Age)

	// 4. CHAQUE INSTANCE EST INDÉPENDANTE : une 2e fiche, ses propres valeurs.
	q := Personne{Nom: "Lou", Age: 25}
	fmt.Println("Autre fiche :", q)
	fmt.Println("Sam a toujours", p.Age, "ans / Lou en a", q.Age)

	// 5. AFFICHER une fiche proprement avec Printf et les verbes de format.
	//    %s = une string (Nom), %d = un entier (Age).
	fmt.Printf("%s a %d ans.\n", p.Nom, p.Age)
}
