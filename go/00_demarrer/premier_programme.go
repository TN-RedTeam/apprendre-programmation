/*
 * MODULE 00 - Premier programme en Go
 * ===================================
 * Ton tout premier programme Go. Objectif : voir le cycle
 * « écrire -> lancer » en action (Go compile tout seul juste avant).
 *
 * Pour le lancer, ouvre un terminal et tape :
 *     go run go/00_demarrer/premier_programme.go
 *
 * Rappel : les commentaires (comme ce bloc) sont ignorés par le compilateur.
 * En Go on écrit  // pour une ligne   ou   ... pour plusieurs lignes.
 */

// (1) package main = "ceci est un programme exécutable" (et non une bibliothèque).
// Tout programme Go que l'on peut lancer commence par cette ligne.
package main

// (2) On importe la boîte à outils d'affichage "fmt" (format).
//     Elle contient Println(). C'est l'équivalent d'un import en Python.
import "fmt"

// (3) func main = le POINT DE DÉPART de tout programme Go. L'exécution commence ici.
// L'accolade { ouvre le corps de la fonction (fermé par } tout en bas).
func main() {

	// (4) fmt.Println affiche du texte SUIVI d'un retour à la ligne automatique
	//     (Println = "print line"). Pas besoin de \n à la fin : c'est inclus.
	fmt.Println("Bonjour le monde !")
	fmt.Println("Je viens de lancer mon premier programme Go.")

	// Le programme s'exécute de haut en bas : cette ligne s'affiche en dernier.
	fmt.Println("Cette ligne s'affiche apres les precedentes.")
}

/*
 * À TOI DE MODIFIER :
 *   - change le texte des Println,
 *   - ajoute un nouveau fmt.Println avec ton message,
 *   - relance avec  go run go/00_demarrer/premier_programme.go
 * Avec go run, pas besoin de recompiler à la main : Go le fait automatiquement.
 */
