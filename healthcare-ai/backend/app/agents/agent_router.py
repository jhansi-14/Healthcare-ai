from fastapi import APIRouter
from backend.app.agents.health_agent import health_agent
router=APIRouter()
@router.get("/agent")
def run_agent(query:str):
    result=health_agent(query)
    return {"response":result}