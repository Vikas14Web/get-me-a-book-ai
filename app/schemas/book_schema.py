from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    year_published: Optional[int]
    summary: Optional[str] = None

class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True