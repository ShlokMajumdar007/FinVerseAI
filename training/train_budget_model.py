import pandas as pd

from sklearn.ensemble import (
    RandomForestRegressor
)

from sklearn.multioutput import (
    MultiOutputRegressor
)

import joblib


# LOAD DATASET

data = pd.read_csv(
    "../dataset/budget_training.csv"
)


# INPUT FEATURES

X = data[[
    "income",
    "food",
    "shopping",
    "entertainment",
    "rent",
    "travel",
    "gym"
]]


# TARGETS

y = data[[
    "recommended_food",
    "recommended_shopping",
    "recommended_entertainment",
    "recommended_savings"
]]


# MODEL

model = MultiOutputRegressor(

    RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
)


# TRAIN

model.fit(X, y)


# SAVE MODEL

joblib.dump(

    model,

    "../models/budget_model.pkl"
)

print(
    "Budget recommendation model trained."
)