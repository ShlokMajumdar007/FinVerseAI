import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv('dataset/anomaly.csv')

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(data)

joblib.dump(model, 'models/anomaly.pkl')

print("Anomaly Model Trained")