#!/usr/bin/python3
"""Here I write some classes"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    "City class here"
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True,)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
