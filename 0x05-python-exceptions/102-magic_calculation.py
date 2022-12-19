#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for elem in range(1, 3):
        try:
            if (elem > a):
                raise Exception("Too far")
            else:
                result += (a ** b) / elem
        except Exception:
            result = b + a
            break
    return result
