# weather.py
def get_weather(city):
    # In reality, this might call an API
    raise NotImplementedError("API not available")

def report(city):
    return f"The weather in {city} is {get_weather(city)}"
