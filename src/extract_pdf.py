from docling.document_converter import DocumentConverter
from pathlib import Path
import tempfile
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using Docling with enhanced compatibility"""
    try:
        converter = DocumentConverter()
        
        # Handle both file paths and file-like objects
        if hasattr(pdf_path, 'read'):
            # Handle uploaded file objects from Streamlit
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(pdf_path.getvalue())
                tmp_path = tmp_file.name
            
            try:
                result = converter.convert(tmp_path)
                text = result.document.export_to_markdown()
                return text
            finally:
                # Clean up temporary file
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
        else:
            # Handle file paths
            source = Path(pdf_path)
            result = converter.convert(source)
            text = result.document.export_to_markdown()
            return text
            
    except Exception as e:
        return f"Error extracting text from PDF with Docling: {str(e)}"

if __name__ == "__main__":
    pdf_path = "sample_document.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    with open("extracted_text.txt", "w", encoding='utf-8') as f:
        f.write(extracted_text)