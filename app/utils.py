# app/utils.py

import os
from datetime import datetime

def sauvegarder_texte_anonymise(texte, nom_fichier=None, dossier="outputs/anonymised_texts/"):
    if not os.path.exists(dossier):
        os.makedirs(dossier)

    if not nom_fichier:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = f"anonymise_{timestamp}.txt"

    chemin_complet = os.path.join(dossier, nom_fichier)

    with open(chemin_complet, "w", encoding="utf-8") as f:
        f.write(texte)

    return chemin_complet
