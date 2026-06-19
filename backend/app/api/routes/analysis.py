from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Transaction, User
from app.ml.budget_engine import budget_engine
from app.ml.forecasting import forecaster
from app.ml.advisor import advisor

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_data(user_id: int = 1, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    txns = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    
    income = 100000.0 # Mocked income, could be stored in User table or derived
    txn_dicts = [{"amount": t.amount, "category": t.category} for t in txns]
    
    budget = budget_engine.generate_budget(income, txn_dicts)
    
    total_spent = sum([t.amount for t in txns])
    savings = income - total_spent
    
    forecast = forecaster.forecast(total_spent, savings)
    investment_advice = advisor.generate_recommendation(user.financial_score if user else 50)
    
    return {
        "financial_score": user.financial_score if user else 50,
        "personality": user.personality_type if user else "Unknown",
        "total_spent": total_spent,
        "savings": savings,
        "budget_recommendation": budget,
        "forecast": forecast,
        "investment_advice": investment_advice
    }
