import pprint
from abc import ABC, abstractmethod
from sqlalchemy import insert
from src.core.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_many(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    @classmethod
    async def add_many(cls, data_list):
        pprint.pprint(data_list)
        async with async_session_maker() as session:
            for data in data_list:
                stmt = insert(cls.model).values(**data)
                await session.execute(stmt)
            await session.commit()
