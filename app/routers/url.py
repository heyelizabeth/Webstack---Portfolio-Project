from fastapi import APIRouter, HTTPException, Depends
from app.schemas import URLCreate, URLResponse
from app.services import create_short_url, get_original_url, get_all_urls

router = APIRouter()

@router.post("/shorten", response_model=URLResponse)
def shorten_url(url: URLCreate):
    return create_short_url(url)

@router.get("/urls", response_model=list[URLResponse])
def list_urls():
    return get_all_urls()

@router.get("/{short_url}")
def redirect_url(short_url: str):
    url_entry = get_original_url(short_url)
    if url_entry:
        return {"original_url": url_entry.original_url, "clicks": url_entry.clicks}
    raise HTTPException(status_code=404, detail="URL not found")
