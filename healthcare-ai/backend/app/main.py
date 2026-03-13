from fastapi import FastAPI
from backend.app.routers import user_router
app=FastAPI()
app.include_router(user_router.router)    
@app.get("/")
def home():
    return{"message":"Healthcare Agent Running"}   
