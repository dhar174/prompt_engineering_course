# 24-Day Prompt Engineering Course Overview

Below is the **expanded 24-day plan** that thoughtfully restructures the original 12-day intensive curriculum into a more manageable and pedagogically sound learning experience. Each day now contains approximately 135 minutes (2.25 hours) of content, allowing for deeper exploration, better retention, and enhanced practical application.

---

## Phase & Day Map

| Phase                               | Days   | New Emphases Added                                                                                                        |
| ----------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------- |
| **Foundations & Core Concepts**     | 1-6    | LLM basics, tokenization deep dive, attention mechanisms, style controls, decoding parameters, debugging practice        |
| **Prompt Patterns & Personas**     | 7-12   | Shot patterns, role engineering, expert personas, template modularity, self-consistency, advanced debugging              |
| **Structured & Reasoning**         | 13-18  | Structured outputs, function calling, PAL, meta-prompting, CoT foundations, advanced CoT variants                        |
| **Retrieval & Specialization**     | 19-20  | RAG systems, GraphRAG, domain-specific prompting, personalization                                                        |
| **Advanced Techniques**            | 21-22  | Soft prompting, automated optimization, security, safety, guardrails                                                     |
| **Production & Evaluation**        | 23-24  | Tool ecosystems, multi-agent systems, evaluation, deployment, future directions                                          |

---

## Detailed 24-Day Schedule

<details>
<summary><strong>Phase 1: Foundations & Core Concepts (Days 1-6)</strong></summary>

### Day 1 – Course Introduction & LLM Fundamentals
**Duration:** 135 minutes | **Theme:** Setting the Foundation

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-15    | Welcome, syllabus, course goals, iterative-development mindset          |
| 15-45   | Prompt Engineering landscape 2025, skills, jobs, applications           |
| 45-75   | What are LLMs? Basic architecture overview, why prompts matter          |
| 75-90   | **BREAK**                                                                |
| 90-120  | First prompt exercise: exploring model behavior                          |
| 120-135 | Homework setup, preview of Day 2                                        |

### Day 2 – Tokenization & Context Windows Deep Dive
**Duration:** 135 minutes | **Theme:** How LLMs "See" Text

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap & day overview                                                     |
| 30-60   | Tokenization deep dive: BPE, WordPiece, SentencePiece                   |
| 60-90   | Context windows, token budgeting, practical implications                |
| 90-105  | **BREAK**                                                                |
| 105-135 | Hands-on lab: Token counting with tiktoken, comparing models            |

### Day 3 – Model Internals & Attention Mechanisms
**Duration:** 135 minutes | **Theme:** Understanding the Engine

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap tokenization concepts                                              |
| 30-75   | Attention mechanisms: self-attention, cross-attention, prompting impact |
| 75-90   | **BREAK**                                                                |
| 90-120  | Model architecture implications for prompt design                        |
| 120-135 | Interactive exploration: attention visualization tools                   |

### Day 4 – Basic Prompt Controls & Style Management
**Duration:** 135 minutes | **Theme:** Controlling Output Quality

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap & bridge to practical prompting                                   |
| 30-75   | Tone, style, formality controls with live demonstrations                |
| 75-90   | **BREAK**                                                                |
| 90-120  | Reading level adjustment, audience targeting                             |
| 120-135 | Style transfer lab: same content, multiple styles                       |

### Day 5 – Decoding Parameters & Sampling Strategies
**Duration:** 135 minutes | **Theme:** Fine-Tuning Generation Behavior

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap style controls                                                     |
| 30-75   | Temperature, top-k, top-p: theory and practice                          |
| 75-90   | **BREAK**                                                                |
| 90-120  | Presence/frequency penalties, logit bias                                |
| 120-135 | Hands-on parameter tuning lab                                           |

### Day 6 – Foundations Review & Debugging Practice
**Duration:** 135 minutes | **Theme:** Consolidation & Troubleshooting

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Comprehensive review of Days 1-5                                        |
| 30-60   | Common prompt failures and debugging strategies                         |
| 60-90   | Hands-on debugging workshop                                             |
| 90-105  | **BREAK**                                                                |
| 105-135 | Mini-project: Design complete prompt solution using foundations         |

</details>

---

<details>
<summary><strong>Phase 2: Prompt Patterns & Personas (Days 7-12)</strong></summary>

### Day 7 – Zero/One/Few-Shot Prompting Patterns
**Duration:** 135 minutes | **Theme:** Learning from Examples

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Introduction to shot-based prompting                                     |
| 30-75   | Zero-shot prompting: when and how to use                                |
| 75-90   | **BREAK**                                                                |
| 90-120  | One-shot and few-shot patterns, example selection strategies            |
| 120-135 | Comparative lab: shot patterns for different tasks                      |

