#!/usr/bin/pyhton3
"""This module  contains the class definition of a State
and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """The states class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
