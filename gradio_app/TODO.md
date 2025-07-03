Here’s a no-code / low-code Gradio RAG chatbot you can run in one line:

Download gradio_rag_app.py


pip install gradio openai langchain-community langchain-openai langchain-huggingface faiss-cpu
python gradio_rag_app.py

What it does

1. Tiny “vector store.”
A placeholder DOCS dict holds reference snippets. Replace with a real vector DB later.


2. Retrieve.
A trivial retrieve() function grabs the most relevant snippet (✅ UPDATED: now uses FAISS similarity search instead of naïve keyword match).


3. Prompt.
Builds a RAG prompt: “Answer using ONLY this context …” and calls OpenAI.


4. Gradio Blocks UI.
Zero UI code beyond gr.Blocks()—type a question, hit Enter, get an answer.



Feel free to expand:

✅ Point retrieve() at your Day-6 embedding_rag_playground FAISS index (COMPLETED).

Add file-upload for docs, or a sidebar to tweak top-k.

Switch to LangChain’s VectorStore for production.



## Recent Updates (✅ COMPLETED)

✅ Fixed LangChain deprecation warnings by updating imports to use langchain-community and langchain-openai
✅ Added proper HuggingFace embeddings support with langchain-huggingface  
✅ Added fallback handling for environments without internet access
✅ Updated retrieve() function to use proper FAISS similarity search instead of naive keyword matching
✅ Maintained backward compatibility with existing usage patterns