import os
import mimetypes
from typing import Optional
from io import BytesIO

# Pour lire les fichiers DOCX
from docx import Document

# Pour extraire du texte depuis des PDF natifs
import fitz  # PyMuPDF

# Pour gérer les PDF scannés (OCR)
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image


def extract_text_from_docx(file: BytesIO) -> str:
    """Lecture simple d’un fichier DOCX"""
    doc = Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])


def extract_text_from_pdf(file: BytesIO) -> str:
    """Extraction de texte depuis un PDF avec PyMuPDF"""
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()


def extract_text_from_scanned_pdf(file: BytesIO) -> str:
    """OCR sur un PDF scanné (image en PDF)"""
    images = convert_from_bytes(file.read())
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text.strip()


def extract_text(file: BytesIO, filename: str) -> Optional[str]:
    """
    Fonction principale appelée par l’interface.
    Détecte le type de fichier et applique la méthode d’extraction appropriée.
    """
    file.seek(0)
    ext = os.path.splitext(filename)[1].lower()

    try:
        if ext == ".docx":
            return extract_text_from_docx(file)
        elif ext == ".pdf":
            # Tentative d’extraction directe (texte natif)
            text = extract_text_from_pdf(BytesIO(file.read()))
            if len(text.strip()) < 20:  # Texte trop court → probablement un scan
                file.seek(0)
                return extract_text_from_scanned_pdf(file)
            return text
        else:
            return "❌ Format non supporté. Veuillez utiliser un fichier PDF ou DOCX."
    except Exception as e:
        return f"⚠️ Erreur lors de l’extraction du texte : {str(e)}"
