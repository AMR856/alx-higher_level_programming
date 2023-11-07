#!/usr/bin/python3
"""A program to read a file"""


def read_file(filename=""):
    """Here is the function for reading
        
    Args: The file name
    """
    if (len(filename) == 0):
        return
    with open(filename, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            print(line)
