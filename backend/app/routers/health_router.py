
import logging

from fastapi import APIRouter
from backend.app.database.db import SessionLocal
from backend.app.database.models import HealthMetrics
router=APIRouter()
@router.post("/health")
def save_health(patient_id:int,hearth_rate:int,steps:int,sleep_hours:float):
    logger=logging.getLogger(__name__)
@router.post("/health")
def save_health(patient_id:int,heart_rate:int,steps:int,sleep_hours:float):
    logger.info("Recieved health data for patient {patient_id}")

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
=======
    logger.info("Health data saved succesfully")
    return {"message":"Health data saved"}
    db.close()
