#!/usr/bin/python3
""" BASEMODEL"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        """ Init Method"""

        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'id':
                        v = str(v)
                    elif k in ['created_at', 'updated_at']:
                        v = datetime.strptime(v,
                                              '%Y-%m-%dT%H:%M:%S.%f')

                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Str """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates updated_at with current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns the __dict__ of the instance """

        new_dict = {}

        for k, v in self.__dict__.items():
            new_dict[k] = v

        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
