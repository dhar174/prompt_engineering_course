# 🚦 Prompt Controls Cheatsheet

## 1. Tokenization & Context Window
- **Token**: The smallest unit the LLM reads (word, part of word, or character).
- **Tokenization**: "cats" ≠ "cat"+"s" – subword units like BPE or WordPiece.
- **Context Window**: Models can only “see” a limited number of tokens (e.g., 8k, 16k, 128k).
- **Truncation**: When the context length is exceeded, earliest tokens are discarded.
- **Controls**:
  - `max_tokens` / `max_new_tokens`: Caps output length.
  - **Tools**: [tiktoken](https://github.com/openai/tiktoken), [HuggingFace Tokenizers](https://huggingface.co/docs/tokenizers)

---

## 2. Role Structure & Delimiters
- **System / User / Assistant**: Role separation helps guide behavior.
  - `system`: Sets up tone/persona.
  - `user`: Asks the question.
  - `assistant`: Responds.
- **Delimiters**: Use markdown, quotes, or custom delimiters (e.g., `[INST]`, triple backticks) to separate instructions.

---

## 3. Length & Output Structure
- Use prompts like:
  - “Respond in exactly 15 words.”
  - “List 3 bullet points.”
  - “Format the output as a CSV table.”
- **Formatting Options**:
  - Markdown, bullet points, numbered lists.
  - Code formatting: `Wrap code in triple backticks`.

---

## 4. Style, Tone, and Register
- **Control voice & audience**:
  - “Explain like I’m 5.”
  - “Reply in a legal memo format.”
  - “Use a formal business tone.”
- **Common Styles**:
  - Poetic, casual, humorous, academic, persuasive.

---

## 5. Divergent vs. Convergent Prompts
- **Divergent**: Encourage ideation/creativity.
  - e.g., “Give 10 ideas for a new product.”
- **Convergent**: Drive focus/summary.
  - e.g., “Summarize this paragraph into one sentence.”

---

## 6. Decoding Parameters (API-Level Controls)
- **Temperature**:
  - 0.0 = deterministic
  - 1.0 = creative/random
- **Top-k Sampling**: Only consider the top-k most likely tokens.
- **Top-p (Nucleus) Sampling**: Only consider the top tokens whose cumulative probability reaches p.
- **Presence Penalty**: Discourages or encourages new ideas.
- **Frequency Penalty**: Discourages repetition of the same phrases.

---

## 7. Prompt Debugging & Readability
- Use versioned edits and isolate variables.
- Be explicit with format and instruction.
- Use modular prompts: reuseable building blocks.
- Participate in prompt libraries and shared repositories.

---

## 8. Common Pitfalls & Fixes
| Problem | Fix |
|--------|-----|
| Response too short or cut off | Raise `max_tokens` |
| Unclear response | Add examples and rephrase |
| Too repetitive | Use frequency penalty |
| Off-topic or
