#!/usr/bin/python3
"""
Define a State class
that inherits from sqlalchemy Base
"""
from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """create class State for MySQL database

    Attributes:
        __tablename__ (str): MySQL table's name to store states.
        id (int): state's id.
        name (str): state's name."""
    __tablename__ = "states"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
