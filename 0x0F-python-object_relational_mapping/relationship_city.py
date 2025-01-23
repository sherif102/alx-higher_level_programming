#!/usr/bin/python3
"""
Model: relationship_city.py
Author: Sheriff Abdulfatai
"""


from relationship_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ ORM class City mapped to the city table """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates='cities')
