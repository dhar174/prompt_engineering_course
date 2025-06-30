
import os, gradio as gr, openai

# -- tiny "vector store" (dict of doc: context). Replace with real DB later --
DOCS = {
    "What is RAG?" : "Retrieval‑Augmented Generation (RAG) combines LLMs with a retrieval component to ground answers in external data.",
    "Who created Python?" : "Python was created by Guido van Rossum and first released in 1991.",
}

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

def retrieve(query, k=1):
    # naive keyword match
    best = sorted(DOCS.items(), key=lambda x: int(x[0].lower() in query.lower()), reverse=True)
    return [ctx for _, ctx in best[:k]]

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
    demo.launch()
