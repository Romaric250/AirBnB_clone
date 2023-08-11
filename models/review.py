#!/usr/bin/python3
"""this model creates the review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """ the review class"""
    user_id = ""
    place_id =  ""
    text = ""
    