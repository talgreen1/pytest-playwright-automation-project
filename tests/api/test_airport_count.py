import requests
import pytest

API_BASE = "https://airportgap.com/api"

def test_airport_count():
    response = requests.get(f"{API_BASE}/airports")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    airports = data.get("data", [])
    assert len(airports) == 30, f"Expected 30 airports, got {len(airports)}"
