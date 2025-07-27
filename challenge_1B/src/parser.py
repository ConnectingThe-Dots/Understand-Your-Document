import pdfplumber
import re
from collections import defaultdict, Counter
from typing import List, Dict

def normalize_text(text: str) -> str:
    return re.sub(r"-\s*\n\s*", "", text).replace("\n", " ").strip()

def parse_pdf(path: str) -> List[Dict]:
    items = []
    with pdfplumber.open(path) as pdf:
        for page_no, page in enumerate(pdf.pages, start=1):
            lines = defaultdict(list)
            for c in page.chars:
                key = round(c["top"], 1)
                lines[key].append(c)
            for top in sorted(lines.keys(), reverse=True):
                chars = sorted(lines[top], key=lambda c: c["x0"])
                text = normalize_text("".join(c["text"] for c in chars))
                if not text:
                    continue
                sizes = [c["size"] for c in chars]
                avg_size = sum(sizes) / len(sizes)
                x0 = min(c["x0"] for c in chars)
                x1 = max(c["x1"] for c in chars)
                top_ = min(c["top"] for c in chars)
                bottom = max(c["bottom"] for c in chars)
                font = Counter(c["fontname"] for c in chars).most_common(1)[0][0]
                items.append({
                    "page": page_no,
                    "text": text,
                    "font_name": font,
                    "size": avg_size,
                    "bbox": [x0, top_, x1, bottom],
                    "is_bold": "Bold" in font,
                    "is_italic": any(i in font for i in ("Italic", "Oblique")),
                    "indent": x0,
                })
    return items
