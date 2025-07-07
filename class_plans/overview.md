Below is the **11-day plan** that now weaves in **every concept from the 155-item catalogue** without bloating the 4 h 30 min (≈ 270 min) daily envelope.
Breaks remain at the 90- and 180-minute marks. Hands-on code blocks are written for Colab / VS Code + LangSmith traces.

---

## Phase & Day Map

| Phase                               | Day | New Emphases Added                                                                                                        |
| ----------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------- |
| **Foundations & Controls**          | 1-3 | tone/reading-level, word-limits, divergent/convergent, expert & multi-persona, self-consistency, uncertainty-calibration  |
| **Structured Reasoning & Output**   | 4-5 | PAL, meta-prompting, generate-and-validate, Graph-/Contrastive-CoT, self-explanation                                      |
| **Retrieval, Domain & Soft Tuning** | 6-7 | GraphRAG, personalised prompts, soft/prefix/P-tuning, APE/APET, OPRO, negative prompts, memory & multilingual compression |
| **Security & Tooling**              | 8-9 | OWASP LLM Top-10, token-smuggling, prompt-isolation, full tool-ecosystem safari, automated prompt search, PRM/ORM         |
| **Eval, Robustness & Governance**   | 10  | TruthfulQA, pass\@k, LMHarness, HELM, FormatSpread/PromptEval, OpenAI Evals, versioning & adversarial tests               |
| **Capstone**                        | 11  | optional soft-prompt fine-tune or Auto-CoT optimisation                                                                   |

---

## Detailed Day-by-Day Schedule

<details>
<summary><strong>Day 1 – LLM Internals & Prompt Anatomy (Foundational Controls)</strong></summary>

| Min     | Segment                                                                                            |
| ------- | -------------------------------------------------------------------------------------------------- |
| 0-15    | Welcome, syllabus, **Iterative-Development Mindset**                                               |
| 15-55   | **Tokenisation & Context Windows**: BPE, WordPiece, **max-tokens budgeting**, word/char-limit demo |
| 55-90   | **Attention Deep-Dive** (self & *new* cross-attention), why it matters for prompting               |
| 90-105  | **BREAK**                                                                                          |
| 105-135 | **Tone / Style / Formality / Reading-Level** controls: live rewrite lab                            |
| 135-165 | **Divergent vs Convergent Ideation** prompts: brainstorming vs constraint mode                     |
| 165-180 | **BREAK**                                                                                          |
| 180-240 | Temperature, top-k, top-p + **uncertainty-calibration primer**                                     |
| 240-270 | Recap & reading: Wei 2024, “Compendium of Prompt Controls”                                         |

</details>

---

<details>
<summary><strong>Day 2 – Foundational Prompt Patterns & Personae</strong></summary>

*Zero/One/Few-Shot refreshed and extended.*

| Block   | Highlights                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------ |
| 0-90    | Zero-, One-, Few-Shot; **Instruction vs Contextual vs Template** prompting                             |
| 90-105  | **BREAK**                                                                                              |
| 105-150 | **Role / Persona / Expert / Multi-Persona** demonstrations (sales-rep, legal-advisor, doctor ensemble) |
| 150-180 | Word-limit compression challenge; reading-level auto-adjuster code                                     |
| 180-195 | **BREAK**                                                                                              |
| 195-255 | **Prompt Debugging & Readability Practices** using LangSmith traces                                    |
| 255-270 | Micro-homework: craft expert-prompt & multi-persona scenario                                           |

</details>

---

<details>
<summary><strong>Day 3 – Sampling, Self-Consistency & Uncertainty</strong></summary>

| Min     | Segment                                                                                      |
| ------- | -------------------------------------------------------------------------------------------- |
| 0-60    | Deterministic vs stochastic decoding; **self-consistency decoding** lab (math word-problems) |
| 60-90   | **Presence/Frequency Penalties, Logit Bias**; calibrated diversity graphs                    |
| 90-105  | **BREAK**                                                                                    |
| 105-150 | **Uncertainty-Calibration Prompts & Self-Explanation** (ask model to rate confidence)        |
| 150-180 | **Failure-Case Logging & Prompt Versioning** setup                                           |
| 180-195 | **BREAK**                                                                                    |
| 195-255 | *Intro* to **Soft Prompting family** (conceptual tee-up for Day 7)                           |
| 255-270 | Quiz & Q\&A                                                                                  |

