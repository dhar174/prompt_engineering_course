# Enhanced Gradio RAG Chatbot

This is an enhanced version of the Gradio RAG (Retrieval-Augmented Generation) chatbot with file upload functionality and adjustable top-k retrieval parameters.

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

### 🎨 Enhanced UI Layout
- **Main Chat Area (75% width)**: Question input and answer display
- **Sidebar Controls (25% width)**: Upload controls and parameter adjustments
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

2. **Upload documents:**
   - Click "Upload Document" in the sidebar
   - Select a .txt or .json file
   - Enter a descriptive title
   - Click "Add to Knowledge Base"

3. **Adjust retrieval parameters:**
   - Use the "Top-K Retrieval" slider to control how many documents are retrieved
   - Higher values (5-10) provide more context
   - Lower values (1-3) focus on most relevant matches

4. **Ask questions:**
   - Type your question in the main input box
   - Click "Submit" or press Enter
   - The system will retrieve relevant documents and generate an answer

## Technical Improvements

- **Fixed LangChain deprecation warnings** by updating import statements
- **Enhanced error handling** with user-friendly feedback messages
- **Modular function design** for better maintainability
- **Dynamic FAISS index updates** for seamless document addition
- **Support for multiple file formats** with automatic content extraction

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
│                         │    │ Status Display  │
└─────────────────────────┘    └─────────────────┘
```

## Requirements

See `requirements.txt` for full dependencies. Key packages:
- `gradio` - Web interface
- `langchain-community` - Vector stores and embeddings
- `faiss-cpu` - Vector similarity search
- `sentence-transformers` - Local embeddings (optional)
- `openai` - OpenAI API integration (optional)

## Files Modified

- `faiss_helper.py` - Updated imports to fix deprecation warnings
- `gradio_rag_app.py` - Added file upload, top-k controls, and enhanced UI
- `.gitignore` - Added Python cache files exclusion