#!/usr/bin/python3
"""This file contains the base models for the project.
    This will permit the other models to inherit
"""
from datetime import datetime  # Importing the datetime module from the datetime package
import uuid  # Importing the uuid module
from models import storage

class BaseModel:
    """This is the parent class, other children classes
        will inherit from it
    """
    def save(self):
        pass
        storage.save()
        #save all objects using the file storage instance

    def __init__(self, *args, **kwargs):
        """This built-in method initializes instance attributes"""
        if kwargs is not None and kwargs !={}:  # Checking if keyword arguments were passed
            for key in kwargs:  # Iterating over the keys of kwargs
                if key == "updated_at":  # Checking if the key is "updated_at"
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    # Converting the value to a datetime object and assigning it to the "updated_at" attribute
                elif key == "created_at":  # Checking if the key is "created_at"
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    # Converting the value to a datetime object and assigning it to the "created_at" attribute
                else:
                    self.__dict__[key] = kwargs[key]  # Assigning the value directly to the corresponding attribute
        else:
            self.id = str(uuid.uuid4())  # Generating a unique identifier and assigning it to the "id" attribute
            self.created_at = datetime.now()  # Assigning the current date and time to the "created_at" attribute
            self.updated_at = datetime.now()  # Assigning the current date and time to the "updated_at" attribute
            storage.new(self)

    def __str__(self):
        """This method returns a string representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """This method returns a dictionary representation of the object"""
        todict = self.__dict__.copy()  # Creating a copy of the instance's __dict__ attribute
        todict["__class__"] = type(self).__name__  # Adding a key-value pair for the class name
        todict["update_at"] = todict["updated_at"].isoformat()  # Adding a key-value pair for the "updated_at" attribute
        todict["created_at"] = todict["created_at"].isoformat()  # Adding a key-value pair for the "created_at" attribute
        return todict
    
""" If you observe very well, you will notice that in the base model, i created only the public instance 
attributes created at, updated at and the id. These three attributes are the ones that will be common to all other child classes
like User, Place etc
"""



 