# tests/test_users.py
import repo

def test_get_user_found(client, monkeypatch):
    # Fake DB: return a specific user regardless of id
    def fake_get_user(user_id: int):
        return {"id": user_id, "name": "Disha", "tier": "platinum"}
    monkeypatch.setattr(repo, "get_user", fake_get_user)

    res = client.get("/users/999")
    assert res.status_code == 200
    data = res.get_json()
    assert data["name"] == "Disha"
    assert data["tier"] == "platinum"

def test_get_user_not_found(client, monkeypatch):
    # Fake DB: always return None
    monkeypatch.setattr(repo, "get_user", lambda _id: None)

    res = client.get("/users/1")
    assert res.status_code == 404
    assert res.get_json()["error"] == "not found"
