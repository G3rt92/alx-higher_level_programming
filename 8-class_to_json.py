#!/usr/bin/python3
"""Python class-to-JSON function definition."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
