from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

class ShortUrl(BaseModel):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    control_token = Column(String(256), nullable=False)
    original_url = Column(String(2048), nullable=False)
    short_code = Column(String(10), unique=True, index=True, nullable=False)