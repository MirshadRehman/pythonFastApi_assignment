from fastapi import FastAPI,HTTPException
from bson import ObjectId
from database import db
from models import BookCreate,BookResponse,BookUpdate,datetime
from typing import List

app = FastAPI()

@app.get("/api/books", response_model=List[BookResponse])
async def list_books(skip: int = 0, limit: int = 10):
    books = await db["books"].find().skip(skip).limit(limit).to_list(limit)
    return [{"id": str(book["_id"]), **book} for book in books]

@app.get("/api/books/{id}", response_model=BookResponse)
async def get_book(id: str):
    book = await db["books"].find_one({"_id": ObjectId(id)})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": str(book["_id"]), **book}

@app.post("/api/books", response_model=BookResponse)
async def add_book(book: BookCreate):
    book_data = book.dict()
    book_data.update({"created_at": datetime.utcnow(), "updated_at": datetime.utcnow()})
    result = await db["books"].insert_one(book_data)
    return {"id": str(result.inserted_id), **book_data}

@app.put("/api/books/{id}", response_model=BookResponse)
async def update_book(id: str, book: BookUpdate):
    book_data = {k: v for k, v in book.dict().items() if v is not None}
    if not book_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    book_data["updated_at"] = datetime.utcnow()
    result = await db["books"].update_one({"_id": ObjectId(id)}, {"$set": book_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    updated_book = await db["books"].find_one({"_id": ObjectId(id)})
    return {"id": str(updated_book["_id"]), **updated_book}

@app.delete("/api/books/{id}")
async def delete_book(id: str):
    result = await db["books"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}