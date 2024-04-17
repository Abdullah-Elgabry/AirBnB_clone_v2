#!/usr/bin/python
""" amenity module """

import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ amenity rel"""
    if models.all_rep == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ obj init """
        super().__init__(*args, **kwargs)
