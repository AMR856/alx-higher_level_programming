#!/usr/bin/python3
"""Here I write some classes"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    "City class here"
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False,)
