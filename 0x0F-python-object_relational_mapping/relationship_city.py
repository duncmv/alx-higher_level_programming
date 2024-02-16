#!/usr/bin/python3
"""defines a City class and an instance of Base"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """City class that inherits from base and has
    id, name and state_id atttributes"""

    __tablename__ = 'cities'
    id = Column('id', Integer(), unique=True, nullable=False,
                autoincrement='auto', primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)
