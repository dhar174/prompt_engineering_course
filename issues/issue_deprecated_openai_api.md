# URGENT: Deprecated OpenAI API usage in 22 notebooks breaks functionality

## Problem
22 notebooks use deprecated OpenAI API calls that fail with current library versions (v1.0+).

## Affected Notebooks
### Core Foundation (HIGH PRIORITY)
- `self_consistency_uncertainty.ipynb`
- `function_calling_demo.ipynb` 
- `prompt_anatomy_template.ipynb`
- `decoding_parameters_playground.ipynb`
- `structured_output_validation.ipynb`
- `shot_prompt_patterns.ipynb`

### All Day 8 Security Notebooks (8 total)
- `day8_adversarial_robustness_logging.ipynb`
- `day8_adversarial_robustness_logging_a.ipynb`
- `day8_bias_alignment_constitutional.ipynb`
- `day8_bias_alignment_constitutional_a.ipynb`
- `day8_guardrails_moderation.ipynb`
- `day8_guardrails_moderation_a.ipynb`
- `day8_moderation_toolkits.ipynb`
- `day8_moderation_toolkits_a.ipynb`
- `day8_privacy_consent_regulatory.ipynb`
- `day8_privacy_consent_regulatory_a.ipynb`
- `day8_prompt_injection_jailbreak.ipynb`
- `day8_prompt_injection_jailbreak_a.ipynb`

### Additional Notebooks
- `decoding_strategies_playground.ipynb`
- `modular_prompt_library_builder.ipynb`
- `persona_roleplay_workbench.ipynb`
- `prompt_versioning_failure_log.ipynb`

## Issues Found
1. **Deprecated API calls**: Using `openai.ChatCompletion.create()` instead of client-based approach
2. **Deprecated API key setting**: Using `openai.api_key` instead of client initialization  
3. **Deprecated function calling**: Using `functions=` parameter instead of `tools=` parameter

## Required Changes
```python
# OLD (deprecated - BREAKS with current versions):
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.ChatCompletion.create(
    model='gpt-4o-mini',
    messages=[...],
    functions=[...]  # Also deprecated
)

# NEW (current API):
from openai import OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[...],
    tools=[...]  # Updated parameter name
)
```

## Impact
🚨 **CRITICAL** - These notebooks will completely fail to run for students using current OpenAI Python library versions.

## Priority
**URGENT** - Should be fixed immediately as this affects the majority of practical exercises.

## Found by
High-level conceptual review (#38)

---
**Recommended Labels**: `bug`, `urgent`, `api-compatibility`, `notebook`