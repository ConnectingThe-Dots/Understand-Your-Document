import pytest
from src.parser import parse_pdf

def test_parse_pdf_empty(tmp_path):
    # create an empty PDF or use a fixture; here we assume a sample.pdf exists
    pdf = tmp_path / "sample.pdf"
    # TODO: generate or copy a minimal PDF into pdf
    items = parse_pdf(str(pdf))
    assert isinstance(items, list)
