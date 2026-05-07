from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from analyzer import OfflineFinanceAI


app = FastAPI()


# =========================
# CORS
# =========================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# =========================
# AI ENGINE
# =========================

ai = OfflineFinanceAI()


# =========================
# INPUT MODELS
# =========================

class Expense(BaseModel):

    title: str

    amount: int


class FinanceInput(BaseModel):

    income: int

    expenses: list[Expense]


# =========================
# ROUTES
# =========================

@app.get("/")
def home():

    return {

        "message":
        "Offline Finance AI Running"
    }


@app.post("/analyze")
def analyze(data: FinanceInput):

    expenses = [

        {
            "title": expense.title,

            "amount": expense.amount
        }

        for expense in data.expenses
    ]


    result = ai.analyze(

        data.income,

        expenses
    )

    return result