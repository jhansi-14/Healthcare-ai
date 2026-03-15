from fastapi import FastAPI
from app.auth import router as auth_router
from app.health_routes import router as health_router
from app.graph import build_graph
from app.models import HealthInput
from reports.report_generator import generate_report

app = FastAPI(
    title="healthcare ai agent",
    description="track b healthcare monitoring system",version="1.0"
)

graph = build_graph()
@app.get("/")
def home():
    return {"message":"healthcare ai agent is running"}
@app.post("/health-data")
def submit_health(data:healthInput):
    health_score=(data.steps/10000)*50+(data.sleep_hours/8)*50
    if health_score>80:
        status="excellent"
    elif health_score>60:
        status="good"
    else:
        status="needs improvement"    
        return{"patient_name":data.patient_name,"health_score":round(health_score,2),"status":status,"symptom":data.symptom}    

@app.post("/health-analysis")

def analyze_health(data: HealthInput):

    result = graph.invoke(data.dict())

    report = generate_report(result)

    return {
        "analysis": result,
        "report": report
    }
app.include_router(auth_router)
app.include_router(health_router)