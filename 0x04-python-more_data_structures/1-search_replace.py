#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    if not my_list:
        return my_list
    return [target if target != search else replace for target in my_list]
