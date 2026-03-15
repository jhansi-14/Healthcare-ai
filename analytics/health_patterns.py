import pandas as pd
from sklearn.cluster import KMeans

def detect_patterns(data):

    df = pd.DataFrame(data)

    model = KMeans(n_clusters=2)

    df["cluster"] = model.fit_predict(df)

    return df.to_dict()