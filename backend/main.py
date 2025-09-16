from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from chatbot.responses import get_investment_response

app = FastAPI()

# CORS setup for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  #

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    msg = data.get("message", "")
    response = get_investment_response(msg)
    return {"response": response}
