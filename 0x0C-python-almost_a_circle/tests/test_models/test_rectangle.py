#!/usr/bin/python3
"""
unittest module for the base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    test the width property of the rectangle
    """

    # test width_private
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 0, 0, 1).__width)

    # normal test
    def test_width(self):
        w1 = Rectangle(1, 2)
        self.assertEqual(w1.width, 1)

    # test_width_getter
    def test_width_getter(self):
        w2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(w2.width, 1)

    # test_width_setter
    def test_width_setter(self):
        w3 = Rectangle(1, 2, 3, 4)
        w3.width = 5
        self.assertEqual(w3.width, 5)

    # test_width_None
    def test_width_None(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(None, 2)

    # test_width_zero
    def test_width_zero(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)

    # test_width_negative
    def test_width_negative(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-1, 2)

    # test_width_float
    def test_width_float(self):
        self.assertRaises(TypeError, lambda: Rectangle(1.5, 2))

    # test_height_private
    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 0, 0, 1).__height)

    # test_normal
    def test_height(self):
        h1 = Rectangle(1, 2)
        self.assertEqual(h1.height, 2)

    # test_height_getter
    def test_height_getter(self):
        h2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(h2.height, 2)

    # test_height_setter
    def test_height_setter(self):
        h3 = Rectangle(1, 2, 3, 4)
        h3.height = 10
        self.assertEqual(h3.height, 10)

    # test_height_None
    def test_height_None(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, None)

    # test_height_zero
    def test_height_zero(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, 0)

    # test_height_negative
    def test_height_negative(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -2)

    # test_height_float
    def test_height_float(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, 2.5)

    # test_x_private
    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 0, 0, 1).__x)

    # test_normal_test
    def test_normal_test(self):
        x1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(x1.x, 3)

    # test_x_getter
    def test_x_getter(self):
        x2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(x2.x, 3)

    # test_x_setter
    def test_x_setter(self):
        x3 = Rectangle(1, 2, 3, 4, 5)
        x3.x = 10
        self.assertEqual(x3.x, 10)

    # test_x_None
    def test_x_None(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, None)

    # test_x_zero
    def test_x_zero(self):
        self.assertEqual(Rectangle(1, 2, 0, 4, 5).x, 0)

    # test_x_negative
    def test_x_negative(self):
        with self.assertRaises(ValueError, msg="x must be > 0"):
            Rectangle(1, 2, -1)

    # test_x_float
    def test_x_float(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, 3.5)

    # test_y_None
    def test_y_None(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, None)

    # test_y_zero
    def test_y_zero(self):
        self.assertEqual(Rectangle(1, 2, 0, 0, 5).y, 0)

    # test_y_negative
    def test_y_negative(self):
        with self.assertRaises(ValueError, msg="y must be > 0"):
            Rectangle(1, 2, -1)

    # test_y_float
    def test_y_float(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3.5)

    def test_rectangle_is_base(self):
        """
        Test that Rectangle instances are instances of Base class.
        """
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """
        Test creating a Rectangle instance with no arguments raises TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """
        Test creating a Rectangle instance with only one argument raises TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """
        Test creating a Rectangle instance with two arguments.
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """
        Test creating a Rectangle instance with three arguments.
        """
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """
        Test creating a Rectangle instance with four arguments.
        """
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """
        Test creating a Rectangle instance with five arguments.
        """
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """
        Test creating a Rectangle instance with more than five arguments raises TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_args(self):
        """
        Test creating a Rectangle instance with arbitrary number of width arguments.
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_kwargs(self):
        """
        Test creating a Rectangle instance with arbitrary keyword arguments.
        """
        r = Rectangle(width=10, height=5, x=1, y=2)
        self.assertEqual(r.id, 13)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_args_and_kwargs(self):
        """
        Test creating a Rectangle instance with a combination of arguments and keyword arguments.
        """
        r = Rectangle(2, 3, x=1, y=2)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_empty_args_and_kwargs(self):
        """
        Test creating a Rectangle instance with no arguments and no keyword arguments.
        """
        with self.assertRaises(TypeError):
            Rectangle(*(), **{})


if __name__ == "__main__":
    unittest.main()
