from app.ui import afficher_interface

import spacy
import subprocess

# Charge ou télécharge le modèle spaCy en français
try:
    spacy.load("fr_core_news_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "fr_core_news_sm"])



if __name__ == "__main__":
    afficher_interface()  # Lance l’interface Streamlit
