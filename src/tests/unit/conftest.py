import pytest
import requests

mocked_input_payload = {
    "age": 35,
    "dependents": 2,
    "house": {"ownership_status": "owned"},
    "income": 0,
    "marital_status": "married",
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": 2018},
}


class Mock200Response:
    content_type = "application/json"
    status_code = 200

    @staticmethod
    def json():
        return {
            "auto": "ineligible",
            "disability": "ineligible",
            "home": "ineligible",
            "life": "regular",
        }


class Mock422Response:
    content_type = "application/json"
    status_code = 422


@pytest.fixture
def mock_200_response(monkeypatch):
    def mock_post(*args, **kwargs):
        return Mock200Response()

    monkeypatch.setattr(requests, "post", mock_post)


@pytest.fixture
def mock_422_response(monkeypatch):
    def mock_post(*args, **kwargs):
        return Mock422Response()

    monkeypatch.setattr(requests, "post", mock_post)
