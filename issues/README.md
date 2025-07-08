# README for Issue Documentation

This directory contains detailed documentation for issues found during the high-level conceptual review of all notebooks in the prompt engineering course repository.

## Issues Documented

### Critical Issues (Require Immediate Attention)
1. **`issue_json_syntax_error.md`** - JSON syntax error in `pal_plan_act_pipeline.ipynb` that prevents notebook execution
2. **`issue_deprecated_openai_api.md`** - 22 notebooks using deprecated OpenAI API that will fail with current library versions

### High Priority Issues  
3. **`issue_string_concatenation_error.md`** - Malformed string concatenation in `LangGraph_Chatbot.ipynb`

### Medium Priority Issues
4. **`issue_missing_educational_structure.md`** - Educational content structure improvements needed

## How to Use These Issue Documents

Each markdown file contains:
- Detailed problem description
- Code examples showing current vs. expected behavior  
- Impact assessment and priority level
- Recommended GitHub issue labels
- Reference to the original review (#38)

Repository owners can use these documents to:
1. Create GitHub issues by copying the content
2. Assign appropriate labels and priorities
3. Track resolution progress
4. Understand the scope and impact of each problem

## Summary Statistics

- **Total notebooks reviewed**: 36
- **Notebooks with critical issues**: 23 (64%)
- **API compatibility issues**: 22 notebooks  
- **Syntax errors**: 2 notebooks
- **Educational structure issues**: Multiple notebooks

## Original Review

These issues were identified during the comprehensive notebook review documented in `../notebook_review_report.md` as part of GitHub issue #38.