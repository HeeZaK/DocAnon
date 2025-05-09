import fitz  # PyMuPDF
import docx
from pdf2image import convert_from_bytes
import pytesseract

def extract_text_pdf_native(file_bytes):
    """
    Tente d'extraire le texte directement depuis un PDF (s'il n'est pas scanné)
    """
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    return "\n".join([page.get_text() for page in pdf])

def extract_text_pdf_ocr(file_bytes):
    """
    Utilise l'OCR sur les pages scannées du PDF
    """
    images = convert_from_bytes(file_bytes)
    texte = ""
    for image in images:
        texte += pytesseract.image_to_string(image) + "\n"
    return texte

def extract_text_docx(file):
    """
    Extrait le texte d'un document Word (.docx)
    """
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def detect_type_and_extract(file):
    """
    Détecte le type de fichier et applique la méthode d'extraction appropriée
    """
    if file.name.endswith(".pdf"):
        try:
            return extract_text_pdf_native(file.read())
        except:
            file.seek(0)
            return extract_text_pdf_ocr(file.read())
    elif file.name.endswith(".docx"):
        return extract_text_docx(file)
    else:
        return ""
