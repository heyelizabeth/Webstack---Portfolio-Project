import os
from fastapi import FastAPI
import uvicorn
from app.routers import url
from fastapi.responses import RedirectResponse
from app.services import get_original_url

app = FastAPI(
    title="URL Shortener API",
    description="A simple API to shorten URLs and redirect to original URLs.",
    version="1.0.0"
)

app.include_router(url.router, prefix="/api", tags=["URL Shortener"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the URL Shortener API! Visit /docs for API documentation."}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
