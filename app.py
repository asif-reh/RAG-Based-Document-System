import streamlit as st
import os
import sys

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
        # Save uploaded file
        temp_path = "temp.pdf"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Extract text
        try:
            text = extract_text_from_pdf(temp_path)
            st.success("✅ Document processed successfully!")
            
            # Show document preview
            with st.expander("Document Preview"):
                st.text(text[:1000] + "..." if len(text) > 1000 else text)
            
            # Store embeddings
            with st.spinner("Creating embeddings..."):
                st.session_state.vectorstore = store_embeddings(text)
                st.session_state.qa_chain = setup_rag_pipeline()
            
            st.success("✅ Embeddings created! You can now ask questions.")
            
        except Exception as e:
            st.error(f"Error processing document: {str(e)}")
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)

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
                
                if result["source_documents"]:
                    st.markdown("### 📄 Source Context:")
                    for i, doc in enumerate(result["source_documents"], 1):
                        with st.expander(f"Source {i}"):
                            st.write(doc.page_content[:500] + "..." if len(doc.page_content) > 500 else doc.page_content)
            except Exception as e:
                st.error(f"Error generating answer: {str(e)}")

else:
    st.info("👆 Please upload a PDF document to get started!") 