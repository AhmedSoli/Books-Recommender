
import os
import feedparser
import pandas as pd
from fastapi import FastAPI, Depends, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.mount("/.well-known", StaticFiles(directory=os.path.join(os.getcwd(), ".well-known")), name=".well-known")

def get_goodreads_books(user_id: str, csv_file: str):
    url = f"https://www.goodreads.com/review/list_rss/{user_id}?shelf=%23ALL%23"
    feed = feedparser.parse(url)
    books = [{'title': entry['title'], 'author': entry['author_name'], 'rating': entry['user_rating']} for entry in feed.entries]
    df = pd.DataFrame(books)
    df.to_csv(csv_file, index=False)
    return df

def get_books_df(profile_id: str) -> pd.DataFrame:
    csv_file = f"data/{profile_id}.csv"
    if os.path.isfile(csv_file):
        return pd.read_csv(csv_file)
    return get_goodreads_books(profile_id, csv_file)


@app.get("/prompt")
def get_prompt(goodreads_profile_id: str = Query(..., min_length=6, regex="^[0-9]+$")):
    """
    Receives as input the [user's goodreads profile ID](https://help.goodreads.com/s/article/Where-can-I-find-my-user-ID) and returns JSON with a prompt and the user's book history.
    """
    if not goodreads_profile_id:
        return {"message": "Please provide your Goodreads profile ID. This is the URL to learn more about it: https://help.goodreads.com/s/article/Where-can-I-find-my-user-ID"}
    else:
        books_df = get_books_df(goodreads_profile_id)
        return {
            "prompt": "Hi ChatGPT, I have compiled a list of the user's reading history below alognside their ratings. \
                Please recommend a book for them that aligns with their interests. Clearly explain why you are recommending the books. \
                    At the end ask them for extra information such as what genre they are interested in and try to make even better recommendations. \
                        Do not make another request to me unless the user changes the Goodreads profile ID since I always return the same message for the same profile ID.",
            "recent_books": books_df.head(10).to_dict('records'),
            "other_books": books_df.tail(-10).to_dict('records')
        }