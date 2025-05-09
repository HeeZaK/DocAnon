import fitz  # PyMuPDF
import docx
from pdf2image import convert_from_bytes
import pytesseract

def extract_text_pdf_native(file_bytes):
    """
    Extraction directe du texte (PDF non scanné).
    """
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    return "\n".join([page.get_text() for page in pdf])

def extract_text_pdf_ocr(file_bytes):
    """
    Extraction par OCR (PDF scanné).
    """
    images = convert_from_bytes(file_bytes)
    return "\n".join(pytesseract.image_to_string(image) for image in images)

def extract_text_docx(file):
    """
    Extraction depuis un document Word.
    """
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def detect_type_and_extract(file):
    """
    Détecte le type de fichier et applique l'extraction.
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
