from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.review_schema import ReviewCreate, ReviewOut
from app.db.session import get_db
from app.db import crud
from typing import List

router = APIRouter()

@router.post("/{book_id}/reviews", response_model=ReviewOut)
async def add_review(book_id: int, review: ReviewCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_review(db, book_id, review)

@router.get("/{book_id}/reviews", response_model=List[ReviewOut])
async def get_reviews(book_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_reviews_by_book(db, book_id)