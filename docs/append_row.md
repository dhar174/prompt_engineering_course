# Append a Row to CSV or Google Sheet

This example demonstrates how to open a local CSV log or a Google Sheet and append a new row using Python.

## Requirements

```bash
pip install pandas gspread oauth2client
```

## Working with a Local CSV

```python
import pandas as pd
from pathlib import Path

LOG_PATH = Path("prompt_versions.csv")

# Load existing log or create a new DataFrame
if LOG_PATH.exists():
    df = pd.read_csv(LOG_PATH)
else:
    df = pd.DataFrame(columns=[
        "timestamp", "prompt_name", "version",
        "prompt_text", "parameters", "outcome", "notes"
    ])

# Example entry to append
entry = {
    "timestamp": "2024-01-01T00:00:00",
    "prompt_name": "email_summarizer",
    "version": "0.1",
    "prompt_text": "Summarize the following email ...",
    "parameters": "{\"temperature\": 0.3}",
    "outcome": "success",
    "notes": "Initial baseline"
}

# Append and save
df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
df.to_csv(LOG_PATH, index=False)
```

## Sync to Google Sheets (optional)

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

creds_json = 'path/to/credentials.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
client = gspread.authorize(creds)
sheet = client.open('PromptVersions').sheet1

# Append the last row from the DataFrame
sheet.append_row(df.iloc[-1].tolist())
```
