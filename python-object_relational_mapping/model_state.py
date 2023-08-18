#!/usr/bin/python3
"""
This module defines the 'State' class, representing the 'states' table,
and creates an instance 'Base' of the declarative base class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    This class is mapped to the 'states' table in the MySQL database.
    Attributes:
        __tablename__ (str): The name of the corresponding database table.
        id (int): The primary key for the 'states' table.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
