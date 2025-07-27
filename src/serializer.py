import json
import os
from datetime import datetime
import pytz
from typing import List, Dict
from jsonschema import validate

def load_schema() -> Dict:
    """Load the JSON schema for output validation."""
    schema_path = os.path.join(os.path.dirname(__file__), "schema", "output.json")
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)

def serialize_outline(
    items: List[Dict],
    title: str,
    config_path: str,
    page_count: int,
) -> Dict:
    """Convert extracted outline to schema-compliant format."""
    data = {
        "title": title,
        "outline": [
            {
                "level": str(itm["level"]),  # Convert level to string to match schema
                "text": itm["text"],
                "page": itm["page"]
            }
            for itm in items
        ]
    }
    # Validate data against schema before returning
    schema = load_schema()
    validate(instance=data, schema=schema)
    return data

def dump_json(data: Dict, output_path: str) -> None:
    """Save data to JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
