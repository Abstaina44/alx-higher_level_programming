#!/usr/bin/python3

"""Geometry Module."""


class BaseGeometry:
    """Represent a Geometry object."""

    def area(self):
        """Compute the raise of a Geometry object."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is a valid integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
