#!/usr/bin/python3
"""file storage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serialization and deserialization of objects"""
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def save(cls):
        """Serializes objs to JSON"""
        with open(cls.__file_path, "w") as f:
            serial_objs = {key: obj.to_dict() for key, obj in
                           cls.__objects.items()}
            json.dump(serial_objs, f)

    @classmethod
    def reload(cls):
        """Deserializes JSON to obj"""
        try:
            with open(cls.__file_path, "r") as f:
                serial_objs = json.load(f)
                for key, value in serial_objs.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        cls.__objects[key] = BaseModel(**value)
                    elif class_name == 'State':
                        cls.__objects[key] = State(**value)
                    elif class_name == 'City':
                        cls.__objects[key] = City(**value)
                    elif class_name == 'Amenity':
                        cls.__objects[key] = Amenity(**value)
                    elif class_name == 'Place':
                        cls.__objects[key] = Place(**value)
                    elif class_name == 'Review':
                        cls.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[k] = obj
