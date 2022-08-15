from typing import Literal

from pydantic import BaseModel, validator


class RiskModel(BaseModel):
    age: int
    dependents: int
    house: dict
    income: int
    marital_status: Literal["married", "single"]
    risk_questions: list
    vehicle: dict

    @validator("house")
    def house_must_be_owned_or_mortgaged(cls, v):
        if v != {}:
            if v["ownership_status"] not in ["owned", "mortgaged", " "]:
                raise ValueError("must be owned or mortgaged STRING")
            return v

    @validator("risk_questions")
    def risk_questions_must_be_3_integers(cls, v):
        if len(v) != 3:
            raise ValueError("must be a list of 3 integers ranging from zero to 3")
        for i in v:
            if i not in range(4):
                raise ValueError("must be a list of 3 integers ranging from zero to 3")
        return v

    @validator("vehicle")
    def if_vehicle_needs_to_have_year(cls, v):
        if v != {}:
            if "year" in v and isinstance(v["year"], int):
                return v
            raise ValueError("must have year and it needs to be an INTEGER")
