import pandas as pd
import numpy as np

class ForecastingEngine:
    def __init__(self):
        pass

    def forecast(self, current_spending: float, current_savings: float, months: int = 6):
        """
        Predict future expenses and savings based on current trends.
        Placeholder logic before Prophet/LSTM integration.
        """
        # Add a simple 2% inflation/growth per month for forecasting
        growth_rate = 1.02
        
        forecasts = []
        for i in range(1, months + 1):
            projected_spending = current_spending * (growth_rate ** i)
            projected_savings = current_savings * (1.05 ** i) # Assuming 5% return on savings
            
            forecasts.append({
                "month": f"Month {i}",
                "predicted_expenses": round(projected_spending, 2),
                "predicted_savings": round(projected_savings, 2),
                "net_worth": round(projected_savings - projected_spending * 0.2, 2)
            })
            
        return forecasts

forecaster = ForecastingEngine()
