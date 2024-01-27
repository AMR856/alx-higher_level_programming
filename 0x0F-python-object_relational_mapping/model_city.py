#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from model_state import Base, State
"""Here I write some classes"""
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False,)
