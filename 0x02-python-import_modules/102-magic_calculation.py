#!/usr/bin/python3
from magic_calculator_102 import add, sub
def magic_calculation(a, b):
    """Match bytecode as the Python bytecode."""
    if a < b:
        sum_ = add(a, b)
        for i in range(4, 6):
            sum_ = add(sum_, i)
        return (sum_)

    else:
        return(sub(a, b))
