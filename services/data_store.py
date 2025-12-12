import json
from pathlib import Path
from typing import Any, Dict

class JSONDataStore:
    """Utility class to read and write JSON data to a file.

    Attributes:
        path (Path): File path for storing JSON data.
    """

    def __init__(self, path: str) -> None:
        """
        Initialize the data store and ensure parent directories exist.

        Args:
            path (str): Path to the JSON file.
        """
        self.path: Path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, data: Dict[str, Any]) -> None:
        """
        Write a dictionary to a JSON file.

        Args:
            data (dict): Data to write to JSON.
        """
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def read(self) -> Dict[str, Any]:
        """
        Read data from the JSON file.

        Returns:
            dict: JSON data, or empty dict if file does not exist.
        """
        if not self.path.exists():
            return {}
        with open(self.path, "r") as f:
            return json.load(f)
