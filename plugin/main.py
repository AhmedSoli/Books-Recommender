import os
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import feedparser
import pandas as pd
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Initialize FastAPI
app = FastAPI()
# Add CORS middleware to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize SQLAlchemy
engine = create_engine("sqlite:///books.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Book(Base):
    """Book model"""
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    rating = Column(Integer)

Base.metadata.create_all(bind=engine)

# Define Pydantic models
class BookBase(BaseModel):
    from datetime import datetime
    title: str
    author: str
    rating: int
    read_at: Optional[datetime] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class GoodreadsProfile(BaseModel):
    """Goodreads profile model"""
    url: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_goodreads_books(user_id: str):
    """Fetches books from a Goodreads user's RSS feed and returns them as a DataFrame."""
    url = f"https://www.goodreads.com/review/list_rss/{user_id}?shelf=%23ALL%23"
    feed = feedparser.parse(url)
    books = [{'title': entry['title'], 'author': entry['author_name'], 'rating': entry['user_rating']} for entry in feed.entries]
    return pd.DataFrame(books)

@app.post("/goodreads_profile")
async def save_goodreads_profile(profile: GoodreadsProfile, db: Session = Depends(get_db)):
    """Endpoint to save Goodreads profile data"""
    user_id = profile.url.split('/')[-1]  # Extract user ID from URL
    books_df = get_goodreads_books(user_id)
    for index, row in books_df.iterrows():
        book = Book(title=row['title'], author=row['author'], rating=row['rating'])
        db.add(book)
    db.commit()
    return {"message": "Profile data saved successfully."}

@app.get("/prompt", response_model=List[Book])
def get_prompt(db: Session = Depends(get_db)):
    """Endpoint to get book recommendations"""
    books = db.query(Book).all()
    return books