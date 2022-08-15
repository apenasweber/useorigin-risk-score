from src.controllers.risk_managment import RiskService
from src.models.risk_user_model import RiskModel


class TestBusinessRules:
    def test_should_return_ineligible_for_no_income_vehicles_or_house(self):
        response = RiskService().generate_risk_score(
            RiskModel.parse_obj(
                {
                    "age": 35,
                    "dependents": 2,
                    "house": {"ownership_status": "owned"},
                    "income": 0,
                    "marital_status": "married",
                    "risk_questions": [0, 1, 0],
                    "vehicle": {"year": 2018},
                }
            )
        )
        assert response == {
            "auto": "ineligible",
            "disability": "ineligible",
            "home": "ineligible",
            "life": "regular",
        }

    def test_should_return_correct_risk_score_for_age_over_60(self):
        response = RiskService().generate_risk_score(
            RiskModel.parse_obj(
                {
                    "age": 62,
                    "dependents": 2,
                    "house": {"ownership_status": "owned"},
                    "income": 0,
                    "marital_status": "married",
                    "risk_questions": [0, 1, 0],
                    "vehicle": {"year": 2018},
                }
            )
        )
        assert response == {
            "auto": "ineligible",
            "disability": "ineligible",
            "home": "ineligible",
            "life": "ineligible",
        }

    def test_should_return_correct_risk_score_for_age_under_30(self):
        response = RiskService().generate_risk_score(
            RiskModel.parse_obj(
                {
                    "age": 25,
                    "dependents": 2,
                    "house": {"ownership_status": "owned"},
                    "income": 0,
                    "marital_status": "married",
                    "risk_questions": [0, 1, 0],
                    "vehicle": {"year": 2018},
                }
            )
        )
        assert response == {
            "auto": "ineligible",
            "disability": "ineligible",
            "home": "ineligible",
            "life": "regular",
        }

    def test_should_return_correct_risk_score_for_age_between_30_and_40(self):
        response = RiskService().generate_risk_score(
            RiskModel.parse_obj(
                {
                    "age": 37,
                    "dependents": 2,
                    "house": {"ownership_status": "owned"},
                    "income": 0,
                    "marital_status": "married",
                    "risk_questions": [0, 1, 0],
                    "vehicle": {"year": 2018},
                }
            )
        )
        assert response == {
            "auto": "ineligible",
            "disability": "ineligible",
            "home": "ineligible",
            "life": "regular",
        }

    def test_should_return_correct_risk_score_for_income_above_200000(self):
        response = RiskService().generate_risk_score(
            RiskModel.parse_obj(
                {
                    "age": 37,
                    "dependents": 2,
                    "house": {"ownership_status": "owned"},
                    "income": 199000,
                    "marital_status": "married",
                    "risk_questions": [0, 1, 0],
                    "vehicle": {"year": 2018},
                }
            )
        )
        assert response == {
            "auto": "regular",
            "disability": "economic",
            "home": "economic",
            "life": "regular",
        }
