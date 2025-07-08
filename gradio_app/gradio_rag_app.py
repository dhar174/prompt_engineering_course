
import os
import argparse
import gradio as gr
import openai
from faiss_helper import load_or_build_index
import json
from langchain_core.documents import Document
import atexit

# -- tiny "vector store" (dict of doc: context). Replace with real DB later --
DOCS = {
    "What is RAG?" : "Retrieval‑Augmented Generation (RAG) combines LLMs with a retrieval component to ground answers in external data.",
    "Who created Python?" : "Python was created by Guido van Rossum and first released in 1991.",
}

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

# Global FAISS index with persistence manager
INDEX = None

def cleanup_index():
    """Cleanup function to ensure index is saved on exit."""
    global INDEX
    if INDEX and hasattr(INDEX, 'shutdown'):
        INDEX.shutdown()

# Register cleanup function
atexit.register(cleanup_index)

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
    """Add a new document to the FAISS index with batched persistence."""
    global INDEX
    if not content.strip():
        return "No content to add"
    
    try:
        # Create a new document
        doc = Document(page_content=content, metadata={"title": title})
        
        # Add to existing index (handles batched persistence automatically)
        INDEX.add_documents([doc])
        
        # Get persistence status
        pending_count = INDEX.get_pending_count()
        is_dirty = INDEX.is_dirty()
        
        # Provide user feedback about persistence status
        status_msg = f"Successfully added document '{title}' to the knowledge base"
        if pending_count > 0:
            status_msg += f" ({pending_count} documents pending save)"
        elif not is_dirty:
            status_msg += " (saved to disk)"
        
        return status_msg
        
    except Exception as e:
        return f"Error adding document: {str(e)}"

def force_save_index() -> str:
    """Force an immediate save of the FAISS index."""
    global INDEX
    try:
        if INDEX is None:
            return "❌ Index not initialized"
        elif not hasattr(INDEX, 'force_save'):
            return "❌ Index lacks save functionality"
        else:
            success = INDEX.force_save()
            if success:
                return "✅ Index saved successfully to disk"
            else:
                return "❌ Failed to save index"
    except Exception as e:
        return f"❌ Error saving index: {str(e)}"

def get_index_status() -> str:
    """Get the current persistence status of the index."""
    global INDEX
    try:
        if INDEX and hasattr(INDEX, 'get_pending_count'):
            pending = INDEX.get_pending_count()
            dirty = INDEX.is_dirty()
            
            if not dirty:
                return "✅ All changes saved"
            elif pending > 0:
                return f"⏳ {pending} documents pending save"
            else:
                return "⏳ Changes pending save"
        else:
            return "❓ Index status unknown"
    except Exception as e:
        return f"❌ Error checking status: {str(e)}"

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
            
            # Persistence controls
            gr.Markdown("### 💾 Persistence")
            
            persistence_status = gr.Markdown(label="Status", value="❓ Index status unknown")
            
            with gr.Row():
                save_btn = gr.Button("💾 Save Now", variant="secondary", scale=1)
                refresh_status_btn = gr.Button("🔄 Refresh", variant="secondary", scale=1)
    
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
    
    def handle_save():
        return force_save_index()
    
    def handle_refresh_status():
        return get_index_status()
    
    # Connect event handlers
    submit_btn.click(handle_chat, [inp, top_k_slider], out)
    inp.submit(handle_chat, [inp, top_k_slider], out)
    upload_btn.click(handle_upload, [file_upload, doc_title], upload_status)
    save_btn.click(handle_save, outputs=persistence_status)
    refresh_status_btn.click(handle_refresh_status, outputs=persistence_status)
    
    # Update persistence status on upload
    upload_btn.click(handle_refresh_status, outputs=persistence_status)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RAG Chatbot with batched FAISS persistence")
    parser.add_argument("--faiss", help="Path to existing FAISS index", default=os.getenv("FAISS_INDEX_PATH"))
    parser.add_argument("--local-model", action="store_true", help="Use local embeddings instead of OpenAI")
    
    # Persistence configuration
    parser.add_argument("--batch-size", type=int, default=5, help="Number of documents to batch before saving (default: 5)")
    parser.add_argument("--max-wait-time", type=float, default=30.0, help="Maximum time to wait before saving in seconds (default: 30)")
    parser.add_argument("--no-auto-persist", action="store_true", help="Disable automatic persistence (save immediately)")
    
    args = parser.parse_args()

    # Initialize INDEX with persistence configuration
    INDEX = load_or_build_index(
        DOCS, 
        path=args.faiss, 
        use_openai=not args.local_model,
        batch_size=args.batch_size,
        max_wait_time=args.max_wait_time,
        auto_persist=not args.no_auto_persist
    )
    
    print(f"🚀 Starting RAG Chatbot with batched persistence:")
    print(f"   - Batch size: {args.batch_size}")
    print(f"   - Max wait time: {args.max_wait_time}s")
    print(f"   - Auto persist: {not args.no_auto_persist}")
    print(f"   - Index path: {args.faiss or 'In-memory only'}")
    
    demo.launch()
