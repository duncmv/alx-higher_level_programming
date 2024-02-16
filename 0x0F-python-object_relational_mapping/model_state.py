#!/usr/bin/python3
"""defines a State class and an instance of Base"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that inherits from base and has
    id and name atttributes"""

    __tablename__ = 'states'
    id = Column('id', Integer(), unique=True, nullable=False,
                autoincrement='auto', primary_key=True)
    name = Column('name', String(128), nullable=False)
