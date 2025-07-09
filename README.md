# Prompt Engineering Course
Prompt engineering is the art and science of crafting effective inputs for large language models (LLMs) like GPT-4. With the rise of AI-driven systems in every domain — from chatbots to research assistants — prompt engineering has become a crucial skill for developers, researchers, and product teams alike.

This course is designed as a hands-on, practical introduction to prompt engineering techniques, using real-world scenarios and interactive Jupyter notebooks. It focuses not only on how to prompt LLMs, but also on why certain prompt designs yield better results — based on model behavior, tokenization mechanics, and decoding strategies.

### By the end of the course, you’ll be equipped to:
* Understand how language models interpret and respond to prompts
* Structure prompts using role separation (system/user/assistant)
* Tune output quality using decoding parameters (`temperature`, `top_p`, etc.)
* Count tokens and manage context length using tools like tiktoken
* Create reusable and modular prompt components with `Jinja2`
* Incorporate function calling, structured outputs, and prompt versioning
* Build prompt-based applications like chatbots, agents, and RAG pipelines

This repository includes both foundational labs (e.g. shot prompting, output structure, tone control) and advanced topics (e.g. soft prompting, multilingual prompting, and negative prompting with diffusion models).

Whether you’re a beginner curious about how LLMs work, or an experienced AI engineer building production systems, this course will level up your prompt engineering fluency.

---
## Course Overview & Objectives
The Prompt Engineering Course is a hands-on, practical guide for developers, researchers, and AI enthusiasts who want to deeply understand how to craft effective prompts for large language models (LLMs). Through a curated set of Jupyter notebooks, real-world demonstrations, and prompt design patterns, this course aims to demystify prompt engineering and empower users to build more reliable, expressive, and controllable AI systems.

Prompt engineering is the art and science of communicating with LLMs using structured natural language instructions. This course provides a structured pathway to learn core techniques, experiment with decoding strategies, track token budgets, enforce response structure, debug unexpected outputs, and modularize reusable prompt components.

### Key Objectives
* By the end of this course, you will be able to:
* Understand how tokenization, sampling, and model context length affect prompt performance.
* Craft prompts that are more precise, modular, and reusable using prompt blocks and templates.
* Explore deterministic vs. stochastic generation through decoding parameters like `temperature`, `top-k`, and `top-p`.
* Build stateful and memory-aware chatbots using LangGraph and LangChain.
* Design prompts for function calling, structured outputs (e.g. JSON), and multi-role conversations.
* Implement versioning, logging, and validation workflows to iteratively improve prompt quality.
* Apply advanced techniques like AutoPrompt, OPRO, negative prompting, multilingual prompting, and soft prompt tuning.
* Measure and control prompt length using token counting tools (`tiktoken`) and token reference guides.
* Integrate tools such as Jinja2, FAISS, Gradio, HuggingFace Transformers, and Google Sheets to enhance prompt experimentation and debugging.

---
## Prerequisites
Before starting this course, ensure you have the following foundational knowledge and tools set up:

### Knowledge Requirements
* Basic Python programming
You should be comfortable with variables, functions, loops, and working with dictionaries and lists.
* Familiarity with Jupyter Notebooks
This course is heavily notebook-driven. Understanding how to navigate and run cells in Jupyter is essential.
* General understanding of Machine Learning or NLP (optional but helpful)
Though not mandatory, a basic understanding of how large language models (LLMs) work will help you get more from the lessons.

