/*
 * MODULE 09 - SELECT (attendre sur PLUSIEURS channels à la fois)
 * ==============================================================
 * Avec un channel simple, on attend UN seul tuyau. Mais souvent on aimerait
 * surveiller PLUSIEURS tuyaux en même temps et réagir au PREMIER prêt.
 * C'est le rôle de `select` : il regarde tous les channels listés, et exécute
 * le bloc du PREMIER qui a quelque chose à offrir.
 *
 * 🏦 ANALOGIE. Tu es à la banque devant DEUX guichets. Tu ne sais pas lequel
 * se libérera en premier : tu surveilles les DEUX et tu fonces vers celui qui
 * t'appelle d'abord. `select`, c'est exactement ça : surveiller plusieurs
 * guichets (channels) et servir le premier qui répond.
 *
 * BONUS : `time.After(d)` renvoie un channel qui "sonne" après une durée d.
 * En l'ajoutant à un `select`, on obtient un TIMEOUT : "si rien n'arrive avant
 * d, je passe à autre chose au lieu d'attendre pour toujours".
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer DEPUIS LA RACINE du dépôt :
 *     go run go/09_concurrence_avancee/select.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer deux channels : "rapide" et "lent".
 *   2. Lancer deux goroutines : l'une envoie vite, l'autre envoie tard.
 *   3. Premier select : il attend les DEUX channels et sert le plus RAPIDE.
 *   4. Deuxième select : on attend un channel TROP lent face à un timeout
 *      court (time.After) -> c'est le timeout qui gagne, de façon sûre.
 */

package main

import (
	"fmt"  // affichage (Println, Printf)
	"time" // durées et minuteries (Sleep, After)
)

func main() {

	// 1. CRÉER deux tuyaux qui transportent du texte.
	rapide := make(chan string)
	lent := make(chan string)

	// 2. Deux goroutines "à côté" qui rempliront chacune leur tuyau.
	//    La première attend 50 ms, la seconde 200 ms : la course est jouée
	//    d'avance, donc la SORTIE est DÉTERMINISTE (toujours la même).
	go func() {
		time.Sleep(50 * time.Millisecond)
		rapide <- "message du guichet RAPIDE"
	}()
	go func() {
		time.Sleep(200 * time.Millisecond)
		lent <- "message du guichet LENT"
	}()

	// 3. PREMIER select : on surveille les DEUX guichets.
	//    `select` BLOQUE jusqu'à ce qu'un cas soit prêt, puis exécute CE cas.
	//    Comme "rapide" répond après 50 ms et "lent" après 200 ms, c'est
	//    TOUJOURS le cas "rapide" qui gagne.
	fmt.Println("--- Course entre deux guichets ---")
	select {
	case msg := <-rapide: // si "rapide" a quelque chose, on le reçoit ici
		fmt.Printf("Premier prêt : %s\n", msg)
	case msg := <-lent: // sinon, si "lent" répond d'abord (pas le cas ici)
		fmt.Printf("Premier prêt : %s\n", msg)
	}

	// 4. DEUXIÈME select : un TIMEOUT.
	//    On attend un tuyau "trainard" qui ne répondra qu'après 300 ms,
	//    mais on n'accepte de patienter que 100 ms grâce à time.After.
	//    100 ms < 300 ms, donc c'est TOUJOURS le timeout qui se déclenche.
	trainard := make(chan string)
	go func() {
		time.Sleep(300 * time.Millisecond)
		trainard <- "réponse arrivée trop tard"
	}()

	fmt.Println("--- Attente avec un délai maximum (timeout) ---")
	select {
	case msg := <-trainard: // si la réponse arrive à temps (pas le cas ici)
		fmt.Printf("Reçu : %s\n", msg)
	case <-time.After(100 * time.Millisecond): // sinon : la minuterie "sonne"
		fmt.Println("Timeout : personne n'a répondu en 100 ms, on abandonne.")
	}
}
