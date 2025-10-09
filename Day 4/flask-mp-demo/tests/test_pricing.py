# tests/test_pricing.py
import repo
import services
import pytest

def test_create_order_happy_path(client, monkeypatch, set_api_key):
    # --- Patch DB lookups ---
    monkeypatch.setattr(repo, "get_user", lambda _id: {"id": _id, "name": "Alice", "tier": "gold"})
    monkeypatch.setattr(repo, "save_order", lambda uid, items: {"order_id": 777, "user_id": uid, "items": items})

    # --- Patch external HTTP ---
    class FakeResp:
        def __init__(self, payload, status=200):
            self._payload = payload
            self.status_code = status
        def raise_for_status(self):
            if self.status_code >= 400:
                raise RuntimeError("bad status")
        def json(self):
            return self._payload

    def fake_post(url, json, headers, timeout):
        assert url == services.PRICER_URL
        assert "Authorization" in headers
        # Return a “priced” response
        return FakeResp({"subtotal": 123.45, "currency": "USD"})

    # Replace only requests.post inside services module
    monkeypatch.setattr(services, "requests", type("R", (), {"post": fake_post}))

    payload = {
        "user_id": 1,
        "items": [{"sku":"ABC","qty":2,"price":10.0}, {"sku":"XYZ","qty":1,"price":50.0}]
    }
    res = client.post("/orders", json=payload)
    assert res.status_code == 201
    body = res.get_json()
    assert body["order"]["order_id"] == 777
    assert body["pricing"]["subtotal"] == 123.45
    assert body["user_tier"] == "gold"

def test_create_order_missing_api_key(client, monkeypatch):
    # Ensure API key is missing
    monkeypatch.delenv("PRICER_API_KEY", raising=False)

    # Patch DB to return a valid user so we reach pricing step
    monkeypatch.setattr(repo, "get_user", lambda _id: {"id": _id, "name": "Alice", "tier": "gold"})

    res = client.post("/orders", json={
        "user_id": 1,
        "items": [{"sku":"ABC","qty":1,"price":10.0}]
    })
    # Our app will hit services.get_api_key() which raises RuntimeError
    # Flask will convert unhandled exception into a 500; in a real app you'd handle it.
    assert res.status_code == 500

@pytest.mark.parametrize("bad_payload", [
    {},  # missing everything
    {"user_id": 1, "items": []},  # empty items
    {"user_id": None, "items": [{"sku":"A","qty":1,"price":1.0}]},  # no user
])
def test_create_order_bad_payload(client, bad_payload):
    res = client.post("/orders", json=bad_payload)
    assert res.status_code == 400
