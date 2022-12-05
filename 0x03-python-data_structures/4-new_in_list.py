#!/usr/bin/python3
def new_in_list(my_list, idx, element):
"""Replace an element at specific index without modifying the whole list"""
    copied_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return copied_list
    else:
        copied_list[idx] = element
        return copied_list
