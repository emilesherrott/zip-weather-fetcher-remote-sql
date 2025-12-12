class MockResponse:
    """Mock object to simulate requests responses."""
    def __init__(self, json_data):
        self._json = json_data

    def raise_for_status(self):
        return

    def json(self):
        return self._json

