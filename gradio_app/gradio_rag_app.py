
import os
import argparse
import gradio as gr
import openai
from faiss_helper import load_or_build_index

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

def chat(query):
    context = "\n".join(retrieve(query))
    prompt = f"Answer the question using ONLY the context below.\n\nContext:\n{context}\n\nQ: {query}\nA:"
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": prompt}],
        temperature=0
    )
    return resp.choices[0].message.content.strip()

with gr.Blocks() as demo:
    gr.Markdown("# 🧑‍💻 No‑Code RAG Chatbot (Gradio)")
    inp = gr.Textbox(label="Ask a question")
    out = gr.Markdown()
    inp.submit(chat, inp, out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--faiss", help="Path to existing FAISS index", default=os.getenv("FAISS_INDEX_PATH"))
    parser.add_argument("--local-model", action="store_true", help="Use local embeddings instead of OpenAI")
    args = parser.parse_args()

    INDEX = load_or_build_index(DOCS, path=args.faiss, use_openai=not args.local_model)
    demo.launch()
