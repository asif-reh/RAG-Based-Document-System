from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from transformers.pipelines import pipeline
import torch

def setup_rag_pipeline(persist_directory="./chroma_db"):
    # Load embeddings and vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Connect to ChromaDB
    client = chromadb.PersistentClient(path=persist_directory)
    collection = client.get_or_create_collection("documents")
    
    # Initialize a simple text generation pipeline
    device = 0 if torch.cuda.is_available() else -1
    text_generator = pipeline(
        "text-generation", 
        model="microsoft/DialoGPT-small",
        device=device,
        max_length=200,
        temperature=0.7,
        do_sample=True
    )
    
    def qa_chain(query_dict):
        query = query_dict["query"]
        
        # Get query embedding
        query_embedding = embeddings.embed_query(query)
        
        # Search for relevant documents
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )
        
        # Combine retrieved documents
        context = "\n".join(results["documents"][0]) if results["documents"] else ""
        
        # Generate answer
        prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
        response = text_generator(prompt, max_new_tokens=100)
        answer = response[0]["generated_text"].split("Answer:")[-1].strip()
        
        # Format source documents
        source_docs = []
        if results["documents"]:
            for doc in results["documents"][0]:
                source_docs.append(type('Document', (), {'page_content': doc})())
        
        return {
            "result": answer,
            "source_documents": source_docs
        }
    
    return qa_chain

if __name__ == "__main__":
    qa_chain = setup_rag_pipeline()
    query = "What is the main topic of the document?"
    result = qa_chain({"query": query})
    print(result["result"])