from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from analyzer import OfflineFinanceAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Expense(BaseModel):
    title: str
    amount: float


class FinanceInput(BaseModel):
    income: float
    expenses: List[Expense]


@app.get("/")
def home():

    return {
        "message": "Offline Finance AI Running"
    }


@app.post("/analyze")
def analyze(data: FinanceInput):

    expenses = []

    for item in data.expenses:

        expenses.append({
            "title": item.title,
            "amount": item.amount
        })

    ai = OfflineFinanceAI(
        data.income,
        expenses
    )

    return ai.run()