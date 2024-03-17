#!/usr/bin/python3
"""
Define City class
that inherits from sqlalchemy Base
"""
# Import necessary modules and classes from SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


# create a base fr declarative class definitions
Base = declarative_base()


# Define the City class, which inherits from the SQLAlchemy Base class
class City(Base):
    """create class city for MySQL database

    Attributes:
        __tablename__ (str): MySQL table's name to store cities.
        id (int) city's id.
        name (str) city's name."""

    # Set the table name for the City class
    __tablename__ = "cities"

    # Define the columns for the cities table
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
