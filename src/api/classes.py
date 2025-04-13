from pydantic import BaseModel

class ShortUrl(BaseModel):
    original_url: str