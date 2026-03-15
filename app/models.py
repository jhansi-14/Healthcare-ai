from pydantic import BaseModel

class HealthInput(BaseModel):

    steps: int
    calories: int
    sleep_hours: float
    protein: int
    carbs: int
    fats: int
    symptom: str