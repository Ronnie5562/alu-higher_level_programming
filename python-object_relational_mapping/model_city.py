#!/usr/bin/python3
"""
This module defines the 'City' class, which represents the 'cities' table,
and an instance 'Base' of the declarative base class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    This class maps to the 'cities' table in the MySQL database.

    Attributes:
        __tablename__ (str): The name of the corresponding database table.
        id (int): The primary key for the 'cities' table.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the 'id' column of the
                        'states' table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
