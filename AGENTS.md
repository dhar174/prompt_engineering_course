# To Pull Issues:

## With GitHub CLI:
```bash
# List issues
gh issue list

# Open a new issue
gh issue create -t "Bug in lesson 3" -b "Steps to reproduce..."
```

## B. With curl

```bash
curl -s -H "Authorization: Bearer $GH_TOKEN" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/repos/dhar174/prompt_engineering_course/issues
```

## C. With Python (PyGithub)
```python
from github import Github
import os

g = Github(os.environ["GH_TOKEN"])
repo = g.get_repo("dhar174/prompt_engineering_course")
repo.create_issue(title="Bug in lesson 3", body="Steps to reproduce...")
```


