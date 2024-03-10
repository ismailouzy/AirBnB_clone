import json
import os
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Testbase_mdel(unittest.TestCase):
    """Test cases for the `Base` class.
    """

    def test_initial(self):
        """Tests for innit
        """
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, artist="Ed Sheeran", album="Divide")
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b2.id, str)
        self.assertEqual(b2_uuid, b2.id)
        self.assertEqual(b2.album, "Divide")
        self.assertEqual(b2.artist, "Ed Sheeran")
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertEqual(str(type(b1)),
                         "<class 'models.base_model.BaseModel'>")

    def test_dictionnary(self):
        """Test for to_dict method"""
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, artist="Ed Sheeran", album="Divide")
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIn('id', b1_dict.keys())
        self.assertIn('created_at', b1_dict.keys())
        self.assertIn('updated_at', b1_dict.keys())
        self.assertEqual(b1_dict['__class__'], type(b1).__name__)
        self.assertNotIn('artist', b1_dict)

    def test_save_method(self):
        """Tests for save method"""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str_method(self):
        """Tests for str method"""
        b1 = BaseModel()
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_from_dictionnary(self):
        """Tests for from_dict method"""
        b_dict = {'id': str(uuid.uuid4()), 'title': 'Test Album',
                  'created_at': datetime.utcnow().isoformat()}
        b = BaseModel(**b_dict)
        self.assertEqual(b.id, b_dict['id'])
        self.assertEqual(b.title, b_dict['title'])
        self.assertEqual(b.created_at.isoformat(), b_dict['created_at'])


if __name__ == "__main__":
    unittest.main()
