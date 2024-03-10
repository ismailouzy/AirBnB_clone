#!/usr/bin/python3
"""the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class.

    Attributes:
        state_id : The state id.
        name : The name of the city.
    """
    state_id = ""
    name = ""
