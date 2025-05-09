import re

def anonymiser_texte(texte, entites):
    # Pour chaque entité détectée, on la remplace par un tag anonymisé
    for entite, label in entites:
        # Nettoie le nom de l’étiquette pour qu’il soit utilisable dans le texte
        safe_label = re.sub(r'\W+', '_', label.upper())
        # Remplace toutes les occurrences de l’entité par le tag [LABEL]
        texte = texte.replace(entite, f"[{safe_label}]")
    return texte
