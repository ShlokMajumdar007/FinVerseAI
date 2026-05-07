class TreeVisualizer:

    def __init__(self, income, budget):

        self.income = income
        self.budget = budget

    def generate(self):

        nodes = []

        edges = []

        nodes.append({
            "id": "income",

            "data": {
                "label":
                f"Income ₹{self.income}"
            },

            "position": {
                "x": 400,
                "y": 0
            }
        })

        x = 100

        for category, amount in self.budget.items():

            if category == "recommendation":
                continue

            nodes.append({

                "id": category,

                "data": {
                    "label":
                    f"{category} ₹{round(amount,2)}"
                },

                "position": {
                    "x": x,
                    "y": 200
                }
            })

            edges.append({

                "id":
                f"e-income-{category}",

                "source":
                "income",

                "target":
                category
            })

            if (
                category == "shopping"
                and amount > 5000
            ):

                nodes.append({

                    "id":
                    "shopping-warning",

                    "data": {
                        "label":
                        "Overspending Detected"
                    },

                    "position": {
                        "x": x,
                        "y": 400
                    }
                })

                edges.append({

                    "id":
                    "shopping-edge",

                    "source":
                    category,

                    "target":
                    "shopping-warning"
                })

            x += 250

        return {
            "nodes": nodes,
            "edges": edges
        }