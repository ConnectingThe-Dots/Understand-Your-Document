import os
import json
from click.testing import CliRunner
from src.cli import main
from tests.utils import create_test_pdf


def test_end_to_end(tmp_path, monkeypatch):
    # Setup sample PDF in tmp_path/input
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    output_dir.mkdir()
    sample_pdf = input_dir / "doc.pdf"
    create_test_pdf(str(sample_pdf))

    runner = CliRunner()
    result = runner.invoke(
        main, [
            "--config", "config/default.yaml",
            "--input-dir", str(input_dir),
            "--output-dir", str(output_dir)
        ]
    )
    assert result.exit_code == 0
    files = os.listdir(output_dir)
    assert any(f.endswith(".json") for f in files)
    data = json.load(open(output_dir / files[0], encoding="utf-8"))
    assert "outline" in data