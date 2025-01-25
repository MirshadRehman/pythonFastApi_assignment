from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    price: float
    quantity: int
    published_date: Optional[datetime]
    genre: Optional[str]
    description: Optional[str]

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    isbn: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    published_date: Optional[datetime]
    genre: Optional[str]
    description: Optional[str]

class BookResponse(BookBase):
    id: str
    created_at: datetime
    updated_at: datetime