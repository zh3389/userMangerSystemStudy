import asyncio
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///./test.db"


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    """
    可以在 FastAPI 应用程序初始化期间调用此函数。
    异步创建数据库及其表的函数。
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_db_and_tables())


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    异步生成一个新的异步会话。
    返回产生AsyncSession的异步生成器。
    """
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """
    一个产生SQLAlchemyUserDatabase实例的协同程序。
    将AsyncSession作为输入，默认为get_async_session。
    """
    yield SQLAlchemyUserDatabase(session, User)

