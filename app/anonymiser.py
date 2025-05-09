# app/anonymiser.py

def anonymiser_texte(texte, entites):
    texte_anonymise = texte
    deja_vu = set()

    for ent, label in entites:
        if ent in deja_vu:
            continue
        deja_vu.add(ent)

        # Remplacer toutes les occurrences de cette entité par un tag
        tag = f"[ANON:{label}]"
        texte_anonymise = texte_anonymise.replace(ent, tag)

    return texte_anonymise
