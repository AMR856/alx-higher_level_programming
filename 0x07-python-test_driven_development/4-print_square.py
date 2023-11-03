#!/usr/bin/python3
"""A function to print a square of hashtags"""


def print_square(size):
    """Here is my function

    Args: size is the number of row and columns
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")

    if size < 0 and type(size) is int:
        raise TypeError("size must be >= 0")

    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size == 0:
        print("")

    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print()
