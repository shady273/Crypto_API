import pprint
from abc import ABC, abstractmethod
from sqlalchemy import insert, exists, update, and_, select
from src.core.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_many(self):
        raise NotImplementedError

    @abstractmethod
    async def check_data_existence(self):
        raise NotImplementedError

    @abstractmethod
    async def update_many(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    @classmethod
    async def update_many(cls, data_list):
        async with async_session_maker() as session:
            for data in data_list:
                update_query = (update(cls.model).where(cls.model.crypto_id == data['crypto_id']).values(data))
                await session.execute(update_query)
            await session.commit()

    @classmethod
    async def add_many(cls, data_list):
        async with async_session_maker() as session:
            for data in data_list:
                new_crypto = cls.model(**data)
                session.add(new_crypto)
            await session.commit()

    @classmethod
    async def check_data_existence(cls, data_list):
        async with async_session_maker() as session:
            for data in data_list:
                query = select(cls.model).where(cls.model.crypto_id == data['crypto_id'])
                result = await session.execute(query)
                return result.scalar()
