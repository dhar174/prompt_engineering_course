# Notebook Sanity Checks Report

This report summarizes the high-level conceptual sanity checks performed on the Jupyter notebooks in this repository.

## Notebooks Reviewed:

*   `Lab1_Chaining_and_Orchestration.ipynb`
*   `Lab2_Multi_Agent_Workflows.ipynb`
*   `Lab3_Logging_Deployment_Eval.ipynb`
*   `LangGraph_Chatbot.ipynb`
*   `chatbot_with_memory.ipynb`
*   `day7_auto_prompt_opro.ipynb`
*   `day7_embedding_prompt_lab.ipynb`
*   `day7_multilingual_lab.ipynb`
*   `day7_negative_prompting.ipynb`
*   `day7_soft_prompt_tuning.ipynb`
*   `day8_adversarial_robustness_logging.ipynb`
*   `day8_bias_alignment_constitutional.ipynb`
*   `day8_guardrails_moderation.ipynb`
*   `day8_moderation_toolkits.ipynb`
*   `day8_privacy_consent_regulatory.ipynb`
*   `day8_prompt_injection_jailbreak.ipynb`
*   `decoding_parameters_playground.ipynb`
*   `decoding_strategies_playground.ipynb`
*   `function_calling_demo.ipynb`
*   `index.ipynb`
*   `modular_prompt_library_builder.ipynb`
*   `pal_plan_act_pipeline.ipynb`
*   `persona_roleplay_workbench.ipynb`
*   `prompt_anatomy_template.ipynb`
*   `prompt_versioning_failure_log.ipynb`
*   `prompt_versioning_tracker.ipynb`
*   `self_consistency_uncertainty.ipynb`
*   `shot_prompt_patterns.ipynb`
*   `structured_output_validation.ipynb`
*   `tokenization_playground.ipynb`

**Note:** Notebooks ending with `_a.ipynb` (e.g., `day8_adversarial_robustness_logging_a.ipynb`) were found to be duplicates of their counterparts without the `_a` suffix and are not separately detailed.

---

## Detailed Findings:

### 1. `Lab1_Chaining_and_Orchestration.ipynb`
*   **Purpose:** Demonstrates building modular prompt pipelines using LangChain (linear chains, graph orchestration).
*   **Sanity Check:** Clear objectives, logical flow, installs dependencies (`langchain openai tiktoken`), handles OpenAI API key. Prefect example is commented out (optional).
*   **Conceptual Issues:** None apparent.

### 2. `Lab2_Multi_Agent_Workflows.ipynb`
*   **Purpose:** Introduces multi-agent design with LangChain Agents (tool-use, memory, delegation).
*   **Sanity Check:** Clear objectives, installs dependencies (`langchain openai`), uses `serpapi` for search (OpenAI key handled, SerpAPI key implicit). Builds researcher/critic example.
*   **Conceptual Issues:**
    *   Use of `serpapi` tool will require users to have a SerpAPI key configured; this is not explicitly prompted for.

### 3. `Lab3_Logging_Deployment_Eval.ipynb`
*   **Purpose:** Covers logging (PromptLayer), deployment (FastAPI sketch), and evaluation (OpenAI Evals concept).
*   **Sanity Check:** Clear objectives, installs dependencies (`promptlayer openai langchain`), handles PromptLayer API key. FastAPI and OpenAI Evals parts are conceptual/commented out.
*   **Conceptual Issues:** None apparent. Assumes PromptLayer API key availability.

### 4. `LangGraph_Chatbot.ipynb`
*   **Purpose:** Demonstrates a LangGraph-based chatbot with long-term memory (FAISS), agentic behavior, and streaming.
*   **Sanity Check:** Clear intro, installs dependencies (`langgraph langchain-openai langchain-community tiktoken`). FAISS index creation/loading logic. Defines tools, constructs LangGraph.
*   **Conceptual Issues:**
    *   OpenAI API key setup `set_env('OPENAI_API_KEY')` is defined but the call is commented out; relies on pre-set env var or other means.
    *   `FAISS_INDEX_PATH` defaults to `./faiss_index` (local directory creation).
    *   Mocked `search` tool is very basic.
    *   `logging.error` is used in `upsert_memory` but `logging` module is not explicitly imported there or globally.

