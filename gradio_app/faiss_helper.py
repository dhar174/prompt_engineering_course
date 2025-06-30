import os
from typing import Dict, List, Optional
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings


def get_embeddings(use_openai: bool = True):
    """Return embeddings instance using OpenAI or a local model."""
    if use_openai:
        return OpenAIEmbeddings()
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


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
