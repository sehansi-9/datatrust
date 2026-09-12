from datetime import datetime, timezone
from validator import validate_order_event

def generate_order_event():
    return {
        "event_id": "evt_000001",
        "event_type": "order.created",
        "event_version": 1,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": "ecommerce",
        "customer_id": "cust_1023",
        "order_id": "ord_78451",
        "amount": 12500.00,
        "currency": "LKR",
    }


if __name__ == "__main__":
    event = generate_order_event()

    if validate_order_event(event):
        print("Event is valid:")
        print(event)