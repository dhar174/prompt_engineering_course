
## Prompt Engineering • Day 12 – “Quality Assurance, Interop, Active-Learning & Release Radar”

| Time (min)  | Segment                                                                                                                                                                                | Gaps Closed (concept #)                                        |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **0-15**    | **Orientation & QA Mind-Set**  <br>• Why “shipping quality” ≠ “demo quality”                                                                                                           | –                                                              |
| **15-45**   | **Test-Driven Prompting Workshop**  <br>• Write formal *unit tests* for prompts  <br>• Red/green cycle: prompt fails → refactor → pass                                                 | Test-Driven Prompting (82) · Refactoring & Explanation (83)    |
| **45-70**   | **Misunderstanding & Ambiguity Lab**  <br>• Catalog 5 common failure causes  <br>• “Rubber-duck” debugging prompts                                                                     | Misunderstandings (95)                                         |
| **70-90**   | **Cross-Model Interoperability Demo**  <br>• Same prompt on GPT-4o-mini, Llama-3-8B, Mistral-7B  <br>• How to normalize outputs / fallbacks                                            | Interoperability (100)                                         |
| **90-105**  | **BREAK**                                                                                                                                                                              |                                                                |
| **105-135** | **Active-Learning Loops & Prompt Retraining**  <br>• Real-time thumbs-up/down feedback → replay buffer  <br>• Tie-in to PRM / ORM & **DeepSeek R1** case study                         | Active-Learning (106) · DeepSeek R1 & Process-Reward Opt (151) |
| **135-160** | **Traceable Reasoning & Audit Trails**  <br>• Build a prompt that emits structured reasoning + hash  <br>• Store chain-of-thought & hashes for compliance                              | Traceable Reasoning (117)                                      |
| **160-180** | **BREAK**                                                                                                                                                                              |                                                                |
| **180-210** | **Search-Integrated Deep-Research Prompting**  <br>• Live agent that calls Web search/API, cites sources  <br>• Compare answer quality with/without retrieval                          | Search + Deep Research (154)                                   |
| **210-225** | **Prompt Authoring GUI Speed-Tour**  <br>• promptIDE, Promptist Optimizer, and PromptHub hands-on                                                                                      | Prompt Authoring Tools (104)                                   |
| **225-245** | **Model-Release Radar**  <br>• Qwen-2 series & fine-tune quirks  <br>• Tiny vs Huge (o3-mini vs 70-B) cost/latency trade-offs                                                          | Qwen Family Updates (155)                                      |
| **245-260** | **AI Rhetoric & Persuasion Ethics Sprint**  <br>• Identify persuasive devices in a marketing prompt  <br>• Revise to meet ethical guidelines                                           | AI Rhetoric & Persuasion (157)                                 |
| **260-270** | **Final Synthesis & Launchpad**  <br>• Show master checklist → every box ticked  <br>• Next-step roadmap: publish to Hub, set up active-learning dashboards, follow new model releases | –                                                              |

---

### Key Take-Home Assets

| Asset                                              | Purpose                                                                     |
| -------------------------------------------------- | --------------------------------------------------------------------------- |
| **`prompt_test_suite.py`**                         | Tiny pytest-style harness for test-driven prompts                           |
| **Interoperability Cheat-sheet**                   | Temperature / stop-token settings that port well across GPT, Mistral, Llama |
| **Active-Learning Template (LangChain + SQLlite)** | Plug-and-play feedback loop                                                 |
| **Traceable-Reasoning JSON schema**                | Standard for hashed CoT + evidence                                          |
| **Release-Radar RSS/Feed list**                    | Stay current on Qwen / DeepSeek / OpenAI drops                              |
| **Ethical-Persuasion Checklist**                   | Guardrails for marketing / rhetoric prompts                                 |

### Outcome

After Day 12 every one of the 163 catalogue concepts has been:

* **Explained** in lecture or lightning talk
* **Demonstrated** live or in code
* **Exercised** by students in at least a mini-lab

Students leave with a **quality-assured, cross-model-ready, actively-learning prompt pipeline** and the literacy to keep pace with monthly model releases and research papers.
