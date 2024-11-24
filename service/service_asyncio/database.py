import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

database_url = os.getenv('database_url')

engine = create_async_engine(database_url)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)

class DGazprom(Model):
    __tablename__ = "gazprom"
    ip = Column(String(15))
    number = Column(String(10))
    address = Column(String(255))
    tip = Column(String(10))
    region = Column(String(100))
    comment = Column(String(500))
  #  geo = Column(String(30))

class DManual(Model):
    __tablename__ = "manual"
    tip = Column(String(255))
    comment = Column(Text)

class DBaseStation(Model):
    __tablename__ = "base_station"
    comment = Column(String(255))
    address = Column(String(255))
    number = Column(Integer())

class DConnFromBs(Model):
    __tablename__ = "conn_from_base"
    sity = Column(String(30))
    bs = Column(String(255))
    street = Column(String(30))
    namber = Column(Integer())
    comment = Column(String(1000))

class DAllInfo(Model):
    __tablename__ = "baza"
    sity = Column(String(20))
    claster = Column(String(20))
    street = Column(String(30))
    namber = Column(String(10))
    comment = Column(Text(1000))
    askue = Column(Integer)

class DKey(Model):
    __tablename__ = "keys"
    street = Column(String(20))
    home = Column(String(20))
    entrance = Column(Integer())
    ind = Column(Integer())
    stand = Column(Integer())

class DInfo(Model):
    __tablename__ = "info"
    reestr = Column(Integer)
    date = Column(Date())
    sity = Column(String(20))
    street = Column(String(30))
    home = Column(String(10))
    apartment = Column(Integer)
    name = Column(String(100))
    cable_1 = Column(Integer)
    cable_2 = Column(Integer)
    cable_3 = Column(Integer)
    connector = Column(Integer)

class DReplacement(Model):
    __tablename__ = "replacement"
    date = Column(Date())
    address = Column(String(50))
    equipment = Column(String(20))
    problem = Column(String(255))
    responsible = Column(String(50))

