import time

def monitor_health(stream):

    for data in stream:

        heart_rate = data["heart_rate"]

        if heart_rate > 120:
            print("Warning: High heart rate")

        time.sleep(1)