### 5. `chatbot_with_memory.ipynb`
*   **Purpose:** Builds a chatbot with memory using LangChain and LangGraph, showing context maintenance.
*   **Sanity Check:** Colab-specific API key handling (`userdata.get`). Progressively builds memory concepts: stateless, manual history, LangGraph `MemorySaver`, `thread_id`, custom prompts, message trimming, streaming.
*   **Conceptual Issues:**
    *   Dependency installation cell is messy (many commented lines).
    *   `userdata.get('OPENAI_API_KEY')` is Colab-specific.
    *   Streaming example at the end with `language = "English"` produces Swahili output, indicating a potential issue in prompt application or an error in the example itself.

### 6. `day7_auto_prompt_opro.ipynb`
*   **Purpose:** Demonstrates AutoPrompt (gradient-based token insertion) and OPRO (search for chain-of-thought prompts).
*   **Sanity Check:** Clear goal, installs dependencies. AutoPrompt uses BERT for sentiment. OPRO uses GPT-2 for arithmetic, with an evolutionary search and a `trl` PPO loop.
*   **Conceptual Issues:**
    *   OPRO `evaluate` function's number parsing (`int(re.findall(r'\d+', ans)[0])`) could fail if no digits are in the output.
    *   PPO `max_steps=30` is likely too short for optimal results (demo purposes).
    *   `RewardConfig` output dir `reward_tmp` will be created.

### 7. `day7_embedding_prompt_lab.ipynb`
*   **Purpose:** Builds a mini RAG pipeline in one prompt using FAISS, sentence-transformers, and GPT-2.
*   **Sanity Check:** Clear goal, installs dependencies. Creates toy knowledge base, FAISS index. Compares answers with/without retrieval. Includes a memory buffer extension.
*   **Conceptual Issues:**
    *   Small knowledge base (4 docs).
    *   Answer parsing `split('Answer:')[-1]` can be brittle.
    *   The "NEW" `buffered_answer` function prepares `buffer_text` but doesn't seem to directly use it in its immediate call to the `answer` function, which reconstructs its own prompt. The buffer is updated for future calls.

### 8. `day7_multilingual_lab.ipynb`
*   **Purpose:** Demonstrates multilingual/cross-lingual prompting with `google/mt5-base`.
*   **Sanity Check:** Clear purpose, installs dependencies. Uses `mt5-base` for translation and Q&A by prefixing tasks (e.g., "translate English to Spanish:").
*   **Conceptual Issues:**
    *   `generate` function's `lang_tag` default parameter is unused; language control is via prompt text.
    *   Summarization for English passes raw headline; a "summarize:" prefix might be more standard for T5.

### 9. `day7_negative_prompting.ipynb`
*   **Purpose:** Shows negative prompts with Stable Diffusion XL and training textual inversion.
*   **Sanity Check:** Clear goals, installs diffusers, loads SDXL (GPU needed). Demonstrates negative prompts.
*   **Conceptual Issues:**
    *   **Major:** Textual Inversion part (`ti_pipe.learn_new_concept`) uses a non-existent simplified API. Actual textual inversion training is more complex and usually involves dedicated scripts. This section is unlikely to work as written.

### 10. `day7_soft_prompt_tuning.ipynb`
*   **Purpose:** Demonstrates soft prompting (Prompt Tuning, P-Tuning v2) with PEFT library on GPT-2 for sentiment analysis.
*   **Sanity Check:** Clear goal, installs dependencies. Uses GPT-2 (8-bit), SST-2. Configures `PromptTuningConfig`, trains a few steps. Includes evaluation metric and t-SNE visualization of virtual tokens.
*   **Conceptual Issues:**
    *   Evaluation metric relies on `generate` function's print output and `split()[-1]`, which is slightly indirect.
    *   t-SNE `perplexity=5` might need tuning for 20 tokens.

