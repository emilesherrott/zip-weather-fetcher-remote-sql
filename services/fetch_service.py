from .api_client import APIClient
from .data_store import JSONDataStore
from .db import WeatherDB
from typing import Any, Dict


class FetchService:
    """Fetch postcode and current weather conditions using free APIs.

    Attributes:
        LOCATION_API (str): Base URL for IP-based location API.
        WEATHER_API (str): Base URL for weather API (wttr.in).
    """

    LOCATION_API: str = "http://ip-api.com/json/"
    WEATHER_API: str = "https://wttr.in"

    @classmethod
    def run(cls, json_path: str) -> Dict[str, Any]:
        """
        Fetch postcode and current weather, then save to JSON and DB.

        Args:
            json_path (str): Path to JSON file for saving results.

        Returns:
            dict: Dictionary containing postcode and current weather info.
        """
        # 0️⃣ Initialize JSON storage
        store: JSONDataStore = JSONDataStore(json_path)
        combined: Dict[str, Any] = {}

        # 1️⃣ Fetch location
        location_client: APIClient = APIClient(cls.LOCATION_API)
        location: Dict[str, Any] = location_client.get()

        # Extract postcode from location API (UK-friendly)
        postcode: str = (
            location.get("postcode") or 
            location.get("postal_code") or 
            location.get("zip")  # fallback for compatibility
        )

        lat: float = location.get("lat")
        lon: float = location.get("lon")

        # Store postcode in combined dictionary
        combined["postcode"] = postcode

        # 2️⃣ Fetch current weather if coordinates exist
        if lat is not None and lon is not None:
            weather_client: APIClient = APIClient(f"{cls.WEATHER_API}/{lat},{lon}?format=j1")
            weather_data: Dict[str, Any] = weather_client.get()
            current: Dict[str, Any] = weather_data.get("current_condition", [{}])[0]

            combined["current_weather"] = {
                "temp_C": current.get("temp_C"),
                "temp_F": current.get("temp_F"),
                "weather_desc": current.get("weatherDesc", [{}])[0].get("value"),
                "humidity": current.get("humidity"),
            }
        else:
            combined["current_weather"] = {"error": "Cannot fetch weather without location"}

        # 3️⃣ Save to local JSON
        store.write(combined)

        # 4️⃣ Save to centralized SQLite DB
        db = WeatherDB()
        db.insert_weather(combined)

        return combined

