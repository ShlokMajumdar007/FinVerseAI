from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Transaction, User
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.ml.anomaly import anomaly_detector

router = APIRouter()

@router.post("/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, user_id: int = 1, db: Session = Depends(get_db)):
    db_txn = Transaction(
        user_id=user_id,
        amount=transaction.amount,
        category=transaction.category,
        merchant=transaction.merchant,
        description=transaction.description,
        date=transaction.date
    )
    
    # Anomaly detection will run periodically or be checked here, but for now we skip
    
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn

@router.get("/", response_model=list[TransactionResponse])
def get_transactions(user_id: int = 1, db: Session = Depends(get_db)):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()

@router.get("/anomalies")
def get_anomalies(user_id: int = 1, db: Session = Depends(get_db)):
    txns = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    txn_dicts = [{"id": t.id, "amount": t.amount, "category": t.category} for t in txns]
    return anomaly_detector.detect_anomalies(txn_dicts)