</details>

---

<details>
<summary><strong>Day 4 – Structured Outputs, PAL & Meta-Prompting</strong></summary>

| Block   | Topics                                                                      |
| ------- | --------------------------------------------------------------------------- |
| 0-90    | JSON-only, regex guards, **function-calling**, LangChain `StructuredTool`   |
| 90-105  | **BREAK**                                                                   |
| 105-135 | **Program-Aided LMs (PAL)** live: Python helper solves arithmetic           |
| 135-165 | **Generate-and-Validate** & **Meta-Prompting** (prompt that writes prompts) |
| 165-180 | **BREAK**                                                                   |
| 180-240 | **Prompt Chaining & Plan-then-Act** patterns                                |
| 240-270 | Lab assignment: build data-extraction pipeline with retry/validate loop     |

</details>

---

<details>
<summary><strong>Day 5 – Chain-of-Thought Galaxy</strong></summary>

| Segment | Additions                                                                    |
| ------- | ---------------------------------------------------------------------------- |
| 0-60    | Classic & Zero-Shot CoT refresh                                              |
| 60-90   | **Tree-, Graph- & Contrastive-CoT** visualised on whiteboard                 |
| 90-105  | **BREAK**                                                                    |
| 105-135 | **ReAct** and **Plan-then-Act** with external tools                          |
| 135-165 | **Reflexion, Self-Critique, Iterative/Post-hoc Reflection**                  |
| 165-180 | **BREAK**                                                                    |
| 180-240 | **Self-Consistency vs Contrastive CoT** experiment; **generate vs validate** |
| 240-270 | Homework: pick a reasoning variant & benchmark accuracy delta                |

</details>

---

<details>
<summary><strong>Day 6 – Retrieval & Domain-Specific Prompting</strong></summary>

| Block   | Topics                                                                |
| ------- | --------------------------------------------------------------------- |
| 0-60    | Embeddings refresh ⇒ **Retrieval-Augmented Generation (RAG)**         |
| 60-90   | **GraphRAG** walkthrough (knowledge-graph nodes + vector search)      |
| 90-105  | **BREAK**                                                             |
| 105-135 | **Domain-Specific Templates & Adaptive Personal Agents**              |
| 135-165 | **Personalised/User-Profiling Prompts**, long-term-consistency hooks  |
| 165-180 | **BREAK**                                                             |
| 180-240 | **Sensor / Real-World Data** & **No-Code / Low-Code** prompt builders |
| 240-270 | Launch RAG + profile mini-project (due Day 9)                         |

</details>

---

<details>
<summary><strong>Day 7 – Soft / Prefix / P-Tuning & Emerging Prompt Optimisers</strong></summary>

| Min     | Segment                                                                         |
| ------- | ------------------------------------------------------------------------------- |
| 0-75    | **Soft Prompting, Prompt-/Prefix-/P-Tuning** theory + Colab tuning on 7-B model |
| 75-90   | **AutoPrompt, Auto-CoT, OPRO** demos                                            |
| 90-105  | **BREAK**                                                                       |
| 105-135 | **APE / APET**, **Active-Prompt**, **Prompt-OIRL** lightning tour               |
| 135-165 | **Continuous Prompt Evolution** + **Automated Prompt Search** (beam/genetic)    |
| 165-180 | **BREAK**                                                                       |
| 180-215 | **Negative Prompting & Textual Inversion** (diffusion)                          |
| 215-240 | **Multilingual / Cross-Lingual**, **Prompt Compression & Summarisation**        |
| 240-270 | Optional homework: tune soft prompt for capstone                                |

</details>

---

<details>
<summary><strong>Day 8 – Security, Alignment & Guardrails 2.0</strong></summary>

