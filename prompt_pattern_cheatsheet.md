### Prompt Pattern Cheatsheet  
*Day 2 — Foundational Prompt Patterns & Persona Workflows*

---

#### 1. Shot-Based Prompting Patterns
| Pattern | When to Use | Minimal Skeleton |
|---------|-------------|------------------|
| **Zero-Shot** | Straightforward tasks the model already excels at; exploratory “first try.” | `System: You are a helpful tutor.  \nUser: Explain photosynthesis in 3 sentences.` |
| **One-Shot** | Task is clear but output style/format is critical. | `Example: “Translate: Bonjour → Hello”  \n---  \nTranslate: Merci →` |
| **Few-Shot (2-5 ex.)** | Complex output schema, subtle tone, or high accuracy needed. | `System: Format each answer as JSON.  \nUser: Q:2+2 A:{"answer":4}  \nUser: Q:5×3 A:{"answer":15}  \nUser: Q:7×6 A:` |
| **“Chain-of-Thought” Shot** | Forces step-by-step reasoning for math, logic, multi-hop QA. | *Add* “Let’s think step by step.” **after** the question _within_ any shot pattern. |
| **Self-Consistency** | Diverse reasoning paths; pick majority answer. | Run multiple (3-5) few-shot prompts with different seeds → vote/aggregate. |

---

#### 2. Persona & Role Patterns
| Sub-pattern | Purpose | Key Tip |
|-------------|---------|---------|
| **Role / Persona** | Adopt voice & POV (e.g., _“You are Dr. House…”_). | Put persona **in the system message** to lock tone. |
| **Expert Prompting** | Force authoritative jargon or domain accuracy. | Start with: “Answer as a senior <domain> expert who cites sources.” |
| **Multi-Persona Dialogue** | Simulate conversations; training, therapy, sales. | Delimit speakers clearly (`Doctor: …\nPatient: …`). |
| **Nested Personas** | One agent “thinks,” another “speaks.” | Use comment blocks: `<!-- Internal thoughts -->` vs visible output. |

---

#### 3. Template Engineering Blocks
```
### <Title>
[CONTEXT]
{context}

[INSTRUCTION]
{instruction}

[EXAMPLES]
{few_shot}

[OUTPUT_FORMAT]
{schema}

###
```
*Fill placeholders via code or UI variables for rapid reuse.*  
*Keep each block ≤ 75 tokens for easy swapping.*

---

#### 4. Readability & Tone Controls
* **Length** — “Limit to 150 words.” or use token ceilings.  
* **Tone** — “…in a friendly, humorous style.”  
* **Formality** — “Rewrite formally.” vs “…for a 5th-grader.”  
* **Delimiter Fences** — wrap long context in `"""` or `````.

---

#### 5. Modular Prompt Design
1. **Context Block** – background facts, citations.  
2. **Task Block** – the actual instruction.  
3. **Example Block** – zero / one / few-shot.  
4. **Constraints Block** – tone, length, format.  
5. **Output Schema Block** – JSON, XML, Markdown, etc.

> Swap or reorder blocks to A/B test without touching others.

---

#### 6. Collaborative Workflow Tips
* **Comment** unused variants with `<!-- … -->` or `# …`.  
* **Version** templates in Git (diff friendly).  
* **Name** each template (`pricing_email_v2`) for quick retrieval.  
* **Pair Review**: teammate runs prompt, highlights ambiguity, refactors.

---

#### 7. Common Pitfalls & Fixes
| Pitfall | Symptom | Quick Fix |
|---------|---------|-----------|
| Missing role segregation | Model slips out of character | Put persona in **system** role; repeat in examples. |
| Example order bias | All outputs copy first example’s style | Shuffle or diversify few-shot list. |
| Over-stuffed context | Hallucinations / truncation | Summarize or link via `CONTEXT:` block ≤ 500 tokens. |
| Ambiguous constraints | Inconsistent length/tone | Convert constraints to explicit bullet list. |

---

#### 8. Fast-Grab Snippets
```text
System: You are a meticulous proofreader.
User: Proofread the following → """{draft}"""
Assistant MUST: 
- Return only the corrected text
- Track changes using Markdown ~~strike~~ and **bold**
```
```text
System: You are Socrates.  
Student: {question}  
Socrates: Ask me *one* probing question that guides the student.
```

---

**Use this cheatsheet as your Day 2 desk-reference: mix-and-match patterns, enforce clarity, and iterate collaboratively for reliable, reusable prompts.**
