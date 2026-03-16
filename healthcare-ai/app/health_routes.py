from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter()
class HealthData(BaseModel):
    steps:int
    sleep_hours:float
    calories:int
@router.post("/post-health")
def post_health(data:HealthData):
    return {"message":"health data recieved","data":data}    