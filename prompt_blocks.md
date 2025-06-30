# Token Counting and Prompt Blocks

This guide explains how to count tokens in your prompts and how to store
them in a JSON file so they can be composed with Jinja2 templates.

## Counting tokens

Language models break text into **tokens**. The number of tokens depends on
the tokenizer used by the model. You can use the `tiktoken` library to
count tokens:

```python
import tiktoken

def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

sample_prompt = "Explain quantum computing in simple terms."
print(count_tokens(sample_prompt))
```

The snippet above prints the number of tokens for `sample_prompt`.

Sample token counts:

| Prompt | Tokens |
| --- | ---: |
| `Hello, world!` | 4 |
| `Explain quantum computing in simple terms.` | 8 |
| `Summarize the plot of the movie Inception in one sentence.` | 14 |


## Saving prompt blocks

You can organize different pieces of a prompt in a dictionary and save them to `prompt_blocks.json`:

```python
import json

prompt_blocks = {
    "system": "You are a helpful assistant.",
    "user": "Explain quantum computing in simple terms."
}

with open("prompt_blocks.json", "w") as f:
    json.dump(prompt_blocks, f, indent=2)
```

The resulting `prompt_blocks.json` file will contain the individual prompt sections.

## Composing a final prompt with Jinja2

After loading the prompt blocks, you can combine them using a Jinja2 template:

```python
from jinja2 import Template
import json

with open("prompt_blocks.json") as f:
    blocks = json.load(f)

template = Template("""{{ system }}\nUser: {{ user }}""")
final_prompt = template.render(**blocks)
print(final_prompt)
```

This will produce a prompt that first includes the system instruction followed by the user request.
