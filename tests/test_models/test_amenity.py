#!/usr/bin/python3
"""
Test cases for Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_instantiation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attribute_types(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_default_attribute_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_set_attributes(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_to_dict_method(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

    def test_str_method(self):
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertIsInstance(amenity_str, str)

    def test_str_method_attributes(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity_str = str(amenity)
        self.assertIn("Swimming Pool", amenity_str)


if __name__ == '__main__':
    unittest.main()
