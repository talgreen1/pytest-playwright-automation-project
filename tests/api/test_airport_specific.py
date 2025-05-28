import requests
import pytest

API_BASE = "https://airportgap.com/api"

def test_airport_includes_specific():
    response = requests.get(f"{API_BASE}/airports")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    airports = data.get("data", [])
    airport_names = [airport["attributes"]["name"] for airport in airports]
    for name in ["Akureyri Airport", "St. Anthony Airport", "CFB Bagotville"]:
        assert name in airport_names, f"{name} not found in airport list"
