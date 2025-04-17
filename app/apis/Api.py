# app/api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .database.DataBase import engine
# from .database.models import Base

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Create tables if they don't exist
# Base.metadata.create_all(bind=engine)

# Include the routers


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
