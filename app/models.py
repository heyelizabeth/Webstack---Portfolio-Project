from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class Url(BaseModel):
    short_url: str
    original_url: HttpUrl
    created_at: datetime
    clicks: int
