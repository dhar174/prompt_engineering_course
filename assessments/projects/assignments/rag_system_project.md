# Project Assignment: Building a Personal RAG System

**Module**: Module 6 - Retrieval & Domain-Specific Prompting  
**Duration**: 4 hours (across 2 sessions)  
**Type**: Individual Project  
**Complexity**: Intermediate  

## Learning Objectives

By completing this project, students will be able to:
- **Implement** a complete Retrieval-Augmented Generation (RAG) system using vector embeddings
- **Apply** domain-specific prompting techniques for knowledge-intensive tasks
- **Evaluate** the effectiveness of different retrieval strategies and prompt designs
- **Optimize** system performance through iterative testing and refinement

## Project Overview

### Problem Statement
Build a personal RAG system that can answer questions about your field of expertise or interest using a custom knowledge base. The system should demonstrate effective retrieval of relevant information and generate coherent, accurate responses based on the retrieved context.

### Real-World Context
RAG systems are widely used in production environments for:
- Customer support chatbots with domain-specific knowledge
- Research assistants for academic or professional work
- Internal knowledge management systems
- Personalized learning assistants

### Success Criteria
- System accurately retrieves relevant documents for queries
- Generated responses are coherent and factually grounded
- Performance metrics show improvement over baseline approaches
- Code is well-documented and reusable
- System handles edge cases gracefully

## Requirements

### Functional Requirements
1. **Document Processing**: Chunk and embed a collection of documents (minimum 10 documents)
2. **Vector Storage**: Store embeddings in a searchable vector database (FAISS or similar)
3. **Retrieval**: Implement semantic search to find relevant document chunks
4. **Generation**: Use retrieved context to generate responses to user queries
5. **Evaluation**: Measure and report system performance metrics

### Technical Requirements
- **Python 3.8+** with required libraries (langchain, faiss, openai, etc.)
- **Document formats**: Support PDF, text, or markdown documents
- **Vector database**: FAISS for local storage or alternative vector DB
- **LLM integration**: OpenAI API or local model integration
- **Evaluation metrics**: Retrieval accuracy, response quality, latency

### Non-Functional Requirements
- **Response time**: < 5 seconds for typical queries
- **Accuracy**: > 80% retrieval relevance based on manual evaluation
- **Scalability**: Handle 50+ documents efficiently
- **Maintainability**: Clean, modular code with clear documentation

## Deliverables

### 1. Code Implementation (50 points)
- **Main Application** (`rag_system.py`): Core RAG system implementation
- **Document Processor** (`document_processor.py`): Document chunking and embedding
- **Retrieval Engine** (`retrieval_engine.py`): Vector search and ranking
- **Response Generator** (`response_generator.py`): Context-aware text generation
- **Evaluation Suite** (`evaluation.py`): Performance measurement tools

### 2. Documentation (25 points)
- **README.md**: System overview, setup instructions, and usage guide
- **Architecture Document**: System design and component interactions
- **API Documentation**: Function and class documentation
- **User Guide**: How to use the system with examples

### 3. Evaluation Report (25 points)
- **Performance Analysis**: Quantitative metrics and analysis
- **Test Cases**: Diverse query examples with expected vs. actual results
- **Optimization Discussion**: Approaches tried and results achieved
- **Reflection**: Challenges encountered and lessons learned

## Implementation Guide

### Phase 1: Setup and Document Processing (Day 1, 2 hours)

#### Step 1: Environment Setup
```bash
# Install required packages
pip install langchain faiss-cpu openai tiktoken pandas numpy

# Set up project structure
mkdir personal-rag-system
cd personal-rag-system
mkdir src data docs tests
```

#### Step 2: Document Collection
- Gather 10-20 documents in your domain of interest
- Supported formats: PDF, .txt, .md
- Ensure documents are substantial (500+ words each)
- Store in `data/documents/` directory

#### Step 3: Document Processing Implementation
```python
# src/document_processor.py
import os
from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader

class DocumentProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    
    def process_documents(self, document_path: str) -> List[Dict]:
        """Process all documents in the specified directory"""
        # Implementation details here
        pass
```

### Phase 2: Vector Storage and Retrieval (Day 1, 2 hours)

#### Step 4: Embedding and Storage
```python
# src/vector_store.py
import faiss
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from typing import List, Dict, Tuple

class VectorStore:
    def __init__(self, embedding_model: str = "text-embedding-ada-002"):
        self.embeddings = OpenAIEmbeddings(model=embedding_model)
        self.index = None
        self.documents = []
    
    def create_index(self, documents: List[Dict]) -> None:
        """Create FAISS index from documents"""
        # Implementation details here
        pass
    
    def search(self, query: str, k: int = 5) -> List[Tuple[Dict, float]]:
        """Search for relevant documents"""
        # Implementation details here
        pass
```

