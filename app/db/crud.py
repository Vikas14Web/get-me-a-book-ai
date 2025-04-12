from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.book import Book
from app.models.review import Review
from app.schemas.book_schema import BookCreate
from app.schemas.review_schema import ReviewCreate

async def create_book(db: AsyncSession, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Book).offset(skip).limit(limit))
    return result.scalars().all()

async def get_book_by_id(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id == book_id))
    return result.scalar_one_or_none()

async def create_review(db: AsyncSession, book_id: int, review: ReviewCreate):
    db_review = Review(book_id=book_id, **review.dict())
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review

async def get_reviews_by_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Review).where(Review.book_id == book_id))
    return result.scalars().all()