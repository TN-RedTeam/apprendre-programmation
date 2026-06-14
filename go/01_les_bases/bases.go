/*
 * MODULE 01 - Les briques de base en Go
 * =====================================
 * Illustre, dans l'ordre, les notions du README : variables et types,
 * fmt.Println / fmt.Printf, conditions, boucle for (ses 3 formes), fonctions.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/01_les_bases/bases.go
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

// ─────────────────────────────────────────────
// FONCTIONS
// (en Go, elles peuvent être définies au-dessus OU en dessous de main)
// ─────────────────────────────────────────────

// (a int, b int) = deux paramètres entiers ; le 'int' APRÈS = type de retour.
func additionner(a int, b int) int {
	return a + b // 'return' renvoie le résultat à l'appelant
}

// Pas de type après les parenthèses = cette fonction ne renvoie rien.
func saluer() {
	fmt.Println("Bonjour depuis une fonction !")
}

// ─────────────────────────────────────────────
// main : le point de départ du programme
// ─────────────────────────────────────────────
func main() {

	// 1. VARIABLES ET TYPES
	var age int = 30 // forme LONGUE : var, nom, type (int), valeur
	taille := 1.68   // forme COURTE : Go devine le type (float64)
	nom := "Sam"     // une chaîne de caractères (string), entre guillemets "
	majeur := true   // un booléen (bool) : true ou false

	// 2. AFFICHER
	//    Println = simple, ajoute un saut de ligne, sépare par des espaces.
	fmt.Println("Nom :", nom)
	//    Printf = contrôle précis ; chaque %... = une valeur ; \n = saut de ligne.
	fmt.Printf("Age : %d ans\n", age)       // %d = entier
	fmt.Printf("Taille : %.2f m\n", taille) // %f = décimal ; .2 = 2 décimales
	fmt.Printf("Majeur : %t\n", majeur)     // %t = booléen

	// 3. CONDITIONS : PAS de parenthèses, mais accolades { } obligatoires.
	note := 12
	if note >= 16 {
		fmt.Println("Mention : Tres bien")
	} else if note >= 10 { // 'else if' (et non 'elif')
		fmt.Println("Mention : Recu")
	} else {
		fmt.Println("Mention : A retravailler")
	}

	// 4. BOUCLE for, forme 1 : (début ; condition ; pas) — comme le for du C.
	for i := 0; i < 3; i++ { // i++ = i = i + 1
		fmt.Println("Tour numero", i)
	}

	// 5. BOUCLE for, forme 2 : une seule condition = le "while" des autres langages.
	compteur := 0
	for compteur < 3 {
		fmt.Println("compteur =", compteur)
		compteur++ // indispensable, sinon boucle infinie
	}

	// 6. BOUCLE for, forme 3 : sans condition = infinie, arrêtée par "break".
	n := 0
	for {
		if n == 2 {
			break // stoppe la boucle
		}
		fmt.Println("n =", n)
		n++
	}

	// 7. APPELER NOS FONCTIONS.
	saluer()
	somme := additionner(7, 5)
	fmt.Printf("7 + 5 = %d\n", somme)
}
