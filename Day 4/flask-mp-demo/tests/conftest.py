# tests/conftest.py
import os
import pytest
from app import app as flask_app

@pytest.fixture
def client():
    # Flask test client
    with flask_app.test_client() as c:
        yield c

@pytest.fixture
def set_api_key(monkeypatch):
    # Ensure API key is present for tests that need it
    monkeypatch.setenv("PRICER_API_KEY", "TEST-KEY-123")
    yield
    # auto-restore handled by monkeypatch
