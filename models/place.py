#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """this is the city class, with its attributes"""
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.00
    amenity_ids = []
