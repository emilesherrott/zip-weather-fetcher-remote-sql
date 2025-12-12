import requests
from typing import Any, Dict

class APIClient:
    """Generic API client for making GET requests to a given base URL.

    Attributes:
        base_url (str): The base URL of the API.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initialize the API client with a base URL.

        Args:
            base_url (str): The base URL of the API.
        """
        self.base_url: str = base_url.rstrip("/")

    def get(self, endpoint: str = "") -> Dict[str, Any]:
        """
        Make a GET request to the API.

        Args:
            endpoint (str, optional): Specific endpoint to append to base URL. Defaults to "".

        Returns:
            dict: JSON response from the API, or error information if request fails.
        """
        url = f"{self.base_url}/{endpoint}".rstrip("/")
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}
