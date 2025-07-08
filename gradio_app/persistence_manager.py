"""
Batched FAISS Persistence Manager

This module provides a wrapper around FAISS indexes that handles persistence
with batching and async operations to avoid performance bottlenecks.
"""

import threading
import time
import logging
from typing import List, Optional
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

logger = logging.getLogger(__name__)


class BatchedPersistenceManager:
    """
    Manages FAISS index persistence with batching and async operations.

    This class wraps a FAISS index and provides:
    - Batched document additions
    - Async persistence to disk
    - Configurable batch size and timing
    - Thread-safe operations
    """

    def __init__(
        self,
        index: FAISS,
        index_path: Optional[str] = None,
        batch_size: int = 5,
        max_wait_time: float = 30.0,
        auto_persist: bool = True,
    ):
        """
        Initialize the persistence manager.

        Args:
            index: The FAISS index to manage
            index_path: Path where the index should be saved
            batch_size: Number of documents to accumulate before persisting
            max_wait_time: Maximum time to wait before persisting (seconds)
            auto_persist: Whether to automatically persist based on batch_size/time
        """
        self.index = index
        self.index_path = index_path
        self.batch_size = batch_size
        self.max_wait_time = max_wait_time
        self.auto_persist = auto_persist

        # State tracking
        self._pending_docs = 0
        self._last_save_time = time.time()
        self._is_dirty = False
        self._lock = threading.Lock()
        self._shutdown = False

        # Background persistence thread
        self._persistence_thread = None
        if auto_persist and index_path:
            self._start_persistence_thread()

    def _start_persistence_thread(self):
        """Start the background persistence thread."""
        self._persistence_thread = threading.Thread(
            target=self._persistence_worker, daemon=True, name="FAISSPersistenceWorker"
        )
        self._persistence_thread.start()

    def _persistence_worker(self):
        """Background worker that handles automatic persistence."""
        while not self._shutdown:
            try:
                time.sleep(1.0)  # Check every second

                with self._lock:
                    should_save = self._is_dirty and (
                        self._pending_docs >= self.batch_size
                        or time.time() - self._last_save_time >= self.max_wait_time
                    )

                if should_save:
                    self._save_now()

            except Exception as e:
                logger.error(f"Error in persistence worker: {e}")

    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the index with batched persistence.

        Args:
            documents: List of documents to add
        """
        # Add documents to the index immediately (in-memory)
        self.index.add_documents(documents)

        # Update persistence state
        with self._lock:
            self._pending_docs += len(documents)
            self._is_dirty = True

        # If auto-persistence is disabled, save immediately
        if not self.auto_persist and self.index_path:
            self._save_now()

    def _save_now(self) -> bool:
        """
        Save the index to disk immediately.

        Returns:
            True if save was successful, False otherwise
        """
        if not self.index_path:
            return False

        try:
            # Check if save is necessary
            with self._lock:
                if not self._is_dirty:
                    return True

            # Save to disk (release lock before disk write)
            self.index.save_local(self.index_path)

            # Reacquire lock to update state
            with self._lock:
                self._pending_docs = 0
                self._last_save_time = time.time()
                self._is_dirty = False

            logger.info(f"Saved FAISS index to {self.index_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to save FAISS index: {e}")
            return False

    def force_save(self) -> bool:
        """
        Force an immediate save of the index.

        Returns:
            True if save was successful, False otherwise
        """
        return self._save_now()

    def get_pending_count(self) -> int:
        """Get the number of documents pending persistence."""
        with self._lock:
            return self._pending_docs

    def is_dirty(self) -> bool:
        """Check if the index has unsaved changes."""
        with self._lock:
            return self._is_dirty

    def shutdown(self):
        """Shutdown the persistence manager and save any pending changes."""
        self._shutdown = True

        # Save any pending changes
        if self._is_dirty:
            self._save_now()

        # Wait for the persistence thread to finish
        if self._persistence_thread and self._persistence_thread.is_alive():
            self._persistence_thread.join(timeout=5.0)

    def __del__(self):
        """Ensure clean shutdown when the object is destroyed."""
        try:
            self.shutdown()
        except Exception:
            pass

    # Delegate other methods to the underlying index
    def similarity_search(self, query: str, k: int = 1, **kwargs):
        """Search for similar documents."""
        return self.index.similarity_search(query, k=k, **kwargs)

    def similarity_search_with_score(self, query: str, k: int = 1, **kwargs):
        """Search for similar documents with similarity scores."""
        return self.index.similarity_search_with_score(query, k=k, **kwargs)

    @property
    def docstore(self):
        """Access the underlying docstore."""        return self.index.docstore
