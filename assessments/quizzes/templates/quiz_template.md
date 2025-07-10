# Knowledge Check Quiz Template

This template provides a standardized format for creating knowledge check quizzes for any module in the prompt engineering course.

## Quiz Configuration

```yaml
quiz:
  title: "Module X: [Topic] Knowledge Check"
  module: "Module X"
  topic: "[Topic Name]"
  duration: "10 minutes"
  attempts: "unlimited"
  passing_score: 80
  feedback_mode: "immediate"
  question_pool: true
  randomize_questions: true
  randomize_answers: true
```

## Question Types

### 1. Multiple Choice (Single Answer)

```yaml
question:
  type: "multiple_choice_single"
  id: "mc_001"
  points: 1
  difficulty: "medium"
  learning_objective: "LO.X.Y"
  
  prompt: |
    Which of the following best describes the primary purpose of tokenization in LLMs?
    
  options:
    a: "To convert text into numerical representations for processing"
    b: "To encrypt sensitive information in prompts"
    c: "To compress text for faster transmission"
    d: "To detect and prevent malicious inputs"
    
  correct_answer: "a"
  
  explanation: |
    Tokenization converts text into numerical tokens that language models can process. 
    Each token represents a word fragment or complete word that the model understands.
    
  feedback:
    correct: "Excellent! You understand the fundamental purpose of tokenization."
    incorrect: "Not quite. Review the section on tokenization basics and try again."
    
  hints:
    - "Think about how computers process text vs. how humans read text"
    - "Consider what happens before a model can 'understand' text input"
    
  tags: ["tokenization", "fundamentals", "preprocessing"]
```

### 2. Multiple Choice (Multiple Answers)

```yaml
question:
  type: "multiple_choice_multiple"
  id: "mc_002"
  points: 2
  difficulty: "medium"
  learning_objective: "LO.X.Y"
  
  prompt: |
    Which of the following are valid strategies for controlling prompt output length? 
    (Select all that apply)
    
  options:
    a: "Setting max_tokens parameter"
    b: "Including explicit word limits in the prompt"
    c: "Using presence penalty to reduce repetition"
    d: "Adjusting temperature to make output more deterministic"
    e: "Providing examples of desired output length"
    
  correct_answers: ["a", "b", "e"]
  
  explanation: |
    Multiple strategies can control output length:
    - max_tokens directly limits token count
    - Explicit instructions ("in 50 words") guide the model
    - Examples demonstrate desired length
    Presence penalty reduces repetition but doesn't control length directly.
    Temperature affects creativity, not length.
    
  feedback:
    all_correct: "Perfect! You understand the various length control strategies."
    partial_correct: "Good start! You identified some strategies but missed others."
    incorrect: "Review the section on output control parameters and try again."
    
  partial_credit: true
  min_selections: 2
  max_selections: 5
```

### 3. True/False

```yaml
question:
  type: "true_false"
  id: "tf_001"
  points: 1
  difficulty: "easy"
  learning_objective: "LO.X.Y"
  
  prompt: |
    True or False: Higher temperature values (e.g., 0.9) make model outputs more 
    deterministic and predictable.
    
  correct_answer: false
  
  explanation: |
    Higher temperature values increase randomness and creativity in model outputs.
    Lower temperature values (closer to 0) make outputs more deterministic and predictable.
    
  feedback:
    correct: "Correct! You understand how temperature affects model behavior."
    incorrect: "Remember: higher temperature = more random, lower temperature = more deterministic."
    
  tags: ["temperature", "decoding", "parameters"]
```

### 4. Short Answer

```yaml
question:
  type: "short_answer"
  id: "sa_001"
  points: 3
  difficulty: "medium"
  learning_objective: "LO.X.Y"
  
  prompt: |
    Explain in 2-3 sentences why context window size is important for prompt engineering.
    
  sample_answers:
    - "Context window limits how much text the model can process at once. Large prompts or conversations may exceed this limit, causing truncation and loss of information."
    - "The context window determines the maximum tokens (input + output) the model can handle. Exceeding this limit results in truncation, affecting model performance and coherence."
    
  evaluation_criteria:
    - "Mentions context window as a token limit"
    - "Explains truncation consequences"
    - "Connects to prompt engineering implications"
    
  rubric:
    exemplary: "Clear explanation with specific examples and implications"
    proficient: "Accurate explanation covering key concepts"
    developing: "Basic understanding with some gaps"
    beginning: "Incorrect or incomplete explanation"
    
  keywords: ["context", "window", "tokens", "limit", "truncation"]
  
  feedback_template: |
    Your answer shows {level} understanding of context windows.
    {specific_feedback}
    Consider reviewing: {suggested_resources}
```

### 5. Matching

```yaml
question:
  type: "matching"
  id: "match_001"
  points: 2
  difficulty: "medium"
  learning_objective: "LO.X.Y"
  
  prompt: |
    Match each prompt engineering technique with its primary purpose:
    
  left_column:
    - "Few-shot prompting"
    - "Chain-of-thought"
    - "Self-consistency"
    - "Retrieval-augmented generation"
    
  right_column:
    - "Accessing external knowledge"
    - "Improving reasoning accuracy"
    - "Providing task examples"
    - "Reducing output variance"
    
  correct_matches:
    "Few-shot prompting": "Providing task examples"
    "Chain-of-thought": "Improving reasoning accuracy"
    "Self-consistency": "Reducing output variance"
    "Retrieval-augmented generation": "Accessing external knowledge"
    
  partial_credit: true
  points_per_match: 0.5
```

