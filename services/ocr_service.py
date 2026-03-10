from pdf2image import convert_from_bytes
import pytesseract
from pypdf import PdfReader
import io


def extract_text(pdf_bytes, company):

    if company.lower() == "premium":
        return extract_text_direct(pdf_bytes)

    return extract_text_ocr(pdf_bytes)


def extract_text_direct(pdf_bytes):

    reader = PdfReader(io.BytesIO(pdf_bytes))

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def extract_text_ocr(pdf_bytes):

    images = convert_from_bytes(pdf_bytes)

    text = ""

    for img in images:
        text += pytesseract.image_to_string(img)

    return text