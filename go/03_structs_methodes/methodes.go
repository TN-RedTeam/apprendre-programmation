/*
 * MODULE 03 - Les MÉTHODES (attacher un comportement à un type) en Go
 * ==================================================================
 * Illustre, dans l'ordre, les notions du README : une méthode = une
 * fonction avec un RÉCEPTEUR. On montre la différence CRUCIALE entre :
 *   - récepteur VALEUR (r Rectangle)  -> reçoit une COPIE : pour LIRE/calculer.
 *   - récepteur POINTEUR (r *Rectangle) -> reçoit le VRAI objet : pour MODIFIER.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/03_structs_methodes/methodes.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer un Rectangle (largeur + hauteur).
 *   2. Appeler Aire() : méthode à récepteur VALEUR, elle CALCULE sans modifier.
 *   3. Appeler Doubler() : méthode à récepteur POINTEUR, elle MODIFIE l'objet.
 *   4. Recalculer Aire() pour PROUVER que l'objet a bien changé.
 *   5. Montrer (contre-exemple) qu'un récepteur VALEUR ne modifie PAS l'original.
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

// Le MODÈLE : un Rectangle, regroupe deux champs liés.
type Rectangle struct {
	Largeur float64 // un côté
	Hauteur float64 // l'autre côté
}

// MÉTHODE À RÉCEPTEUR VALEUR : (r Rectangle).
// r est une COPIE du rectangle. C'est parfait pour LIRE/calculer : on ne
// touche pas à l'original. Elle renvoie l'aire (un float64).
func (r Rectangle) Aire() float64 {
	return r.Largeur * r.Hauteur
}

// MÉTHODE À RÉCEPTEUR POINTEUR : (r *Rectangle).
// Le "*" veut dire "le VRAI rectangle, pas une copie". Donc ce qu'on modifie
// ici reste vrai APRÈS l'appel. Ici on double les deux côtés.
func (r *Rectangle) Doubler() {
	r.Largeur = r.Largeur * 2
	r.Hauteur = r.Hauteur * 2
}

// CONTRE-EXEMPLE volontaire : récepteur VALEUR qui ESSAIE de modifier.
// Comme r est une copie, le changement reste LOCAL et l'original ne bouge pas.
func (r Rectangle) DoublerRate() {
	r.Largeur = r.Largeur * 2
	r.Hauteur = r.Hauteur * 2
}

func main() {

	// 1. CRÉER un rectangle de 4 par 3.
	rect := Rectangle{Largeur: 4, Hauteur: 3}
	fmt.Println("Rectangle de depart :", rect)

	// 2. APPELER une méthode à récepteur VALEUR (lecture/calcul).
	//    On l'appelle SUR l'objet, avec le point "." et des parenthèses.
	fmt.Printf("Aire : %.1f\n", rect.Aire())

	// 3. APPELER la méthode à récepteur POINTEUR : elle MODIFIE le rectangle.
	//    (Pas besoin d'écrire "&rect" : Go s'en charge tout seul.)
	rect.Doubler()
	fmt.Println("Apres Doubler() :", rect)

	// 4. PREUVE que l'objet a changé : la nouvelle aire est différente.
	fmt.Printf("Nouvelle aire : %.1f\n", rect.Aire())

	// 5. CONTRE-EXEMPLE : un récepteur VALEUR ne change PAS l'original.
	rect.DoublerRate()
	fmt.Println("Apres DoublerRate() (recepteur valeur) :", rect, "-> inchange, normal !")
}
