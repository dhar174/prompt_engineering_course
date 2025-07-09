# Sample Prompt Repository 📚

A mini‑collection of reusable, production‑ready prompt templates.  
Each entry is self‑contained, fully annotated, and follows the block‑label conventions from the **Template Formatting Guide**.

---

## How to Use

1. **Copy** the desired template into your code / playground.  
2. **Replace** placeholders inside `{curly_braces}` with real values.  
3. **Adjust** constraints or examples as needed.  
4. **Version** any edits by adding a `_v2` suffix to the `name` field and updating the `version` tag.

---

## Index

| # | Name | Category | Purpose |
|---|------|----------|---------|
| 1 | `basic_summary` | Summarization | 3‑bullet digest of any text |
| 2 | `quick_translate` | Translation | Fast EN ↔️ XX sentence translation |
| 3 | `sentiment_fewshot` | Classification | Classify sentiment (pos/neg/neutral) |
| 4 | `key_value_extraction` | Information Extraction | Pull structured fields from docs |
| 5 | `sql_query_generator` | Code Generation | Convert plain‑English question → SQL |
| 6 | `doctor_patient_dialogue` | Role‑Play | Medical triage conversation |
| 7 | `bug_report_triage` | Routing | Auto‑route GitHub issues by label |
| 8 | `chain_of_thought_math` | Reasoning | Step‑by‑step math solver |

---

## Templates

### 1. basic_summary
```yaml
name: basic_summary
category: summarization
version: 1.0
description: Summarize any text into three concise bullet points.
template: |
  [SYSTEM]
  System: You are a world‑class executive summarizer.

  [CONTEXT]
  """{source_text}"""

  [USER TASK]
  User: Summarize the above document into exactly **3** Markdown bullet points,
        each ≤ 20 words, capturing the key insights only.

  [OUTPUT FORMAT]
  - • Point 1
  - • Point 2
  - • Point 3
```

---

### 2. quick_translate
```yaml
name: quick_translate
category: translation
version: 1.0
description: Single‑sentence EN ↔️ XX translator with one‑shot style guidance.
template: |
  [SYSTEM]
  System: You are a professional translator, fluent in English and {target_language}.

  [EXAMPLE]
  User: Bonjour →
  Assistant: Hello

  [USER]
  User: {source_sentence} →
  Assistant:
```

---

### 3. sentiment_fewshot
```yaml
name: sentiment_fewshot
category: classification
version: 1.1
description: Label text sentiment as Positive, Negative, or Neutral.
template: |
  [SYSTEM]
  System: You are a sentiment‑analysis engine that outputs JSON.

  [EXAMPLES]
  Text: "I love this phone!"
  Sentiment: "Positive"

  Text: "Ugh, the battery dies fast."
  Sentiment: "Negative"

  Text: "It arrived yesterday."
  Sentiment: "Neutral"

  [USER]
  Text: "{user_text}"
  Sentiment:
```

---

### 4. key_value_extraction
```yaml
name: key_value_extraction
category: extraction
version: 1.0
description: Extract invoice fields (date, total, supplier) into JSON.
template: |
  [SYSTEM]
  System: You are an information‑extraction assistant.

  [CONTEXT]
  """{invoice_text}"""

  [USER]
  User: Return a JSON object with keys:
    - "invoice_date" (YYYY‑MM‑DD)
    - "supplier_name"
    - "total_amount" (number)

  [OUTPUT_FORMAT]
  {"invoice_date":"", "supplier_name":"", "total_amount":0.0}
```

---

### 5. sql_query_generator
```yaml
name: sql_query_generator
category: code_generation
version: 1.0
description: Convert English questions into SQL for a PostgreSQL employees DB.
template: |
  [SYSTEM]
  System: You are a senior data engineer.

  [CONTEXT]
  Table schemas:
    employees(id, name, hire_date, salary, dept_id)
    departments(id, dept_name)

  [USER]
  User: {english_question}

  [CONSTRAINTS]
  - Output **only** the SQL query.
  - Use snake_case aliases.

  [OUTPUT_FORMAT]
  ```sql
  SELECT ...
  ```
```

---

### 6. doctor_patient_dialogue
```yaml
name: doctor_patient_dialogue
category: roleplay
version: 1.0
description: Triaging patient symptoms with doctor & patient personas.
template: |
  [SYSTEM]
  System: You are Dr. Gupta, an ER physician.

  [DIALOGUE]
  Patient: "{patient_complaint}"
  Doctor:
```

---

### 7. bug_report_triage
```yaml
name: bug_report_triage
category: routing
version: 1.0
description: Auto‑label GitHub issues.
template: |
  [SYSTEM]
  System: You are an issue‑triage bot. Labels: ["bug","feature","docs","question"]

  [USER]
  Issue:
  """
  {issue_text}
  """

  [TASK]
  Classify with one label and return JSON:
  {"label":""}
```

---

### 8. chain_of_thought_math
```yaml
name: chain_of_thought_math
category: reasoning
version: 1.0
description: Force explicit reasoning steps for arithmetic word problems.
template: |
  [USER]
  {math_problem}

  [CONSTRAINT]
  - Think step‑by‑step, then give final answer as "Answer: X".

  [EXAMPLE]
  Q: If Alice has 3 apples and buys 2 more, how many?
  A: Let's think step by step.
     1) Alice initially has 3.
     2) She buys 2 → 3+2=5.
     Answer: 5
```

---

### License

All templates are provided under the **MIT License** — free to modify and redistribute with attribution.
