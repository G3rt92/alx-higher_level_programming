#!/usr/bin/python3

"""string-to-JSON function definition."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
