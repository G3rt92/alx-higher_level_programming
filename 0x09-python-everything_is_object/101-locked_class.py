#!/usr/bin/python3
"""
Module of a class that prevents a dynamic attribute creation
"""


class LockedClass():
    """prevents dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """create no object."""
        pass
