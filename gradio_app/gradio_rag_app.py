
import os
import argparse
import gradio as gr
import openai
from faiss_helper import load_or_build_index
import json
from langchain_core.documents import Document

# -- tiny "vector store" (dict of doc: context). Replace with real DB later --
DOCS = {
    "What is RAG?" : "Retrieval‑Augmented Generation (RAG) combines LLMs with a retrieval component to ground answers in external data.",
    "Who created Python?" : "Python was created by Guido van Rossum and first released in 1991.",
}

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

# Global FAISS index populated at runtime
INDEX = None

def retrieve(query: str, k: int = 1):
    """Search the FAISS index for relevant documents."""
    if INDEX is None:
        raise ValueError("FAISS index not initialized")
    results = INDEX.similarity_search(query, k=k)
    return [doc.page_content for doc in results]

def process_uploaded_file(file_path) -> str:
    """Process uploaded file and return its content."""
    if file_path is None:
        return "No file uploaded"
    
    try:
        # Read file content
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        elif file_path.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                content = json.dumps(data, indent=2)
        else:
            # For other file types, try to read as text
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"

def add_document_to_index(content: str, title: str = "Uploaded Document") -> str:
    """Add a new document to the FAISS index."""
    global INDEX
    if not content.strip():
        return "No content to add"
    
    try:
        from faiss_helper import get_embeddings
        
        # Create a new document
        doc = Document(page_content=content, metadata={"title": title})
        
        # Add to existing index
        INDEX.add_documents([doc])
        
        return f"Successfully added document '{title}' to the knowledge base"
    except Exception as e:
        return f"Error adding document: {str(e)}"

def chat(query: str, top_k: int):
    """Chat function that uses dynamic top_k value."""
    if not query.strip():
        return "Please enter a question."
    
    try:
        context = "\n".join(retrieve(query, k=top_k))
        prompt = f"Answer the question using ONLY the context below.\n\nContext:\n{context}\n\nQ: {query}\nA:"
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content": prompt}],
            temperature=0
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="🧑‍💻 RAG Chatbot with File Upload") as demo:
    gr.Markdown("# 🧑‍💻 No‑Code RAG Chatbot (Gradio)")
    gr.Markdown("Upload documents to expand the knowledge base and adjust retrieval parameters.")
    
    with gr.Row():
        # Main chat area
        with gr.Column(scale=3):
            with gr.Row():
                inp = gr.Textbox(label="Ask a question", placeholder="Enter your question here...", scale=4)
                submit_btn = gr.Button("Submit", scale=1, variant="primary")
            out = gr.Markdown(label="Answer")
        
        # Sidebar for controls
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ Controls")
            
            # Top-k parameter
            top_k_slider = gr.Slider(
                minimum=1, 
                maximum=10, 
                value=1, 
                step=1, 
                label="Top-K Retrieval",
                info="Number of documents to retrieve"
            )
            
            gr.Markdown("### 📁 Upload Documents")
            
            # File upload
            file_upload = gr.File(
                label="Upload Document",
                file_types=[".txt", ".json"],
                type="filepath"
            )
            
            doc_title = gr.Textbox(
                label="Document Title",
                placeholder="Enter a title for the document",
                value="Uploaded Document"
            )
            
            upload_btn = gr.Button("Add to Knowledge Base", variant="secondary")
            upload_status = gr.Markdown(label="Upload Status")
    
    # Event handlers
    def handle_upload(file, title):
        if file is None:
            return "Please select a file to upload."
        
        content = process_uploaded_file(file)
        if content.startswith("Error"):
            return content
        
        result = add_document_to_index(content, title)
        return result
    
    def handle_chat(query, top_k):
        return chat(query, int(top_k))
    
    # Connect event handlers
    submit_btn.click(handle_chat, [inp, top_k_slider], out)
    inp.submit(handle_chat, [inp, top_k_slider], out)
    upload_btn.click(handle_upload, [file_upload, doc_title], upload_status)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--faiss", help="Path to existing FAISS index", default=os.getenv("FAISS_INDEX_PATH"))
    parser.add_argument("--local-model", action="store_true", help="Use local embeddings instead of OpenAI")
    args = parser.parse_args()

    INDEX = load_or_build_index(DOCS, path=args.faiss, use_openai=not args.local_model)
    demo.launch()
