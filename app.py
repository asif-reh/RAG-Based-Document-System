import streamlit as st
import os
import sys

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.extract_pdf import extract_text_from_pdf
from src.store_embeddings import store_embeddings
from src.rag_pipeline import setup_rag_pipeline

st.set_page_config(page_title="RAG Document Q&A System", page_icon="📚", layout="wide")

st.title("📚 RAG-Based Document Q&A System")
st.markdown("Upload a PDF document and ask questions about its content using **Docling** for advanced document processing!")

# Initialize session state
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = None
if 'processed_file' not in st.session_state:
    st.session_state.processed_file = None

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and uploaded_file != st.session_state.processed_file:
    with st.spinner("🔄 Processing document with Docling..."):
        try:
            # Extract text using Docling
            text = extract_text_from_pdf(uploaded_file)
            
            if text and not text.startswith("Error"):
                st.success("✅ Document processed successfully with Docling!")
                
                # Show document preview
                with st.expander("📄 Document Preview"):
                    preview_text = text[:2000] + "..." if len(text) > 2000 else text
                    st.markdown(preview_text)
                
                # Store embeddings
                with st.spinner("🧠 Creating embeddings..."):
                    try:
                        st.session_state.vectorstore = store_embeddings(text)
                        st.session_state.qa_chain = setup_rag_pipeline()
                        st.session_state.processed_file = uploaded_file
                        st.success("✅ Embeddings created! You can now ask questions.")
                        
                        # Show document stats
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Document Length", f"{len(text):,} chars")
                        with col2:
                            word_count = len(text.split())
                            st.metric("Word Count", f"{word_count:,} words")
                        with col3:
                            st.metric("Processing", "Complete ✅")
                            
                    except Exception as e:
                        st.error(f"❌ Error creating embeddings: {str(e)}")
                        st.info("💡 This might be due to memory limitations or dependency issues.")
            else:
                st.error(f"❌ Failed to extract text: {text}")
                st.info("💡 Make sure you uploaded a valid PDF file. Docling works best with text-based PDFs.")
                
        except Exception as e:
            st.error(f"❌ Error processing document: {str(e)}")
            st.info("💡 If this persists, the document might be too complex or corrupted.")

# Query interface
if st.session_state.qa_chain:
    st.markdown("---")
    st.subheader("💬 Ask Questions About Your Document")
    
    # Sample questions
    with st.expander("💡 Example Questions"):
        st.markdown("""
        - What is the main topic of this document?
        - Can you summarize the key points?
        - What are the conclusions or recommendations?
        - Are there any important dates or numbers mentioned?
        - What problems does this document address?
        """)
    
    query = st.text_input(
        "Ask a question about the document:", 
        placeholder="What is this document about?",
        help="Type your question and press Enter"
    )
    
    if query:
        with st.spinner("🤔 Generating answer..."):
            try:
                result = st.session_state.qa_chain({"query": query})
                
                st.markdown("### 🤖 Answer:")
                st.write(result["result"])
                
                if result.get("source_documents"):
                    st.markdown("### 📄 Source Context:")
                    for i, doc in enumerate(result["source_documents"], 1):
                        with st.expander(f"📄 Source {i}"):
                            content = getattr(doc, 'page_content', str(doc))
                            st.write(content[:800] + "..." if len(content) > 800 else content)
                            
            except Exception as e:
                st.error(f"❌ Error generating answer: {str(e)}")
                st.info("💡 Try rephrasing your question or check if the document was processed correctly.")

else:
    if not uploaded_file:
        st.info("👆 Please upload a PDF document to get started!")
        
        # Add feature highlights
        st.markdown("### 🚀 Powered by Docling")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **📄 Advanced PDF Processing**
            - Layout analysis
            - Table extraction
            - Figure recognition
            """)
            
        with col2:
            st.markdown("""
            **🧠 AI-Powered Q&A**
            - Contextual answers
            - Source attribution
            - Multiple retrieval
            """)
            
        with col3:
            st.markdown("""
            **⚡ Features**
            - Fast processing
            - High accuracy
            - Rich document understanding
            """)
    
        # Usage instructions
        with st.expander("ℹ️ How to use this app"):
            st.markdown("""
            1. **Upload a PDF**: Click the upload button above and select your PDF file
            2. **Wait for processing**: Docling will analyze the document structure and extract text
            3. **Ask questions**: Type your question in the input box
            4. **Get answers**: The AI will provide answers based on your document content with source references
            
            **Supported file types**: PDF files only
            **Best results**: Works with all types of PDFs including complex layouts, tables, and figures
            **Powered by**: Docling for document processing + LangChain for AI capabilities
            """)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using **Docling**, **LangChain**, and **Streamlit**") 