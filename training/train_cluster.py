import pandas as pd
from sklearn.cluster import KMeans
import joblib

data = pd.read_csv('dataset/users.csv')

model = KMeans(
    n_clusters=4,
    random_state=42
)

model.fit(data)

joblib.dump(model, 'models/cluster.pkl')

print("Cluster Model Trained Successfully")