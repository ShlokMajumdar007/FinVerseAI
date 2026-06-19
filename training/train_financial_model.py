import pandas as pd

import joblib

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.model_selection import (
    train_test_split
)


# LOAD DATASET

data = pd.read_csv(
    "../dataset/budget_training.csv"
)


# FEATURES

X = data[[
    "income",
    "food",
    "shopping",
    "entertainment",
    "rent",
    "travel",
    "gym"
]]


# TARGET

y = data["risk_score"]


# SPLIT

X_train, X_test, y_train, y_test = (

    train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42
    )
)


# MODEL

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42
)


# TRAIN

model.fit(
    X_train,
    y_train
)


# SAVE

joblib.dump(

    model,

    "../models/financial_risk_model.pkl"
)


print(
    "Financial risk model trained."
)