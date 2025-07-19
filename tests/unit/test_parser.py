import pytest
from src.parser import parse_pdf


def test_parse_pdf_minimal(tmp_path):
    # Create a minimal PDF fixture or load a sample
    pdf = tmp_path / "sample.pdf"
    # ... generate or copy a small PDF into pdf ...
    items = parse_pdf(str(pdf))
    assert isinstance(items, list)
    assert all("text" in itm for itm in items)