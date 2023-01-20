#!/usr/bin/python3
"""class Rectangle,inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets a width of a rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets a heigth of a rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x-value of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x-value of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """sets the y-value of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """gets the y-value of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle."""
        return self.width * self.height

    def display(self):
        """Display a rectangle."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        recstr = "[Rectangle] ({}) {}/{} - {}/{}"
        return recstr.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update method."""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i, _ in enumerate(args):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