#### Step 5: Retrieval Engine
```python
# src/retrieval_engine.py
from typing import List, Dict, Tuple
from .vector_store import VectorStore

class RetrievalEngine:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store
        self.reranking_enabled = True
    
    def retrieve(self, query: str, k: int = 5) -> List[Dict]:
        """Retrieve and rank relevant documents"""
        # Implementation details here
        pass
    
    def rerank_results(self, query: str, results: List[Dict]) -> List[Dict]:
        """Re-rank results based on relevance"""
        # Implementation details here
        pass
```

### Phase 3: Response Generation (Day 2, 1 hour)

#### Step 6: Response Generator
```python
# src/response_generator.py
import openai
from typing import List, Dict

class ResponseGenerator:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.client = openai.OpenAI()
    
    def generate_response(self, query: str, context: List[Dict]) -> str:
        """Generate response using retrieved context"""
        # Create context-aware prompt
        prompt = self._create_prompt(query, context)
        
        # Generate response
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    
    def _create_prompt(self, query: str, context: List[Dict]) -> str:
        """Create context-aware prompt"""
        context_text = "\n\n".join([doc['content'] for doc in context])
        
        prompt = f"""
Based on the following context, please answer the question accurately and comprehensively.

Context:
{context_text}

Question: {query}

Please provide a detailed answer based on the context provided. If the context doesn't contain enough information to answer the question, please say so clearly.

Answer:
"""
        return prompt
```

### Phase 4: System Integration and Testing (Day 2, 1 hour)

#### Step 7: Main Application
```python
# src/rag_system.py
from .document_processor import DocumentProcessor
from .vector_store import VectorStore
from .retrieval_engine import RetrievalEngine
from .response_generator import ResponseGenerator

class RAGSystem:
    def __init__(self, document_path: str):
        self.document_processor = DocumentProcessor()
        self.vector_store = VectorStore()
        self.retrieval_engine = RetrievalEngine(self.vector_store)
        self.response_generator = ResponseGenerator()
        
        # Initialize system
        self._initialize_system(document_path)
    
    def _initialize_system(self, document_path: str):
        """Initialize the RAG system with documents"""
        # Process documents
        documents = self.document_processor.process_documents(document_path)
        
        # Create vector index
        self.vector_store.create_index(documents)
    
    def query(self, question: str) -> Dict:
        """Process a query and return response with metadata"""
        # Retrieve relevant documents
        relevant_docs = self.retrieval_engine.retrieve(question)
        
        # Generate response
        response = self.response_generator.generate_response(question, relevant_docs)
        
        return {
            'question': question,
            'response': response,
            'sources': relevant_docs,
            'metadata': {
                'num_sources': len(relevant_docs),
                'confidence': self._calculate_confidence(relevant_docs)
            }
        }
    
    def _calculate_confidence(self, docs: List[Dict]) -> float:
        """Calculate confidence score based on retrieval quality"""
        # Implementation details here
        pass
```

### Phase 5: Evaluation and Optimization (Day 2, 1 hour)

#### Step 8: Evaluation Suite
```python
# src/evaluation.py
import json
import time
from typing import List, Dict, Tuple
from .rag_system import RAGSystem

class RAGEvaluator:
    def __init__(self, rag_system: RAGSystem):
        self.rag_system = rag_system
        self.test_queries = []
        self.results = []
    
    def load_test_queries(self, queries_file: str):
        """Load test queries from JSON file"""
        with open(queries_file, 'r') as f:
            self.test_queries = json.load(f)
    
    def run_evaluation(self) -> Dict:
        """Run comprehensive evaluation"""
        results = {
            'total_queries': len(self.test_queries),
            'avg_response_time': 0,
            'retrieval_accuracy': 0,
            'response_quality': 0,
            'detailed_results': []
        }
        
        total_time = 0
        
        for query_data in self.test_queries:
            start_time = time.time()
            result = self.rag_system.query(query_data['question'])
            end_time = time.time()
            
            response_time = end_time - start_time
            total_time += response_time
            
            # Evaluate result
            evaluation = self._evaluate_response(query_data, result)
            evaluation['response_time'] = response_time
            
            results['detailed_results'].append(evaluation)
        
        # Calculate averages
        results['avg_response_time'] = total_time / len(self.test_queries)
        results['retrieval_accuracy'] = self._calculate_retrieval_accuracy()
        results['response_quality'] = self._calculate_response_quality()
        
        return results
    
    def _evaluate_response(self, query_data: Dict, result: Dict) -> Dict:
        """Evaluate a single response"""
        # Implementation details here
        pass
```

