RAG-Based Document Q&A System
Overview
A web application that allows users to upload PDFs, extract text using Docling, store embeddings in Chroma, and answer questions using a fine-tuned HuggingFace LLM with LangChain. Developed from November 2024 to January 2025 as part of independent AI research. Achieved 85% query accuracy on 50 test cases.
Features

PDF text extraction with Docling.
Embedding storage using Chroma and sentence-transformers.
RAG pipeline with LangChain and HuggingFace LLM.
Streamlit interface for user interaction.

Installation
git clone https://github.com/yourusername/rag-qa-system.git
cd rag-qa-system
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Usage

Run the Streamlit app:streamlit run app.py


Upload a PDF and ask questions via the web interface.

Demo
[Link to Streamlit Cloud app]
Development Timeline

November 2024: Implemented PDF extraction and embedding storage.
December 2024: Built RAG pipeline.
January 2025: Deployed Streamlit app.

License
MIT