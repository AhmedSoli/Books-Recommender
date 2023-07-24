import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Optional, List
import sqlite3


# Initialize FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/.well-known",
    StaticFiles(directory=os.path.join(os.getcwd(), ".well-known")),
    name=".well-known",
)

# Initialize SQLite
conn = sqlite3.connect("books.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
             title TEXT NOT NULL,
             rating INTEGER NOT NULL,
             comment TEXT)"""
)


# Define Pydantic models
class Book(BaseModel):
    id: Optional[int]
    title: str
    rating: int
    comment: Optional[str]


class Books(BaseModel):
    books: List[Book]


@app.post("/books")
def add_book(book: Book):
    c.execute(
        "INSERT INTO books (title, rating, comment) VALUES (?, ?, ?)",
        (book.title, book.rating, book.comment),
    )
    conn.commit()
    return {"success": True, "book_id": c.lastrowid}


@app.put("/books/{id}")
def update_book(id: int, book: Book):
    c.execute(
        "UPDATE books SET title = ?, rating = ?, comment = ? WHERE id = ?",
        (book.title, book.rating, book.comment, id),
    )
    if c.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    conn.commit()
    return {"success": True}


@app.delete("/books/{id}")
def delete_book(id: int):
    c.execute("DELETE FROM books WHERE id = ?", (id,))
    if c.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    conn.commit()
    return {"success": True}


@app.get("/books", response_model=Books)
def list_books():
    c.execute("SELECT * FROM books")
    books = [
        Book(id=row[0], title=row[1], rating=row[2], comment=row[3])
        for row in c.fetchall()
    ]
    return {"books": books}


@app.get("/recommendations")
def get_recommendations():
    c.execute("SELECT * FROM books")
    books = [
        Book(id=row[0], title=row[1], rating=row[2], comment=row[3])
        for row in c.fetchall()
    ]
    prompt = "Hello, you're my AI for book recommendations. Here are my ratings and comments on some books:\n\n"
    for book in books:
        prompt += (
            f"- '{book.title}' ({book.rating}/5): {book.comment or 'No comment'}\n"
        )
    prompt += "\nBased on this, can you recommend three books for me? Please provide explanations."
    return {"prompt": prompt}
