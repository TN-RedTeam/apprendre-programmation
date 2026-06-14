"""
MODULE 09 (avancé) - Concurrence avec asyncio (async / await)
=============================================================
Même idée que threads.py (occuper les temps d'attente), mais avec asyncio :
UN SEUL thread jongle entre les tâches, comme un serveur de restaurant qui
s'occupe de plusieurs tables sans en laisser aucune attendre pour rien.

Lance-le :  python3 python/automatisation/09_concurrence/async_demo.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS   : asyncio (la boîte à outils de concurrence) + time (mesure).
   2. COROUTINE : telecharger(page) est une 'async def' ; elle 'await' une
                  attente sans bloquer les autres.
   3. main()    : asyncio.gather lance toutes les coroutines EN MÊME TEMPS.
   4. DÉMARRAGE : asyncio.run(main()) lance la boucle puis s'arrête.
"""

import asyncio
import time

PAGES = ["page1", "page2", "page3", "page4", "page5"]
DUREE_PAR_PAGE = 0.5


# 'async def' déclare une COROUTINE : une fonction qui sait se mettre en pause
# (au 'await') pour laisser les autres avancer pendant qu'elle attend.
async def telecharger(page):
    """Simule un téléchargement asynchrone (une tâche qui attend)."""
    # await asyncio.sleep(...) = l'attente "polie" : pendant ce temps, les
    # autres coroutines peuvent progresser. (≠ time.sleep qui, lui, bloquerait tout.)
    await asyncio.sleep(DUREE_PAR_PAGE)
    return f"contenu de {page}"


async def main():
    debut = time.perf_counter()

    # asyncio.gather LANCE toutes les coroutines en même temps et attend qu'elles
    # soient TOUTES finies. Les résultats reviennent DANS L'ORDRE donné (déterministe).
    # L'astérisque * déplie la liste de coroutines en arguments séparés.
    resultats = await asyncio.gather(*(telecharger(p) for p in PAGES))

    duree = time.perf_counter() - debut
    print(f"{len(PAGES)} pages téléchargées en {duree:.1f} s (au lieu de "
          f"{len(PAGES) * DUREE_PAR_PAGE:.1f} s en séquentiel)")
    print(f"Résultats : {resultats}")


if __name__ == "__main__":
    # asyncio.run() est le POINT D'ENTRÉE : il démarre la boucle asyncio,
    # exécute la coroutine main(), puis referme tout proprement.
    asyncio.run(main())
