import requests
import pytest

API_BASE = "https://airportgap.com/api"

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
