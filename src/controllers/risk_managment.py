from datetime import datetime

from src.utils.calculate_risk_variables import RiskVariables


class RiskService:
    def generate_risk_score(self, payload):
        payload = payload.dict()
        base_score = sum(payload["risk_questions"])
        insurance_scores = {
            "auto": base_score,
            "disability": base_score,
            "home": base_score,
            "life": base_score,
        }

        if payload["income"] == 0 or payload["vehicle"] == {} or payload["house"] == {}:
            RiskVariables.turns_args_ineligible(
                self, insurance_scores, "auto", "disability", "home"
            )

        if payload["age"] > 60:
            RiskVariables.turns_args_ineligible(
                self, insurance_scores, "disability", "life"
            )

        if payload["age"] < 30:
            RiskVariables.decrease_points(
                self, insurance_scores, 2, "auto", "disability", "home", "life"
            )

        elif payload["age"] <= 40:
            RiskVariables.decrease_points(
                self, insurance_scores, 1, "auto", "disability", "home", "life"
            )

        if payload["income"] > 200000:
            RiskVariables.decrease_points(
                self, insurance_scores, 1, "auto", "disability", "home", "life"
            )

        if payload["house"] and payload["house"]["ownership_status"] == "mortgaged":
            RiskVariables.increase_points(
                self, insurance_scores, 1, "home", "disability"
            )

        if payload["dependents"] > 0:
            RiskVariables.increase_points(
                self, insurance_scores, 1, "disability", "life"
            )

        if payload["marital_status"] == "married":
            RiskVariables.increase_points(self, insurance_scores, 1, "life")
            RiskVariables.decrease_points(self, insurance_scores, 1, "disability")

        if payload["vehicle"]["year"] and payload["vehicle"]["year"] > (
            datetime.now().year - 5
        ):
            RiskVariables.increase_points(self, insurance_scores, 1, "auto")

        for key, value in insurance_scores.items():
            if value != "ineligible":
                if value < 1:
                    insurance_scores[key] = "economic"
                elif value < 3:
                    insurance_scores[key] = "regular"
                else:
                    insurance_scores[key] = "responsible"
        return insurance_scores
