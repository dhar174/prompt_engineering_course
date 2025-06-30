Here’s a no-code / low-code Gradio RAG chatbot you can run in one line:

Download gradio_rag_app.py


pip install gradio openai
python gradio_rag_app.py

What it does

1. Tiny “vector store.”
A placeholder DOCS dict holds reference snippets. Replace with a real vector DB later.


2. Retrieve.
A trivial retrieve() function grabs the most relevant snippet (naïve keyword match—swap in FAISS/Chroma when ready).


3. Prompt.
Builds a RAG prompt: “Answer using ONLY this context …” and calls OpenAI.


4. Gradio Blocks UI.
Zero UI code beyond gr.Blocks()—type a question, hit Enter, get an answer.



Feel free to expand:

Point retrieve() at your Day-6 embedding_rag_playground FAISS index.

Add file-upload for docs, or a sidebar to tweak top-k.

Switch to LangChain’s VectorStore for production.


