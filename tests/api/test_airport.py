import requests
import pytest

API_BASE = "https://airportgap.com/api"

def test_airport_count():
    response = requests.get(f"{API_BASE}/airports")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    airports = data.get("data", [])
    assert len(airports) == 30, f"Expected 30 airports, got {len(airports)}"

def test_airport_includes_specific():
    response = requests.get(f"{API_BASE}/airports")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    airports = data.get("data", [])
    airport_names = [airport["attributes"]["name"] for airport in airports]
    for name in ["Akureyri Airport", "St. Anthony Airport", "CFB Bagotville"]:
        assert name in airport_names, f"{name} not found in airport list"

@pytest.mark.parametrize(
    "from_code,to_code,min_distance",
    [
        ("KIX", "NRT", 400),
        ("JFK", "LAX", 3900),
        ("LHR", "CDG", 300),
        ("SYD", "MEL", 700),
        ("SFO", "SEA", 1000),
    ]
)
def test_distance_between_airports(from_code, to_code, min_distance):
    payload = {"from": from_code, "to": to_code}
    response = requests.post(f"{API_BASE}/airports/distance", json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    distance_km = data.get("data", {}).get("attributes", {}).get("kilometers")
    assert distance_km is not None, "Distance in kilometers not found in response."
    assert distance_km > min_distance, f"Expected distance > {min_distance} km, got {distance_km} km"
