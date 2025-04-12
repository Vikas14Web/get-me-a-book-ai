from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.book_schema import BookCreate, BookOut
from app.db.session import get_db
from app.db import crud
from typing import List

router = APIRouter()

@router.post("/", response_model=BookOut)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_book(db, book)

@router.get("/", response_model=List[BookOut])
async def read_books(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.get_books(db, skip, limit)