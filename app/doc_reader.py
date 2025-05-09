import fitz  # PyMuPDF
import docx
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
import io

def extract_text_pdf_native(file_bytes):
    """
    Tente d'extraire le texte directement depuis un PDF non-scanné
    """
    try:
        pdf = fitz.open(stream=file_bytes, filetype="pdf")
        return "\n".join(page.get_text() for page in pdf)
    except Exception as e:
        print(f"[Erreur extraction PDF native] {e}")
        return ""

def extract_text_pdf_ocr(file_bytes):
    """
    Applique l'OCR sur un PDF scanné (pages image)
    """
    try:
        images = convert_from_bytes(file_bytes)
        texte = ""
        for image in images:
            if isinstance(image, Image.Image):
                texte += pytesseract.image_to_string(image, lang="fra") + "\n"
        return texte
    except Exception as e:
        print(f"[Erreur OCR PDF] {e}")
        return ""

def extract_text_docx(file):
    """
    Extrait le texte d'un document Word (.docx)
    """
    try:
        doc = docx.Document(file)
        return "\n".join(para.text for para in doc.paragraphs)
    except Exception as e:
        print(f"[Erreur extraction DOCX] {e}")
        return ""

def detect_type_and_extract(file):
    """
    Détecte le type de fichier et applique la méthode d'extraction appropriée
    """
    file_bytes = file.getvalue()

    if file.name.lower().endswith(".pdf"):
        text = extract_text_pdf_native(file_bytes)
        if text.strip():  # Si du texte a bien été extrait
            return text
        else:
            return extract_text_pdf_ocr(file_bytes)

    elif file.name.lower().endswith(".docx"):
        return extract_text_docx(file)

    else:
        return ""
