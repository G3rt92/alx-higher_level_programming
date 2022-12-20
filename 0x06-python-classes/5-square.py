#!/usr/bin/python3
"""Blueprint of a square"""


class Square():
    """Square with setter"""

    def __init__(self, size=0):
        """Instantiate the constructor

        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """access the current size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the current size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the current area of a square"""
        return self.__size ** self.__size

    def my_print(self):
        """Print the square with the # character."""
        for i in range(self.__size):
            print("#" * self.__size)
        if not self.__size:
            print("")