### 11. `day8_adversarial_robustness_logging.ipynb`
*   **Purpose:** Red-team prompts, log interactions (JSONL), apply patches to improve robustness.
*   **Sanity Check:** Clear objective, installs `openai`. Simple logger. `test_prompt` calls GPT-3.5-Turbo. Shows patching example.
*   **Conceptual Issues:**
    *   `test_prompt` combines system prompt and user attack into the `system` role message content, which is unusual.
    *   `LOG_FILE` created in CWD.

### 12. `day8_bias_alignment_constitutional.ipynb`
*   **Purpose:** Apply bias-reduction and Constitutional AI principles via prompting.
*   **Sanity Check:** Clear objective, installs `openai`. Uses system prompts for bias reduction, constitutional rules, and transparency (explainability).
*   **Conceptual Issues:** Prompt-based techniques; effectiveness varies. No quantitative evaluation.

### 13. `day8_guardrails_moderation.ipynb`
*   **Purpose:** Implement defenses: input sanitization, prompt isolation, output moderation (OpenAI Moderation API).
*   **Sanity Check:** Clear objective, installs `openai`. `sanitize_input` removes keywords and some Unicode. `isolated_chat` combines sanitization with system prompt. `moderate` uses Moderation API.
*   **Conceptual Issues:** `sanitize_input` keyword list is basic and easily bypassed.

### 14. `day8_moderation_toolkits.ipynb`
*   **Purpose:** Quick demo of OpenAI Moderation API and PromptLayer logging.
*   **Sanity Check:** Clear objective, installs `openai promptlayer`. Uses `promptlayer_openai` wrapper for logging and `openai.Moderation` for moderation.
*   **Conceptual Issues:** Assumes availability of OpenAI and PromptLayer API keys.

### 15. `day8_privacy_consent_regulatory.ipynb`
*   **Purpose:** Build prompts handling PII, consent, and regulatory rules (e.g., EU AI Act).
*   **Sanity Check:** Clear objective, installs `openai`. `consented_chat` has a boolean consent gate. `compliant_chat` uses a system prompt for EU AI Act.
*   **Conceptual Issues:** Consent gate is client-side. Regulatory prompts are high-level.

### 16. `day8_prompt_injection_jailbreak.ipynb`
*   **Purpose:** Demonstrate prompt injection and jailbreak attacks (general and token-smuggling).
*   **Sanity Check:** Clear objective, installs `openai`. Shows baseline, direct injection, and Unicode (`\u202E`) attack.
*   **Conceptual Issues:** Effectiveness of specific attacks can vary with model updates.

### 17. `decoding_parameters_playground.ipynb`
*   **Purpose:** Interactive exploration of temperature, top-p, presence/frequency penalties for `gpt-4o-mini`.
*   **Sanity Check:** Clear purpose, installs `openai ipywidgets`. UI with sliders and prompt box.
*   **Conceptual Issues:** Requires manual OpenAI API key replacement (`'sk-YOUR_KEY_HERE'`).

### 18. `decoding_strategies_playground.ipynb`
*   **Purpose:** Interactive comparison of decoding presets and custom parameters.
*   **Sanity Check:** Clear purpose, installs `openai ipywidgets`. UI with presets and sliders.
*   **Conceptual Issues:** Notes that `top_k` slider is illustrative as API doesn't directly support it. API key needs user setup (env or default 'sk-' fails).

### 19. `function_calling_demo.ipynb`
*   **Purpose:** Demonstrates OpenAI function calling with `gpt-4o-mini`.
*   **Sanity Check:** Clear purpose, installs `openai ipywidgets`. Defines local function, schema, and calls LLM to get arguments.
*   **Conceptual Issues:** API key needs user setup. Well-contained demo.

### 20. `index.ipynb`
*   **Purpose:** List of links to other demo notebooks.
*   **Sanity Check:** Markdown file with relative links.
*   **Conceptual Issues:** None (static info).

