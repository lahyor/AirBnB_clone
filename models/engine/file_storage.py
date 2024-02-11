#!/usr/bin/python3
""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Corrected file path """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Corrected file variable name """
        with open(FileStorage.__file_path, "w") as json_file:
            serialized = {key: obj.to_dict() for key, obj in
                          FileStorage.__objects.items()}
            json.dump(serialized, json_file)

    def reload(self):
        """checking if the file exists"""
        if os.path.exists(FileStorage.__file_path):
            """ Corrected exists function and file path variable """
            with open(FileStorage.__file_path, "r") as json_file:
                """ Corrected file variable name """
                serialized = json.load(json_file)
                for key, obj_dict in serialized.items():
                    class_name, obj_id = key.split('.')

                    obj = create_object_from_dict(class_name, obj_dict)
                    FileStorage.__objects[key] = obj
