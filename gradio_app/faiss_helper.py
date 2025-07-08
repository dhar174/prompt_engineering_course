import os
from typing import Dict, Optional
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import (
    OpenAIEmbeddings,
    HuggingFaceEmbeddings,
)

# Import the persistence manager
try:
    from .persistence_manager import BatchedPersistenceManager
except ImportError:
    # Fallback for direct execution
    from persistence_manager import BatchedPersistenceManager


def get_embeddings(use_openai: bool = True):
    """Return embeddings instance using OpenAI or a local model."""
    if use_openai:
        return OpenAIEmbeddings()

    try:
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    except Exception as e:
        print(f"Warning: Could not load HuggingFace embeddings ({e})")
        print("Falling back to OpenAI embeddings (requires OPENAI_API_KEY)")
        # Fallback to OpenAI if HuggingFace model is not available
        return OpenAIEmbeddings()


def load_or_build_index(
    docs: Dict[str, str],
    path: Optional[str] = None,
    *,
    use_openai: bool = True,
    batch_size: int = 5,
    max_wait_time: float = 30.0,
    auto_persist: bool = True,
) -> BatchedPersistenceManager:
    """
    Load FAISS index from path or build a new one from docs.

    Args:
        docs: Dictionary of document titles to content
        path: Path to save/load the index
        use_openai: Whether to use OpenAI embeddings
        batch_size: Number of documents to accumulate before persisting
        max_wait_time: Maximum time to wait before persisting (seconds)
        auto_persist: Whether to automatically persist based on batch_size/time

    Returns:
        BatchedPersistenceManager wrapping the FAISS index
    """
    embeddings = get_embeddings(use_openai)

    # Try to load existing index
    if path and os.path.exists(path):
        index = FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True,
        )
    else:
        # Build new index from docs
        texts = list(docs.values())
        metadatas = [{"title": t} for t in docs]
        index = FAISS.from_texts(
            texts=texts,
            embedding=embeddings,
            metadatas=metadatas,
        )

        # Save initial index if path is provided
        if path:
            index.save_local(path)

    # Wrap in persistence manager
    return BatchedPersistenceManager(
        index=index,
        index_path=path,
        batch_size=batch_size,
        max_wait_time=max_wait_time,
        auto_persist=auto_persist
    )
