#!/usr/bin/python3

"""Module that greets by first and last names"""


def say_my_name(first_name, last_name=""):
    """Function that greets by first and last names
    Args:
        first_name: First name parameter
        last_name: Last name parameter

    Returns: 
        Nothing
    """

    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
