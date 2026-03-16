from advanced_features.ml_models.health_risk_model import HealthRiskModel
from advanced_features.monitoring.alert_system import generate_alert

model = HealthRiskModel()

def advanced_health_analysis(hr, steps, sleep):

    risk = model.predict_risk(hr,steps,sleep)

    alert = generate_alert(hr)

    return {
        "risk": risk,
        "alert": alert
    }