import os
import textract  # Pour les formats complexes (optionnel)
from PyPDF2 import PdfReader  # Pour lire le contenu textuel des PDF
from docx import Document  # Pour lire les .docx
from app.ocr import extraire_texte_pdf_scane  # Pour OCR si PDF est scanné

def detect_type_and_extract(fichier):
    filename = fichier.name.lower()  # Récupère le nom de fichier en minuscule

    if filename.endswith(".pdf"):
        try:
            # Essaye de lire le texte d’un PDF "natif"
            reader = PdfReader(fichier)
            texte = "\n".join([page.extract_text() or "" for page in reader.pages])

            # Si texte vide, probablement scanné => OCR
            if not texte.strip():
                fichier.seek(0)  # Revenir au début du fichier
                texte = extraire_texte_pdf_scane(fichier)
        except:
            # Si erreur, tente OCR quand même
            fichier.seek(0)
            texte = extraire_texte_pdf_scane(fichier)
        return texte

    elif filename.endswith(".docx"):
        # Lecture standard d’un document Word
        doc = Document(fichier)
        texte = "\n".join([para.text for para in doc.paragraphs])
        return texte

    else:
        # Format non reconnu
        raise ValueError("Format non pris en charge. Veuillez fournir un PDF ou DOCX.")
