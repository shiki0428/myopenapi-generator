# coding: utf-8
from sqlalchemy import Column, Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    id2 = Column(Integer)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(20))
    hashed_password = Column(String(20))
    is_active = Column(Boolean)