### Day 8 – Role & Persona Engineering
**Duration:** 135 minutes | **Theme:** Identity and Perspective

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap shot patterns, introduce persona concepts                         |
| 30-75   | Role prompting: expert roles, professional personas                     |
| 75-90   | **BREAK**                                                                |
| 90-120  | Persona consistency, character development                               |
| 120-135 | Role-playing lab: create and test personas                              |

### Day 9 – Expert & Multi-Persona Scenarios
**Duration:** 135 minutes | **Theme:** Advanced Character Interaction

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap single personas                                                    |
| 30-75   | Expert persona engineering: domain specialists                          |
| 75-90   | **BREAK**                                                                |
| 90-120  | Multi-persona scenarios: debates, collaborations                        |
| 120-135 | Multi-persona project: expert panel simulation                          |

### Day 10 – Template Engineering & Modularity
**Duration:** 135 minutes | **Theme:** Reusable Prompt Architecture

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap persona work, introduce modularity                                |
| 30-75   | Prompt templates: structure, placeholders, reusability                  |
| 75-90   | **BREAK**                                                                |
| 90-120  | Modular prompt blocks, component libraries                              |
| 120-135 | Template building lab: create reusable components                       |

### Day 11 – Self-Consistency & Uncertainty Calibration
**Duration:** 135 minutes | **Theme:** Reliability and Confidence

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap templates, introduce reliability concepts                         |
| 30-75   | Self-consistency decoding, multiple sampling                            |
| 75-90   | **BREAK**                                                                |
| 90-120  | Uncertainty calibration, confidence estimation                          |
| 120-135 | Reliability lab: measuring and improving consistency                     |

### Day 12 – Patterns Review & Advanced Debugging
**Duration:** 135 minutes | **Theme:** Mastery and Troubleshooting

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Comprehensive review of prompt patterns                                 |
| 30-60   | Advanced debugging techniques                                           |
| 60-90   | Pattern combination strategies                                          |
| 90-105  | **BREAK**                                                                |
| 105-135 | Capstone exercise: complex prompt solution design                       |

</details>

---

<details>
<summary><strong>Phase 3: Structured Outputs & Reasoning (Days 13-18)</strong></summary>

### Day 13 – Structured Outputs & Validation
**Duration:** 135 minutes | **Theme:** Reliable Data Extraction

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Introduction to structured outputs                                       |
| 30-75   | JSON, XML, YAML generation and validation                               |
| 75-90   | **BREAK**                                                                |
| 90-120  | Schema enforcement, error handling                                       |
| 120-135 | Structured output lab: data extraction pipeline                         |

### Day 14 – Function Calling & Tool Integration
**Duration:** 135 minutes | **Theme:** LLMs as System Components

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap structured outputs                                                 |
| 30-75   | Function calling concepts, OpenAI function calling                      |
| 75-90   | **BREAK**                                                                |
| 90-120  | Tool integration patterns, API connectivity                             |
| 120-135 | Function calling lab: build a tool-using agent                          |

### Day 15 – Program-Aided Language Models (PAL)
**Duration:** 135 minutes | **Theme:** Hybrid Reasoning Systems

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap function calling                                                   |
| 30-75   | PAL concepts: code generation for reasoning                              |
| 75-90   | **BREAK**                                                                |
| 90-120  | Python helper patterns, mathematical reasoning                           |
| 120-135 | PAL lab: arithmetic and logical reasoning                               |

### Day 16 – Meta-Prompting & Prompt Chaining
**Duration:** 135 minutes | **Theme:** Prompts Creating Prompts

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap PAL concepts                                                       |
| 30-75   | Meta-prompting: prompts that write prompts                              |
| 75-90   | **BREAK**                                                                |
| 90-120  | Prompt chaining, sequential processing                                   |
| 120-135 | Meta-prompting lab: automated prompt generation                         |

### Day 17 – Chain-of-Thought Foundations
**Duration:** 135 minutes | **Theme:** Step-by-Step Reasoning

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Introduction to reasoning patterns                                       |
| 30-75   | Classic CoT, zero-shot CoT fundamentals                                 |
| 75-90   | **BREAK**                                                                |
| 90-120  | Reasoning quality assessment, step validation                           |
| 120-135 | CoT lab: reasoning problem solving                                       |

### Day 18 – Advanced CoT Variants
**Duration:** 135 minutes | **Theme:** Sophisticated Reasoning Patterns

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap basic CoT                                                          |
| 30-75   | Tree-of-Thought, Graph-of-Thought variants                              |
| 75-90   | **BREAK**                                                                |
| 90-120  | Contrastive CoT, self-critique patterns                                 |
| 120-135 | Advanced reasoning lab: complex problem solving                          |

</details>

---

<details>
<summary><strong>Phase 4: Retrieval & Specialization (Days 19-20)</strong></summary>

