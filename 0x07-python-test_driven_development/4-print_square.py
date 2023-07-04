#!/usr/bin/python3

"""Module to print a square using the # symbol"""


def print_square(size):
    """Function to print a square using the # symbol
    Args:
        size (int): Length of squares side

    Returns:
        Nothing
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
