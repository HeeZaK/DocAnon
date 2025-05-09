import re
import spacy

# Chargement du modèle français
def load_spacy_model():
    try:
        return spacy.load("fr_core_news_sm")
    except OSError:
        raise RuntimeError(
            "Le modèle spaCy 'fr_core_news_sm' est manquant. "
            "Ajoutez-le à requirements.txt ou installez-le avec : "
            "python -m spacy download fr_core_news_sm"
        )

nlp = load_spacy_model()

def detect_entities_with_offsets(text):
    """
    Détecte les entités sensibles (NLP + regex).
    """
    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        if ent.label_ in ["PER", "ORG", "LOC", "DATE"]:
            entities.append((ent.label_, ent.start_char, ent.end_char))

    regex_patterns = {
        "EMAIL": r"[\w\.-]+@[\w\.-]+",
        "TEL": r"\+?\d[\d\s\-]{7,}\d"
    }

    for label, pattern in regex_patterns.items():
        for match in re.finditer(pattern, text):
            entities.append((label, match.start(), match.end()))

    return entities

def anonymiser_texte(text):
    """
    Remplace les entités par des balises [ANONYME-...].
    """
    entities = detect_entities_with_offsets(text)
    for label, start, end in sorted(entities, key=lambda x: -x[1]):
        text = text[:start] + f"[ANONYME-{label}]" + text[end:]
    return text
