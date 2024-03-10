#!/usr/bin/python3
"""the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class.

    Attributes:
        place_id : The Place id.
        user_id : The User id.
        text : The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
