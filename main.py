from app.ui import afficher_interface

import spacy
import subprocess

# Télécharger le modèle français si pas installé
try:
    spacy.load("fr_core_news_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "fr_core_news_sm"])


if __name__ == "__main__":
    afficher_interface()  # Lance l’interface Streamlit
