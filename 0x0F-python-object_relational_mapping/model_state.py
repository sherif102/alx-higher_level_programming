#!/usr/bin/python3
"""
Module: model_state.py
Author: Sheriff Abdulfatai
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """ ORM class for state table """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
