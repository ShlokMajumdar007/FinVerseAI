import joblib
import os

class BudgetEngine:
    def __init__(self):
        # We'll load a mocked ML model, fallback to rule-based if not found
        model_path = os.path.join(os.path.dirname(__file__), "models", "budget_model.pkl")
        try:
            self.model = joblib.load(model_path)
        except Exception:
            self.model = None

    def generate_budget(self, income: float, expenses: list):
        """
        Generate a personalized budget based on income and past expenses.
        Uses a 50/30/20 rule fallback if ML prediction isn't available.
        """
        needs_ratio = 0.50
        wants_ratio = 0.30
        savings_ratio = 0.20

        # Extract breakdown
        breakdown = self._generate_breakdown(expenses)

        # ML Prediction if model exists
        if self.model:
            # Example feature extraction
            features = [[income, breakdown.get('food', 0), breakdown.get('shopping', 0)]]
            prediction = self.model.predict(features)[0]
            # Map prediction array to budget dict
            return {
                "needs": float(prediction[0]),
                "wants": float(prediction[1]),
                "savings": float(prediction[2]),
                "explanations": ["AI-driven budget generation based on your past spending patterns."]
            }

        # Rule-based fallback
        budget = {
            "needs": income * needs_ratio,
            "wants": income * wants_ratio,
            "savings": income * savings_ratio,
            "explanations": [
                "Using the 50/30/20 rule to structure your budget.",
                f"Allocate ₹{int(income * needs_ratio)} for essential needs like rent and groceries.",
                f"Allocate ₹{int(income * wants_ratio)} for flexible spending like dining and entertainment.",
                f"Save/Invest ₹{int(income * savings_ratio)} for future security."
            ]
        }
        
        # Adjust for emergency fund / specific limits
        return budget

    def _generate_breakdown(self, expenses):
        breakdown = {}
        for exp in expenses:
            cat = exp.get("category", "other")
            breakdown[cat] = breakdown.get(cat, 0.0) + exp.get("amount", 0.0)
        return breakdown

budget_engine = BudgetEngine()
