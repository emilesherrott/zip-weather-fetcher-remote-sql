import pytest
from services.api_client import APIClient

def test_get_success(requests_mock):
    client = APIClient("http://example.com")
    requests_mock.get("http://example.com", json={"ok": True})

    resp = client.get()
    assert resp == {"ok": True}

def test_get_failure(requests_mock):
    client = APIClient("http://example.com")
    requests_mock.get("http://example.com", status_code=404)

    resp = client.get()
    assert "error" in resp

