#!/usr/bin/python3
"""
module that creates a class 'city' based on Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    City class that inherits from Base

    Attributes:

        id: Id city
        name: Name of city
        state_id: State id

    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
