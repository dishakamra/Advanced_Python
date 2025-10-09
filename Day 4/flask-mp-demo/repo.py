# repo.py
# Pretend data layer (could be SQL/ORM in real life)

_USERS = {
    1: {"id": 1, "name": "Alice", "tier": "gold"},
    2: {"id": 2, "name": "Bob", "tier": "standard"},
}

def get_user(user_id: int) -> dict | None:
    # Imagine a DB lookup here
    return _USERS.get(user_id)

def save_order(user_id: int, items: list[dict]) -> dict:
    # Imagine INSERT + returning the order id
    return {"order_id": 123, "user_id": user_id, "items": items}
