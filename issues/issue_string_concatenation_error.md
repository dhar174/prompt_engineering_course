# String concatenation syntax error in LangGraph_Chatbot.ipynb

## Problem
The `LangGraph_Chatbot.ipynb` notebook contains malformed string concatenation that causes syntax errors.

## Details
- **Location**: Function definition around line 38-46
- **Issue**: Malformed multi-line string concatenation with quotes and newlines
- **Impact**: Code cell fails to execute

## Current Problematic Code
```python
def set_env(var: str):
"
                               "    if not os.environ.get(var):
"
                               "        os.environ[var] = getpass.getpass(f'Enter {var}: ')

"
                               "# Set your OpenAI API key
"
                               "set_env('OPENAI_API_KEY')
```

## Expected Fix
Proper function definition structure:
```python
def set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f'Enter {var}: ')

# Set your OpenAI API key
set_env('OPENAI_API_KEY')
```

## Priority
⚠️ **HIGH** - This is a popular advanced notebook that students expect to work.

## Found by
High-level conceptual review (#38)

---
**Recommended Labels**: `bug`, `high-priority`, `notebook`