from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.book import Book
from app.schemas.book_schema import BookCreate

async def create_book(db: AsyncSession, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id == book_id))
    return result.scalar_one_or_none()

async def get_books(db: AsyncSession):
    result = await db.execute(select(Book))
    return result.scalars().all()

async def update_book(db: AsyncSession, book_id: int, book_data: BookCreate):
    await db.execute(update(Book).where(Book.id == book_id).values(**book_data.dict()))
    await db.commit()

async def delete_book(db: AsyncSession, book_id: int):
    await db.execute(delete(Book).where(Book.id == book_id))
    await db.commit()