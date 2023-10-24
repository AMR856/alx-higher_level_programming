#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """The init function for my class which is the function
    that is called first

    """
    def __init__(self, size):
        """Making the size attibute private and assigning its value

        Args:
            It's the size of the created object

        """
        self.__size = size
