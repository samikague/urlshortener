from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    None

class ShortUrl(BaseModel):
    """Модель для хранения сокращенных URL"""
    __tablename__ = "short_urls"

    original_url = Column(String(2048), nullable=False)
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
    expires_at = Column(DateTime, nullable=True)
