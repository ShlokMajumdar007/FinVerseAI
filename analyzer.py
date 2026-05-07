import joblib

from collections import defaultdict

from tree_visualizer import TreeVisualizer


classifier = joblib.load('models/classifier.pkl')

predictor = joblib.load('models/predictor.pkl')

cluster = joblib.load('models/cluster.pkl')

anomaly = joblib.load('models/anomaly.pkl')

optimizer = joblib.load('models/optimizer.pkl')


class OfflineFinanceAI:

    def __init__(self, income, expenses):

        self.income = income
        self.expenses = expenses

    def classify_expenses(self):

        for item in self.expenses:

            prediction = classifier.predict(
                [item['title']]
            )

            item['category'] = prediction[0]

    def calculate_totals(self):

        totals = defaultdict(float)

        for item in self.expenses:

            totals[item['category']] += item['amount']

        return totals

    def predict_future_spending(self):

        prediction = predictor.predict([
            [self.income]
        ])

        return round(prediction[0], 2)

    def detect_personality(self, totals):

        food = totals.get('food', 0)

        shopping = totals.get('shopping', 0)

        entertainment = totals.get(
            'entertainment',
            0
        )

        savings = self.income - sum(
            totals.values()
        )

        cluster_id = cluster.predict([[
            food,
            shopping,
            entertainment,
            savings
        ]])[0]

        mapping = {
            0: "Balanced",
            1: "Saver",
            2: "Luxury",
            3: "Impulsive"
        }

        return mapping.get(
            cluster_id,
            "Unknown"
        )

    def detect_anomalies(self):

        warnings = []

        for item in self.expenses:

            result = anomaly.predict([
                [item['amount']]
            ])[0]

            if result == -1:

                warnings.append(
                    f"Unusual spending detected: "
                    f"{item['title']}"
                )

        return warnings

    def optimize_budget(self, totals):

        shopping = totals.get(
            'shopping',
            0
        )

        food = totals.get(
            'food',
            0
        )

        entertainment = totals.get(
            'entertainment',
            0
        )

        savings = self.income - sum(
            totals.values()
        )

        recommendation = optimizer.predict([[
            shopping,
            food,
            entertainment,
            savings
        ]])[0]

        optimized = {
            "food": food,
            "shopping": shopping,
            "entertainment": entertainment,
            "recommendation": recommendation
        }

        if recommendation == "reduce_shopping":

            optimized['shopping'] *= 0.7

        elif recommendation == "reduce_entertainment":

            optimized['entertainment'] *= 0.75

        return optimized

    def run(self):

        self.classify_expenses()

        totals = self.calculate_totals()

        personality = self.detect_personality(
            totals
        )

        prediction = self.predict_future_spending()

        warnings = self.detect_anomalies()

        optimized = self.optimize_budget(
            totals
        )

        tree = TreeVisualizer(
            self.income,
            optimized
        ).generate()

        return {
            "personality": personality,
            "future_prediction": prediction,
            "warnings": warnings,
            "optimized_budget": optimized,
            "tree": tree
        }