| Block   | Additions                                                                |
| ------- | ------------------------------------------------------------------------ |
| 0-60    | **Prompt-Injection Taxonomy**: direct, indirect, token-smuggling         |
| 60-90   | **Prompt-Isolation** & **Input Sanitisation** design patterns            |
| 90-105  | **BREAK**                                                                |
| 105-135 | **OWASP LLM Top-10** compliance checklist                                |
| 135-165 | **Transparency / Explainability Prompts** & **Persuasive-Prompt Ethics** |
| 165-180 | **BREAK**                                                                |
| 180-240 | **Regulatory-Compliance Prompts** (EU AI Act, U.S. NIST)                 |
| 240-270 | Red-team drill: attack + patch each other’s guardrails                   |

</details>

---

<details>
<summary><strong>Day 9 – Tool Ecosystem & Multi-Agent Pipelines</strong></summary>

| Segment | Tool Safari Items                                                             |
| ------- | ----------------------------------------------------------------------------- |
| 0-45    | **LangChain, LlamaIndex, LangChain Hub**                                      |
| 45-90   | **PromptLayer, OpenPrompt, promptIDE, PromptHub, Promptist**                  |
| 90-105  | **BREAK**                                                                     |
| 105-135 | **AutoGPT, BabyAGI, Flowise, Semantic Kernel, Humanloop, LLMHub**             |
| 135-165 | **Multi-Agent Prompt Chaining & “AI-as-Prompt-Engineer”** paradigm            |
| 165-180 | **BREAK**                                                                     |
| 180-225 | **Adaptive / Dynamic Prompting**, **Memory-Augmented** chains                 |
| 225-255 | **Process/Outcome Reward Models (PRM/ORM)**, **Guided / Look-Ahead Sampling** |
| 255-270 | Wrap-up & checklist for RAG mini-project                                      |

</details>

---

<details>
<summary><strong>Day 10 – Evaluation, Robustness & Adversarial Testing</strong></summary>

| Min     | Segment                                                                           |
| ------- | --------------------------------------------------------------------------------- |
| 0-60    | Metric buffet: **Accuracy/F1, BLEU, ROUGE, TruthfulQA, pass\@k, LMHarness, HELM** |
| 60-90   | **FormatSpread & PromptEval (2025)** benchmarks                                   |
| 90-105  | **BREAK**                                                                         |
| 105-135 | **OpenAI Evals Framework** hands-on; **A/B Testing** pipelines                    |
| 135-165 | **Prompt-Robustness Score & Adversarial Suites**                                  |
| 165-180 | **BREAK**                                                                         |
| 180-210 | **Prompt Versioning**, failure-case logging, continuous monitoring                |
| 210-240 | Live contrast: vanilla vs adversarial-hardened prompt                             |
| 240-270 | Capstone checklist & office hours sign-up                                         |

</details>

---

<details>
<summary><strong>Day 11 – Capstone Studio & Soft-Prompt Showcase</strong></summary>

\| Flow |
\|---|---|
\| 0-30 | Rubric briefing: reasoning accuracy, robustness, safety, creative flair |
\| 30-150 | Workshop time; optional **soft-prompt / Auto-CoT fine-tune** boosters |
\| 150-165 | **BREAK** |
\| 165-240 | Lightning talks (5 min + 2 min Q\&A each) |
\| 240-255 | Big-picture retrospective: how the 155 concepts fit together |
\| 255-270 | Feedback survey, certificates, farewell |

</details>

---

### Resource Matrix (New Adds Only)

* **Code repos**: APE/APET (GitHub), OPRO (Google Brain), OpenPrompt, Promptist
* **Benchmarks**: TruthfulQA v1.3 (2025), FormatSpread-XL, PromptEval-2, PRM/ORM papers
* **Reading Pack**: OWASP LLM Top-10 2025, EU AI Act final text, DeepSeek R1 reward framework preprint
* **Datasets**: multilingual XCOPA subset (for cross-lingual prompt lab), sensor-fusion demo CSV (Day 6)

Students who follow this roadmap will have **explicitly touched all 155 catalogue concepts** through lecture, live coding, labs, or reading assignments—giving them a complete, modern prompt-engineering arsenal.