### Technical Requirements
* Python 3.8 or higher
This course requires modern Python versions to ensure compatibility with LLM libraries.
* OpenAI API Key
Several notebooks rely on OpenAI models like gpt-3.5-turbo or gpt-4.
* [Get your API key here](https://platform.openai.com/api-keys)
* Set it as an environment variable:

```bash

export OPENAI_API_KEY=your_key_here
```
* Google Account (for Google Sheets integration)
Some prompt versioning examples demonstrate logging to Google Sheets using gspread and `oauth2client`.
* Basic Git & CLI skills
You’ll need to clone this repo and run some commands in a terminal.

### Optional but Recommended
* Hugging Face account
Useful if you want to explore open-source models using `transformers`.
* Colab account or JupyterLab installed locally
You can either run notebooks in the cloud or on your machine.
* Familiarity with Prompt Engineering Concepts
If you're brand new to prompt engineering, review the provided `common_prompt_pitfalls.md` and `prompt_control_cheatsheet.md` for foundational concepts.

---
## Notebook Overview

This repository includes a curated collection of hands-on Jupyter notebooks, each focusing on a specific prompt engineering technique. These notebooks are designed to build practical skills, explore advanced LLM behaviors, and experiment with real-world use cases.

| Notebook | Description |
| --- | --- |
| `LangGraph_Chatbot.ipynb` | Build a LangGraph-powered chatbot with support for long-term memory, tool usage, and streaming responses. |
| `chatbot_with_memory.ipynb` | Create a minimal chatbot that maintains user context across multiple turns using memory mechanisms. |
| `decoding_parameters_playground.ipynb` | Play with decoding parameters like temperature, top-p, frequency penalty, and presence penalty to control generation behavior. |
| `decoding_strategies_playground.ipynb` | Compare deterministic (e.g., greedy) and stochastic (e.g., sampling) decoding strategies. |
| `function_calling_demo.ipynb` | Demonstrate OpenAI function calling to convert natural language inputs into structured API calls. |
| `modular_prompt_library_builder.ipynb` | Learn to build reusable, modular prompt blocks using Jinja2 templating and track token usage. |
| `pal_plan_act_pipeline.ipynb` | Use a Plan-and-Act prompting framework where the LLM plans its response and executes Python code. |
| `persona_roleplay_workbench.ipynb` | Craft multi-character persona simulations with controllable tone, behavior, and output length. |
| `prompt_anatomy_template.ipynb` | Dissect prompts into structured components using system/user/assistant roles with clear delimiters. |
| `prompt_versioning_failure_log.ipynb` | Record and analyze failures in prompt iterations to improve robustness through failure logging. |
| `prompt_versioning_tracker.ipynb` | Track prompt versions and results either locally or via integration with Google Sheets. |
| `self_consistency_uncertainty.ipynb` | Generate multiple completions and measure uncertainty or confidence using self-consistency techniques. |
| `shot_prompt_patterns.ipynb` | Explore zero-shot, one-shot, and few-shot prompting patterns for better task alignment. |
| `structured_output_validation.ipynb` | Ensure valid structured outputs like JSON and perform schema validation. |
| `tokenization_playground.ipynb` | Visualize how models tokenize inputs and understand the limitations of context windows. |
| `day7_auto_prompt_opro.ipynb` | Learn about AutoPrompt and OPRO techniques for automated prompt tuning via optimization. |
| `day7_embedding_prompt_lab.ipynb` | Build a retrieval-augmented generation (RAG) system using embeddings and FAISS indexing. |
| `day7_multilingual_lab.ipynb` | Practice multilingual prompting and cross-lingual generation using models like mT5. |
| `day7_negative_prompting.ipynb` | Investigate the effects of negative prompting and prompt inversion for image generation. |
| `day7_soft_prompt_tuning.ipynb` | Experiment with soft prompts and prompt tuning using HuggingFace PEFT and Lora adapters. |
| `day8_adversarial_robustness_logging.ipynb` | Red-team prompts, log failures, and apply robustness patches. |
| `day8_adversarial_robustness_logging_a.ipynb` | Answer key for adversarial robustness and logging exercises. |
| `day8_bias_alignment_constitutional.ipynb` | Apply bias-reduction and constitutional alignment techniques. |
| `day8_bias_alignment_constitutional_a.ipynb` | Answer key for bias mitigation and constitutional AI exercises. |
| `day8_guardrails_moderation.ipynb` | Implement prompt isolation, input sanitization, and output moderation defenses. |
| `day8_guardrails_moderation_a.ipynb` | Answer key for guardrails and moderation exercises. |
| `day8_moderation_toolkits.ipynb` | Use OpenAI moderation API and PromptLayer for content filtering and logging. |
| `day8_moderation_toolkits_a.ipynb` | Answer key for moderation toolkits exercises. |
| `day8_privacy_consent_regulatory.ipynb` | Build prompts that handle PII, consent, and regulatory compliance rules. |
| `day8_privacy_consent_regulatory_a.ipynb` | Answer key for privacy, consent, and regulatory compliance exercises. |
| `day8_prompt_injection_jailbreak.ipynb` | Understand and demonstrate prompt injection and jailbreak attacks. |
| `day8_prompt_injection_jailbreak_a.ipynb` | Answer key for prompt injection and jailbreak exercises. |
| `Lab1_Chaining_and_Orchestration.ipynb` | Build modular prompt pipelines using LangChain (Day 9 content). |
| `Lab2_Multi_Agent_Workflows.ipynb` | Design cooperating LLM agents with tool use and memory (Day 11 content). |
| `Lab3_Logging_Deployment_Eval.ipynb` | Track, scale, and evaluate prompt-driven applications (Day 10 content). |
| `00_Kickstart_Gap_Map.ipynb` | Orientation and gap assessment for prompt engineering fundamentals. |
| `00_Overview_Day10.ipynb` | Introduction to evaluation metrics and deployment strategies. |
| `00_Overview_Day10_b.ipynb` | Advanced evaluation frameworks and testing methodologies. |
| `01_Metrics_and_HumanEval.ipynb` | Learn evaluation metrics and human-in-the-loop assessment techniques. |
| `01_Style_Structured_Formatting_Lab.ipynb` | Practice prompt styling and structured output formatting. |
| `02_Automated_Eval_AB_Testing.ipynb` | Implement automated evaluation pipelines and A/B testing for prompts. |
| `02_Length_Reading_Level_Tone.ipynb` | Control output length, reading level, and tone in generated content. |
| `03_Benchmarking_Suites.ipynb` | Build comprehensive benchmarking suites for prompt performance evaluation. |
| `03_Error_Spotting_Feedback_Loops.ipynb` | Create feedback loops for error detection and prompt improvement. |
| `04_Application_Quick_Hits.ipynb` | Deploy prompt-based applications with quick wins and practical use cases. |
| `04_Robustness_and_Adversarial.ipynb` | Build robust prompts that withstand adversarial inputs and edge cases. |
| `05_Continuous_Optimization_and_Capstone.ipynb` | Implement continuous optimization workflows and capstone project planning. |
| `05_Group_Prompting_Community.ipynb` | Explore collaborative prompting techniques and community-driven approaches. |
| `06_Advanced_Adversarial_Fuzzing.ipynb` | Advanced techniques for adversarial testing and prompt fuzzing. |
| `06_HITL_Constraint_Balancing.ipynb` | Human-in-the-loop constraint balancing and preference optimization. |
| `07_Frontier_Research_Wrap.ipynb` | Overview of cutting-edge research and future directions in prompt engineering. |
| `07_StatSig_and_Sequential_AB.ipynb` | Statistical significance testing and sequential A/B testing for prompts. |
| `08_CI_CD_GitHub_Actions.ipynb` | Implement CI/CD pipelines for prompt-based applications using GitHub Actions. |
| `09_Bias_and_Fairness_Eval.ipynb` | Evaluate and mitigate bias in prompt outputs for fairness and ethics. |
| `day12_1_orientation_QA.ipynb` | Advanced course orientation and Q&A session. |
| `day12_2_test_driven_prompting.ipynb` | Test-driven development approaches for prompt engineering. |
| `day12_3_misunderstanding_ambiguity.ipynb` | Handle misunderstandings and ambiguity in prompt responses. |
| `day12_4_cross_model_interop.ipynb` | Achieve cross-model interoperability and prompt portability. |
| `day12_5_active_learning_loops.ipynb` | Implement active learning loops for continuous prompt improvement. |
| `day12_6_traceable_reasoning.ipynb` | Build traceable reasoning chains for transparent AI decision-making. |
| `day12_7_search_integrated_deep_research.ipynb` | Integrate search capabilities for deep research and knowledge retrieval. |
| `day12_8_release_radar_ethics.ipynb` | Monitor release radar and implement ethical guidelines for AI deployment. |

> 💡 **Tip:** Each notebook builds on foundational concepts and introduces hands-on tasks. Feel free to modify prompts, adjust parameters, and explore what works best for your use case.

## Course Modules
- [Module 1: Introduction to Prompt Engineering](docs/module_1_intro.md)

---
## Installation Instructions

To get started with the Prompt Engineering Course on your local machine, follow these steps:

---

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/dhar174/prompt_engineering_course.git
cd prompt_engineering_course
```
### 2. Set Up a Virtual Environment
It's recommended to use a virtual environment to isolate dependencies:

On macOS/Linux:
```bash

python3 -m venv venv
source venv/bin/activate
```
On Windows:
```bash

python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
All required packages are listed in requirements.txt. Install them using:

```bash

pip install -r requirements.txt
```
This will install the following key libraries (among others):

`openai` – access OpenAI models

`tiktoken` – count prompt tokens

`jinja2` – render prompt templates

`langchain`, `langgraph` – advanced LLM pipelines

`gradio` – interactive UI for prompt tools

`ipywidgets` – notebook widgets

`gspread`, `oauth2client` – Google Sheets logging

`transformers` – tokenizer comparisons

`faiss-cpu` – for semantic search and RAG labs

Install them with: 

```
pip install openai langgraph langchain-openai langchain-community tiktoken ipywidgets pandas jinja2 textstat gspread oauth2client transformers python-dotenv
```

### 4. Set Up OpenAI API Key
Most notebooks require an OpenAI key to run. Set it as an environment variable:

On macOS/Linux:
```bash

export OPENAI_API_KEY=your-key-here
```
On Windows:
```powershell

$env:OPENAI_API_KEY="your-key-here"
```
Alternatively, create a `.env` file or use a secrets manager in Colab.

### Running in Google Colab
* Open a notebook on GitHub and select Open in Colab.
* Run the setup cell to install dependencies.
* Enter your OPENAI_API_KEY when prompted.
* Execute the remaining cells.

Running Locally

* Clone this repository and create a Python virtual environment.
* Install the packages listed above.
* Export your OpenAI key (export OPENAI_API_KEY=...).
* Launch Jupyter and open the desired notebook:
```
jupyter notebook
```
### Optional: Use Google Colab
Most notebooks can also be opened directly in Google Colab:
* Navigate to a .ipynb file on GitHub
* Click Open in Colab button (or prefix the URL with `https://colab.research.google.com/github/`).
* Run the setup cell and provide your OpenAI API key.
* Enjoy cloud-based execution—no local setup needed.

---
## How to Use the Materials
 
This repository contains a rich collection of Jupyter notebooks, Python scripts, and prompt engineering resources designed for hands-on learning and experimentation with Large Language Models (LLMs). Here's how you can make the most of it:

### A. Explore the Notebooks
Each notebook in the repository focuses on a specific concept in prompt engineering, from decoding strategies to structured output validation and LangGraph workflows.

Suggested Learning Path:
* Start with foundational notebooks:
  - prompt_anatomy_template.ipynb
  - chatbot_with_memory.ipynb
  - decoding_parameters_playground.ipynb

* Progress to advanced use-cases:
  - LangGraph_Chatbot.ipynb
  - persona_roleplay_workbench.ipynb
  - day7_embedding_prompt_lab.ipynb

* Use topic-specific labs for experimentation:
  - prompt_versioning_failure_log.ipynb
  - tokenization_playground.ipynb
  - structured_output_validation.ipynb

📎 Tip: Refer to the notebook table in the README for learning goals and brief descriptions.


### B. Use Prompt Libraries

The repository includes modular prompt blocks stored as .json and .yaml files.

You can load and reuse them in your own workflows or via templating using Jinja2.
* Examples:
  - prompt_blocks.json
  - prompt_block.yml
  - prompt_block_io_demo.py

> For custom prompt composition, refer to: modular_prompt_library_builder.ipynb

### C. Count Tokens Before Prompting
To avoid exceeding model context limits:
* Use tiktoken to count tokens.
* Token counting utilities are demonstrated in:
  - tokenization_playground.ipynb
  - prompt_block.md
  - token_count_reference.md

Use `count_tokens(text)` to estimate token usage before sending a prompt to the model.

### D. Experiment Locally or in Colab

You can run the notebooks in two environments:

**Option A: Google Colab (Recommended for Beginners)**
* Click “Open in Colab” on the notebook page.
* Install dependencies using the setup cell.
* Provide your OPENAI_API_KEY when prompted.

**Option B: Run Locally**
```

git clone https://github.com/dhar174/prompt_engineering_course.git
cd prompt_engineering_course

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```
### E. Use Tools & References
This repo includes companion resources:
*  Cheatsheets: `prompt_control_cheatsheet.md`, common_prompt_pitfalls.md`
*  Token limits: `token_count_reference.md`
*  GitHub issue workflows: `agentss.md` (how to create issues via CLI, API, or Python)
*  Version tracking: `prompt_versioning_tracker.ipynb`

### F.  Build Your Own Prompt Workflows
* Try composing custom prompts using reusable blocks and templates.
* Use prompt_block_io_demo.py to understand how to read/write prompt blocks from files.
* Log, test, and iterate with versioning notebooks.

### G.  Learn by Debugging
Many notebooks include deliberate pitfalls, e.g.:
* Hallucinated outputs
* Broken formats
* Repetitive completions

Use these to learn how to debug, tune decoding parameters, and refine prompts.
> See `prompt_versioning_failure_log.ipynb` and `common_prompt_pitfalls.md.`

By following these steps, you'll develop a robust understanding of prompt engineering and how to practically apply it to real-world LLM use cases.

## Helpful Guides
* [Append a Row to CSV or Google Sheet](https://github.com/dhar174/prompt_engineering_course/blob/main/docs/append_row.md)

### Examples
```
prompt_block_io_demo.py – demonstrates saving and loading prompt blocks from JSON or YAML files.
```
### Token Counting
Language models process prompts as tokens rather than raw characters. A token is roughly a word fragment and token limits determine how much text a model can handle. You can pre-count tokens with the tiktoken library to stay within a model's context window.

The token count of a Jinja template may differ from the count of its rendered output. For example, with the gpt-4o tokenizer:
```
import tiktoken

template = "Hello {{ name }}, you have {{ count }} new messages."
rendered = "Hello John, you have 5 new messages."

enc = tiktoken.encoding_for_model("gpt-4o")
print(len(enc.encode(template)))  # 13 tokens
print(len(enc.encode(rendered)))  # 10 tokens
```

---
## Contributing Guidelines

We welcome contributions to make this Prompt Engineering course better for everyone! Whether you're fixing a typo, improving a notebook, adding a new lesson, or enhancing documentation, your contributions are appreciated.

Please read the following guidelines before submitting a pull request:

---

### Ground Rules

- Ensure your contribution aligns with the purpose of this repository: **teaching and demonstrating prompt engineering techniques**.
- Follow clean coding practices and maintain readability—especially important for educational content.
- Avoid including proprietary or sensitive API keys in code or environment files.
- Write clear commit messages and use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) if possible.

---

### Ways You Can Contribute

| Type of Contribution | Examples |
|----------------------|----------|
| ✍️ Content | Improve or create Jupyter notebooks, add new demos, fix errors |
| 🐛 Bug Reports | Found something broken? Open an issue with reproduction steps |
| 📚 Docs | Clarify instructions, fix typos, improve markdown formatting |
| 🚀 Features | Add new tools, utilities, or extensions for prompt experimentation |
| 🧪 Testing | Verify behavior across models or platforms (e.g., Colab, local) |
| 💡 Suggestions | Propose improvements to course flow, structure, or UX |

---

### Workflow for Pull Requests

1. **Fork** the repository.
2. Create a new branch:
```
git checkout -b your-feature-name
```
3. Make your changes.
4. Test your notebooks and scripts.
5. Format Python code using Black and ensure it passes linting via flake8 or ruff.
6. Commit with a clear message:

```
git commit -m "fix: improve roleplay notebook example"
```
7. Push your changes
```
git push origin your-feature-name
```
8. Open a pull request (PR) with a description of what you changed and why.

9. **IMPORTANT: Code Style & linting**
This repo uses flake8 and ruff for code linting. Make sure your code:

* Has a max line length of 100 characters.
* Excludes `.ipynb` files from linting.
* Avoids unnecessary imports or commented-out code.
* Run locally with:
```
ruff .
flake8 .
```
## Dependency Management
Add any new packages to `requirements.txt`. If you're contributing notebooks that require additional setup, clearly document it in a cell or markdown block at the top.

## Issue Tracking
* Use GitHub Issues to report bugs, request features, or suggest improvements.
* Include labels like`bug`, `enhancement`, `question`, or `good first issue`.
* Use the `agents.md` guide to file issues via CLI, curl, or Python.

---
##  License
This repository is licensed under the MIT License.
```
MIT License

Copyright (c) 2025 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```

## Acknowledgement

This repository and its contents build upon open-source tools, libraries, and prior research in the field of prompt engineering and LLM applications. Special thanks to:

* **OpenAI** – for providing powerful models and the `tiktoken` tokenizer library.
* **LangChain & LangGraph teams** – for open-source tools enabling composable and memory-aware LLM agents.
* **Hugging Face Transformers** – for state-of-the-art tokenizers and multilingual model support.
* **Google & Gradio** – for making tools like Colab and easy-to-deploy UI components accessible.
* **Community contributors** – whose techniques and frameworks inspired this modular prompt architecture.

---

Official Repo Owner: [**Charles I Niswander II**](https://github.com/dhar174)

Readme.md created by [**Shishir Tambe**](https://github.com/SHISKEBAB)

---
