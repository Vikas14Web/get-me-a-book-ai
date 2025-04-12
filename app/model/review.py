from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(String, nullable=False)
    review_text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)

    book = relationship("Book", back_populates="reviews")