from sqlalchemy import Column, Integer, String, Text, BOOLEAN
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    "mysql+asyncmy://user:password@localhost/databasestr_gomel"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass


class DGazprom(Model):
    __tablename__ = "gazprom"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20))
    number = Column(String(10))
    address = Column(String(255))
    tip = Column(String(30))
    region = Column(String(100))
    comment = Column(String(500))
    geo = Column(String(50))


class DBaseStation(Model):
    __tablename__ = "baz"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(10))
    address = Column(String(255))
    comment = Column(String(255))


class DAllInfo(Model):
    __tablename__ = "baza"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sity = Column(String(20))
    claster = Column(String(20))
    street = Column(String(25))
    namber = Column(String(7))
    comment = Column(String(255))
    askue = Column(Integer)


class DManual(Model):
    __tablename__ = "pol"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tip = Column(String(255))
    comment = Column(Text)

