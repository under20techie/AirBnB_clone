#!/usr/bin/python3
"""Contains User Model"""


from models.base_model import BaseModel


class User(BaseModel):
    """ User Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
