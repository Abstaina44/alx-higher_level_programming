#!/usr/bin/python3

"""Square Class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class initialization
            Args:
                size: Square size
                x: X coordinate of square
                y: Y coordinate of square
                id: id parameter
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of square"""
        return (
            f"[Square] ({self.id}) "
            f"{self._Rectangle__x}/{self._Rectangle__y} - "
            f"{self._Rectangle__width}"
        )

    @property
    def size(self):
        """Returns size of square"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Sets the dimension of square
            Args:
                value: Square's dimension
        """
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """Updates the properties of square
            Args:
                args: Updates using *args
                kwargs: Updates using **kwargs
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        return {
            "id": self.id,
            "size": self._Rectangle__width,
            "x": self._Rectangle__x,
            "y": self._Rectangle__y
        }
