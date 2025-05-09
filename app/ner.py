# app/ner.py

import spacy

# Chargement du modèle de langue français
nlp = spacy.load("fr_core_news_md")

def detecter_entites(texte):
    doc = nlp(texte)
    entites = []

    for ent in doc.ents:
        if ent.label_ in ["PER", "LOC", "GPE"]:  # PER = personne, LOC = lieu, GPE = pays/villes
            entites.append((ent.text, ent.label_))

    return entites
