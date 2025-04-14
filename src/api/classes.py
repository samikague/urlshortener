from pydantic import BaseModel

class ShortUrl_class(BaseModel):
    original_url: str

class Authorize_Class(BaseModel):
    control_token: str