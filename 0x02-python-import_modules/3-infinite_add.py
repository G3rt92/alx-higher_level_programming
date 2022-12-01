#!/usr/bin/python3
import sys
if __name__ == "__main__":
    summed = 0
    for i in range(len(sys.argv) - 1):
        summed = summed + int(sys.argv[i + 1])
    print("{}".format(summed))
