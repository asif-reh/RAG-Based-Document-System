import pytest
from src.extract_pdf import extract_text_from_pdf
from src.store_embeddings import store_embeddings
from src.rag_pipeline import setup_rag_pipeline

def test_pdf_extraction():
    text = extract_text_from_pdf("sample_document.pdf")
    assert isinstance(text, str) and len(text) > 0, "PDF extraction failed"

def test_embedding_storage():
    with open("extracted_text.txt", "w") as f:
        f.write("This is a test document.")
    vectorstore = store_embeddings("This is a test document.")
    assert vectorstore is not None, "Embedding storage failed"

def test_rag_pipeline():
    qa_chain = setup_rag_pipeline()
    result = qa_chain({"query": "What is the main topic?"})
    assert "result" in result and len(result["result"]) > 0, "RAG pipeline failed"

if __name__ == "__main__":
    pytest.main()