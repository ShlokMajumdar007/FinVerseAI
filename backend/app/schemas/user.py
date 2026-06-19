from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str
    full_name: str
    risk_profile: Optional[str] = "Balanced"
    personality_type: Optional[str] = "Unknown"

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    financial_score: int

    class Config:
        orm_mode = True
