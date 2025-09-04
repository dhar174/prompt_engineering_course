# Day 2 — Tokenization & Context Windows Deep Dive

> **Theme:** *How LLMs "See" Text: Understanding the Fundamental Processing Unit*

**Duration:** 135 minutes | **Focus:** Deep understanding of tokenization, context windows, and their implications for prompt engineering

---

## Overview

Day 2 provides a comprehensive exploration of how language models process text through tokenization. Students gain crucial understanding of the fundamental unit that drives all LLM behavior, learning to count tokens, manage context limits, and design prompts that work within model constraints.

### Learning Objectives

By the end of Day 2, students will be able to:
1. **Understand tokenization algorithms** (BPE, WordPiece, SentencePiece) and their differences
2. **Count tokens accurately** using tools like tiktoken for different models
3. **Manage context windows** effectively for long-form and complex prompts
4. **Design token-efficient prompts** that maximize information within limits
5. **Debug tokenization issues** that affect prompt performance

---

## Session Timeline

### 0–30 min | Recap & Day Overview

**Bridge from Day 1:**
* From high-level LLM concepts to implementation details
* Why understanding tokenization matters for prompt engineering
* Connection between model behavior and text processing

**Day 2 Agenda:**
* Tokenization fundamentals and algorithms
* Hands-on token counting and visualization
* Context window management strategies
* Practical implications for prompt design

**Key Questions to Explore:**
- Why do models sometimes fail on simple tasks?
- How does text length affect model performance?
- What's the difference between characters, words, and tokens?

---

### 30–60 min | Tokenization Algorithms Deep Dive

**Tokenization Fundamentals:**
* What are tokens? (not words, not characters, but subword units)
* Why subword tokenization? (vocabulary size vs. expressiveness trade-off)
* Impact on model performance and behavior

**Algorithm Comparison:**

**Byte Pair Encoding (BPE):**
* Most common approach (GPT models)
* Merging frequent character pairs
* Handling out-of-vocabulary words
* Advantages and limitations

**WordPiece:**
* Google's approach (BERT family)
* Likelihood-based merging
* Subword unit selection
* Differences from BPE

**SentencePiece:**
* Language-agnostic approach
* Unicode normalization
* Multilingual considerations
* Use in T5 and other models

**Live Demonstration:**
```python
import tiktoken

# Compare tokenization across models
text = "Hello, world! How are you today?"
gpt4_enc = tiktoken.encoding_for_model("gpt-4")
gpt35_enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

print("GPT-4 tokens:", gpt4_enc.encode(text))
print("GPT-3.5 tokens:", gpt35_enc.encode(text))
```

---

### 60–90 min | Context Windows & Token Budgeting

**Context Window Concepts:**
* What is a context window? (input + output token limit)
* Model-specific limits (GPT-3.5: 4K, GPT-4: 8K/32K, etc.)
* How context affects performance (attention degradation)

**Token Budgeting Strategies:**
* Input vs. output token allocation
* Prompt compression techniques
* Strategic information prioritization
* Dynamic content truncation

**Practical Implications:**
* Long document processing
* Conversation maintenance
* Multi-turn dialog management
* Batch processing considerations

**Budget Planning Exercise:**
Students practice allocating tokens for:
- System prompts
- User input
- Examples and context
- Expected output length
- Safety margins

**Context Window Visualization:**
```
[System Prompt: 50 tokens] [Examples: 200 tokens] [User Input: 300 tokens] [Response: 400 tokens]
├─────────── Input Budget: 550 tokens ──────────┤ ├─ Output: 400 ─┤
└─────────────────── Total Context: 950 tokens ─────────────────┘
```

---

### 90–105 min | BREAK

---

### 105–135 min | Hands-On Lab: Token Counting & Model Comparison

**Lab Activities:**

**Activity 1: Token Counting Mastery**
* Use tiktoken to count tokens for various text types
* Compare counts across different models
* Identify tokenization surprises and edge cases
* Practice estimating token counts without tools

**Activity 2: Context Window Experiments**
* Design prompts that approach context limits
* Test behavior near and at context boundaries
* Explore truncation strategies and effects
* Measure performance degradation with context length

**Activity 3: Token-Efficient Prompt Design**
* Take verbose prompts and optimize for token count
* Maintain clarity while reducing token usage
* Compare effectiveness of original vs. optimized versions
* Develop personal tokenization best practices

**Activity 4: Cross-Model Tokenization Analysis**
* Compare how different models tokenize the same text
* Identify model-specific tokenization quirks
* Understand implications for prompt portability
* Document findings for future reference

**Tools and Resources:**
* Enhanced `tokenization_playground.ipynb`
* Token counting utilities and helpers
* Visual tokenization tools
* Cross-model comparison scripts

**Deliverable:**
Students create a "tokenization cheat sheet" with:
- Personal token estimation guidelines
- Model-specific tokenization notes
- Common tokenization pitfalls to avoid
- Token optimization strategies

---

## Materials Provided

### Enhanced Notebooks
* `tokenization_playground.ipynb` - Comprehensive tokenization exploration
* `context_window_management.ipynb` - Advanced context handling techniques
* `token_optimization_lab.ipynb` - Prompt efficiency workshop

### Tools & Utilities
* Cross-model tokenization comparison tool
* Token counting and estimation utilities
* Context window visualization tools
* Token budget planning templates

### Reference Materials
* `Token_Count_Reference.md` - Updated with comprehensive model comparison
* Tokenization algorithm comparison guide
* Context window best practices
* Token optimization strategies guide

---

## Homework Assignment

**Project:** Token-Efficient Prompt Library
Create a collection of optimized prompts for common tasks:
* Compare verbose vs. optimized versions
* Measure token savings while maintaining effectiveness
* Document optimization strategies used
* Test across multiple models if possible

**Analysis Component:**
* Token count analysis and comparison
* Effectiveness measurement methodology
* Optimization technique documentation
* Recommendations for future prompt design

---

## Connection to Course Arc

**Foundation for Future Days:**
- Token understanding enables effective prompt design (Days 3-6)
- Context management crucial for complex applications (Days 13-24)
- Efficiency principles support advanced techniques

**Previous Day Integration:**
- Builds on LLM fundamentals from Day 1
- Provides concrete implementation details for abstract concepts

**Next Day Preparation:**
- Token knowledge enables understanding of attention mechanisms (Day 3)
- Context management supports model internals exploration

This deep understanding of tokenization and context windows provides the essential technical foundation for all subsequent prompt engineering techniques and applications.

---

## Success Metrics

Students successfully completing Day 2 will demonstrate:
- Accurate token counting for various text types
- Understanding of tokenization algorithm differences
- Effective context window management strategies
- Ability to optimize prompts for token efficiency
- Awareness of tokenization implications for prompt design

This tokenization mastery is crucial for effective prompt engineering across all model types and applications covered in the remainder of the course.