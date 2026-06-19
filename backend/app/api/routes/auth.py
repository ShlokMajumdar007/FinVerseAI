from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Simple hash for demo (Use passlib in production)
    hashed_password = user.password + "notreallyhashed"
    
    new_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        risk_profile=user.risk_profile,
        personality_type=user.personality_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or user.hashed_password != password + "notreallyhashed":
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # Return mock JWT
    return {"access_token": "mock_jwt_token_" + str(user.id), "token_type": "bearer"}
