from fastapi import FastAPI
from backend.app.routers.user_router import router
from backend.app.agents.agent_router import router as agent_router
app=FastAPI()    
@app.get("/")
def home():
    return{"message":"Healthcare Agent Running"} 
app.include_router(router) 
app.include_router(agent_router)         
