import json
from datetime import datetime
import pytz
from typing import List, Dict

def serialize_outline(
    items: List[Dict],
    title: str,
    config_path: str,
    page_count: int,
) -> Dict:
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    return {
        "title": title,
        "metadata": {
            "pages": page_count,
            "generated_at": now.isoformat(),
            "config_used": config_path,
        },
        "outline": [
            {
                "level": itm["level"],
                "text": itm["text"],
                "page": itm["page"],
                "bbox": itm["bbox"],
                "font": {"name": itm["font_name"], "size": itm["size"]},
            }
            for itm in items
        ],
    }


def dump_json(data: Dict, output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)