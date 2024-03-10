#!/usr/bin/python3
"""Unit tests for Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def test_default_attributes(self):
        """
        Test default attribute values.
        """
        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_set_attributes(self):
        """
        Test setting attribute values.
        """
        place = Place()

        place.city_id = "1"
        place.user_id = "2"
        place.name = "Cozy Apartment"
        place.description = "A cozy apartment in the heart of the city"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["1", "2", "3"]

        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A cozy apartment in the heart of the city")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    def test_to_dict(self):
        """
        Test conversion to dictionary.
        """
        place = Place(city_id="1", user_id="2", name="Cozy Apartment",
                      description="A cozy apartment in the heart of the city",
                      number_rooms=2, number_bathrooms=1, max_guest=4,
                      price_by_night=100, latitude=37.7749, longitude=-122.4194,
                      amenity_ids=["1", "2", "3"])

        place_dict = place.to_dict()

        expected_dict = {
            "__class__": "Place",
            "city_id": "1",
            "user_id": "2",
            "name": "Cozy Apartment",
            "description": "A cozy apartment in the heart of the city",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "amenity_ids": ["1", "2", "3"],
            "id": place.id,
            "created_at": place.created_at.isoformat(),
            "updated_at": place.updated_at.isoformat()
        }

        self.assertEqual(place_dict, expected_dict)

    def test_str_representation(self):
        """
        Test string representation.
        """
        place = Place(city_id="1", user_id="2", name="Cozy Apartment",
                      description="A cozy apartment in the heart of the city",
                      number_rooms=2, number_bathrooms=1, max_guest=4,
                      price_by_night=100, latitude=37.7749, longitude=-122.4194,
                      amenity_ids=["1", "2", "3"])

        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)


if __name__ == "__main__":
    unittest.main()
