#!/usr/bin/python3

"""Rectangle Class"""

from .base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class initialization
            Args:
                width: Rectangle width
                height: Rectangle height
                x: X coordinate of rectangle
                y: Y coordinate of rectangle
                id: id parameter
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets rectangle width
            Args:
                value: Value to set width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Returns rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets rectangle height
            Args: 
                value: Value to set height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Returns rectangle's x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets rectangle's x coordinate
            Args:
                value: Value to set x coordinate
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Returns rectangle's y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets rectangle's y coordinate
            Args:
                value: Value to set y coordinate
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Calculates and returns rectangle's area"""
        return self.__width * self.__height

    def display(self):
        """Displays rectangle with #"""
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns string representation of rectangle"""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """Updates the properties of rectangle
            Args:
                args: Updates using *args
                kwargs: Updates using **kwargs
        """
        args_len = len(args)

        if args != None and args_len > 0:
            if args_len > 0:
                if args_len >= 1:
                    self.id = args[0]
                if args_len >= 2:
                    self.width = args[1]
                if args_len >= 3:
                    self.height = args[2]
                if args_len >= 4:
                    self.x = args[3]
                if args_len >= 5:
                    self.y = args[4]

            return

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
