from fastapi import fastapi
app=FastAPI()
@app.get("/")
def home():
    return {"message":"Healthcare Agent Running"}