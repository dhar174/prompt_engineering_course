# prompt_engineering_course
Full course content for Prompt Engineering

## Token Counting and Prompt Blocks

The notebooks use the **tiktoken** library to measure how many tokens a prompt
uses. Counting tokens helps keep prompts within the context window for a model.
Below is a short example:

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o-mini")
prompt = "Translate this sentence into French."
tokens = enc.encode(prompt)
print(len(tokens))  # 6
```

``prompt_blocks.json`` demonstrates how prompt snippets can be stored. A YAML
version is also included. Both files contain blocks referenced by Jinja2
templates:

```json
{
  "intro": "You are a helpful assistant.",
  "task": "Summarize the following article in three bullet points."
}
```

To render a final prompt from these blocks:

```python
from jinja2 import Template
import json

with open("prompt_blocks.json") as fp:
    blocks = json.load(fp)

template = Template("{{ intro }}\n\n{{ task }}")
final_prompt = template.render(**blocks)
```

This approach makes it easy to reuse prompt components and check their token
cost before sending them to a model.
