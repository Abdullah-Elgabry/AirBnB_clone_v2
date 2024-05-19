#!/usr/bin/python3
"""Module containg State class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import Column, Integer, String
import shlex
import models


class State(BaseModel, Base):
    """class state for eash state info
    Attributes:
        name: user search
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        st_lst = []
        result = []
        for lst in var:
            city = lst.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                st_lst.append(var[lst])
        for elem in st_lst:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)