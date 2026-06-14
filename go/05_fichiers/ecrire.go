/*
 * MODULE 05 - ÉCRIRE dans un fichier en Go
 * ========================================
 * Montre la façon LA PLUS SIMPLE d'écrire un fichier : tout donner d'un coup
 * avec os.WriteFile(chemin, []byte(...), 0644). Comme toute opération qui peut
 * échouer, elle renvoie une error : on la teste TOUT DE SUITE (réflexe du module 04).
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer DEPUIS LA RACINE du dépôt :
 *     go run go/05_fichiers/ecrire.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer le sous-dossier "exemples/" s'il n'existe pas (anti-pollution).
 *   2. Préparer le texte à écrire (plusieurs lignes, séparées par des \n).
 *   3. Tout écrire d'un coup dans "exemples/notes.txt" avec os.WriteFile.
 *   4. Tester l'erreur : si l'écriture a échoué, on prévient et on s'arrête.
 *   5. Confirmer que le fichier a bien été écrit.
 */

package main

import (
	"fmt" // boîte à outils d'affichage (Println)
	"os"  // boîte à outils "système" : fichiers, dossiers...
)

func main() {

	// 1. CRÉER le dossier "exemples/" s'il manque (MkdirAll ne râle pas s'il
	//    existe déjà). 0755 = permissions standard pour un dossier.
	if err := os.MkdirAll("exemples", 0755); err != nil {
		fmt.Println("Erreur en creant le dossier :", err)
		return
	}

	// 2. PRÉPARER le texte. Chaque \n marque une fin de ligne.
	contenu := "Liste de courses\n" +
		"- pommes\n" +
		"- pain\n" +
		"- fromage\n"

	// 3. ÉCRIRE tout d'un coup. []byte(contenu) convertit le texte en octets
	//    (un fichier stocke des octets). 0644 = permissions standard d'un fichier.
	err := os.WriteFile("exemples/notes.txt", []byte(contenu), 0644)

	// 4. TESTER l'erreur AVANT de continuer (le réflexe "if err != nil" du module 04).
	if err != nil {
		fmt.Println("Erreur en ecrivant le fichier :", err)
		return
	}

	// 5. Tout s'est bien passé : on confirme.
	fmt.Println("Fichier ecrit : exemples/notes.txt")
}
