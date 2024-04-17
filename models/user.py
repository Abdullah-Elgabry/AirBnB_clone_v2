#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """this is a use db
    Attributes:
        __tablename__ (str): db table name.
        email: (sqlalchemy String): e-mail add.
        password (sqlalchemy String): user pass.
        first_name (sqlalchemy String):user fn.
        last_name (sqlalchemy String): user ln.
        places (sqlalchemy relationship): user rel of the place.
        reviews (sqlalchemy relationship): user review of the place
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all", backref="user")
    reviews = relationship("Review", cascade="all", backref="user")