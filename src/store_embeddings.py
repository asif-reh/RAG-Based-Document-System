from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from langchain.docstore.document import Document



def store_embeddings(text, persist_directory="./chroma_db"):
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    
    # Generate embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create ChromaDB client
    client = chromadb.PersistentClient(path=persist_directory)
    collection = client.get_or_create_collection("documents")
    
    # Store embeddings
    for i, chunk in enumerate(chunks):
        embedding = embeddings.embed_query(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(i)]
        )
    
    return collection

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as f:
        text = f.read()
    vectorstore = store_embeddings(text)