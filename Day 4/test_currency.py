# Test it with monkeypatch

# test_currency.py
import currency

class MockResponse:
    def json(self):
        return {"rate": 1.40}

def test_get_usd_to_inr(monkeypatch):
    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(currency.requests, "get", mock_get)

    assert currency.get_usd_to_cad() == 1.40