### 6. Ordering/Sequencing

```yaml
question:
  type: "ordering"
  id: "order_001"
  points: 2
  difficulty: "medium"
  learning_objective: "LO.X.Y"
  
  prompt: |
    Arrange these steps in the correct order for implementing a RAG system:
    
  items:
    - "Embed query and retrieve relevant documents"
    - "Generate response using retrieved context"
    - "Preprocess and chunk document collection"
    - "Create embeddings for document chunks"
    - "Receive user query"
    
  correct_order:
    1: "Preprocess and chunk document collection"
    2: "Create embeddings for document chunks"
    3: "Receive user query"
    4: "Embed query and retrieve relevant documents"
    5: "Generate response using retrieved context"
    
  partial_credit: true
  adjacent_penalty: 0.5  # Reduced penalty for adjacent swaps
```

## Quiz Implementation

### Python Class Structure

```python
class QuizQuestion:
    def __init__(self, question_data):
        self.id = question_data['id']
        self.type = question_data['type']
        self.prompt = question_data['prompt']
        self.points = question_data['points']
        self.difficulty = question_data['difficulty']
        self.learning_objective = question_data['learning_objective']
        
    def evaluate(self, student_answer):
        """Evaluate student answer and return score with feedback"""
        pass
        
    def get_feedback(self, student_answer, is_correct):
        """Generate appropriate feedback based on answer"""
        pass

class Quiz:
    def __init__(self, quiz_config):
        self.title = quiz_config['title']
        self.module = quiz_config['module']
        self.questions = []
        self.total_points = 0
        
    def add_question(self, question):
        self.questions.append(question)
        self.total_points += question.points
        
    def calculate_score(self, student_answers):
        """Calculate final score and provide detailed feedback"""
        pass
```

### Jupyter Notebook Integration

```python
# Example widget-based quiz implementation
import ipywidgets as widgets
from IPython.display import display, clear_output

class InteractiveQuiz:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.current_question = 0
        self.answers = {}
        self.score = 0
        
    def display_question(self, question_index):
        """Display current question with interactive widgets"""
        question = self.quiz_data['questions'][question_index]
        
        # Create question widget based on type
        if question['type'] == 'multiple_choice_single':
            return self.create_multiple_choice_widget(question)
        elif question['type'] == 'true_false':
            return self.create_true_false_widget(question)
        # Add other question types...
        
    def create_multiple_choice_widget(self, question):
        """Create multiple choice widget"""
        options = [(f"{k}: {v}", k) for k, v in question['options'].items()]
        
        widget = widgets.RadioButtons(
            options=options,
            description=question['prompt'],
            disabled=False,
            style={'description_width': 'initial'}
        )
        
        return widget
        
    def submit_answer(self, question_id, answer):
        """Submit answer and provide feedback"""
        self.answers[question_id] = answer
        # Evaluate and provide feedback
        pass
```

## Assessment Analytics

### Question Performance Metrics

```python
class QuizAnalytics:
    def __init__(self):
        self.question_stats = {}
        self.student_performance = {}
        
    def track_question_performance(self, question_id, responses):
        """Track how well students perform on each question"""
        correct_count = sum(1 for r in responses if r['is_correct'])
        total_count = len(responses)
        
        self.question_stats[question_id] = {
            'difficulty_actual': 1 - (correct_count / total_count),
            'discrimination': self.calculate_discrimination(responses),
            'common_mistakes': self.identify_common_mistakes(responses)
        }
        
    def calculate_discrimination(self, responses):
        """Calculate question discrimination index"""
        # Implementation for discrimination analysis
        pass
        
    def generate_improvement_report(self):
        """Generate report on quiz effectiveness"""
        pass
```

## Accessibility Features

### Screen Reader Support
- Proper ARIA labels for all interactive elements
- Descriptive text for images and diagrams
- Keyboard navigation support

### Visual Accessibility
- High contrast mode support
- Scalable text and interface elements
- Clear visual hierarchy

### Cognitive Accessibility
- Clear, simple language
- Consistent navigation patterns
- Progress indicators
- Optional extended time

## Quality Assurance

### Question Review Checklist
- [ ] Learning objective alignment
- [ ] Clear, unambiguous language
- [ ] Appropriate difficulty level
- [ ] Accurate correct answers
- [ ] Meaningful distractors
- [ ] Comprehensive feedback
- [ ] Accessibility compliance
- [ ] Technical functionality

### Validation Process
1. **Content Review**: Subject matter expert validation
2. **Clarity Review**: Plain language assessment
3. **Bias Review**: Cultural and linguistic sensitivity
4. **Technical Review**: Implementation testing
5. **Student Testing**: Pilot with sample students

## Usage Instructions

### Creating a New Quiz
1. Copy this template
2. Update quiz configuration
3. Add questions using appropriate templates
4. Validate all questions
5. Test implementation
6. Deploy to course platform

### Customization Options
- Question randomization
- Time limits
- Attempt limits
- Feedback timing
- Scoring methods
- Accessibility accommodations

This template ensures consistent, high-quality quizzes that support learning objectives while maintaining technical reliability and accessibility standards.