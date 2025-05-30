from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import books, reviews
from app.utils.auth import get_current_user
from fastapi import FastAPI
from app.api import recommendations

app = FastAPI(title="Get Me A Book AI System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(reviews.router, prefix="/books", tags=["Reviews"])
app.include_router(recommendations.router)
app.include_router(summaries.router)
app.include_router(books.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Book AI System!"}