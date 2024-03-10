#!/usr/bin/python3
"""unitests for review
"""
import os
import models
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    def test_instantiation(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attribute_types(self):
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_default_attribute_values(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_attributes(self):
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place!")

    def test_to_dict_method(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(type(review_dict), dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

    def test_str_method(self):
        review = Review()
        review_str = str(review)
        self.assertIsInstance(review_str, str)

    def test_str_method_attributes(self):
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place!"
        review_str = str(review)
        self.assertIn("123", review_str)
        self.assertIn("456", review_str)
        self.assertIn("Great place!", review_str)


if __name__ == '__main__':
    unittest.main()
