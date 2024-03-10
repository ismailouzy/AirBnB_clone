#!/usr/bin/python3
"""the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class inherratce from BaseModel.

    Attributes:
        name : The name of the amenity.
    """

    name = ""
