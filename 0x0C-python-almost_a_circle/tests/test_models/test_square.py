#!/usr/bin/python3
"""
test for square class
"""
import unittest
from models.base import Base
from models.square import Square

"""
the square test cases
"""


class TestSquare(unittest.TestCase):
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Square(1, 0, 0, 1).__width

    def test_width(self):
        w1 = Square(1, 2)
        self.assertEqual(w1.width, 1)

    def test_width_getter(self):
        w2 = Square(1, 2, 3, 4)
        self.assertEqual(w2.width, 1)

    def test_width_setter(self):
        w3 = Square(1, 2, 3, 4)
        w3.width = 5
        self.assertEqual(w3.width, 5)

    def test_width_None(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(None, 2)

    def test_width_zero(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(0, 2)

    def test_width_negative(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(-1, 2)

    def test_width_float(self):
        self.assertRaises(TypeError, lambda: Square(1.5, 2))

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Square(2, 0, 0, 1).__height

    def test_height(self):
        h1 = Square(1, 2)
        self.assertEqual(h1.height, 1)

    def test_height_getter(self):
        h2 = Square(1, 2, 3, 4)
        self.assertEqual(h2.height, 1)

    def test_height_setter(self):
        h3 = Square(1, 2, 3, 4)
        h3.height = 10
        self.assertEqual(h3.height, 10)

    def test_height_None(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Square(1, None)

    def test_height_zero(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Square(0, 0)

    def test_height_negative(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Square(1, -2)

    def test_height_float(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Square(1, 2.5)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Square(1, 0, 0, 1).__x

    def test_normal_test(self):
        x1 = Square(2, 3, 4, 5)
        self.assertEqual(x1.x, 3)

    def test_x_getter(self):
        x2 = Square(2, 3, 4, 5)
        self.assertEqual(x2.x, 3)

    def test_x_setter(self):
        x3 = Square(2, 3, 4, 5)
        x3.x = 10
        self.assertEqual(x3.x, 10)

    def test_x_None(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, 2, None)

    def test_x_zero(self):
        self.assertEqual(Square(1, 2, 0, 4).x, 2)

    def test_x_negative(self):
        with self.assertRaises(ValueError, msg="x must be > 0"):
            Square(1, 2, -1)

    def test_x_float(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, 2, 3.5)

    def test_y_None(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, None)

    def test_y_zero(self):
        self.assertEqual(Square(2, 0, 0, 5).y, 0)

    def test_y_negative(self):
        with self.assertRaises(ValueError, msg="y must be > 0"):
            Square(1, 2, -1)

    def test_y_float(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, 3.5)

    def test_Square_is_base(self):
        self.assertIsInstance(Square(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Square(1.5)

    def test_two_args(self):
        r1 = Square(10, 2)
        r2 = Square(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Square(2, 2, 4)
        r2 = Square(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Square(1, 2, 3, 4)
        r2 = Square(1, 3, 2, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Square(10, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)

    def test_args(self):
        r = Square(1, 2, 3, 4)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_kwargs(self):
        r = Square(10, x=1, y=2)
        self.assertEqual(r.id, 39)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_args_and_kwargs(self):
        r = Square(2, x=1, y=2, id=1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_empty_args_and_kwargs(self):
        with self.assertRaises(TypeError):
            Square(*(), **{})


if __name__ == "__main__":
    unittest.main()
