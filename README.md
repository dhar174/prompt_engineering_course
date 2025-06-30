# prompt_engineering_course
Full course content for Prompt Engineering

## Token Counting

Language models process prompts as tokens rather than raw characters. A token is roughly a word fragment and token limits determine how much text a model can handle. You can pre-count tokens with the **tiktoken** library to stay within a model's context window.

The token count of a Jinja template may differ from the count of its rendered output. For example, with the `gpt-4o` tokenizer:

```python
import tiktoken

template = "Hello {{ name }}, you have {{ count }} new messages."
rendered = "Hello John, you have 5 new messages."

enc = tiktoken.encoding_for_model("gpt-4o")
print(len(enc.encode(template)))  # 13 tokens
print(len(enc.encode(rendered)))  # 10 tokens
```

Keeping track of these numbers helps ensure your final rendered prompts do not exceed model limits.
