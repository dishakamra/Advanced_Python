# services.py
import os
import requests

PRICER_URL = "https://example-pricer.com/v1/quote"

def get_api_key() -> str:
    key = os.getenv("PRICER_API_KEY")
    if not key:
        raise RuntimeError("PRICER_API_KEY not set")
    return key

def get_quote(items: list[dict]) -> dict:
    """
    Calls an external pricing API; returns {"subtotal": float, "currency": "USD"}
    """
    headers = {"Authorization": f"Bearer {get_api_key()}"}
    resp = requests.post(PRICER_URL, json={"items": items}, headers=headers, timeout=5)
    resp.raise_for_status()
    return resp.json()
