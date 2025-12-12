import pytest
from services.fetch_service import FetchService
from tests.conftest import MockResponse

class MockLocationClient:
    def get(self, endpoint=""):
        return {"postcode": "ZZ99", "lat": 51.5, "lon": -0.1}

class MockWeatherClient:
    def get(self, endpoint=""):
        return {"current_condition": [{
            "temp_C": "25",
            "temp_F": "77",
            "humidity": "40",
            "weatherDesc": [{"value": "Clear"}]
        }]}

def test_fetch_service(monkeypatch, tmp_path):
    """
    Test FetchService.run with separate location and weather API mocks.
    """

    # Patch APIClient constructor to return different mocks depending on URL
    def mock_api_client_init(self, base_url):
        if "ip-api.com" in base_url:
            self.get = MockLocationClient().get
        else:
            self.get = MockWeatherClient().get
        self.base_url = base_url

    monkeypatch.setattr("services.api_client.APIClient.__init__", mock_api_client_init)

    # Run FetchService
    json_path = str(tmp_path / "out.json")
    res = FetchService.run(json_path)

    # Assertions
    assert res["postcode"] == "ZZ99"
    assert res["current_weather"]["temp_C"] == "25"
    assert res["current_weather"]["temp_F"] == "77"
    assert res["current_weather"]["humidity"] == "40"
    assert res["current_weather"]["weather_desc"] == "Clear"

