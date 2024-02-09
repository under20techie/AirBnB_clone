#!/usr/bin/python3
""" BASEMODEL"""
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel """

    def __init__(self):
        """ Init Method"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Str """

        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):                                                                          """ returns the __dict__ of the instance """

        new_dict = {}

        for k, v in self.__dict__.items():
            new_dict[k] = v

        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['updated_at'] = self.updated_at.isoformat('%Y-%m-%dT%H:%M:%S.%f')

        return new_dict

