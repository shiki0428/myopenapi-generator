# coding: utf-8
from sqlalchemy import Boolean, Column, Integer, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class QandA(Base):
    __tablename__ = 'QandA'

    question_id = Column(Text, primary_key=True, server_default=text("''::text"))
    question = Column(Text, nullable=False, server_default=text("''::text"))
    answer = Column(Text, nullable=False, server_default=text("''::text"))
    dir_id = Column(Text, nullable=False, server_default=text("''::text"))
    favorite_count = Column(Text, nullable=False, server_default=text("''::text"))
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    is_completed = Column(Boolean, nullable=False, server_default=text("false"))


t_aaa = Table(
    'aaa', metadata,
    Column('name', String),
    Column('value', String)
)


class Favorite(Base):
    __tablename__ = 'favorite'

    favorite_id = Column(Text, primary_key=True, server_default=text("''::text"))
    user_id = Column(Text, nullable=False, server_default=text("''::text"))
    question_id = Column(Text, nullable=False, server_default=text("''::text"))
    Is_favorite = Column(Boolean, nullable=False, server_default=text("false"))


class ShareDirectory(Base):
    __tablename__ = 'share_directory'

    dir_id = Column(Text, primary_key=True, server_default=text("''::text"))
    descritpion = Column(Text, nullable=False, server_default=text("''::text"))
    user_id = Column(Text, nullable=False, server_default=text("''::text"))
    is_secret = Column(Boolean, nullable=False, server_default=text("false"))
    secret_password = Column(Text, nullable=False, server_default=text("''::text"))
    is_edit = Column(Boolean, nullable=False, server_default=text("false"))
    edit_password = Column(Text, nullable=False, server_default=text("''::text"))
    tag_id = Column(Text, nullable=False, server_default=text("''::text"))
    total_favorite_count = Column(Integer, nullable=False, server_default=text("0"))


class Tag(Base):
    __tablename__ = 'tag'

    tag_id = Column(Text, primary_key=True, server_default=text("''::text"))
    name = Column(Text, nullable=False, server_default=text("''::text"))
    color = Column(Text, nullable=False, server_default=text("''::text"))
    is_active = Column(Boolean)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Text, primary_key=True, server_default=text("''::text"))
    name = Column(Text, nullable=False, server_default=text("''::text"))
    description = Column(Text, nullable=False, server_default=text("''::text"))
    email = Column(Text, nullable=False, server_default=text("''::text"))
    password = Column(Text, nullable=False, server_default=text("''::text"))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, server_default=text("nextval('users_id_seq'::regclass)"))
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean)
