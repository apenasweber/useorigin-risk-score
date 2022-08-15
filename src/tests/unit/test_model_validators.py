import pytest

from src.controllers.risk_managment import RiskService
from src.models.risk_user_model import RiskModel


class TestModelValidations:
    def test_should_raises_exception_with_wrong_risk_questions(self):
        with pytest.raises(ValueError):
            RiskModel.parse_obj(
                {
                    "age": 35,
                    "dependents": 2,
                    "house": {"ownership_status": "owned"},
                    "income": 0,
                    "marital_status": "married",
                    "risk_questions": [1000000000],
                    "vehicle": {"year": 2018},
                }
            )

    def test_should_raises_exception_with_wrong_marital_status(self):
        with pytest.raises(ValueError):
            RiskModel.parse_obj(
                {
                    "age": 35,
                    "dependents": 2,
                    "house": {"ownership_status": "owned"},
                    "income": 0,
                    "marital_status": "tinder",
                    "risk_questions": [0, 1, 0],
                    "vehicle": {"year": 2018},
                }
            )

    def test_should_raises_exception_with_wrong_house_ownership_status(self):
        with pytest.raises(ValueError):
            RiskModel.parse_obj(
                {
                    "age": 35,
                    "dependents": 2,
                    "house": {"ownership_status": "python"},
                    "income": 0,
                    "marital_status": "single",
                    "risk_questions": [0, 1, 0],
                    "vehicle": {"year": 2018},
                }
            )