### 21. `modular_prompt_library_builder.ipynb`
*   **Purpose:** Design reusable prompt blocks, render with Jinja2, track tokens, save to JSON. Interactive UI.
*   **Sanity Check:** Clear purpose, installs `jinja2 openai tiktoken textstat`. UI for managing blocks, templates, context vars, and running.
*   **Conceptual Issues:** API key needs user setup. `textstat` imported but not used. `prompt_blocks.json` created in CWD.

### 22. `pal_plan_act_pipeline.ipynb`
*   **Purpose:** LLM writes Python (PAL), code is executed, LLM explains.
*   **Sanity Check:** Clear purpose, installs `openai ipywidgets`. LLM generates plan/python. Python code is `exec()`-d.
*   **Conceptual Issues:**
    *   **Security Risk:** `exec()` of LLM-generated code is dangerous. Needs strong warning.
    *   Regex for plan/python parsing might be brittle.
    *   API key needs user setup.

### 23. `persona_roleplay_workbench.ipynb`
*   **Purpose:** Interactively adjust multi-role persona parameters and simulate dialogue.
*   **Sanity Check:** Clear purpose, installs `openai ipywidgets textstat`. Dynamic UI for scenario, roles (name, tone, reading level, length), and simulation. Uses `textstat` for readability.
*   **Conceptual Issues:** API key needs user setup. LLM adherence to detailed persona constraints varies.

### 24. `prompt_anatomy_template.ipynb`
*   **Purpose:** Create modular prompts with System/User/Assistant roles and Jinja2.
*   **Sanity Check:** Clear purpose, installs `jinja2 openai`. Uses Jinja to fill template, then maps to API message roles.
*   **Conceptual Issues:** API key needs replacement. `SYSTEM_TMPL` defined but not fully utilized.

### 25. `prompt_versioning_failure_log.ipynb`
*   **Purpose:** Track prompt iterations, log failures/successes to CSV. Interactive UI.
*   **Sanity Check:** Clear purpose, installs `pandas ipywidgets openai tiktoken`. UI for prompt details, run & log. Saves to `prompt_fail_log.csv`.
*   **Conceptual Issues:** API key needs user setup.
    *   **Security Risk:** Uses `eval()` for parsing decoding config string.
    *   CSV created in CWD.

### 26. `prompt_versioning_tracker.ipynb`
*   **Purpose:** Programmatic logger for prompt versions to CSV, optional Google Sheets.
*   **Sanity Check:** Clear purpose, installs `pandas gspread oauth2client`. `log_prompt` function for logging.
*   **Conceptual Issues:** Google Sheets part requires user setup. CSV created in CWD.

### 27. `self_consistency_uncertainty.ipynb`
*   **Purpose:** Self-consistency (majority vote from multiple completions) and prompting for confidence.
*   **Sanity Check:** Clear purpose, installs `openai pandas ipywidgets textstat`. UI for prompt, #runs, temp. Majority vote on completions.
*   **Conceptual Issues:** API key needs user setup. `textstat` imported but not used. Majority vote is exact string match.

### 28. `shot_prompt_patterns.ipynb`
*   **Purpose:** Explore zero-, one-, and few-shot prompting interactively.
*   **Sanity Check:** Clear purpose, installs `openai ipywidgets`. UI for task, #shots, examples, temp. Builds messages with examples.
*   **Conceptual Issues:** API key needs user setup. Example parsing is basic.

### 29. `structured_output_validation.ipynb`
*   **Purpose:** Generate JSON-only responses, validate, and auto-retry.
*   **Sanity Check:** Clear purpose, installs `openai ipywidgets`. UI for prompt, temp, retries. System prompt asks for JSON. Loop with `json.loads()` and retries.
*   **Conceptual Issues:** API key needs user setup.

### 30. `tokenization_playground.ipynb`
*   **Purpose:** Explore tokenization (tiktoken, Hugging Face) and context window limits.
*   **Sanity Check:** Clear purpose, installs `tiktoken transformers`. Functions to count tokens for OpenAI/HF models. Text input for user testing.
*   **Conceptual Issues:** Comparison for HF tokenizer defaults to `gpt2`.
---
This report should provide a good overview of the conceptual state of each notebook.
