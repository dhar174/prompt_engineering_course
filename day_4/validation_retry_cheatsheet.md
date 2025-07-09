# Validation & Retry Cheat Sheet

Use this cheat sheet to implement robust validation and retry logic for structured-output LLM pipelines.

---

## 1. Validation Types

- **Schema Validation**  
  - Use JSON Schema (Draft-07+) to enforce field types, required keys, and value constraints.  
  - Libraries: `jsonschema`, `pydantic` (Python), `Ajv` (JavaScript).
- **Regex Validation**  
  - Full-response regex to ensure no extra text:  
    ```regex
    ^\s*\{(?:[^{}]|(?:\{[^{}]*\}))*\}\s*$
    ```  
  - Field-specific patterns (dates, emails, codes): include in separate regex checks.
- **Custom Code Checks**  
  - Post-parse assertions (e.g., array length, numeric ranges).  
  - Example:
    ```python
    assert isinstance(data['year'], int) and 1900 <= data['year'] <= 2050
    ```

---

## 2. Retry Logic Patterns

- **Simple Loop**  
  ```python
  for attempt in range(MAX_RETRIES):
      response = call_llm(prompt)
      if validate(response):
          break
  else:
      handle_failure(response)
  ```
- **With Exponential Backoff**  
  ```python
  import time
  delay = INITIAL_DELAY
  for attempt in range(MAX_RETRIES):
      response = call_llm(prompt)
      if validate(response):
          break
      time.sleep(delay)
      delay *= BACKOFF_FACTOR
  ```
- **Using `tenacity`**  
  ```python
  from tenacity import retry, stop_after_attempt, wait_exponential

  @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
  def get_valid_response():
      resp = call_llm(prompt)
      if not validate(resp):
          raise ValueError("Invalid output")
      return resp
  ```

---

## 3. Retry Limits & Escalation

- **Max Retries**: 2–5 attempts to avoid runaway loops.  
- **Timeouts**: Set per-call timeouts to avoid hanging on API.  
- **Escalation**: After failures, decide to:
  - Alert operator or monitoring system.
  - Fallback to simpler prompt or default response.
  - Queue for manual review.

---

## 4. Fallback Prompts

- **“Fix Formatting Only” Prompt**  
  ```text
  The JSON you provided failed validation. Please only correct the formatting errors and return valid JSON per the same schema.
  ```
- **Simplify Prompt**:  
  - Remove complex instructions.
  - Narrow fields to essentials.
  - Use bullet lists instead of free text tasks.

---

## 5. Logging & Monitoring

- **Log Details**:  
  - Request prompt, raw LLM output, validation errors, attempt count, timestamps.  
- **Metrics**:  
  - Validation success rate, average attempts, error types by frequency.  
- **Dashboards**:  
  - Visualize error trends; set alerts on rising failure rates.

---

## 6. Best Practices

- **Idempotent Validation**: Ensure validators give same result on same output.  
- **Stateless Retries**: Keep retries independent; avoid stateful side-effects between attempts.  
- **Versioned Prompts & Validators**: Tag with version numbers to track changes.  
- **Team Training**: Update team docs with common failure modes and recommended fixes.

---

_End of Cheat Sheet._
