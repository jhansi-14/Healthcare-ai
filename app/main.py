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