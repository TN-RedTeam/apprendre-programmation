/*
 * MODULE 05 - LIRE un fichier LIGNE PAR LIGNE en Go
 * =================================================
 * Montre la lecture morceau par morceau (ici, ligne par ligne) avec
 * os.Open + bufio.NewScanner. On ouvre le fichier, on le referme avec defer,
 * puis on parcourt les lignes une à une. Et si le fichier n'existe pas ?
 * os.Open renvoie une error : on la teste TOUT DE SUITE (réflexe du module 04).
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer DEPUIS LA RACINE du dépôt (après avoir lancé ecrire.go) :
 *     go run go/05_fichiers/lire.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Ouvrir "exemples/notes.txt" avec os.Open.
 *   2. Tester l'erreur : si le fichier n'existe pas, on prévient et on s'arrête.
 *   3. Prévoir de le refermer à la fin, quoi qu'il arrive (defer Close).
 *   4. Créer un "scanner" qui sait découper le fichier en lignes.
 *   5. Parcourir les lignes une par une et les afficher (numérotées).
 */

package main

import (
	"bufio" // boîte à outils pour lire efficacement (le Scanner de lignes)
	"fmt"   // boîte à outils d'affichage (Println, Printf)
	"os"    // boîte à outils "système" : ouvrir des fichiers...
)

func main() {

	// 1. OUVRIR le fichier en lecture (os.Open ne lit rien encore, il prépare).
	fichier, err := os.Open("exemples/notes.txt")

	// 2. TESTER l'erreur AVANT de s'en servir : si le fichier n'existe pas
	//    (ex. on n'a pas encore lancé ecrire.go), on le dit proprement et on sort.
	if err != nil {
		fmt.Println("Impossible d'ouvrir le fichier :", err)
		fmt.Println("Astuce : lance d'abord 'go run go/05_fichiers/ecrire.go'.")
		return
	}

	// 3. PRÉVOIR la fermeture : defer = "fais-le plus tard, juste avant de
	//    quitter main". Ainsi on n'oublie jamais de refermer le fichier.
	defer fichier.Close()

	// 4. CRÉER le scanner : par défaut, il découpe le fichier ligne par ligne.
	scanner := bufio.NewScanner(fichier)

	// 5. PARCOURIR : Scan() avance d'une ligne et renvoie true tant qu'il en reste.
	numero := 1
	for scanner.Scan() {
		ligne := scanner.Text() // le texte de la ligne courante (sans le \n)
		fmt.Printf("%d: %s\n", numero, ligne)
		numero++
	}
}
