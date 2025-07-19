import os
import click
from src.utils import setup_logger
from src.parser import parse_pdf
from src.analyzer import load_config, assign_levels
from src.serializer import serialize_outline, dump_json
import pdfplumber

@click.command()
@click.option(
    "--config", "config_path", default="config/default.yaml",
    help="Path to YAML config file."
)
@click.option(
    "--input-dir", default="input",
    help="Directory with PDF files."
)
@click.option(
    "--output-dir", default="output",
    help="Directory for JSON output."
)
@click.option(
    "--log-level", default="INFO",
    help="Logging level: DEBUG, INFO, WARNING, ERROR."
)
def main(config_path, input_dir, output_dir, log_level):
    setup_logger(log_level)
    cfg = load_config(config_path)
    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(input_dir):
        if not fname.lower().endswith(".pdf"):
            continue
        pdf_path = os.path.join(input_dir, fname)
        items = parse_pdf(pdf_path)
        with pdfplumber.open(pdf_path) as pdf:
            page_count = len(pdf.pages)
        headings = assign_levels(items, cfg)
        data = serialize_outline(headings, fname, config_path, page_count)
        out_fname = os.path.splitext(fname)[0] + ".json"
        dump_json(data, os.path.join(output_dir, out_fname))
        click.echo(f"Processed {fname} → {out_fname}")

if __name__ == "__main__":
    main()