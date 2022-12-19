#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elem in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            i++
    print()
    return i
