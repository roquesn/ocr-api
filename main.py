from fastapi import FastAPI, UploadFile, File, Form
from services.ocr_service import extract_text
from services.parser_service import parse_document

app = FastAPI()


@app.post("/extract-document")
async def extract_document(
    file: UploadFile = File(...),
    company: str = Form(...)
):

    pdf_bytes = await file.read()

    text = extract_text(pdf_bytes, company)

    data = parse_document(text, company)

    return data