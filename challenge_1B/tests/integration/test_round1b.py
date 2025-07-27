import os
import json
from click.testing import CliRunner
from src.cli import main

def test_round1b(tmp_path):
    inp = tmp_path / "input"
    out = tmp_path / "output"
    inp.mkdir()
    out.mkdir()
    # TODO: copy a small PDF fixture into inp / "sample.pdf"
    runner = CliRunner()
    result = runner.invoke(main, [
        "--config",      "config/default.yaml",
        "--input-dir",   str(inp),
        "--output-dir",  str(out),
        "--persona-desc","AI dev",
        "--job",         "Extract topics",
    ])
    assert result.exit_code == 0
    data = json.loads((out / "sample.json").read_text())
    assert "outline" in data
    assert "extracted_sections" in data
