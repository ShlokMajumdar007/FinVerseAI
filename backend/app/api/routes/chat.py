from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Transaction
from app.ml.nlp_assistant import nlp_assistant

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    query: str
    history: list[Message] = []

@router.post("/")
def chat(request: ChatRequest, user_id: int = 1, db: Session = Depends(get_db)):
    txns = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    total_spent = sum([t.amount for t in txns])
    income = 100000.0
    savings = income - total_spent
    
    financial_context = {
        "savings": savings,
        "total_spent": total_spent,
        "income": income
    }
    
    response = nlp_assistant.chat(request.query, request.history, financial_context)
    return {"reply": response}
