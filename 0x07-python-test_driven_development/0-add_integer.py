#!/usr/bin/python3
"""This is a function that adds two numbers together
and that's all it has some error's checking but this
is not important
"""

def add_integer(a, b=98):
    """A function to add two numbers
    Args:
        a: first number
        b: Second number
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))