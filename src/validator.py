import json
from pathlib import Path

from jsonschema import validate

SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "order_created.json"

def validate_order_event(event):
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        schema = json.load(file)

    validate(instance=event, schema=schema) 

    return True   