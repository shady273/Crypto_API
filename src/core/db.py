from src.core.config import db_config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = (f"postgresql+asyncpg://{db_config.db_user}:{db_config.db_pass}@{db_config.db_host}:"
                f"{db_config.db_port}/{db_config.db_name}")
Base = declarative_base()


engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session