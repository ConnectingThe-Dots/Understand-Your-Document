import os
import click
import pdfplumber
from src.utils import setup_logger
from src.parser import parse_pdf
from src.analyzer import load_config, assign_levels
from src.serializer import serialize_outline, dump_json

@click.command()
@click.option("--config",    "cfg_path",      default="config/default.yaml")
@click.option("--input-dir", default="input")
@click.option("--output-dir",default="output")
@click.option("--persona-desc", default="", help="Persona description")
@click.option("--job",         "job_to_be_done", default="", help="Job to be done")
@click.option("--log-level",   default="INFO")
def main(cfg_path, input_dir, output_dir, persona_desc, job_to_be_done, log_level):
    setup_logger(log_level)
    cfg = load_config(cfg_path)
    cfg["persona"]["description"]    = persona_desc
    cfg["persona"]["job_to_be_done"] = job_to_be_done
    os.makedirs(output_dir, exist_ok=True)

    for fn in os.listdir(input_dir):
        if not fn.lower().endswith(".pdf"): continue
        path = os.path.join(input_dir, fn)
        items = parse_pdf(path)
        pages = len(pdfplumber.open(path).pages)
        headings = assign_levels(items, cfg)
        
        # Create schema-compliant output
        out = serialize_outline(headings, fn, cfg_path, pages)
        dump_json(out, os.path.join(output_dir, fn.replace(".pdf", ".json")))
        click.echo(f"{fn} → {fn.replace('.pdf','.json')}")

if __name__=="__main__":
    main()
