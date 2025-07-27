import os
import click
import pdfplumber
from challenge_1B.src.utils import setup_logger
from challenge_1B.src.parser import parse_pdf
from challenge_1B.src.analyzer import (
    load_config,
    assign_levels,
    chunk_sections,
    score_sections,
)
from challenge_1B.src.serializer import serialize_round1b, dump_json

@click.command()
@click.option("--config",    "cfg_path",      default="config/default.yaml")
@click.option("--input-dir", "input_dir",     default="input")
@click.option("--output-dir","output_dir",    default="output")
@click.option("--persona-desc", "persona_desc", default="", help="Persona description")
@click.option("--job",           "job_to_be_done", default="", help="Job to be done")
@click.option("--log-level",     default="INFO")
def main(cfg_path, input_dir, output_dir, persona_desc, job_to_be_done, log_level):
    setup_logger(log_level)
    cfg = load_config(cfg_path)
    cfg["persona"]["description"]    = persona_desc
    cfg["persona"]["job_to_be_done"] = job_to_be_done
    os.makedirs(output_dir, exist_ok=True)

    for fn in sorted(os.listdir(input_dir)):
        if not fn.lower().endswith(".pdf"):
            continue
        path = os.path.join(input_dir, fn)
        items = parse_pdf(path)
        pages = len(pdfplumber.open(path).pages)
        headings = assign_levels(items, cfg)

        if persona_desc and job_to_be_done:
            secs   = chunk_sections(headings, cfg["persona"]["max_section_chars"])
            scored = score_sections(secs, cfg["persona"])
            out    = serialize_round1b(headings, scored, cfg_path, fn, pages)
        else:
            out = serialize_round1b(headings, [], cfg_path, fn, pages)

        dump_json(out, os.path.join(output_dir, fn.replace(".pdf", ".json")))
        click.echo(f"[1B] {fn} → {fn.replace('.pdf','.json')}")

if __name__ == "__main__":
    main()
