#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_first(self):
        result = max_integer([3, 4, 5, 6, 2])
        self.assertEqual(result, 6)

    def test_second(self):
        result = max_integer([4, 4, 2])
        self.assertEqual(result, 4)

    def test_third(self):
        result = max_integer([-200, -44, -77])
        self.assertEqual(result, -44)

    def test_invalid_element(self):
        with self.assertRaises(TypeError):
            max_integer(['a', '2', None, 3.23])

    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
