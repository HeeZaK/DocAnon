import spacy  # Librairie NLP

# Charge un modèle français avec reconnaissance d'entités
nlp = spacy.load("fr_core_news_md")

def detecter_entites(texte):
    doc = nlp(texte)  # Analyse le texte avec spaCy
    # Renvoie une liste de tuples : (texte de l'entité, type)
    return [(ent.text, ent.label_) for ent in doc.ents]
