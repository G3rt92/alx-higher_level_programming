#!/usr/bin/python3
"""Defines a class MyList that inherits from a list."""


class MyList(list):
    """Implements sorted printing for the built-in class list."""

    def print_sorted(self):
        """Print a list in a sorted ascending order."""
        print(sorted(self))
