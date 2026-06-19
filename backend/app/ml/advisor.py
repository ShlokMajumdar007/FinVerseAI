class InvestmentAdvisor:
    def __init__(self):
        self.risk_profiles = {
            "Conservative": {
                "Emergency Fund": 30,
                "Index Funds": 40,
                "Mutual Funds": 20,
                "Stocks": 10,
                "High-Risk Assets": 0
            },
            "Balanced": {
                "Emergency Fund": 20,
                "Index Funds": 30,
                "Mutual Funds": 20,
                "Stocks": 20,
                "High-Risk Assets": 10
            },
            "Aggressive": {
                "Emergency Fund": 10,
                "Index Funds": 20,
                "Mutual Funds": 10,
                "Stocks": 40,
                "High-Risk Assets": 20
            }
        }

    def generate_recommendation(self, score: int):
        if score > 80:
            profile = "Aggressive"
        elif score > 50:
            profile = "Balanced"
        else:
            profile = "Conservative"
            
        allocation = self.risk_profiles[profile]
        
        return {
            "risk_profile": profile,
            "allocation": allocation,
            "roadmap": [
                "Build 6 months of emergency fund.",
                "Max out tax-advantaged accounts.",
                "Diversify with index funds.",
                "Explore individual stocks if risk appetite allows."
            ]
        }

advisor = InvestmentAdvisor()
