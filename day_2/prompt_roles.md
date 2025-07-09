# Prompt Roles in Chat-based Prompts

Large language models like GPT use a chat format with explicit roles for each message. Understanding these roles is essential for crafting effective prompts.

## System Role

- **Purpose**: Establishes overall context, tone and constraints for the assistant.
- **Typical usage**: The first message in a conversation. Keeps instructions short but clear so the model can consistently follow them.
- **Examples**: Setting persona ("You are a helpful travel assistant"), defining formatting requirements or limiting what the assistant should discuss.

## User Role

- **Purpose**: Represents the request or question from the end user. Can include detailed instructions or extra context.
- **Characteristics**: Usually phrased as a direct question or command. May also supply examples or additional background information.
- **Examples**: "Summarize this article," "Explain quantum computing like I'm five."  

## Assistant Role

- **Purpose**: Holds previous responses from the assistant or any system-authored guidance that is meant to appear from the assistant perspective.
- **Use cases**: Maintaining conversation history, providing step-by-step reasoning, or priming the model with an example response.
- **Examples**: A short answer to a prior question, or a message clarifying how the assistant will proceed.

When crafting prompts you can combine these roles to control model behavior. A typical pattern is:

```python
messages = [
    {"role": "system", "content": "You are an expert tutor."},
    {"role": "user", "content": "Explain black holes."},
]
```

The assistant uses the system instructions to guide its reply to the user's question. By carefully structuring each role you can achieve more reliable and context-aware responses.
