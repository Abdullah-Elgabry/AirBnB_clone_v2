#!/usr/bin/python3
""" thia is the module of  State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """this is the class of  state """
    if models.all_rep == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """instance creator for state """
        super().__init__(*args, **kwargs)

    if models.all_rep != "db":
        @property
        def cities(self):
            """ this func will make an obj """
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
