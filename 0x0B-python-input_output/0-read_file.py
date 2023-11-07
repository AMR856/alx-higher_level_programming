#!/usr/bin/python3
"""A program to read a file"""


def read_file(filename=""):
    """Here is the function for reading

    Args: The file name
    """
    if (len(filename) == 0 or filename is None):
        return
    with open(filename, 'r', encoding='utf-8') as myFile:
        print(myFile.read(), end="")
