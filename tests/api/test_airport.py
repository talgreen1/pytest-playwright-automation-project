import requests
import pytest
import allure
from .api_utils import attach_request_response_to_allure

API_BASE = "https://airportgap.com/api"

@pytest.fixture
def airports_response():
    """
    Pytest fixture that sends a GET request to the '/airports' endpoint of the API.
    Asserts that the response status code is 200 (OK) and returns the response object.

    Returns:
        requests.Response: The response object from the GET request to the airports endpoint.
    """
    response = requests.get(f"{API_BASE}/airports")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    return response

@allure.feature("Airport API")
@allure.story("Airport List")
@allure.title("Verify airport count is 30")
@allure.description("Checks that the /airports endpoint returns exactly 30 airports.")
@allure.label("category", "API")
def test_airport_count(airports_response):
    with allure.step("Request airport list from /airports endpoint"):
        response = airports_response
        attach_request_response_to_allure(response)
    with allure.step("Parse response and validate airport count"):
        data = response.json()
        airports = data.get("data", [])
        assert len(airports) == 30, f"Expected 30 airports, got {len(airports)}"

@allure.feature("Airport API")
@allure.story("Airport List")
@allure.title("Verify specific airport is present")
@allure.description("Checks that a known airport is present in the /airports endpoint response.")
@allure.label("category", "API")
@pytest.mark.parametrize("airport_name", [
    "Akureyri Airport",
    "St. Anthony Airport",
    "CFB Bagotville"
])
def test_airport_includes_specific(airports_response, airport_name):
    with allure.step("Request airport list from /airports endpoint"):
        response = airports_response
        attach_request_response_to_allure(response)
    with allure.step(f"Parse response and check for airport: {airport_name}"):
        data = response.json()
        airports = data.get("data", [])
        airport_names = [airport["attributes"]["name"] for airport in airports]
        assert airport_name in airport_names, f"{airport_name} not found in airport list"

@allure.feature("Airport API")
@allure.story("Airport Distance")
@allure.title("Verify distance between airports is above minimum")
@allure.description("Checks that the calculated distance between two airports is greater than the specified minimum value.")
@allure.label("category", "API")
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
    with allure.step(f"Request distance between {from_code} and {to_code} from /airports/distance endpoint"):
        response = requests.post(f"{API_BASE}/airports/distance", json=payload)
        attach_request_response_to_allure(
            response,
            request_info=f"POST {response.request.url}\nPayload: {payload}"
        )
    with allure.step("Parse response and validate distance"):
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        data = response.json()
        distance_km = data.get("data", {}).get("attributes", {}).get("kilometers")
        assert distance_km is not None, "Distance in kilometers not found in response."
        assert distance_km > min_distance, f"Expected distance > {min_distance} km, got {distance_km} km"
