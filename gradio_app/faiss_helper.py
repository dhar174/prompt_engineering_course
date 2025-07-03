import os
from typing import Dict, List, Optional
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings


def get_embeddings(use_openai: bool = True):
    """Return embeddings instance using OpenAI or a local model."""
    if use_openai:
        return OpenAIEmbeddings()
    
    try:
        return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    except Exception as e:
        print(f"Warning: Could not load HuggingFace embeddings ({e})")
        print("Falling back to OpenAI embeddings (requires OPENAI_API_KEY)")
        # Fallback to OpenAI if HuggingFace model is not available
        return OpenAIEmbeddings()


def load_or_build_index(docs: Dict[str, str], path: Optional[str] = None, *, use_openai: bool = True) -> FAISS:
    """Load FAISS index from path or build a new one from docs."""
    embeddings = get_embeddings(use_openai)
    if path and os.path.exists(path):
        return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

    texts = list(docs.values())
    metadatas = [{"title": t} for t in docs]
    index = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas)
    if path:
        index.save_local(path)
    return index
