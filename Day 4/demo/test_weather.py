# test_weather.py
import weather

def test_report(monkeypatch):
    def fake_get_weather(city):
        return "Sunny"
    
    # Replace original function with fake one
    monkeypatch.setattr(weather, "get_weather", fake_get_weather)

    result = weather.report("Delhi")
    assert result == "The weather in Delhi is Sunny"
