from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from backend.app.database.db import Base

class HealthMetrics(Base):
    __tablename__ = "health_metrics"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    heart_rate = Column(Integer)
    steps = Column(Integer)
    sleep_hours = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)