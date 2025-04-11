from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from .models import Base

<<<<<<< HEAD

DATABASE_URL = "sqlite+aiosqlite://database.db"


=======
DATABASE_URL = "sqlite+aiosqlite://database.db"

>>>>>>> refs/remotes/origin/master
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    poolclass=NullPool
)


async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
