#!/usr/bin/python3
"""FileStorage class"""
import json
import os
import models
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __objects"""
        return self.__objects

    def new(self, obj):
        """ sets the obj with key <obj class name>.id"""
        key = f"{self.__class__.__name__}.{self.id}"
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
                    func = f"{v['__class__']}({**v})"
                    self.__objects[k] = eval(func)
        except Exception as e:
            pass
