"""
MODULE 09 (avancé) - Concurrence avec ThreadPoolExecutor
========================================================
On simule le téléchargement de plusieurs pages (des tâches qui ATTENDENT).
On compare le temps en SÉQUENTIEL (une après l'autre) au temps en PARALLÈLE
(toutes lancées en même temps) pour voir le gain.

Lance-le :  python3 python/automatisation/09_concurrence/threads.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS   : time (mesurer/simuler l'attente) + ThreadPoolExecutor.
   2. FONCTION  : telecharger(page) attend un peu (simule le réseau) puis
                  renvoie un faux contenu.
   3. SÉQUENTIEL: on télécharge les pages une par une et on mesure le temps.
   4. PARALLÈLE : on relance tout via un ThreadPoolExecutor et on mesure.
   5. BILAN     : on affiche les deux durées pour comparer.
"""

import time
from concurrent.futures import ThreadPoolExecutor

# La liste des "pages" à télécharger (juste des noms, pour la démo).
PAGES = ["page1", "page2", "page3", "page4", "page5"]

# Chaque téléchargement simulé prend ce temps (en secondes).
DUREE_PAR_PAGE = 0.5


def telecharger(page):
    """Simule le téléchargement d'une page : ça ATTEND, ça ne calcule pas."""
    # time.sleep met la tâche en pause : c'est notre "attente réseau".
    # Pendant ce sommeil, un autre thread peut avancer (le GIL est relâché).
    time.sleep(DUREE_PAR_PAGE)
    return f"contenu de {page}"


if __name__ == "__main__":
    # ─── 1. SÉQUENTIEL : une page après l'autre ───
    # perf_counter() renvoie un instant précis ; la différence = la durée écoulée.
    debut = time.perf_counter()
    resultats_seq = []
    for page in PAGES:
        resultats_seq.append(telecharger(page))   # on attend 0.5 s à CHAQUE tour
    duree_seq = time.perf_counter() - debut
    print(f"Séquentiel : {len(PAGES)} pages en {duree_seq:.1f} s")

    # ─── 2. PARALLÈLE : toutes les pages "en même temps" ───
    debut = time.perf_counter()
    # 'with ... as executor' ouvre une équipe de threads puis la referme proprement.
    with ThreadPoolExecutor() as executor:
        # .map applique telecharger à CHAQUE page en parallèle, et renvoie les
        # résultats DANS L'ORDRE de la liste d'entrée (donc résultat déterministe).
        resultats_par = list(executor.map(telecharger, PAGES))
    duree_par = time.perf_counter() - debut
    print(f"Parallèle  : {len(PAGES)} pages en {duree_par:.1f} s")

    # ─── 3. BILAN ───
    # Comme les attentes se chevauchent, le parallèle est proche de 0.5 s
    # (la durée d'UNE page) au lieu de 2.5 s.
    print(f"\nRésultats  : {resultats_par}")
    print(f"Gain       : environ {duree_seq / duree_par:.1f}x plus rapide 🚀")
