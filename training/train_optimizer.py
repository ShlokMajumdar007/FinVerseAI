import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv('dataset/optimizer.csv')

X = data[
    ['shopping', 'food', 'entertainment', 'savings']
]

y = data['recommendation']

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(model, 'models/optimizer.pkl')

print("Optimizer Model Trained Successfully")