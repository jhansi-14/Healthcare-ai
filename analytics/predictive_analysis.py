from sklearn.linear_model import LogisticRegression
import numpy as np

def predict_risk(data):

    X = np.array(data["features"])
    y = np.array(data["labels"])

    model = LogisticRegression()
    model.fit(X,y)

    prediction = model.predict([data["new_data"]])

    return prediction.tolist()