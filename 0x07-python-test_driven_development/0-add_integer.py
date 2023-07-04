#!/usr/bin/python3

"""Module that adds two integer or floating numbers"""


def add_integer(a, b=98):
    """Function that adds two integer or floating numbers
    Args:
        a (int/float): First parameter
        b (int/float): Second parameter
    Returns:
        Numeric: sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (a + b)
