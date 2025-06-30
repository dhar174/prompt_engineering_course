
import os
import gradio as gr
import openai
import faiss
import numpy as np

# -- tiny "vector store" (dict of doc: context). Replace with real DB later --
DOCS = {
    "What is RAG?" : "Retrieval‑Augmented Generation (RAG) combines LLMs with a retrieval component to ground answers in external data.",
    "Who created Python?" : "Python was created by Guido van Rossum and first released in 1991.",
}

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", "sk-..."))

# initialize FAISS index
EMBED_DIM = 1536
index = faiss.IndexFlatL2(EMBED_DIM)
texts = []

def _embed(text_list):
    """Embed a list of texts using OpenAI."""
    resp = client.embeddings.create(input=text_list, model="text-embedding-3-small")
    return [np.array(d.embedding, dtype=np.float32) for d in resp.data]

def _add_docs(docs):
    """Add raw text docs to the FAISS index."""
    if not docs:
        return
    vectors = np.vstack(_embed(docs))
    index.add(vectors)
    texts.extend(docs)

def add_files(files):
    """Read uploaded files and insert their contents into the index."""
    docs = []
    for file in files:
        try:
            with open(file.name, "r", encoding="utf-8") as f:
                docs.append(f.read())
        except Exception:
            continue
    _add_docs(docs)
    return f"Uploaded {len(docs)} document(s)."

_add_docs(list(DOCS.values()))

def retrieve(query, k=1):
    """Return top-k document texts for a query using the FAISS index."""
    if index.ntotal == 0:
        return []
    query_vec = np.vstack(_embed([query]))
    k = min(int(k), index.ntotal)
    _, ids = index.search(query_vec, k)
    return [texts[i] for i in ids[0]]

def chat(query, k):
    context = "\n".join(retrieve(query, k))
    prompt = f"Answer the question using ONLY the context below.\n\nContext:\n{context}\n\nQ: {query}\nA:"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return resp.choices[0].message.content.strip()

with gr.Blocks() as demo:
    gr.Markdown("# 🧑‍💻 No‑Code RAG Chatbot (Gradio)")
    upload = gr.Files(label="Upload text files", file_count="multiple", file_types=["text"])
    upload_msg = gr.Markdown()
    upload.upload(lambda f: add_files(f), upload, upload_msg)

    inp = gr.Textbox(label="Ask a question")
    k_slider = gr.Slider(1, 5, value=1, step=1, label="top_k")
    out = gr.Markdown()
    inp.submit(chat, [inp, k_slider], out)

if __name__ == "__main__":
    demo.launch()
