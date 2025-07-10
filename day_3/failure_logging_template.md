# Prompt Failure Logging Template

| Date       | Prompt ID/Name | Prompt Version | Input (Prompt/Context) | Expected Output              | Actual Output               | Failure Type                  | Notes                                    | Resolution / Next Steps               |
|------------|----------------|----------------|------------------------|------------------------------|-----------------------------|--------------------------------|------------------------------------------|---------------------------------------|
| YYYY-MM-DD | e.g., Q1_Greedy | v1.0          | "Translate X to Y"      | Correct translation of X     | Hallucinated content        | Hallucination / Off-topic      | Model invented facts about X            | Lowered temperature; added explicit constraints |
| YYYY-MM-DD |                |                |                        |                              |                             |                                |                                          |                                       |

**Columns:**
- **Date:** When the failure occurred or was logged (YYYY-MM-DD).  
- **Prompt ID/Name:** Unique identifier for the prompt (e.g., Q1_Greedy).  
- **Prompt Version:** Version number or tag of the prompt.  
- **Input:** The exact prompt text and any context.  
- **Expected Output:** What the model should have produced.  
- **Actual Output:** What the model actually produced.  
- **Failure Type:** Category (e.g., timeout, hallucination, repetition, formatting error).  
- **Notes:** Additional observations (e.g., context ambiguity, API errors).  
- **Resolution / Next Steps:** Actions taken or planned (e.g., adjust parameters, refine prompt).  

_Use this template to consistently track and troubleshoot prompt failures, facilitating systematic improvements._