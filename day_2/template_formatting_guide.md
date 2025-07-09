## Prompt Template Formatting Guide

---

### 1. Why Use Prompt Templates?

- **Consistency:** Reduces errors and output drift across tasks, users, or sessions.
- **Reusability:** Quickly adapt for new tasks or teams.
- **Maintainability:** Easy versioning, sharing, and peer review.
- **Clarity:** Makes intentions and constraints explicit for both LLM and humans.

---

### 2. Core Template Structure

```
[HEADER / TITLE]
# Short description or title of prompt

[SYSTEM ROLE / INSTRUCTIONS]
System: {persona/role/voice statement}

[CONTEXT / BACKGROUND]
{context}

[USER TASK / INSTRUCTION]
User: {task_instruction}

[EXAMPLES]
# (Optional, for few-shot/fine control)

[CONSTRAINTS / REQUIREMENTS]
# e.g., "Limit output to 150 words. Use Markdown. Reply as a pirate."

[OUTPUT FORMAT / SCHEMA]
# Define explicit output structure (e.g., JSON, bullet list, table)

[DELIMITERS / FENCES]
# Use ``` or """ to clearly enclose large context, code, or expected output
```

---

### 3. Formatting Conventions & Style

- **Block Labels:** Use ALL CAPS or [brackets] for section headers.
- **Placeholders:** `{curly_braces}` for variables; use descriptive names.
- **Comments:** `#` for inline notes; `<!-- ... -->` for block annotations.
- **Delimiters:** Enclose multi-line content in triple quotes (`"""` or ```).
- **Indentation:** 2–4 spaces for nested JSON/YAML structures.

---

### 4. Best Practices

- **Modular Blocks:** Isolate context, instruction, and output.
- **Block Size:** Aim for <100 tokens per block.
- **Explicit Constraints:** Use bullet lists for tone, length, format.
- **Avoid Ambiguity:** Clearly define expected output.
- **Versioning:** Tag templates with version or date.

---

### 5. Common Blocks & Schemas

| Block             | Example                                 |
|-------------------|-----------------------------------------|
| [TITLE]           | Summarize Academic Article              |
| [SYSTEM]          | System: You are a scientific assistant. |
| [CONTEXT]         | """Article excerpt..."""                |
| [USER TASK]       | User: Write a 3-sentence summary.       |
| [EXAMPLES]        | (Input-output pairs)                    |
| [CONSTRAINTS]     | - Markdown list
- 80 words max         |
| [OUTPUT FORMAT]   | {"summary":"<text>"}                    |

---

### 6. Annotated Full Example

```markdown
[TEMPLATE_TITLE]
Summarize Legal Text (v1.2, 2025-07-08)

[SYSTEM]
System: You are a legal expert summarizing statutes.

[CONTEXT]
"""
This law governs AI sales in the EU...
"""

[USER TASK]
User: Provide a plain-English summary.

[EXAMPLES]
User: "Right to be forgotten..."  
Assistant: "Allows data erasure requests."

[CONSTRAINTS]
- Max 60 words
- 8th-grade level
- No direct quotes

[OUTPUT FORMAT]
Return only the summary.
```

---

### 7. Anti-Patterns & Fixes

| Problem            | Example                 | Fix                                    |
|--------------------|-------------------------|----------------------------------------|
| Ambiguous roles    | "Answer as expert."     | Specify role in [SYSTEM] block        |
| Unlabeled blocks   | No clear sections       | Use [CONTEXT], [USER TASK], etc.      |
| Vague placeholders | `{input}`               | Use `{article_excerpt}`               |
| Missing constraints| No format/length given  | Add [CONSTRAINTS] block               |

---

### 8. Design Checklist

- [ ] Blocks labeled and separated  
- [ ] Descriptive placeholders  
- [ ] Explicit instructions & constraints  
- [ ] Version/comment included  
- [ ] Delimiters for long data  
- [ ] Examples for nontrivial tasks  
- [ ] Automation-compatible structure  
