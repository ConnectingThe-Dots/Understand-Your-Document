import pdfplumber
import re
from typing import List, Dict

def normalize_text(text: str) -> str:
    # Join hyphenated line breaks
    return re.sub(r"-\n", "", text).strip()


def parse_pdf(path: str) -> List[Dict]:
    """
    Extract text runs with metadata from each page.
    Returns list of dicts: {
      page: int,
      text: str,
      font_name: str,
      size: float,
      bbox: [x0, top, x1, bottom],
      is_bold: bool,
      is_italic: bool,
      indent: float
    }
    """
    items = []
    with pdfplumber.open(path) as pdf:
        for page_no, page in enumerate(pdf.pages, start=1):
            for char in page.chars:
                # grouping on line-level later
                pass  # handled by pdfplumber.extract_words
            words = page.extract_words(extra_attrs=["fontname", "size", "adv"])
            for w in words:
                text = normalize_text(w.get("text", ""))
                if not text:
                    continue
                font = w.get("fontname", "")
                size = w.get("size", 0.0)
                bbox = [w.get("x0"), w.get("top"), w.get("x1"), w.get("bottom")]
                is_bold = 'Bold' in font
                is_italic = 'Italic' in font or 'Oblique' in font
                indent = w.get("x0", 0.0)
                items.append({
                    "page": page_no,
                    "text": text,
                    "font_name": font,
                    "size": size,
                    "bbox": bbox,
                    "is_bold": is_bold,
                    "is_italic": is_italic,
                    "indent": indent,
                })
    return items