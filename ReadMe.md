Here's an updated version of the ReadMe to match the new purpose of the code:

# Book Recommendations Plugin for OpenAI

## Description
This plugin allows users to interact with a book recommendation system that uses Large Language Models (LLMs). It's designed to provide highly personalized book recommendations based on user ratings and comments.

## Getting Started
To get started with this plugin, you'll need to run the backend server locally and connect it to the ChatGPT UI. Here are the steps to do so:

### Plugin Backend
1. Create and activate a new virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
uvicorn main:app --reload
```

### ChatGPT Connection
1. Navigate to the ChatGPT UI.
2. Select "Develop your own plugin".
3. Enter your localhost address and port number (e.g., `localhost:8000`).
> **Note**: Only the `auth` type `none` is currently supported for localhost development.

## Working of the Plugin
This plugin uses an SQLite database to store book ratings and comments provided by the user. When a GET request is made to `/recommendations`, it retrieves the user's book ratings and comments and returns a prompt ready to be passed to the OpenAI API for generating book recommendations.

The generated prompt is returned in the JSON format as follows:
```json
{
  "prompt": "generated_prompt"
}
```

## How to Add, Update, and Remove Book Ratings
The plugin provides the following endpoints for managing book ratings:

- `POST /books`: Add a new book with rating and optional comment.
- `PUT /books/{id}`: Update a book's rating and comment.
- `DELETE /books/{id}`: Remove a book's rating.

## Acknowledgments
This plugin is developed using the FastAPI framework and it's designed to work with OpenAI's ChatGPT.

Feel free to modify and customize this ReadMe file according to your specific requirements.