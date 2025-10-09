def test_get_username(monkeypatch):
    # Fake environment variable
    monkeypatch.setenv("USER", "Disha")

    from app import get_user_name
    assert get_user_name() == "Disha"