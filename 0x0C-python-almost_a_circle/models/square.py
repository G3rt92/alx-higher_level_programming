#!/usr/bin/python3
""" Module that contains class Square,
inheritance of class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the size of a square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets both the width and height of a square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a square."""
        recstr = "[Square] ({}) {}/{} - {}/{}"
        return recstr.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i, _ in enumerate(args):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
