#!/usr/bin/python3
"""Blueprint of a square"""


class Square():
    """Square with setter"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate the constructor

        Args:
            size (int): size of square
            position (int): position of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """access the current size of a square"""
        return self.__size

    @property
    def position(self):
        """get the current position of a square"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets the current size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(elem, int) for elem in value) or
                not all(elem >= 0 for elem in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the current area of a square"""
        return self.__size ** self.__size

    def my_print(self):
        """Print the square with the # character."""
        for i in range(self.__size):
            print(" " * self.position[0], end="")
            print("#" * self.__size)
            print("")
        if not self.__size:
            print("")
            return

    def __str__(self):
        """Define the String representation of a Square."""
        if self.__size != 0:
            [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            if x != self.__size - 1:
                print("")
        return ("")
