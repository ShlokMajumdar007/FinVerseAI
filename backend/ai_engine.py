from collections import defaultdict


def generate_financial_advice(expenses):
    total = sum([e.amount for e in expenses])

    category_totals = defaultdict(float)

    for e in expenses:
        category_totals[e.category] += e.amount

    highest_category = max(
        category_totals,
        key=category_totals.get,
        default="None"
    )

    savings_tip = "Good financial balance."

    if total > 10000:
        savings_tip = (
            "Your spending is high. Try reducing unnecessary purchases."
        )

    score = max(0, 100 - int(total / 100))

    report = f"""
    Total Spending: ₹{total}

    Highest Spending Category:
    {highest_category}

    Savings Advice:
    {savings_tip}

    Financial Health Score:
    {score}/100
    """

    return report