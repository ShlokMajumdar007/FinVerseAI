import numpy as np
import joblib
import os

class AnomalyDetector:
    def __init__(self):
        self.model = None
        model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'anomaly_model.pkl')
        try:
            if os.path.exists(model_path):
                self.model = joblib.load(model_path)
                print("Loaded ML Anomaly Model successfully.")
        except Exception as e:
            print(f"Failed to load ML anomaly model: {e}")

    def detect_anomalies(self, transactions: list):
        """
        Takes a list of transactions and flags potential anomalies based on historical amounts.
        Simple statistical Z-score approach as a fallback if no ML model is present.
        """
        if not transactions:
            return []
            
        anomalies = []
        
        if self.model:
            # Prepare data for model
            amounts = [[t.get("amount", 0.0)] for t in transactions]
            try:
                predictions = self.model.predict(amounts)
                # Isolation Forest returns -1 for outliers and 1 for inliers
                for idx, pred in enumerate(predictions):
                    if pred == -1:
                        anomalies.append({
                            "transaction_id": transactions[idx].get("id"),
                            "reason": f"Machine Learning model flagged amount (₹{transactions[idx].get('amount')}) as highly anomalous."
                        })
                return anomalies
            except Exception as e:
                print(f"Error predicting with ML model: {e}")
                # Fallback to statistical if error
                pass

        # Fallback Statistical Method
        amounts = [t.get("amount", 0.0) for t in transactions]
        if not amounts:
            return []
            
        mean = np.mean(amounts)
        std = np.std(amounts)
        
        for t in transactions:
            amount = t.get("amount", 0.0)
            if std > 0 and (amount - mean) / std > 2.5: # Z-score > 2.5
                anomalies.append({
                    "transaction_id": t.get("id"),
                    "reason": f"Unusually high spending detected (₹{amount}) compared to average (₹{int(mean)})."
                })
        return anomalies

anomaly_detector = AnomalyDetector()
