#!/usr/bin/python3
"""
This is the script for the base model.

Module: base_model
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for all models.

    Attributes:
        - id (str): The unique identifier of the instance.
        - created_at (datetime): The datetime when the instance was created.
        - updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes instance attributes.

        Args:
            - *args: List of arguments.
            - **kwargs: Dictionary of key-value arguments.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the official string representation of the instance.

        Returns:
            str: The formatted string representation.
        """

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 'updated_at' and saves the instance.

        Returns:
            None
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.

        Returns:
            dict: The dictionary representation of the instance.
        """

        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic
