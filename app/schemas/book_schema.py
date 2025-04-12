from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    year_published: int
    summary: Optional[str] = None

class BookOut(BookCreate):
    id: int

    class Config:
        orm_mode = True