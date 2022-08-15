import requests

from src.tests.unit.conftest import mocked_input_payload


class TestHttpRiskScore:
    def test_should_return_200_status_code_with_correct_body(self, mock_200_response):
        response = requests.post(
            "http://0.0.0.0:8000/generate-risk-score/", json=mocked_input_payload
        )
        print(response)
        assert response.status_code == 200

    def test_should_return_422_status_code_for_invalid_json(self, mock_422_response):
        response = requests.post(
            "http://0.0.0.0:8000/generate-risk-score/", json=mocked_input_payload
        )
        assert response.status_code == 422

    def test_should_return_json_body(self, mock_200_response):
        response = requests.post(
            "http://0.0.0.0:8000/generate-risk-score/", json=mocked_input_payload
        )
        assert response.content_type == "application/json"
