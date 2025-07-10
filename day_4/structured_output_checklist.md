# Structured Output Checklist

Use this checklist to design, validate, and troubleshoot your structured-output prompts. Copy into slides, handouts, or your project docs.

---

## 1. Prompt Design

- **System Directive**: Include a `SYSTEM` or introductory instruction emphasizing JSON-only output.
- **Clear Task Description**: State the task and required fields explicitly under a `USER` section.
- **Output Format Block**: Provide an exact JSON template with placeholder fields.
- **Schema Rules**: List hard constraints on types, field presence, ranges, and lengths.
- **Regex Guards**: Supply one or more regex patterns to catch formatting errors (e.g., unbalanced braces, trailing commas).
- **Validation Rationale**: Optionally explain to the model how you'll validate (e.g., “I will mentally run regex checks before output”).

---

## 2. Schema Validation

- **JSON-Schema Validator**: Implement a formal JSON schema (Draft-07 or newer).
- **Pydantic/Marshmallow**: (Python) Use data models for type-checked parsing.
- **Type Checks**: Ensure strings, numbers, booleans, arrays, objects match expected types.
- **Required Fields**: Mark mandatory keys and enforce presence.
- **Value Constraints**: Enforce min/max for numbers, length limits for strings/arrays.

---

## 3. Regex Validation

- **Full-Response Regex**: Match the entire output to ensure no extra text.
- **Field-Specific Patterns**: RegEx for dates, 4-digit years, email formats, etc.
- **Key Whitelist**: Ensure only allowed top-level keys appear.
- **No Trailing Commas**: Regex to disallow trailing commas or dangling brackets.
- **No Inline Comments**: Disallow `//` or `/* */` in JSON output.

---

## 4. Testing & Debugging

- **Sample Prompts**: Prepare positive and negative examples.
- **Intentional Failures**: Test cases that violate schema/regex to confirm rejection.
- **Automatic Retry Logic**: Implement retry loops (e.g., `while not valid: retry()`).
- **Error Reporting**: Log raw output and validation errors for debugging.
- **Fallback Prompts**: Provide a “Fix formatting only” follow-up to the LLM.

---

## 5. Pipeline Integration

- **Parsing Module**: Centralize JSON parsing and validation in one function/class.
- **Logging**: Record request, raw response, validation status, and errors.
- **Alerting**: Notify on repeated validation failures.
- **Retries & Backoff**: Exponential backoff or max retries for rate limits.
- **Monitoring**: Track error rates over time to tune prompts.

---

## 6. Documentation & Training

- **Cheat Sheet**: Keep a one-page summary of schema and regex patterns.
- **Examples Library**: Curate a repo of valid and invalid prompt-response pairs.
- **Team Guidelines**: Document best practices and common pitfalls.
- **Version Control**: Tag prompt templates with version numbers.
- **Review Process**: Peer review for new structured-output templates.

---

_End of checklist._

