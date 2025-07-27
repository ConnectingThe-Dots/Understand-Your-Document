import json
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import List, Dict

def serialize_round1b(
    headings: List[Dict],
    sections: List[Dict],
    cfg_path: str,
    title: str,
    pages: int,
) -> Dict:
    now = datetime.now(ZoneInfo("Asia/Kolkata"))
    return {
        "title": title,
        "metadata": {
            "pages": pages,
            "generated_at": now.isoformat(),
            "config_used": cfg_path,
        },
        "extracted_sections": [
            {"title": s["title"], "page": s["page"], "importance_rank": s["importance_rank"]}
            for s in sections
        ],
        "outline": [
            {"level": h["level"], "text": h["text"], "page": h["page"]} for h in headings
        ],
    }

def dump_json(data: Dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
