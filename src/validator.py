import json
from pathlib import Path

from jsonschema import validate

SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "order_created.json"

def validate_order_event(event):
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        schema = json.load(file)

    validate(instance=event, schema=schema) 

    return True   

test_event = {
    "event_id": "evt_000001",
    "event_type": "order.created",
    "event_version": 1,
    "timestamp": "2026-09-12T10:15:32Z",
    "source": "ecommerce",
    "customer_id": "cust_1023",
    "order_id": "ord_78451",
    "amount": 12500.00,
    "currency": "LKR"
}

print(validate_order_event(test_event))