# Prompt Engineering Course

This repo contains a collection of Jupyter notebooks demonstrating various prompt engineering techniques and tools. Use them as interactive playgrounds or reference examples when building your own LLM workflows.

## Notebook Overview

- **LangGraph_Chatbot.ipynb** – LangGraph chatbot with long‑term memory, agentic behavior, and real‑time streaming.
- **chatbot_with_memory.ipynb** – Persist conversation history across turns using LangGraph memory.
- **decoding_parameters_playground.ipynb** – Explore temperature, top‑p, and frequency/presence penalties.
- **decoding_strategies_playground.ipynb** – Compare deterministic vs. stochastic decoding strategies.
- **function_calling_demo.ipynb** – Convert user intent to structured arguments and call Python functions.
- **modular_prompt_library_builder.ipynb** – Build reusable prompt blocks with Jinja2 and save them to JSON.
- **pal_plan_act_pipeline.ipynb** – Let the model generate Python, execute it, then ask for an explanation.
- **persona_roleplay_workbench.ipynb** – Create multi‑persona role‑play scenarios with tone and length controls.
- **prompt_anatomy_template.ipynb** – Template prompts with system/user/assistant roles and placeholders.
- **prompt_versioning_failure_log.ipynb** – Track prompt iterations and failures for robustness analysis.
- **prompt_versioning_tracker.ipynb** – Log prompt versions with outcomes and notes; export to CSV or Sheets.
- **self_consistency_uncertainty.ipynb** – Generate multiple answers, vote for consensus, and capture confidence.
- **shot_prompt_patterns.ipynb** – Try zero‑shot, one‑shot, and few‑shot prompting techniques.
- **structured_output_validation.ipynb** – Produce JSON‑only responses, validate them, and retry on errors.
- **tokenization_playground.ipynb** – Inspect tokenization for different models and context‑window limits.

For quick access to all notebooks, see the optional [index.ipynb](index.ipynb) file.

## Requirements

Most notebooks rely on the OpenAI API and interactive widgets. Install the common packages with:

```bash
pip install -r requirements.txt
```

Set your `OPENAI_API_KEY` environment variable so the notebooks can call the API.

## Running Locally

1. Install dependencies as shown above.
2. Export `OPENAI_API_KEY` in your shell (or use a `.env` file).
3. Launch Jupyter and open any notebook:
   ```bash
   jupyter notebook
   ```

## Running in Google Colab

Open any notebook via the GitHub URL prefixed with `https://colab.research.google.com/`. For example:

```
https://colab.research.google.com/github/USERNAME/REPO/blob/main/LangGraph_Chatbot.ipynb
```

Colab will prompt you for an `OPENAI_API_KEY` the first time a notebook runs.
