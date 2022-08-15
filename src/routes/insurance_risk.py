from fastapi import FastAPI

from src.controllers.risk_managment import RiskService
from src.models.risk_user_model import RiskModel

app = FastAPI()


@app.post("/generate-risk-score/")
def read_item(item: RiskModel):
    risk_service = RiskService()
    return risk_service.generate_risk_score(item)
