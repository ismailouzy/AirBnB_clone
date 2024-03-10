#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """

    def test_default_attributes(self):
        """
        Test default attribute values.
        """
        state = State()

        self.assertEqual(state.name, "")

    def test_set_attributes(self):
        """
        Test setting attribute values.
        """
        state = State()

        state.name = "California"

        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        """
        Test conversion to dictionary.
        """
        state = State(name="California")

        state_dict = state.to_dict()

        expected_dict = {
            "__class__": "State",
            "name": "California",
            "id": state.id,
            "created_at": state.created_at.isoformat(),
            "updated_at": state.updated_at.isoformat()
        }

        self.assertEqual(state_dict, expected_dict)

    def test_str_representation(self):
        """
        Test string representation.
        """
        state = State(name="California")

        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)


if __name__ == "__main__":
    unittest.main()
