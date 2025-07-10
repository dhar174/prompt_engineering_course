#!/usr/bin/env python3
"""
GitHub Actions CI Script for PDF Markdown Artifact Detection
Fails the build if raw markdown artifacts are found in PDFs
"""

import re
import subprocess
import sys
from pathlib import Path

def is_raw_markdown_artifact(pdf_path):
    """Check for obvious raw markdown that should have been rendered"""
    try:
        result = subprocess.run(['pdftotext', pdf_path, '-'], capture_output=True, text=True, timeout=10)
        content = result.stdout.lower()
        
        # Check for clearly unrendered markdown patterns
        
        # 1. Raw headers that start lines with # (not in code examples)
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if re.match(r'^#{1,6}\s+\w', line) and 'example' not in line and 'code' not in line:
                return True, f"Raw header found: {line[:50]}..."
        
        # 2. Bold text that wasn't rendered (**text**)
        bold_matches = re.findall(r'\*\*[^*\s][^*]*[^*\s]\*\*', content)
        if bold_matches:
            # Check if this is in a documentation context (teaching markdown syntax)
            for match in bold_matches:
                # Look for context clues that this is intentional documentation
                match_lines = [line for line in lines if match in line]
                for line in match_lines:
                    # Skip if it's in a context that suggests it's meant to show markdown syntax
                    if any(keyword in line.lower() for keyword in ['markdown', 'syntax', 'example', 'track changes', 'format', 'delimiter', 'snippet']):
                        continue
                    # If no context clues found, it's likely unrendered markdown
                    return True, f"Raw bold markdown found: {match}"
        
        # 3. Table pipes in obvious table context
        table_lines = [line for line in lines if line.count('|') >= 2 and len(line) > 10]
        if len(table_lines) > 2:  # Multiple lines suggest a raw table
            # Check if it looks like a markdown table (not properly rendered)
            for line in table_lines[:3]:
                if re.match(r'^\s*\|.*\|.*\|\s*$', line):
                    return True, f"Raw table found: {line[:50]}..."
        
        # 4. Code blocks with ``` that weren't rendered
        if content.count('```') >= 2:
            # Check if this is in a documentation context (teaching markdown syntax)
            lines_with_backticks = [line for line in lines if '```' in line]
            for line in lines_with_backticks:
                # Skip if it's in a context that suggests it's meant to show markdown syntax
                if any(keyword in line.lower() for keyword in ['delimiter', 'quote', 'format', 'example', 'syntax', 'enclose', 'fences']):
                    continue
                # If no context clues found, it's likely unrendered markdown
                return True, "Raw code blocks found with ``` markers"
        
        return False, None
        
    except Exception as e:
        return False, f"Error checking {pdf_path}: {e}"

def main():
    """CI script main function"""
    print("🔍 Checking PDFs for raw markdown artifacts...")
    
    # Find all PDFs
    pdf_files = list(Path('.').glob('**/*.pdf'))
    
    if not pdf_files:
        print("✅ No PDF files found")
        return 0
    
    failures = []
    
    for pdf_file in pdf_files:
        has_artifacts, message = is_raw_markdown_artifact(str(pdf_file))
        if has_artifacts:
            print(f"❌ {pdf_file}: {message}")
            failures.append(pdf_file)
        else:
            print(f"✅ {pdf_file}")
    
    if failures:
        print(f"\n❌ CI FAIL: {len(failures)} PDFs contain raw markdown artifacts")
        print("\n💡 To fix:")
        print("1. Find the .md source file")
        print("2. Run: python render_pdf.py source.md output.pdf")
        print("3. Commit the properly rendered PDF")
        return 1
    else:
        print(f"\n✅ CI PASS: All {len(pdf_files)} PDFs are properly formatted")
        return 0

if __name__ == "__main__":
    sys.exit(main())