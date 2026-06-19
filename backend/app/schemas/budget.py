from pydantic import BaseModel
from typing import Optional

class BudgetBase(BaseModel):
    month: int
    year: int
    category: str
    allocated_amount: float
    spent_amount: Optional[float] = 0.0

class BudgetCreate(BudgetBase):
    pass

class BudgetResponse(BudgetBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
