from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from .models import Base

# URL базы данных
DATABASE_URL = "sqlite+aiosqlite://database.db"

# Создаем асинхронный движок
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Включаем логирование SQL-запросов
    poolclass=NullPool  # Используем NullPool для асинхронной работы
)

# Создаем фабрику сессий
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)