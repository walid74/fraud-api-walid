# fraud-api-walid/main.py
from fastapi import FastAPI
from app import router  # assuming you have a router in app.py

app = FastAPI()
app.include_router(router)