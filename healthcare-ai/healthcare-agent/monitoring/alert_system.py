def generate_alert(heart_rate):

    if heart_rate > 120:
        return "Emergency Alert: Heart rate too high"

    if heart_rate < 40:
        return "Emergency Alert: Heart rate too low"

    return "Vitals Normal"