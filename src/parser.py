# src/parser.py  (updated parse_pdf)
import pdfplumber
import re
from typing import List, Dict
from collections import defaultdict

def normalize_text(text: str) -> str:
    # Join hyphenated line breaks and collapse whitespace
    return re.sub(r"-\s*\n\s*", "", text).replace("\n", " ").strip()

def parse_pdf(path: str) -> List[Dict]:
    """
    Extracts text lines (not single letters) with metadata from each page.
    Groups chars by similar 'top' position to form lines.
    """
    items = []
    with pdfplumber.open(path) as pdf:
        for page_no, page in enumerate(pdf.pages, start=1):
            # bucket chars into lines by rounding their 'top' coordinate
            lines = defaultdict(list)
            for char in page.chars:
                # round top to nearest integer (or e.g. to nearest 2‐px)
                line_key = round(char["top"], 1)
                lines[line_key].append(char)

            for top_key in sorted(lines.keys(), reverse=True):
                chars = sorted(lines[top_key], key=lambda c: c["x0"])
                text = normalize_text("".join(c["text"] for c in chars))
                if not text:
                    continue

                # metadata: average font size, bbox covering the line
                sizes = [c["size"] for c in chars]
                avg_size = sum(sizes) / len(sizes)
                x0 = min(c["x0"] for c in chars)
                x1 = max(c["x1"] for c in chars)
                top = min(c["top"] for c in chars)
                bottom = max(c["bottom"] for c in chars)
                font_names = [c["fontname"] for c in chars]
                # pick the most common font for this line
                from collections import Counter
                font = Counter(font_names).most_common(1)[0][0]

                items.append({
                    "page": page_no,
                    "text": text,
                    "font_name": font,
                    "size": avg_size,
                    "bbox": [x0, top, x1, bottom],
                    "is_bold": "Bold" in font,
                    "is_italic": any(i in font for i in ("Italic", "Oblique")),
                    "indent": x0,
                })
    return items
