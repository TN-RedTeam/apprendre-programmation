/*
 * MODULE 09 - WORKER POOL (un "pool de travailleurs")
 * ===================================================
 * Imagine une PILE de tickets à traiter et une ÉQUIPE qui se les partage :
 * chaque membre prend un ticket, le traite, prend le suivant... jusqu'à ce
 * que la pile soit vide. C'est le motif WORKER POOL.
 *
 * 🎫 ANALOGIE. Un channel "jobs" = la pile de tickets à faire. N goroutines
 * "travailleuses" (les workers) y piochent un ticket chacune à leur tour. Le
 * résultat de chaque ticket part dans un channel "résultats" où on le collecte.
 * Plusieurs mains se partagent la même pile : le travail va plus vite, sans
 * que deux personnes traitent le même ticket (le channel s'en occupe).
 *
 * On réutilise les outils du module 06 :
 *   - les CHANNELS (`chan`) pour distribuer les jobs et remonter les résultats ;
 *   - un `sync.WaitGroup` pour ATTENDRE que TOUS les workers aient fini.
 *
 * Ici : 3 workers traitent 9 jobs (élever un nombre au carré), on collecte
 * tous les carrés et on en fait la SOMME. Résultat DÉTERMINISTE : peu importe
 * QUEL worker traite QUEL job, la somme des carrés de 1..9 est toujours 285.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer DEPUIS LA RACINE du dépôt :
 *     go run go/09_concurrence_avancee/worker_pool.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer deux tuyaux : "jobs" (les nombres à traiter) et "resultats".
 *   2. Démarrer 3 workers : chacun lit dans "jobs" et écrit dans "resultats".
 *   3. Envoyer les 9 jobs (1..9) dans "jobs", puis FERMER "jobs".
 *   4. Une goroutine attend la fin des workers (WaitGroup) puis ferme "resultats".
 *   5. main collecte tous les résultats avec `range` et en fait la somme.
 *   6. Afficher la somme totale (toujours 285).
 */

package main

import (
	"fmt"  // affichage (Println, Printf)
	"sync" // WaitGroup : attendre que toutes les goroutines aient fini
)

// worker = un membre de l'équipe.
//   - id        : son numéro, juste pour l'affichage.
//   - jobs      : tuyau OÙ IL PIOCHE les nombres à traiter (<-chan = lecture seule).
//   - resultats : tuyau OÙ IL DÉPOSE les carrés (chan<- = écriture seule).
//   - wg        : le compteur partagé pour signaler "j'ai fini" à la fin.
func worker(id int, jobs <-chan int, resultats chan<- int, wg *sync.WaitGroup) {
	// defer wg.Done() : quoi qu'il arrive, on signale notre fin en sortant.
	defer wg.Done()

	// `for n := range jobs` : pioche un job à chaque tour ; s'arrête TOUT SEUL
	// quand "jobs" est fermé ET vide. Si deux workers lisent le même tuyau,
	// chaque valeur n'est livrée qu'à UN SEUL d'entre eux (pas de doublon).
	for n := range jobs {
		carre := n * n
		fmt.Printf("worker %d : %d au carré = %d\n", id, n, carre)
		resultats <- carre // on dépose le résultat dans le tuyau de sortie
	}
}

func main() {

	const nbWorkers = 3 // taille de l'équipe
	const nbJobs = 9    // nombre de tickets à traiter (les nombres 1..9)

	// 1. CRÉER les deux tuyaux. On leur donne une petite réserve (buffer) de
	//    taille nbJobs pour que les envois ne bloquent pas inutilement.
	jobs := make(chan int, nbJobs)
	resultats := make(chan int, nbJobs)

	// Le compteur qui nous dira quand TOUS les workers auront terminé.
	var wg sync.WaitGroup

	// 2. DÉMARRER les workers. Add(1) AVANT de lancer chaque goroutine.
	for id := 1; id <= nbWorkers; id++ {
		wg.Add(1)
		go worker(id, jobs, resultats, &wg)
	}

	// 3. ENVOYER tous les jobs (1, 2, ..., 9) puis FERMER "jobs".
	//    Fermer dit aux workers : "plus de tickets, finissez et arrêtez-vous".
	for n := 1; n <= nbJobs; n++ {
		jobs <- n
	}
	close(jobs)

	// 4. Une goroutine "fermeuse" : elle attend que les 3 workers aient fini
	//    (wg.Wait), PUIS ferme "resultats". Sans elle, le `range` du point 5
	//    attendrait pour toujours (le tuyau ne serait jamais fermé).
	go func() {
		wg.Wait()
		close(resultats)
	}()

	// 5. COLLECTER : on reçoit chaque carré et on l'ajoute à la somme.
	//    Le `range` s'arrête seul quand "resultats" est fermé (point 4).
	somme := 0
	for carre := range resultats {
		somme += carre
	}

	// 6. BILAN. Somme des carrés de 1 à 9 = 1+4+9+16+25+36+49+64+81 = 285.
	//    Toujours le même total, quel que soit l'ordre de traitement.
	fmt.Printf("Somme des carrés de 1 à %d = %d\n", nbJobs, somme)
}
