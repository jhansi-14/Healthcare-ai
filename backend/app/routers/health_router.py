from fastapi import APIRouter
from backend.app.database.db import SessionLocal
from backend.app.database.models import HealthMetrics
router=APIRouter()
@router.post("/health")
def save_health(patient_id:int,hearth_rate:int,steps:int,sleep_hours:float):
    db=SessionLocal()
    record=HealthMetrics(
        patient_id=patient_id,
        heart_rate=heart_rate,
        steps=steps,
        sleep_hours=sleep_hours
    )
    db.add(record)
    db.commit()
    return {"message":"Health data saved"}