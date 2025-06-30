
import os
import gradio as gr
import openai
import numpy as np

try:
    import faiss                   # optional faiss for similarity search
    from sentence_transformers import SentenceTransformer
    _model = SentenceTransformer("all-MiniLM-L6-v2")
    _dim = _model.get_sentence_embedding_dimension()
    _index = faiss.IndexFlatL2(_dim)
    _texts = []

    def _embed(text: str) -> np.ndarray:
        return _model.encode([text])[0].astype("float32")

    def _add_doc(text: str):
        vec = _embed(text)
        _index.add(vec.reshape(1, -1))
        _texts.append(text)

    def _search(query: str, k: int) -> list[str]:
        vec = _embed(query)
        _k = min(k, _index.ntotal)
        if _k == 0:
            return []
        _, idx = _index.search(vec.reshape(1, -1), _k)
        return [_texts[i] for i in idx[0]]

except Exception:  # pragma: no cover - optional deps missing
    faiss = None
    _texts: list[str] = []

    def _embed(text: str) -> np.ndarray:
        vec = np.zeros(128, dtype="float32")
        for t in text.lower().split():
            vec[hash(t) % 128] += 1
        norm = np.linalg.norm(vec)
        return vec if norm == 0 else vec / norm

    def _add_doc(text: str):
        _texts.append(text)

    def _search(query: str, k: int) -> list[str]:
        if not _texts:
            return []
        q = _embed(query)
        mat = np.vstack([_embed(t) for t in _texts])
        sims = mat @ q
        idx = sims.argsort()[::-1][:k]
        return [_texts[i] for i in idx]

# -- tiny "vector store" (dict of doc: context). Replace with real DB later --
DOCS = {
    "What is RAG?" : "Retrieval‑Augmented Generation (RAG) combines LLMs with a retrieval component to ground answers in external data.",
    "Who created Python?" : "Python was created by Guido van Rossum and first released in 1991.",
}

for text in DOCS.values():
    _add_doc(text)

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

def retrieve(query: str, k: int = 1) -> list[str]:
    return _search(query, k)

def chat(query: str, top_k: int = 1) -> str:
    context = "\n".join(retrieve(query, top_k))
    prompt = f"Answer the question using ONLY the context below.\n\nContext:\n{context}\n\nQ: {query}\nA:"
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": prompt}],
        temperature=0
    )
    return resp.choices[0].message.content.strip()

def upload_files(files: list[gr.File]) -> str:
    if not files:
        return "No files uploaded"
    for f in files:
        try:
            text = f.read().decode("utf-8")
        except Exception:
            text = ""
        _add_doc(text)
    return f"Added {len(files)} document(s)"

with gr.Blocks() as demo:
    gr.Markdown("# 🧑‍💻 No‑Code RAG Chatbot (Gradio)")
    with gr.Row():
        inp = gr.Textbox(label="Ask a question", scale=3)
        top_k = gr.Slider(1, 5, value=1, step=1, label="top_k", scale=1)
    uploader = gr.File(label="Upload text docs", file_count="multiple")
    out = gr.Markdown()
    uploader.upload(upload_files, uploader, out, queue=False)
    inp.submit(chat, [inp, top_k], out)

if __name__ == "__main__":
    demo.launch()
