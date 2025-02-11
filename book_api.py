from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# Book model
class Book(BaseModel):
    id: str
    book_name: str
    author: str
    publisher: str

# Simulated database (in-memory storage)
books_db = []

# Create a new book (POST)
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    book.id = str(uuid4())  # Generate unique ID
    books_db.append(book)
    return book

# Read all books (GET)
@app.get("/books/", response_model=List[Book])
def get_books():
    return books_db

# Read a single book by ID (GET)
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: str):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Update a book by ID (PUT)
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: str, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book by ID (DELETE)
@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(index)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

