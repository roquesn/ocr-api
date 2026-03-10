import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")