from fastapi import APIRouter, Depends
from services.cache import get_cached_health_data
from middleware.auth import verify_token

router = APIRouter(prefix="/performance", tags=["Performance"])

@router.get("/cached-health/{user_id}")
def cached_health(user_id: str):
    return get_cached_health_data(user_id)

@router.get("/secure-data", dependencies=[Depends(verify_token)])
def secure_data():
    return {"message": "Secure health data"}