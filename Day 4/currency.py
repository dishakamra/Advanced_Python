# write a function that fetaches the latest exchange rate from an API (simulated)

import requests

def get_usd_to_cad():
    response = requests.get("https://api.exchangerate.com/usd-cad")
    return response.json()["rate"]