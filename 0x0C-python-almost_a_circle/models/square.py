#!/usr/bin/python3

"""Square Class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (
            f"[Square] ({self.id}) "
            f"{self._Rectangle__x}/{self._Rectangle__y} - "
            f"{self._Rectangle__width}"
        )

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
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
