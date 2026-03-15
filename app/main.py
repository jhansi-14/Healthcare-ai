from fastapi import FastAPI
from app.graph import build_graph
from app.models import HealthInput
from reports.report_generator import generate_report

app = FastAPI()

graph = build_graph()


@app.post("/health-analysis")

def analyze_health(data: HealthInput):

    result = graph.invoke(data.dict())

    report = generate_report(result)

    return {
        "analysis": result,
        "report": report
    }