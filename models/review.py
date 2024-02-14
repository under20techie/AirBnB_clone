#!/usr/bin/python3
"""Contains Review Model"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Model"""
    place_id = ""
    user_id = ""
    text = ""
