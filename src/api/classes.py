from pydantic import BaseModel

class ShortUrl(BaseModel):
    url: str