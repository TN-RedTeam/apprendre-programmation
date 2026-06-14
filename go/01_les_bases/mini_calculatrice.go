/*
 * MODULE 01 - Mini-projet : une calculatrice en Go
 * ================================================
 * On combine ce qu'on a vu (variables, saisie, conditions, fonctions) dans un
 * petit programme utile : il lit une opération et deux nombres, puis calcule.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/01_les_bases/mini_calculatrice.go
 * Puis tape, par exemple :  +   (Entrée)   7   (Entrée)   5   (Entrée)
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. PACKAGE + IMPORT : package main, et "fmt" pour Println / Scan.
 *    2. FONCTIONS        : une fonction par opération (additionner, soustraire...).
 *    3. main             : (a) demander l'opération, (b) demander deux nombres,
 *                          (c) choisir le calcul selon l'opération, (d) afficher.
 */

package main

import "fmt"

// Une fonction par opération : code clair et réutilisable.
// On travaille avec des 'float64' pour gérer aussi les nombres à virgule.
func additionner(a float64, b float64) float64 { return a + b }
func soustraire(a float64, b float64) float64  { return a - b }
func multiplier(a float64, b float64) float64  { return a * b }

func diviser(a float64, b float64) float64 {
	// On se protège de la division par zéro.
	if b == 0 {
		fmt.Println("Erreur : division par zero impossible.")
		return 0
	}
	return a / b
}

func main() {
	// Des variables avec leur type : un texte pour l'opération, des décimaux pour les nombres.
	var operation string
	var n1, n2, resultat float64

	// 1. DEMANDER l'opération. fmt.Scan lit ce qui est tapé au clavier et le
	//    range dans la variable. Le & = "range la saisie À L'ADRESSE de operation".
	fmt.Print("Operation (+, -, *, /) : ")
	fmt.Scan(&operation)

	// 2. DEMANDER les deux nombres (Scan lit directement des float64 ici).
	fmt.Print("Premier nombre  : ")
	fmt.Scan(&n1)
	fmt.Print("Deuxieme nombre : ")
	fmt.Scan(&n2)

	// 3. CHOISIR le calcul selon l'opération (operation est une string : guillemets ").
	if operation == "+" {
		resultat = additionner(n1, n2)
	} else if operation == "-" {
		resultat = soustraire(n1, n2)
	} else if operation == "*" {
		resultat = multiplier(n1, n2)
	} else if operation == "/" {
		resultat = diviser(n1, n2)
	} else {
		fmt.Println("Operation inconnue.")
		return // on quitte main : le programme s'arrête ici
	}

	// 4. AFFICHER le résultat (%.2f = 2 chiffres après la virgule).
	fmt.Printf("Resultat : %.2f\n", resultat)
}