### Day 19 – Retrieval-Augmented Generation (RAG)
**Duration:** 135 minutes | **Theme:** Knowledge Integration

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Introduction to RAG concepts                                             |
| 30-75   | Embedding-based retrieval, vector databases                             |
| 75-90   | **BREAK**                                                                |
| 90-120  | GraphRAG, hybrid retrieval approaches                                   |
| 120-135 | RAG lab: build a knowledge-enhanced system                              |

### Day 20 – Domain-Specific & Personalized Prompting
**Duration:** 135 minutes | **Theme:** Specialized Applications

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Recap RAG systems                                                        |
| 30-75   | Domain-specific prompt engineering                                       |
| 75-90   | **BREAK**                                                                |
| 90-120  | Personalized prompting, user profiling                                  |
| 120-135 | Specialization lab: domain-specific solution                            |

</details>

---

<details>
<summary><strong>Phase 5: Advanced Techniques (Days 21-22)</strong></summary>

### Day 21 – Soft Prompting & Automated Optimization
**Duration:** 135 minutes | **Theme:** Learning to Prompt

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Introduction to automated prompting                                      |
| 30-75   | Soft prompting, prompt tuning concepts                                  |
| 75-90   | **BREAK**                                                                |
| 90-120  | AutoPrompt, OPRO, evolutionary approaches                               |
| 120-135 | Optimization lab: automated prompt improvement                           |

### Day 22 – Security, Safety & Guardrails
**Duration:** 135 minutes | **Theme:** Responsible AI Implementation

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Security threats in prompt engineering                                  |
| 30-75   | Prompt injection, jailbreaking, defense strategies                      |
| 75-90   | **BREAK**                                                                |
| 90-120  | Safety guardrails, content filtering                                    |
| 120-135 | Security lab: attack and defense scenarios                              |

</details>

---

<details>
<summary><strong>Phase 6: Production & Evaluation (Days 23-24)</strong></summary>

### Day 23 – Tool Ecosystems & Multi-Agent Systems
**Duration:** 135 minutes | **Theme:** Production-Scale Systems

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Overview of production considerations                                    |
| 30-75   | Tool ecosystem tour: LangChain, LlamaIndex, etc.                        |
| 75-90   | **BREAK**                                                                |
| 90-120  | Multi-agent architectures, agent coordination                           |
| 120-135 | Production lab: scalable prompt system                                   |

### Day 24 – Evaluation, Deployment & Future Directions
**Duration:** 135 minutes | **Theme:** Measurement and Growth

| Min     | Segment                                                                  |
| ------- | ------------------------------------------------------------------------ |
| 0-30    | Evaluation methodologies                                                 |
| 30-75   | Metrics, benchmarking, continuous improvement                           |
| 75-90   | **BREAK**                                                                |
| 90-120  | Deployment strategies, monitoring                                        |
| 120-135 | Course synthesis, future learning paths                                  |

</details>

---

## Key Improvements in 24-Day Structure

### Enhanced Learning Experience
- **Reduced Cognitive Load**: 135 minutes vs. 270 minutes per session
- **Better Retention**: Spaced learning with regular review sessions
- **Deeper Practice**: More hands-on time for skill development
- **Natural Progression**: Logical breakpoints and smooth transitions
- **Reflection Opportunities**: Dedicated consolidation sessions

### Pedagogical Benefits
- **Scaffolded Learning**: Gradual complexity increase with solid foundations
- **Mastery-Based Progression**: Clear achievement markers at each phase
- **Real-World Application**: Extended project time and practical exercises
- **Flexible Scheduling**: Accommodates various learning schedules
- **Assessment Opportunities**: More granular progress tracking

### Content Enhancements
- **Foundational Depth**: Expanded coverage of core concepts
- **Practice Integration**: Dedicated labs and workshops
- **Review Sessions**: Systematic knowledge consolidation
- **Advanced Applications**: Enhanced coverage of cutting-edge techniques
- **Future Preparation**: Clear pathways for continued learning

---

## Resource Matrix

### Core Materials (Enhanced)
* **Interactive Notebooks**: Expanded with additional exercises and examples
* **Code Libraries**: Modular prompt components and utilities
* **Reference Guides**: Comprehensive best practices and troubleshooting
* **Assessment Tools**: Progress tracking and skill validation

### New Additions
* **Foundation Labs**: Hands-on exploration of core concepts
* **Review Workshops**: Systematic knowledge consolidation sessions
* **Project Templates**: Scaffolded assignments for practical application
* **Integration Examples**: Real-world system implementations

Students following this enhanced 24-day roadmap will develop comprehensive prompt engineering expertise through a well-paced, pedagogically sound learning experience that maintains all original objectives while significantly improving depth, retention, and practical application capabilities.