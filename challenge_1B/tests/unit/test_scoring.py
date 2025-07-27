import pytest
from src.analyzer import chunk_sections, score_sections

def test_chunk_and_score():
    headings = [
        {"level":1,"text":"Intro","page":1},
        {"level":2,"text":"Detail A","page":1},
        {"level":1,"text":"Conclusion","page":5},
    ]
    sections = chunk_sections(headings, max_chars=100)
    persona = {
        "embed_model":"all-MiniLM-L6-v2",
        "description":"Test persona",
        "job_to_be_done":"Test job",
        "relevance_threshold":0.0,
    }
    scored = score_sections(sections, persona)
    assert all("importance_rank" in sec for sec in scored)
