#!/usr/bin/python3
"""Idk what I'm doing"""
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

myMetaData = MetaData()
Base = declarative_base()


class State(Base):
    """A state table here"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
