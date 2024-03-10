#!/usr/bin/python3
from models.base_model import BaseModel
"""the User Class"""


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
