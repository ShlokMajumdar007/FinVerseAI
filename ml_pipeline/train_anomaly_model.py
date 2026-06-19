import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

def train_anomaly_model():
    dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'transactions.csv')
    
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset not found at {dataset_path}")
        return

    print("Loading data...")
    df = pd.read_csv(dataset_path)

    # For Isolation Forest, we'll train on 'amount' as the primary feature for numerical anomalies
    # In a real scenario, we'd also encode 'merchant' and 'category'
    X = df[['amount']].values

    print("Training Isolation Forest model...")
    # contamination is the expected proportion of outliers (we generated ~2%)
    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(X)

    # Save the model
    models_dir = os.path.join(os.path.dirname(__file__), '..', 'backend', 'models')
    os.makedirs(models_dir, exist_ok=True)
    model_path = os.path.join(models_dir, 'anomaly_model.pkl')
    
    joblib.dump(model, model_path)
    print(f"Model successfully saved to {model_path}")

if __name__ == '__main__':
    train_anomaly_model()
