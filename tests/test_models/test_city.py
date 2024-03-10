#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def test_default_attributes(self):
        """
        Test default attribute values.
        """
        city = City()

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_set_attributes(self):
        """
        Test setting attribute values.
        """
        city = City()

        city.state_id = "CA"
        city.name = "San Francisco"

        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_to_dict(self):
        """
        Test conversion to dictionary.
        """
        city = City(state_id="CA", name="San Francisco")

        city_dict = city.to_dict()

        expected_dict = {
            "__class__": "City",
            "state_id": "CA",
            "name": "San Francisco",
            "id": city.id,
            "created_at": city.created_at.isoformat(),
            "updated_at": city.updated_at.isoformat()
        }

        self.assertEqual(city_dict, expected_dict)

    def test_str_representation(self):
        """
        Test string representation.
        """
        city = City(state_id="CA", name="San Francisco")

        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == "__main__":
    unittest.main()
