#!/usr/bin/python3
"""square-printing definition."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
