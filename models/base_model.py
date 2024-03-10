#!/usr/bin/python3
"""
BaseModel

"""
from datetime import datetime
import uuid


class BaseModel:
    """
    a class BaseModel that defines
    all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instances of the BaseModel
        Args:
            @id:
            @created_at:
            @updated_at:
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == __class__:
                    continue
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at with
        the current time"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """a dictionary containing all keys/values
        of __dict__ of the instance"""
        dic_inst = self.__dict__.copy()
        dic_inst["__class__"] = self.__class__.__name__
        dic_inst["created_at"] = self.created_at.isoformat()
        dic_inst["updated_at"] = self.updated_at.isoformat()

        return dic_inst
