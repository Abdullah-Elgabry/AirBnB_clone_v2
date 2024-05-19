#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
import shlex


class FileStorage:
    """this is for converting and reverse the converting
    of json file
    Attributes:
        __file_path: json loc
        __objects: repo
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """this def will get * obj
        Return:
            obj {}
        """

        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """a setter function for object
        Args:
            obj: the obj data
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """saving the data as a json file"""

        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """reloading the json data"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ make the elem empty"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ def for call the reload() func"""
        self.reload()