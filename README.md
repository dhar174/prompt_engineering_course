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

