from sklearn.linear_model import LogisticRegression
import numpy as np

class HealthRiskModel:

    def __init__(self):
        self.model = LogisticRegression()

        X = [
            [60, 150, 4],
            [70, 200, 3],
            [80, 300, 2],
            [65, 120, 6]
        ]

        y = [0,1,1,0]

        self.model.fit(X,y)

    def predict_risk(self, heart_rate, steps, sleep):

        prediction = self.model.predict([[heart_rate,steps,sleep]])

        if prediction[0] == 1:
            return "High Risk"

        return "Low Risk"