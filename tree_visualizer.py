class TreeVisualizer:

    def __init__(
        self,
        income,
        budget
    ):

        self.income = income

        self.budget = budget


    def generate(self):

        nodes = []

        edges = []


        # =========================
        # ROOT NODE
        # =========================

        nodes.append({

            "id": "income",

            "data": {

                "label":
                f"Monthly Income\n₹{self.income}"
            },

            "position": {

                "x": 500,

                "y": 0
            },

            "style": {

                "background": "#2563eb",

                "color": "white",

                "padding": 15,

                "borderRadius": 15,

                "fontWeight": "bold",

                "fontSize": 16,

                "border":
                "2px solid #1d4ed8"
            }
        })


        CATEGORY_COLORS = {

            "food": "#16a34a",

            "shopping": "#9333ea",

            "entertainment": "#f59e0b",

            "gym": "#0891b2",

            "rent": "#dc2626",

            "travel": "#ea580c",

            "default": "#334155"
        }


        x = 100


        # =========================
        # CATEGORY NODES
        # =========================

        for category, amount in self.budget.items():

            if category == "recommendation":
                continue

            if category == "expected_savings":
                continue


            node_color = (
                CATEGORY_COLORS.get(
                    category,
                    CATEGORY_COLORS["default"]
                )
            )


            nodes.append({

                "id": category,

                "data": {

                    "label":
                    f"{category.upper()}\n₹{round(amount,2)}"
                },

                "position": {

                    "x": x,

                    "y": 220
                },

                "style": {

                    "background":
                    node_color,

                    "color": "white",

                    "padding": 12,

                    "borderRadius": 14,

                    "fontWeight": "bold",

                    "fontSize": 14,

                    "border":
                    "2px solid rgba(255,255,255,0.15)"
                }
            })


            edges.append({

                "id":
                f"e-income-{category}",

                "source":
                "income",

                "target":
                category,

                "animated":
                True,

                "style": {

                    "stroke":
                    "#94a3b8",

                    "strokeWidth":
                    2
                }
            })


            # =========================
            # WARNING NODE
            # =========================

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

                        "y": 430
                    },

                    "style": {

                        "background":
                        "#dc2626",

                        "color":
                        "white",

                        "padding":
                        12,

                        "borderRadius":
                        14,

                        "fontWeight":
                        "bold"
                    }
                })


                edges.append({

                    "id":
                    "shopping-edge",

                    "source":
                    category,

                    "target":
                    "shopping-warning",

                    "animated":
                    True,

                    "style": {

                        "stroke":
                        "#dc2626",

                        "strokeWidth":
                        2
                    }
                })


            x += 230


        # =========================
        # SAVINGS NODE
        # =========================

        if "expected_savings" in self.budget:

            savings = (
                self.budget[
                    "expected_savings"
                ]
            )


            nodes.append({

                "id": "savings",

                "data": {

                    "label":
                    f"SAVINGS\n₹{savings}"
                },

                "position": {

                    "x": 500,

                    "y": 500
                },

                "style": {

                    "background":
                    "#16a34a",

                    "color":
                    "white",

                    "padding":
                    15,

                    "borderRadius":
                    16,

                    "fontWeight":
                    "bold",

                    "fontSize":
                    15
                }
            })


            edges.append({

                "id":
                "income-savings",

                "source":
                "income",

                "target":
                "savings",

                "animated":
                True,

                "style": {

                    "stroke":
                    "#16a34a",

                    "strokeWidth":
                    3
                }
            })


        return {

            "nodes": nodes,

            "edges": edges
        }