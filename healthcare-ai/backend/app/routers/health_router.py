from fastapi import APIRouter
from backend.app.database.db import SessionLocal
from backend.app.database.models import HealthMetrics
import logging

router = APIRouter()
logger = logging.getLogger(_name_)

@router.post("/health")
def save_health(patient_id: int, heart_rate: int, steps: int, sleep_hours: float):
    logger.info(f"Recieved health data for patient {patient_id}")

    db = SessionLocal()

    record = HealthMetrics(
        patient_id=patient_id,
        heart_rate=heart_rate,
        steps=steps,
        sleep_hours=sleep_hours
    )

    db.add(record)
    db.commit()
    db.close()

    logger.info("Health data saved successfully")