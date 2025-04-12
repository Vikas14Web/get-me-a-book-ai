from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import books, reviews
from app.utils.auth import get_current_user

app = FastAPI(title="Book AI System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(reviews.router, prefix="/books", tags=["Reviews"])

@app.get("/")
def root():
    return {"message": "Welcome to the Book AI System!"}