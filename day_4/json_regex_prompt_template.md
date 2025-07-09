# JSON/Regex Prompt Template

## Template (annotated)

```text
### SYSTEM
You are a precise JSON-producing assistant.  
When you respond, you MUST return **only** valid JSON that passes the schema and regex checks below.

### USER
TASK:
{<<Put the real task here – e.g. “Summarise the article in exactly three bullet points and extract the author’s name and publication year.”>>}

OUTPUT FORMAT (strict):
```json
{
  "summary_bullets": [
    "<bullet-1>",
    "<bullet-2>",
    "<bullet-3>"
  ],
  "author": "<string>",
  "year": <integer>
}
```

SCHEMA RULES (hard constraints):
1. `summary_bullets` ➜ array of **exactly three** non-empty strings.  
2. `author` ➜ non-empty string, no quotation marks inside.  
3. `year` ➜ four-digit integer between 1900 and the current year.

REGEX GUARD (the output must match **all** of these):
* Entire response matches:  
  `^\s*\{(?:[^{}]|(?:\{[^{}]*\}))*\}\s*$`
* Year field matches:  
  `"year"\s*:\s*(19[0-9]{2}|20[0-4][0-9]|2050)`
* No extra keys:  
  `"(\bsummary_bullets\b|\bauthor\b|\byear\b)"` must be the **only** top-level keys.

RETURN ONLY THE JSON OBJECT — **no prose, no markdown fencing, no comments**.
```

## Quick-Start Usage

1. Copy the template into your playground / API call.  
2. Replace the `TASK:` placeholder with your real instruction.  
3. Adjust the **schema** & **regex** lines to fit your required fields and constraints.  
4. Fire the prompt.  
5. In your driver code, run the same regex (or a JSON-schema validator) to accept/reject.  
6. If the output fails, automatically retry with the *same* prompt (up to N times) or send a “Fix formatting only” follow-up.

## Example Fill-In

```text
TASK:
“Create a two-item shopping list for an Italian pasta dinner, with each item’s name
and exact grams needed.”

# (Adjust schema/regex for two items.)
```

Valid response:

```json
{
  "shopping_list": [
    { "item": "Spaghetti", "grams": 400 },
    { "item": "Parmesan Cheese", "grams": 100 }
  ]
}
```

## Teaching Pointers

| Concept | Emphasis | Demo Tip |
|---------|----------|----------|
| Schema vs. Regex | Schema enforces structure; regex catches formatting issues like extra keys or trailing commas. | Show a malformed output and watch the regex guard reject it. |
| Guardrail Prompting | Explain that downstream code depends on precise JSON. | Temporarily remove the guard text to see error rate increase. |
| Retry Loop | Use a simple `if not re.fullmatch(): retry()` pattern. | Demonstrate with a Colab loop or use the `tenacity` library. |

## Minimal Copy-Friendly Version

```text
### SYSTEM
You are a precise JSON-producing assistant.

### USER
TASK: {…}

FORMAT:
{"field_a":"<string>","field_b":<int>}

SCHEMA: field_a non-empty string, field_b 0-100.
REGEX: ^\s*\{(?:[^{}]|(?:\{[^{}]*\}))*\}\s*$

Return ONLY the JSON.
```
