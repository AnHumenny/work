from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
import asyncpg
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "postgresql+asyncpg://login:password@localhost/database"

engine = create_async_engine(url=DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class DUser(Model):
    __tablename__ = "_userbot"
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(30))
    name = Column(String(30))
    status = Column(String(15))
    password = Column(String)
    phone = Column(String(14))
    email = Column(String(50))
    tg_id = Column(String(50))


class DVisitedUser(Model):
    __tablename__ = "_visited_users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(30))
    date_created = Column(DateTime(timezone=False))
    action = Column(String(50))
