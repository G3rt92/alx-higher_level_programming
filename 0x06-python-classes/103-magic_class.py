#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialization

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius * self.__radius * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
