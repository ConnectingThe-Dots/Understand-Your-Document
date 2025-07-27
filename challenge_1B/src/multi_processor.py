# Challenge_1b/src/multi_processor.py

import os
import json
import glob
import click
from src.parser import parse_pdf
from src.analyzer import load_config, assign_levels, chunk_sections, score_sections

@click.command()
@click.option(
    "--config", "cfg_path",
    default="config/default.yaml",
    help="Path to default.yaml"
)
@click.option(
    "--collections-root", default=".",
    help="Root dir containing Collection*/ subfolders"
)
def main(cfg_path: str, collections_root: str):
    """
    Process each Collection*/ folder under collections_root:
    - Read challenge1b_input.json
    - Run persona-driven analysis on each PDF in PDFs/
    - Write challenge1b_output.json
    """
    cfg = load_config(cfg_path)

    pattern = os.path.join(collections_root, "Collection */")
    for coll_dir in sorted(glob.glob(pattern)):
        input_json  = os.path.join(coll_dir, "challenge1b_input.json")
        output_json = os.path.join(coll_dir, "challenge1b_output.json")
        if not os.path.isfile(input_json):
            click.secho(f"⚠️  Skipping {coll_dir} (no input JSON)", fg="yellow")
            continue

        cfg_in = json.load(open(input_json, encoding="utf-8"))
        docs   = cfg_in.get("documents", [])
        persona = cfg_in.get("persona", {}).get("role", "")
        job     = cfg_in.get("job_to_be_done", {}).get("task", "")

        cfg["persona"]["description"]    = persona
        cfg["persona"]["job_to_be_done"] = job

        extracted_sections = []
        subsection_analysis = []

        for doc in docs:
            fname = doc["filename"]
            pdf_path = os.path.join(coll_dir, "PDFs", fname)
            if not os.path.isfile(pdf_path):
                click.secho(f"  ❌ PDF not found: {pdf_path}", fg="red")
                continue

            items    = parse_pdf(pdf_path)
            headings = assign_levels(items, cfg)
            secs     = chunk_sections(headings, cfg["persona"]["max_section_chars"])
            scored   = score_sections(secs, cfg["persona"])

            for sec in scored:
                extracted_sections.append({
                    "document":       fname,
                    "section_title":  sec["title"],
                    "importance_rank": sec["importance_rank"],
                    "page_number":    sec["page"]
                })

            for h in headings:
                subsection_analysis.append({
                    "document":     fname,
                    "refined_text": h["text"],
                    "page_number":  h["page"]
                })

        out = {
            "metadata": {
                "input_documents": [d["filename"] for d in docs],
                "persona": persona,
                "job_to_be_done": job
            },
            "extracted_sections": extracted_sections,
            "subsection_analysis": subsection_analysis
        }

        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
        click.secho(f"✅ Processed {coll_dir} → {output_json}", fg="green")

if __name__ == "__main__":
    main()
