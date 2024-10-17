URL Shortener API

This API is designed to convert long URLs into short, easy-to-share links using FastAPI and MongoDB.

Tech Stack

Framework: FastAPI

Database: MongoDB

Server: Uvicorn

Containerization: Docker



Features

Shorten URLs: Quickly create shorter versions of long links.

Redirect: Send users from short URLs to the original links.

Track Clicks: Monitor how many times each short URL is accessed.


Setup Instructions

Requirements

Docker installed

Access to a MongoDB instance


Running Locally

1. Clone the Repository:

git clone <repository-url>
cd url-shortener-api


2. Set Up Environment:
Create a .env file with your MongoDB connection string:

MONGO_URI=mongodb://<username>:<password>@<host>:<port>/


3. Build and Run:

docker build -t url-shortener-app .
docker run -d -p 8000:8000 url-shortener-app


4. Access API Docs:
Open http://localhost:8000/docs.



Without Docker

1. Install Dependencies:

pip install -r requirements.txt


2. Run the App:

uvicorn app.main:app --reload



API Endpoints

Base URL:
http://localhost:8000


1. POST /shorten: Shortens a URL.
Request:

{ "original_url": "https://example.com" }

Response:

{ "short_url": "http://localhost:8000/{short_code}" }


2. GET /{short_code}: Redirects to the original URL.


3. GET /stats/{short_code}: Retrieves click statistics for a short URL.
Response:

{ "original_url": "https://example.com", "clicks": 25 }