## Assessment Criteria

### Technical Implementation (40 points)
- **Code Quality** (15 points): Clean, readable, well-organized code
- **Functionality** (15 points): All components work as specified
- **Error Handling** (5 points): Graceful handling of edge cases
- **Performance** (5 points): Meets response time requirements

### System Design (25 points)
- **Architecture** (10 points): Clear separation of concerns, modularity
- **Integration** (10 points): Components work together effectively
- **Scalability** (5 points): System can handle additional documents

### Documentation (20 points)
- **Code Documentation** (10 points): Clear docstrings and comments
- **User Documentation** (10 points): Comprehensive README and guides

### Evaluation and Analysis (15 points)
- **Metrics** (8 points): Appropriate evaluation metrics and analysis
- **Reflection** (7 points): Thoughtful analysis of results and challenges

## Submission Guidelines

### Repository Structure
```
personal-rag-system/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── rag_system.py
│   ├── document_processor.py
│   ├── vector_store.py
│   ├── retrieval_engine.py
│   ├── response_generator.py
│   └── evaluation.py
├── data/
│   ├── documents/
│   └── test_queries.json
├── docs/
│   ├── architecture.md
│   ├── api_documentation.md
│   └── user_guide.md
├── tests/
│   └── test_rag_system.py
├── results/
│   └── evaluation_report.json
└── examples/
    └── example_usage.py
```

### Submission Checklist
- [ ] All code files are properly documented with docstrings
- [ ] README.md provides clear setup and usage instructions
- [ ] System processes at least 10 documents successfully
- [ ] Evaluation report includes quantitative metrics
- [ ] Code follows PEP 8 style guidelines
- [ ] All dependencies are listed in requirements.txt
- [ ] Example usage demonstrates key functionality
- [ ] Reflection document discusses challenges and solutions

## Evaluation Rubric

### Exemplary (90-100 points)
- Professional-quality implementation with advanced features
- Comprehensive documentation and thorough evaluation
- Creative optimizations and innovative approaches
- Exceeds all functional requirements
- Demonstrates deep understanding of RAG concepts

### Proficient (80-89 points)
- Solid implementation meeting all requirements
- Good documentation and reasonable evaluation
- Effective use of prompt engineering techniques
- System works reliably for intended use cases
- Shows good understanding of key concepts

### Developing (70-79 points)
- Basic implementation with some issues
- Adequate documentation with gaps
- Limited evaluation and analysis
- System works but may have reliability issues
- Shows basic understanding with some confusion

### Beginning (60-69 points)
- Incomplete implementation with significant issues
- Poor documentation and minimal evaluation
- System fails to meet several requirements
- Shows limited understanding of concepts
- Requires substantial improvement

## Extension Opportunities

### For Advanced Students
- **Multi-modal RAG**: Integrate image or audio document processing
- **Advanced Retrieval**: Implement hybrid search (semantic + keyword)
- **Fine-tuning**: Fine-tune embedding models for domain-specific performance
- **Web Interface**: Create a web-based interface using Streamlit or Gradio
- **Evaluation Framework**: Develop automated evaluation using LLM judges

### For Struggling Students
- **Simplified Scope**: Focus on basic RAG pipeline with fewer documents
- **Template Usage**: Use provided code templates with guided implementation
- **Pair Programming**: Work with a partner for collaborative development
- **Extended Timeline**: Request additional time for completion

## Resources and Support

### Technical Resources
- [LangChain Documentation](https://python.langchain.com/)
- [FAISS Documentation](https://faiss.ai/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [RAG System Examples](https://github.com/langchain-ai/langchain/tree/master/cookbook)

### Learning Materials
- Module 6 course materials on RAG systems
- Research papers on retrieval-augmented generation
- Tutorial videos on vector databases and embeddings
- Community forums for technical support

### Support Channels
- **Office Hours**: Tuesdays and Thursdays, 2-4 PM
- **Discussion Forum**: Course Discord channel #rag-project
- **Peer Study Groups**: Organized through course platform
- **Technical Help**: Email instructor for debugging assistance

## Tips for Success

1. **Start with a Simple Implementation**: Get the basic pipeline working first
2. **Test Incrementally**: Test each component before integration
3. **Use Quality Documents**: Choose documents that are relevant and substantial
4. **Iterate on Prompts**: Experiment with different prompt designs
5. **Monitor Performance**: Track metrics throughout development
6. **Document as You Go**: Don't leave documentation until the end
7. **Seek Help Early**: Don't wait until the last minute to ask questions

This project will give you hands-on experience with one of the most important applications of prompt engineering in production systems. Focus on building a solid, working system that demonstrates your understanding of the key concepts.