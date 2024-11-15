from docling.document_converter import DocumentConverter
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    converter = DocumentConverter()
    source = Path(pdf_path)
    result = converter.convert(source)
    text = result.document.export_to_markdown()
    return text

if __name__ == "__main__":
    pdf_path = "sample_document.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    with open("extracted_text.txt", "w") as f:
        f.write(extracted_text)