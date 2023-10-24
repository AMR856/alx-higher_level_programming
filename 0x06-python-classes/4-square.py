#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """My square class"""
    def __init__(self, size=0):
        """Making the size attibute private and assigning its value

        Args:
            It's the size of the created object

        """
        self.size = size

    @property
    def size(self):
        """A getter for the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter for the size

        Args:
            value of the size of the to be set

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Getting the area of the square

        """
        return self.__size * self.__size
