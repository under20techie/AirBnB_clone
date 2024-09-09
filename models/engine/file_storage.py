#!/usr/bin/python3
"""FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __objects"""
        return self.__objects

    def new(self, obj):
        """ sets the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            file_object = {k: v.to_dict()
                           for k, v in self.__objects.items()}
            json.dump(file_object, f)

    def reload(self):
        """ Deserialises whats in filepath"""
        try:
            with open(self.__file_path, 'r') as f:
                new_object = json.load(f)
                for k, v in new_object.items():
                    func = f"{v['__class__']}(**v)"
                    self.__objects[k] = eval(func)
        except Exception as e:
            pass
