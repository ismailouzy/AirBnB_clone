import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def test_default_attributes(self):
        """
        Test default attribute values.
        """
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_set_attributes(self):
        """
        Test setting attribute values.
        """
        user = User()

        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict(self):
        """
        Test conversion to dictionary.
        """
        user = User(email="test@example.com", password="password123",
                    first_name="John", last_name="Doe")

        user_dict = user.to_dict()

        expected_dict = {
            "__class__": "User",
            "email": "test@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "id": user.id,
            "created_at": user.created_at.isoformat(),
            "updated_at": user.updated_at.isoformat()
        }

        self.assertEqual(user_dict, expected_dict)

    def test_str_representation(self):
        """
        Test string representation.
        """
        user = User(email="test@example.com", password="password123",
                    first_name="John", last_name="Doe")

        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)


if __name__ == "__main__":
    unittest.main()
