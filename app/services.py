import string
import random
from datetime import datetime
from app.database import urls_collection
from app.schemas import URLCreate, URLResponse
from app.models import Url
from typing import Optional

def generate_short_url(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choices(characters, k=length))
        if not urls_collection.find_one({"short_url": short_url}):
            return short_url



def create_short_url(url_entry: URLCreate):
    
    url_dict = url_entry.dict()
    url_dict['original_url'] = str(url_dict['original_url'])


    url_dict['short_url'] = generate_short_url()

   
    url_dict['created_at'] = datetime.utcnow()
    url_dict['clicks'] = 0

    urls_collection.insert_one(url_dict)

    return URLResponse(**url_dict)




def get_original_url(short_url: str) -> Optional[URLResponse]:
    url_entry = urls_collection.find_one({"short_url": short_url})
    if url_entry:
        urls_collection.update_one({"short_url": short_url}, {"$inc": {"clicks": 1}})
        return URLResponse(**url_entry)
    return None

def get_all_urls() -> list[URLResponse]:
    urls = list(urls_collection.find())
    # print(urls)
    return [URLResponse(**url) for url in urls]
