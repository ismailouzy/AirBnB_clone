#!/usr/bin/python3
"""Unitest for file storage
"""

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for instantiation FileStorage"""
    def test_custom_file_storage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_custom_file_storage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_custom_file_storage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_custom_file_storage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods"""
    def setUp(self):
        pass

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_custom_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_custom_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_custom_new(self):
        basemodel_obj = BaseModel()
        user_obj = User()
        state_obj = State()
        place_obj = Place()
        city_obj = City()
        amenity_obj = Amenity()
        review_obj = Review()
        models.storage.new(basemodel_obj)
        models.storage.new(user_obj)
        models.storage.new(state_obj)
        models.storage.new(place_obj)
        models.storage.new(city_obj)
        models.storage.new(amenity_obj)
        models.storage.new(review_obj)
        self.assertIn("BaseModel." + basemodel_obj.id,
                      models.storage.all().keys())
        self.assertIn(basemodel_obj, models.storage.all().values())
        self.assertIn("User." + user_obj.id, models.storage.all().keys())
        self.assertIn(user_obj, models.storage.all().values())
        self.assertIn("State." + state_obj.id, models.storage.all().keys())
        self.assertIn(state_obj, models.storage.all().values())
        self.assertIn("Place." + place_obj.id, models.storage.all().keys())
        self.assertIn(place_obj, models.storage.all().values())
        self.assertIn("City." + city_obj.id, models.storage.all().keys())
        self.assertIn(city_obj, models.storage.all().values())
        self.assertIn("Amenity." + amenity_obj.id, models.storage.all().keys())
        self.assertIn(amenity_obj, models.storage.all().values())
        self.assertIn("Review." + review_obj.id, models.storage.all().keys())
        self.assertIn(review_obj, models.storage.all().values())

    def test_custom_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_custom_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_custom_save(self):
        basemodel_obj = BaseModel()
        user_obj = User()
        state_obj = State()
        place_obj = Place()
        city_obj = City()
        amenity_obj = Amenity()
        review_obj = Review()
        models.storage.new(basemodel_obj)
        models.storage.new(user_obj)
        models.storage.new(state_obj)
        models.storage.new(place_obj)
        models.storage.new(city_obj)
        models.storage.new(amenity_obj)
        models.storage.new(review_obj)
        models.storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("BaseModel." + basemodel_obj.id, file_content)
            self.assertIn("User." + user_obj.id, file_content)
            self.assertIn("State." + state_obj.id, file_content)
            self.assertIn("Place." + place_obj.id, file_content)
            self.assertIn("City." + city_obj.id, file_content)
            self.assertIn("Amenity." + amenity_obj.id, file_content)
            self.assertIn("Review." + review_obj.id, file_content)

    def test_custom_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_custom_reload(self):
        """ Tests custom_reload() method """
        basemodel_obj1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(basemodel_obj1)
        fs1.save()
        dict1 = fs1.reload()
        self.assertTrue(dict1 is fs1.reload())

    def test_custom_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
