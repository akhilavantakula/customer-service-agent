from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from classify import classify_intent
from handlers import handle_technical, handle_feature, handle_sales, handle_escalation
from utils import log_interaction

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Inquiry(BaseModel):
    message: str

@app.post("/chat")
async def chat(inquiry: Inquiry):
    message = inquiry.message.strip()

    intent = classify_intent(message)

    if intent == "Technical Support":
        response = handle_technical(message)
    elif intent == "Product Feature Request":
        response = handle_feature(message)
    elif intent == "Sales Lead":
        response = handle_sales(message)
    else:
        response = handle_escalation(message)

    log_interaction(message, intent, response)

    return {
        "intent": intent,
        "response": response
    }