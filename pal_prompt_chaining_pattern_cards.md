# PAL & Prompt Chaining Pattern Cards

Use these double‑sided “cards” as quick references for designing Program-Aided Language Model (PAL) pipelines and Prompt Chaining workflows.

---

## Card 1: Program-Aided Language Model (PAL)

**Pattern Name:** Program-Aided Language Model (PAL)

**Description:**  
Leverage external code execution within your LLM pipeline to handle computation-heavy or logic-based tasks, improving reliability and precision.

**When to Use:**  
- Arithmetic or math problems  
- Data transformation or aggregation  
- External API integration  
- Tasks requiring deterministic computation

**Template:**
```text
### SYSTEM
You are a collaborative assistant that writes and executes code for sub-tasks.

### USER
TASK: <<Describe the high-level task>>

### PAL PIPELINE:
1. Generate code snippet to solve sub-task.
2. Execute the generated code in a secure environment.
3. Return the raw result to the model.
4. Instruct the model to integrate or explain the result in context.
```

**Example:**  
- **User Task:** “Compute the standard deviation of [10, 12, 23, 23, 16, 23, 21, 16] and explain the significance.”  
- **PAL Steps:**
  1. LLM writes Python code using `statistics.stdev`.  
  2. Code runs, returns `std_dev = 5.33`.  
  3. LLM reads `5.33` and writes: “The standard deviation is 5.33, indicating moderate spread around the mean...”

**Best Practices:**  
- Validate generated code before execution.  
- Limit execution environment to safe operations (no file I/O unless intended).  
- Use clear markers to separate code generation and explanation phases.  
- Log code, output, and validation results for debugging.

---

## Card 2: Prompt Chaining

**Pattern Name:** Prompt Chaining

**Description:**  
Create multi-step workflows by feeding the output of one prompt into the next, enabling complex tasks through smaller, manageable subtasks.

**When to Use:**  
- Multi-turn tasks requiring intermediate reasoning  
- Plan-then-act or pipeline architectures  
- Generating structured data, then transforming it  
- Iterative refinement and validation loops

**Template:**
```text
### CHAIN STEP 1: Planning
SYSTEM: “You produce a step-by-step plan for <TASK>.”
USER: “<TASK description>”

### CHAIN STEP 2: Execution
SYSTEM: “You follow the plan steps to generate or fetch results.”
USER: “[Insert plan from Step 1]”

### (Optional) CHAIN STEP 3: Validation
SYSTEM: “You review the output and correct errors.”
USER: “[Insert output from Step 2]”
```

**Example:**  
- **Task:** “Extract key takeaways from the meeting transcript and draft action items.”  
  1. **Step 1 (Plan):** LLM outlines “Identify speakers, summarize points, list actions.”  
  2. **Step 2 (Execute):** LLM summarizes content per outline.  
  3. **Step 3 (Validate):** LLM checks that all speakers are covered and items are actionable.

**Best Practices:**  
- Keep each step focused on a single objective.  
- Pass context explicitly (include previous outputs verbatim).  
- Validate intermediate outputs before proceeding.  
- Use versioned prompts for reproducibility.  
- Monitor chain depth to avoid context window overflow.

