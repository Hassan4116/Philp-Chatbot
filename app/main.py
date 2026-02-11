from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="Philp AI Assistant")

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Welcome to Philp AI Assistant! Use the /chat endpoint to interact with Philp."}