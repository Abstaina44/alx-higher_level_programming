#!/usr/bin/python3
"""
unittest module for the base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        """
        set up the test case by resetting the __nb_objects counter to 0
        return:
            nothing
        """
        Base.__nb_objects = 0

    def test_default_id_assignment(self):
        """
        test the default id assignment when no custom_id is provided
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id_assignment(self):
        """
        test the id assignment when a custom_id is provided
        """
        b4 = Base(12)
        b5 = Base(40)
        b6 = Base(99)

        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 40)
        self.assertEqual(b6.id, 99)

    def test_mixed_id_assignment(self):
        """
        Test the id assignment when a mixture of custom and default ids are used.
        """
        b7 = Base()
        b8 = Base(50)
        b9 = Base()

        self.assertEqual(b7.id, 5)
        self.assertEqual(b8.id, 50)
        self.assertEqual(b9.id, 6)

    def test_id_increment_after_custom_id(self):
        """
        Test that the id counter increments correctly even after a custom id is assigned.
        """
        b10 = Base(100)
        b11 = Base()

        self.assertEqual(b10.id, 100)
        self.assertEqual(b11.id, 4)


if __name__ == "__main__":
    unittest.main()
