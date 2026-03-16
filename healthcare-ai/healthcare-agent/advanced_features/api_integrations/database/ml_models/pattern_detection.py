import numpy as np

def detect_patterns(data):

    avg = np.mean(data)

    if avg > 150:
        return "Abnormal heart rate trend detected"

    return "Normal health pattern"