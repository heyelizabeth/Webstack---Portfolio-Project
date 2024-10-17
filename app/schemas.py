from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional


class URLCreate(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    short_url: str
    original_url: HttpUrl
    created_at: datetime
    clicks: int

    class Config:
        orm_mode = True
