from pydantic import BaseModel
from typing import Optional

class ReviewCreate(BaseModel):
    user_id: int
    review_text: Optional[str]
    rating: int

class ReviewRead(ReviewCreate):
    id: int
    book_id: int

    class Config:
        orm_mode = True