class OfflineFinanceAI:

    def __init__(self):
        pass


    # ===================================
    # CATEGORY DETECTION
    # ===================================

    def categorize_expense(self, title):

        title = title.lower()


        categories = {

            "food": [
                "food",
                "swiggy",
                "zomato",
                "restaurant"
            ],

            "shopping": [
                "amazon",
                "shopping",
                "flipkart"
            ],

            "entertainment": [
                "movie",
                "netflix",
                "game",
                "entertainment"
            ],

            "investment": [
                "investment",
                "stocks",
                "mutual fund"
            ],

            "rent": [
                "rent",
                "house"
            ],

            "travel": [
                "travel",
                "trip",
                "uber"
            ],

            "gym": [
                "gym",
                "fitness"
            ]
        }


        for category, keywords in categories.items():

            for keyword in keywords:

                if keyword in title:

                    return category


        return "other"


    # ===================================
    # BUDGET BREAKDOWN
    # ===================================

    def generate_budget_breakdown(
        self,
        expenses
    ):

        breakdown = {}


        for expense in expenses:

            category = self.categorize_expense(
                expense["title"]
            )

            amount = expense["amount"]


            if category not in breakdown:

                breakdown[category] = 0


            breakdown[category] += amount


        return breakdown


    # ===================================
    # PERSONALITY ANALYSIS
    # ===================================

    def detect_personality(
        self,
        total_spending,
        income
    ):

        ratio = (
            total_spending / income
        )


        if ratio > 0.85:

            return "High Risk Spender"


        elif ratio > 0.65:

            return "Lifestyle Spender"


        elif ratio > 0.45:

            return "Balanced"


        return "Smart Saver"


    # ===================================
    # FINANCIAL SCORE
    # ===================================

    def calculate_financial_score(

        self,

        income,

        spending_ratio,

        savings
    ):

        score = 100


        if spending_ratio > 0.8:

            score -= 35


        elif spending_ratio > 0.6:

            score -= 20


        elif spending_ratio > 0.4:

            score -= 10


        if savings < income * 0.2:

            score -= 20


        return max(score, 10)


    # ===================================
    # FUTURE SPENDING
    # ===================================

    def predict_future_spending(
        self,
        total_spending
    ):

        return int(
            total_spending * 1.12
        )


    # ===================================
    # BUDGET OPTIMIZATION
    # ===================================

    def optimize_budget(
        self,
        breakdown
    ):

        optimized = {}


        for category, amount in breakdown.items():

            if category == "shopping":

                optimized[category] = int(
                    amount * 0.70
                )


            elif category == "entertainment":

                optimized[category] = int(
                    amount * 0.75
                )


            elif category == "food":

                optimized[category] = int(
                    amount * 0.90
                )


            else:

                optimized[category] = amount


        return optimized


    # ===================================
    # WARNING ENGINE
    # ===================================

    def detect_warnings(

        self,

        income,

        breakdown
    ):

        warnings = []


        LIMITS = {

            "shopping": 0.20,

            "entertainment": 0.15,

            "food": 0.18,

            "travel": 0.20
        }


        for category, amount in breakdown.items():

            if category in LIMITS:

                limit = (
                    income *
                    LIMITS[category]
                )


                if amount > limit:

                    warnings.append(

                        f"High spending on "
                        f"{category}"
                    )


        return warnings


    # ===================================
    # AI INSIGHTS
    # ===================================

    def generate_insights(

        self,

        income,

        savings,

        breakdown
    ):

        insights = []


        if savings > income * 0.4:

            insights.append(

                "Excellent savings rate detected."
            )


        if (
            "entertainment" in breakdown
            and breakdown[
                "entertainment"
            ] > income * 0.15
        ):

            insights.append(

                "Entertainment spending is above recommended levels."
            )


        if (
            "shopping" in breakdown
            and breakdown[
                "shopping"
            ] > income * 0.20
        ):

            insights.append(

                "Shopping expenses can be optimized further."
            )


        if len(insights) == 0:

            insights.append(

                "Your financial habits look stable."
            )


        return insights


    # ===================================
    # MONTHLY HISTORY
    # ===================================

    def generate_monthly_history(

        self,

        income,

        total_spending
    ):

        history = []


        monthly_spending = total_spending


        for month in [

            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ]:

            history.append({

                "month": month,

                "income": income,

                "spending":
                monthly_spending,

                "savings":
                income -
                monthly_spending
            })


            monthly_spending = int(
                monthly_spending * 1.03
            )


        return history


    # ===================================
    # TREE VISUALIZATION
    # ===================================

    def generate_tree(

        self,

        income,

        breakdown
    ):

        nodes = []

        edges = []


        nodes.append({

            "id": "income",

            "data": {

                "label":
                f"Income\n₹{income}"
            },

            "position": {

                "x": 450,

                "y": 0
            },

            "style": {

                "background": "#2563eb",

                "color": "white",

                "padding": 15,

                "borderRadius": 15
            }
        })


        CATEGORY_COLORS = {

            "food": "#16a34a",

            "shopping": "#9333ea",

            "entertainment": "#f59e0b",

            "investment": "#0891b2",

            "rent": "#dc2626",

            "travel": "#ea580c",

            "gym": "#0f766e",

            "other": "#334155"
        }


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
                },

                "style": {

                    "background":
                    CATEGORY_COLORS.get(
                        category,
                        "#334155"
                    ),

                    "color": "white",

                    "padding": 12,

                    "borderRadius": 14
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


    # ===================================
    # MAIN ANALYSIS
    # ===================================

    def analyze(

        self,

        income,

        expenses
    ):

        breakdown = (
            self.generate_budget_breakdown(
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


        personality = (
            self.detect_personality(

                total_spending,

                income
            )
        )


        financial_score = (
            self.calculate_financial_score(

                income,

                spending_ratio,

                savings
            )
        )


        future_prediction = (
            self.predict_future_spending(

                total_spending
            )
        )


        optimized_budget = (
            self.optimize_budget(
                breakdown
            )
        )


        warnings = (
            self.detect_warnings(

                income,

                breakdown
            )
        )


        insights = (
            self.generate_insights(

                income,

                savings,

                breakdown
            )
        )


        monthly_history = (
            self.generate_monthly_history(

                income,

                total_spending
            )
        )


        tree = self.generate_tree(

            income,

            breakdown
        )


        return {

            "financial_score":
            financial_score,

            "personality":
            personality,

            "future_prediction":
            future_prediction,

            "savings":
            savings,

            "expense_ratio":
            round(
                spending_ratio,
                2
            ),

            "budget_breakdown":
            breakdown,

            "optimized_budget":
            optimized_budget,

            "warnings":
            warnings,

            "insights":
            insights,

            "monthly_history":
            monthly_history,

            "tree":
            tree
        }