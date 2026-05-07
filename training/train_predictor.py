import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.DataFrame({
    'income': [20000, 30000, 40000, 50000],
    'spending': [15000, 22000, 28000, 35000]
})

X = data[['income']]
y = data['spending']

model = RandomForestRegressor()

model.fit(X, y)

joblib.dump(model, 'models/predictor.pkl')

print("Predictor Trained Successfully")