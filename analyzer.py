class OfflineFinanceAI:

    def __init__(self):
        pass


    # =========================
    # PERSONALITY ANALYSIS
    # =========================

    def detect_personality(
        self,
        expenses,
        income
    ):

        total_spending = sum(
            e["amount"] for e in expenses
        )

        spending_ratio = (
            total_spending / income
        )


        entertainment = 0
        shopping = 0
        essentials = 0


        for expense in expenses:

            title = expense["title"].lower()

            amount = expense["amount"]


            if (
                "shopping" in title or
                "amazon" in title
            ):

                shopping += amount


            elif (
                "movie" in title or
                "netflix" in title or
                "game" in title or
                "entertainment" in title
            ):

                entertainment += amount


            else:
                essentials += amount


        if shopping > income * 0.25:
            return "Impulsive Shopper"

        elif entertainment > income * 0.20:
            return "Lifestyle Spender"

        elif spending_ratio < 0.45:
            return "Smart Saver"

        elif spending_ratio > 0.85:
            return "High Risk Spender"

        return "Balanced"


    # =========================
    # FUTURE PREDICTION
    # =========================

    def predict_future_spending(
        self,
        expenses
    ):

        total = sum(
            e["amount"] for e in expenses
        )

        future_prediction = int(
            total * 1.12
        )

        return future_prediction


    # =========================
    # BUDGET OPTIMIZATION
    # =========================

    def optimize_budget(
        self,
        expenses,
        income
    ):

        optimized = {}

        total_after_optimization = 0


        for expense in expenses:

            title = expense["title"].lower()

            amount = expense["amount"]


            # SMART REDUCTIONS

            if (
                "shopping" in title or
                "amazon" in title
            ):

                optimized_amount = int(
                    amount * 0.70
                )


            elif (
                "food" in title or
                "swiggy" in title or
                "zomato" in title
            ):

                optimized_amount = int(
                    amount * 0.85
                )


            elif (
                "movie" in title or
                "entertainment" in title
            ):

                optimized_amount = int(
                    amount * 0.75
                )


            else:

                optimized_amount = amount


            optimized[title] = optimized_amount

            total_after_optimization += (
                optimized_amount
            )


        savings = (
            income - total_after_optimization
        )


        optimized["expected_savings"] = (
            savings
        )

        return optimized


    # =========================
    # SMART WARNING ENGINE
    # =========================

    def detect_warnings(
        self,
        expenses,
        income
    ):

        warnings = []


        CATEGORY_LIMITS = {

            "rent": 0.45,

            "food": 0.18,

            "groceries": 0.18,

            "gym": 0.08,

            "shopping": 0.20,

            "entertainment": 0.12,

            "travel": 0.20,

            "medicine": 0.12,

            "electricity": 0.08,

            "wifi": 0.05,

            "swiggy": 0.15,

            "zomato": 0.15
        }


        for expense in expenses:

            title = expense["title"].lower()

            amount = expense["amount"]

            category_found = False


            for category, limit in CATEGORY_LIMITS.items():

                if category in title:

                    category_found = True

                    threshold = (
                        income * limit
                    )


                    if amount > threshold:

                        warnings.append(

                            f"High spending on "
                            f"{category} "
                            f"(₹{amount})"
                        )

                    break


            # UNKNOWN CATEGORY

            if not category_found:

                if amount > income * 0.15:

                    warnings.append(

                        f"Unusual spending detected: "
                        f"{title} "
                        f"(₹{amount})"
                    )

        return warnings


    # =========================
    # TREE VISUALIZATION
    # =========================

    def generate_tree(
        self,
        income,
        expenses
    ):

        nodes = [

            {
                "id": "income",

                "data": {
                    "label":
                    f"Income ₹{income}"
                },

                "position": {
                    "x": 450,
                    "y": 0
                }
            }
        ]


        edges = []


        x_position = 100


        for index, expense in enumerate(expenses):

            expense_id = (
                f"expense-{index}"
            )


            nodes.append(

                {
                    "id": expense_id,

                    "data": {

                        "label":
                        f'{expense["title"]}'
                        f'\n₹{expense["amount"]}'
                    },

                    "position": {
                        "x": x_position,
                        "y": 220
                    }
                }
            )


            edges.append(

                {
                    "id":
                    f"edge-{index}",

                    "source":
                    "income",

                    "target":
                    expense_id
                }
            )


            x_position += 220


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

        personality = (
            self.detect_personality(
                expenses,
                income
            )
        )


        future_prediction = (

            self.predict_future_spending(
                expenses
            )
        )


        optimized_budget = (

            self.optimize_budget(
                expenses,
                income
            )
        )


        warnings = (

            self.detect_warnings(
                expenses,
                income
            )
        )


        tree = self.generate_tree(
            income,
            expenses
        )


        return {

            "personality":
            personality,

            "future_prediction":
            future_prediction,

            "optimized_budget":
            optimized_budget,

            "warnings":
            warnings,

            "tree":
            tree
        }