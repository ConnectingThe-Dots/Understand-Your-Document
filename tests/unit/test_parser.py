import pytest
from src.parser import parse_pdf
from tests.utils import create_test_pdf


def test_parse_pdf_minimal(tmp_path):
    pdf = tmp_path / "sample.pdf"
    create_test_pdf(str(pdf))
    items = parse_pdf(str(pdf))
    assert isinstance(items, list)
    assert all("text" in itm for itm in items)