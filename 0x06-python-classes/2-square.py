#!/usr/bin/python3
"""Blueprint for a Square"""


class Square():
    """Validated Square Class"""

    def __init__(self, size=0):
        """Instantiate the constructor

        Args:
            size (int): size of square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
