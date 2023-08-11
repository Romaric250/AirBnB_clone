#!/usr/bin/python3
"""the code for theis file is still t be determined."""

from models.engine.file_storage import FileStorage

storage = FileStorage() #creates a unique file storage instance

storage.reload() #loads obj from json file if it exist

