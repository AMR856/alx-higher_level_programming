#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """My square class"""
    def __init__(self, size=0):
        """Making the size attibute private and assigning its value

        Args:
            It's the size of the created object

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
