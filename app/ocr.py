# app/ocr.py

import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import tempfile

def extraire_texte(fichier):
    texte_total = ""

    # Si PDF : on convertit en images
    if fichier.type == "application/pdf":
        images = convert_from_bytes(fichier.read())
    else:
        image = Image.open(fichier)
        images = [image]

    # Extraction OCR pour chaque page/image
    for img in images:
        texte = pytesseract.image_to_string(img, lang='fra')  # 'fra' pour le français
        texte_total += texte + "\n"

    return texte_total
