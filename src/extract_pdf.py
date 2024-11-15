import PyPDF2
from pathlib import Path
import io

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using PyPDF2 (more reliable for cloud deployment)"""
    try:
        text = ""
        
        # Handle both file path and file-like objects
        if isinstance(pdf_path, (str, Path)):
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n"
        else:
            # Handle file-like objects (uploaded files)
            pdf_reader = PyPDF2.PdfReader(pdf_path)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
        
        return text.strip()
    
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

if __name__ == "__main__":
    pdf_path = "sample_document.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    with open("extracted_text.txt", "w", encoding='utf-8') as f:
        f.write(extracted_text)