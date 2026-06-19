import joblib


class OfflineFinanceAI:

    def __init__(self):

        try:

            self.model = joblib.load(
                "models/budget_model.pkl"
            )

        except:

            self.model = None


    # =========================
    # CATEGORY DETECTION
    # =========================

    def categorize(self, title):

        title = title.lower()

        categories = {

            "food": [
                "food",
                "swiggy",
                "zomato"
            ],

            "shopping": [
                "amazon",
                "shopping",
                "flipkart"
            ],

            "entertainment": [
                "movie",
                "netflix",
                "game"
            ],

            "rent": [
                "rent"
            ],

            "travel": [
                "uber",
                "ola",
                "travel"
            ],

            "gym": [
                "gym"
            ],

            "investment": [
                "stocks",
                "sip",
                "mutual"
            ]
        }

        for category, keywords in categories.items():

            if any(
                word in title
                for word in keywords
            ):

                return category

        return "other"


    # =========================
    # BREAKDOWN
    # =========================

    def generate_breakdown(
        self,
        expenses
    ):

        breakdown = {}

        for expense in expenses:

            category = self.categorize(
                expense["title"]
            )

            breakdown[category] = (

                breakdown.get(
                    category,
                    0
                )

                + expense["amount"]
            )

        return breakdown


    # =========================
    # ML BUDGET PREDICTION
    # =========================

    def predict_budget(
        self,
        income,
        breakdown
    ):

        if self.model is None:

            return {

                "food":
                int(income * 0.15),

                "shopping":
                int(income * 0.10),

                "entertainment":
                int(income * 0.08),

                "savings":
                int(income * 0.30)
            }

        features = [[

            income,

            breakdown.get("food", 0),

            breakdown.get(
                "shopping",
                0
            ),

            breakdown.get(
                "entertainment",
                0
            ),

            breakdown.get("rent", 0),

            breakdown.get("travel", 0),

            breakdown.get("gym", 0)
        ]]

        prediction = (
            self.model.predict(
                features
            )[0]
        )

        return {

            "food":
            int(prediction[0]),

            "shopping":
            int(prediction[1]),

            "entertainment":
            int(prediction[2]),

            "savings":
            int(prediction[3])
        }


    # =========================
    # AI INSIGHTS
    # =========================

    def generate_insights(
        self,
        income,
        spending,
        breakdown
    ):

        insights = []

        if spending > income * 0.8:

            insights.append(
                "High spending ratio detected."
            )

        if breakdown.get(
            "shopping",
            0
        ) > income * 0.2:

            insights.append(
                "Shopping expenses are excessive."
            )

        if breakdown.get(
            "investment",
            0
        ) == 0:

            insights.append(
                "No investments detected."
            )

        if len(insights) == 0:

            insights.append(
                "Financial habits look stable."
            )

        return insights


    # =========================
    # TREE VISUALIZATION
    # =========================

    def generate_tree(
        self,
        income,
        breakdown
    ):

        nodes = [{
            "id": "income",

            "data": {
                "label":
                f"Income\n₹{income}"
            },

            "position": {
                "x": 450,
                "y": 0
            }
        }]

        edges = []

        x = 100

        for category, amount in breakdown.items():

            nodes.append({

                "id": category,

                "data": {
                    "label":
                    f"{category}\n₹{amount}"
                },

                "position": {
                    "x": x,
                    "y": 220
                }
            })

            edges.append({

                "id":
                f"edge-{category}",

                "source":
                "income",

                "target":
                category,

                "animated":
                True
            })

            x += 220

        return {
            "nodes": nodes,
            "edges": edges
        }


    # =========================
    # MAIN ANALYSIS
    # =========================

    def analyze(
        self,
        income,
        expenses
    ):

        breakdown = (
            self.generate_breakdown(
                expenses
            )
        )

        total_spending = sum(
            breakdown.values()
        )

        savings = (
            income - total_spending
        )

        spending_ratio = (
            total_spending / income
        )


        ai_budget = (
            self.predict_budget(
                income,
                breakdown
            )
        )


        warnings = [

            f"Overspending in {k}"

            for k, v in breakdown.items()

            if v > income * 0.2
        ]


        score = max(

            100 -

            int(
                spending_ratio * 100
            ),

            10
        )


        if score > 80:

            personality = "Smart Saver"

        elif score > 60:

            personality = "Balanced"

        elif score > 40:

            personality = "Lifestyle Spender"

        else:

            personality = "High Risk Spender"


        return {

            "financial_score":
            score,

            "personality":
            personality,

            "total_spending":
            total_spending,

            "savings":
            savings,

            "expense_ratio":
            round(
                spending_ratio,
                2
            ),

            "budget_breakdown":
            breakdown,

            "ai_budget":
            ai_budget,

            "warnings":
            warnings,

            "insights":
            self.generate_insights(
                income,
                total_spending,
                breakdown
            ),

            "future_prediction":
            int(
                total_spending *
                1.10
            ),

            "tree":
            self.generate_tree(
                income,
                breakdown
            )
        }