# Enhanced Gradio RAG Chatbot

This is an enhanced version of the Gradio RAG (Retrieval-Augmented Generation) chatbot with file upload functionality, adjustable top-k retrieval parameters, and **efficient batched FAISS persistence**.

## New Features

### 📁 File Upload
- Upload text documents (.txt) and JSON files (.json) to expand the knowledge base
- Custom document titles for better organization
- Real-time integration with the FAISS vector store
- Automatic content processing and indexing

### ⚙️ Top-K Parameter Control
- Adjustable retrieval depth via sidebar slider (1-10 documents)
- Real-time parameter adjustment affects answer quality and context breadth
- Higher values provide more context but may include less relevant information

### 💾 **Batched FAISS Persistence** (NEW!)
- **Performance optimized**: Batches document additions to reduce disk I/O
- **Non-blocking**: Background persistence thread doesn't freeze the UI
- **Configurable**: Adjust batch size and save frequency
- **User control**: Manual save button and real-time status display
- **Robust**: Thread-safe operations with graceful shutdown

### 🎨 Enhanced UI Layout
- **Main Chat Area (75% width)**: Question input and answer display
- **Sidebar Controls (25% width)**: Upload controls and parameter adjustments
- **Persistence Controls**: Save button and status display
- Clean, organized interface with clear visual hierarchy
- Responsive design that works on different screen sizes

## Usage

1. **Start the application:**
   ```bash
   cd gradio_app
   python gradio_rag_app.py --local-model  # Use local embeddings
   # OR
   python gradio_rag_app.py  # Use OpenAI embeddings (requires API key)
   ```

2. **Advanced persistence configuration:**
   ```bash
   # Custom batch size and timing
   python gradio_rag_app.py --batch-size 10 --max-wait-time 60
   
   # Disable batching (save immediately)
   python gradio_rag_app.py --no-auto-persist
   
   # Specify index path
   python gradio_rag_app.py --faiss ./my_index
   ```

3. **Upload documents:**
   - Click "Upload Document" in the sidebar
   - Select a .txt or .json file
   - Enter a descriptive title
   - Click "Add to Knowledge Base"
   - Monitor persistence status in the sidebar

4. **Adjust retrieval parameters:**
   - Use the "Top-K Retrieval" slider to control how many documents are retrieved
   - Higher values (5-10) provide more context
   - Lower values (1-3) focus on most relevant matches

5. **Manage persistence:**
   - Check the "Persistence" section for save status
   - Use "Save Now" to force immediate save
   - Use "Refresh" to update the status display

6. **Ask questions:**
   - Type your question in the main input box
   - Click "Submit" or press Enter
   - The system will retrieve relevant documents and generate an answer

## Technical Improvements

- **Fixed LangChain deprecation warnings** by updating import statements
- **Enhanced error handling** with user-friendly feedback messages
- **Modular function design** for better maintainability
- **Dynamic FAISS index updates** for seamless document addition
- **Support for multiple file formats** with automatic content extraction
- **🆕 Batched FAISS persistence** to solve performance bottlenecks:
  - Background thread for async persistence (no UI blocking)
  - Configurable batch size and timing
  - Thread-safe operations with proper cleanup
  - User feedback on persistence status
  - Command-line configuration options

## Architecture

```
Main Chat Area                 Sidebar Controls
┌─────────────────────────┐    ┌─────────────────┐
│ Question Input          │    │ ⚙️ Controls     │
│ [Submit Button]         │    │ Top-K Slider    │
│                         │    │                 │
│ Answer Display          │    │ 📁 Upload       │
│ (Markdown formatted)    │    │ File Selector   │
│                         │    │ Document Title  │
│                         │    │ [Add Button]    │
│                         │    │                 │
│                         │    │ 💾 Persistence  │
│                         │    │ Status Display  │
│                         │    │ [Save] [Refresh]│
└─────────────────────────┘    └─────────────────┘
```

## Persistence Configuration

The FAISS index persistence can be configured via command-line arguments:

| Option | Default | Description |
|--------|---------|-------------|
| `--batch-size N` | 5 | Number of documents to accumulate before saving |
| `--max-wait-time N` | 30 | Maximum time to wait before saving (seconds) |
| `--no-auto-persist` | False | Disable batching, save immediately |
| `--faiss PATH` | None | Path to save/load the FAISS index |

**Performance Trade-offs:**
- **Larger batch sizes**: Better performance, higher risk of data loss
- **Smaller batch sizes**: More frequent saves, slightly higher I/O overhead
- **Immediate persistence**: Maximum data safety, potential UI blocking
- **Batched persistence**: Optimal balance of performance and reliability

## Requirements

See `requirements.txt` for full dependencies. Key packages:
- `gradio` - Web interface
- `langchain-community` - Vector stores and embeddings
- `faiss-cpu` - Vector similarity search
- `sentence-transformers` - Local embeddings (optional)
- `openai` - OpenAI API integration (optional)

## Files Modified

- `faiss_helper.py` - Updated imports to fix deprecation warnings, added BatchedPersistenceManager support
- `gradio_rag_app.py` - Added file upload, top-k controls, enhanced UI, and persistence management
- `persistence_manager.py` - **New file** implementing batched FAISS persistence with async operations
- `.gitignore` - Added Python cache files exclusion
- `README.md` - Updated documentation with new persistence features