import streamlit as st
import os
import sys
import io

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.extract_pdf import extract_text_from_pdf
from src.store_embeddings import store_embeddings
from src.rag_pipeline import setup_rag_pipeline

st.set_page_config(page_title="Document Q&A System", page_icon="📚", layout="wide")

st.title("📚 RAG-Based Document Q&A System")
st.markdown("Upload a PDF document and ask questions about its content!")

# Initialize session state
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = None

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing document..."):
        try:
            # Extract text directly from uploaded file
            text = extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
            
            if text and not text.startswith("Error"):
                st.success("✅ Document processed successfully!")
                
                # Show document preview
                with st.expander("Document Preview"):
                    st.text(text[:1000] + "..." if len(text) > 1000 else text)
                
                # Store embeddings
                with st.spinner("Creating embeddings..."):
                    try:
                        st.session_state.vectorstore = store_embeddings(text)
                        st.session_state.qa_chain = setup_rag_pipeline()
                        st.success("✅ Embeddings created! You can now ask questions.")
                    except Exception as e:
                        st.error(f"Error creating embeddings: {str(e)}")
                        st.info("💡 Try with a smaller document or check if all dependencies are installed.")
            else:
                st.error(f"Failed to extract text: {text}")
                
        except Exception as e:
            st.error(f"Error processing document: {str(e)}")
            st.info("💡 Make sure you uploaded a valid PDF file.")

# Query interface
if st.session_state.qa_chain:
    st.markdown("---")
    st.subheader("💬 Ask Questions")
    
    query = st.text_input("Ask a question about the document:", placeholder="What is this document about?")
    
    if query:
        with st.spinner("Generating answer..."):
            try:
                result = st.session_state.qa_chain({"query": query})
                
                st.markdown("### 🤖 Answer:")
                st.write(result["result"])
                
                if result.get("source_documents"):
                    st.markdown("### 📄 Source Context:")
                    for i, doc in enumerate(result["source_documents"], 1):
                        with st.expander(f"Source {i}"):
                            content = getattr(doc, 'page_content', str(doc))
                            st.write(content[:500] + "..." if len(content) > 500 else content)
            except Exception as e:
                st.error(f"Error generating answer: {str(e)}")
                st.info("💡 Try rephrasing your question or check if the document was processed correctly.")

else:
    st.info("👆 Please upload a PDF document to get started!")
    
    # Add some helpful information
    with st.expander("ℹ️ How to use this app"):
        st.markdown("""
        1. **Upload a PDF**: Click the upload button above and select your PDF file
        2. **Wait for processing**: The app will extract text and create embeddings
        3. **Ask questions**: Type your question in the input box
        4. **Get answers**: The AI will provide answers based on your document content
        
        **Supported file types**: PDF files only
        **Best results**: Clear, text-based PDFs work better than scanned images
        """) 