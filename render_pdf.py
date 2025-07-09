#!/usr/bin/env python3
"""
PDF Rendering Script for Markdown Files
Based on the instructions in docs/howto_render_pdf.md
"""

from pathlib import Path
import re
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle, ListFlowable, ListItem
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def markdown_to_story(md_text, styles):
    story, i = [], 0
    lines = md_text.splitlines()
    
    while i < len(lines):
        line = lines[i].rstrip()

        # 1. blank → vertical spacing
        if not line.strip():
            story.append(Spacer(1, 6))
            i += 1
            continue

        # 2. headings (#, ##, ###)
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            text = line[level:].strip()
            # Remove emoji and extra spaces
            text = re.sub(r'[^\w\s\-.,;:!?()]', '', text).strip()
            heading_style = f"Heading{min(level, 3)}"
            story.append(Paragraph(text, styles[heading_style]))
            story.append(Spacer(1, 12))  # Extra space after headings
            i += 1
            continue

        # 3. table block (consecutive lines starting with `|`)
        if line.startswith("|"):
            table_raw = []
            while i < len(lines) and lines[i].startswith("|"):
                table_raw.append(lines[i].strip("|"))
                i += 1
            # drop optional separator row (`---`)
            if len(table_raw) >= 2 and set(table_raw[1].replace("-","").replace("|","").strip()) <= {" ", ""}:
                table_raw.pop(1)
            
            # Process table data
            data = []
            for row in table_raw:
                cells = [cell.strip() for cell in row.split("|")]
                # Apply bold/italic formatting to cells
                formatted_cells = []
                for cell in cells:
                    formatted_cell = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", cell)
                    formatted_cell = re.sub(r"\*(.+?)\*", r"<i>\1</i>", formatted_cell)
                    formatted_cells.append(formatted_cell)
                data.append(formatted_cells)
            
            if data:  # Only create table if we have data
                tbl = Table(data, hAlign="LEFT")
                tbl.setStyle(TableStyle([
                    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#d0d0d0")),
                    ("GRID", (0,0), (-1,-1), 0.25, colors.grey),
                    ("FONT", (0,0), (-1,0), "Helvetica-Bold"),
                    ("VALIGN", (0,0), (-1,-1), "TOP"),
                    ("LEFTPADDING", (0,0), (-1,-1), 6),
                    ("RIGHTPADDING", (0,0), (-1,-1), 6),
                ]))
                story.append(tbl)
                story.append(Spacer(1, 12))
            continue

        # 4. bullet list block
        if line.lstrip().startswith(("- ", "* ")):
            def parse_list(lines, start_index, base_indent):
                items, i = [], start_index
                while i < len(lines) and lines[i].lstrip().startswith(("- ", "* ")):
                    bullet = lines[i].lstrip()[2:].strip()
                    indent_level = (len(lines[i]) - len(lines[i].lstrip())) // 2
                    bullet_html = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", bullet)
                    bullet_html = re.sub(r"\*(.+?)\*", r"<i>\1</i>", bullet_html)
                    bullet_html = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", bullet_html)
                    if indent_level > base_indent:
                        sublist, i = parse_list(lines, i, indent_level)
                        items.append(ListFlowable(sublist, bulletType="bullet"))
                    else:
                        items.append(ListItem(Paragraph(bullet_html, styles["BodyText"])))
                        i += 1
                return items, i
            
            items, i = parse_list(lines, i, 0)
            story.append(ListFlowable(items, bulletType="bullet"))
            story.append(Spacer(1, 6))
            continue

        # 5. code block (```)
        if line.strip().startswith("```"):
            code_lines = [line]
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):  # Add closing ```
                code_lines.append(lines[i])
                i += 1
            
            # Create preformatted text block
            code_content = "\n".join(code_lines[1:-1])  # Remove opening and closing ```
            if code_content.strip():
                story.append(Paragraph(f"<font name='Courier' size='10'>{code_content}</font>", styles["BodyText"]))
                story.append(Spacer(1, 6))
            continue

        # 6. horizontal rule (---)
        if line.strip() == "---":
            story.append(Spacer(1, 12))
            i += 1
            continue

        # 7. normal paragraph with inline bold / italic
        html = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)
        html = re.sub(r"\*(.+?)\*", r"<i>\1</i>", html)
        html = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", html)
        # Handle links [text](url) -> show as underlined text
        html = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"<u>\1</u>", html)
        
        if html.strip():  # Only add non-empty paragraphs
            story.append(Paragraph(html, styles["BodyText"]))
            story.append(Spacer(1, 6))
        i += 1

    return story

def render_pdf(md_path, pdf_path):
    """Render a markdown file to PDF"""
    print(f"Rendering {md_path} -> {pdf_path}")
    
    text = Path(md_path).read_text(encoding='utf-8')
    styles = getSampleStyleSheet()
    
    # Ensure Heading3 exists
    if "Heading3" not in styles:
        styles.add(ParagraphStyle(
            name="Heading3",
            parent=styles["Heading2"],
            fontSize=12,
            spaceAfter=6
        ))
    
    # Create document with margins
    doc = SimpleDocTemplate(
        pdf_path, 
        pagesize=letter,
        leftMargin=40, 
        rightMargin=40, 
        topMargin=40, 
        bottomMargin=40
    )
    
    story = markdown_to_story(text, styles)
    doc.build(story)
    print(f"✅ Successfully created {pdf_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python render_pdf.py <input.md> <output.pdf>")
        sys.exit(1)
    
    md_path = sys.argv[1]
    pdf_path = sys.argv[2]
    
    if not Path(md_path).exists():
        print(f"Error: {md_path} does not exist")
        sys.exit(1)
    
    try:
        render_pdf(md_path, pdf_path)
    except Exception as e:
        print(f"Error rendering PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()