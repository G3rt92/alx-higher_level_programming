#!/usr/bin/python3
"""Blueprint for a square"""


class Square():
    """Square with a single method"""

    def __init__(self, size=0):
        """instantiate the constructor

        Args:
            size (int): size of square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates an area of a square"""
        return self.__size * self.__size
