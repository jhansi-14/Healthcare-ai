from fastapi import FastAPI
from backend.app.routers.user_router import router
from backend.app.agents.agent_router import router as agent_router
from backend.app.database.models import Base
from backend.app.database.db import engine
from backend.app.routers.health_router import router as health_router
app=FastAPI()    
Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    return{"message":"Healthcare Agent Running"} 
app.include_router(router) 
app.include_router(agent_router) 
app.include_router(health_router)        
