from pdf2image import convert_from_bytes  # Convertit un PDF en images (1 image/page)
import pytesseract  # Utilisé pour faire l'OCR sur chaque image

def extraire_texte_pdf_scane(fichier_pdf):
    # Convertit les pages du PDF (en mémoire) en images
    images = convert_from_bytes(fichier_pdf.read())

    texte = ""
    for image in images:
        # OCR pour chaque image, avec reconnaissance du français
        texte += pytesseract.image_to_string(image, lang="fra") + "\n"

    return texte  # Renvoie tout le texte reconnu dans le PDF
