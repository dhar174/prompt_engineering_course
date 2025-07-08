# prompt_engineering_course
Full course content for Prompt Engineering


# Prompt Engineering Course

This repository contains a collection of Jupyter notebooks demonstrating key prompt engineering techniques.

## Notebook Overview

| Notebook | Learning goal |
| --- | --- |
| `LangGraph_Chatbot.ipynb` | LangGraph chatbot with long-term memory, tool use, and streaming responses. |
| `chatbot_with_memory.ipynb` | Minimal chatbot that maintains conversation state. |
| `decoding_parameters_playground.ipynb` | Explore temperature, top-p and penalty parameters. |
| `decoding_strategies_playground.ipynb` | Compare deterministic vs stochastic decoding strategies. |
| `function_calling_demo.ipynb` | Convert user intent to structured arguments and call Python functions. |
| `modular_prompt_library_builder.ipynb` | Build reusable prompt blocks with Jinja2 and track token counts. |
| `pal_plan_act_pipeline.ipynb` | Use a Plan-then-Act pipeline where the LLM writes Python and explains the result. |
| `persona_roleplay_workbench.ipynb` | Create multi-persona role‑play scenarios with tone and length controls. |
| `prompt_anatomy_template.ipynb` | Template prompts using System/User/Assistant sections. |
| `prompt_versioning_failure_log.ipynb` | Record failures while iterating on prompts. |
| `prompt_versioning_tracker.ipynb` | Log prompt versions locally or to Google Sheets. |
| `self_consistency_uncertainty.ipynb` | Generate multiple answers and capture model confidence. |
| `shot_prompt_patterns.ipynb` | Playground for zero-, one-, and few-shot prompting. |
| `structured_output_validation.ipynb` | Produce JSON-only responses and validate them. |
| `tokenization_playground.ipynb` | Visualize tokenization and context window limits. |
| `day7_auto_prompt_opro.ipynb` | AutoPrompt & OPRO for automated gradient-based prompt engineering. |
| `day7_embedding_prompt_lab.ipynb` | Embedding-based retrieval prompt lab with FAISS and RAG pipeline. |
| `day7_multilingual_lab.ipynb` | Multilingual and cross-lingual prompting with mT5. |
| `day7_negative_prompting.ipynb` | Negative prompting and textual inversion with Stable Diffusion XL. |
| `day7_soft_prompt_tuning.ipynb` | Soft prompting and prompt tuning with PEFT library. |
| `day8_adversarial_robustness_logging.ipynb` | Red-team prompts, log failures, and apply robustness patches. |
| `day8_bias_alignment_constitutional.ipynb` | Apply bias-reduction and constitutional alignment techniques. |
| `day8_guardrails_moderation.ipynb` | Implement prompt isolation, input sanitization, and output moderation defenses. |
| `day8_moderation_toolkits.ipynb` | Use OpenAI moderation API and PromptLayer for content filtering and logging. |
| `day8_privacy_consent_regulatory.ipynb` | Build prompts that handle PII, consent, and regulatory compliance rules. |
| `day8_prompt_injection_jailbreak.ipynb` | Understand and demonstrate prompt injection and jailbreak attacks. |
| `Lab1_Chaining_and_Orchestration.ipynb` | Build modular prompt pipelines using LangChain (Day 9 content). |
| `Lab2_Multi_Agent_Workflows.ipynb` | Design cooperating LLM agents with tool use and memory (Day 11 content). |
| `Lab3_Logging_Deployment_Eval.ipynb` | Track, scale, and evaluate prompt-driven applications (Day 10 content). |

## Dependencies

All notebooks require an **OpenAI API key** set as `OPENAI_API_KEY`. Common packages used include:

- `openai`
- `langgraph` and `langchain`
- `tiktoken`
- `ipywidgets`
- `pandas`
- `jinja2`
- `textstat`
- `gspread` and `oauth2client`
- `transformers` (for the tokenization demo)
- `python-dotenv` (optional for loading environment variables)

Install them with:

```bash
pip install openai langgraph langchain-openai langchain-community tiktoken ipywidgets pandas jinja2 textstat gspread oauth2client transformers python-dotenv
```

## Running in Google Colab

1. Open a notebook on GitHub and select **Open in Colab**.
2. Run the setup cell to install dependencies.
3. Enter your `OPENAI_API_KEY` when prompted.
4. Execute the remaining cells.

## Running Locally

1. Clone this repository and create a Python virtual environment.
2. Install the packages listed above.
3. Export your OpenAI key (`export OPENAI_API_KEY=...`).
4. Launch Jupyter and open the desired notebook:

```bash
jupyter notebook
```
## Helpful Guides
- [Append a Row to CSV or Google Sheet](docs/append_row.md)
## Examples
- **prompt_block_io_demo.py** – demonstrates saving and loading prompt blocks from JSON or YAML files.

## Token Counting

Language models process prompts as tokens rather than raw characters. A token is roughly a word fragment and token limits determine how much text a model can handle. You can pre-count tokens with the **tiktoken** library to stay within a model's context window.

The token count of a Jinja template may differ from the count of its rendered output. For example, with the `gpt-4o` tokenizer:

```python
import tiktoken

template = "Hello {{ name }}, you have {{ count }} new messages."
rendered = "Hello John, you have 5 new messages."

enc = tiktoken.encoding_for_model("gpt-4o")
print(len(enc.encode(template)))  # 13 tokens
print(len(enc.encode(rendered)))  # 10 tokens
```

Keeping track of these numbers helps ensure your final rendered prompts do not exceed model limits.
