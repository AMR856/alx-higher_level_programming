#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """The init function for my class which is the function
    that is called first

    """
    def __init__(self, size=0):
        """Making the size attibute private and assigning its value

        Args:
            It's the size of the created object

        """
        self.size = size
    """defining the property and setter for my instance"""
    @proprety
    def size(self):
        """It's just a getter for the field size"""
        return self.__size
    """Now a setter"""
    @size.setter
    def size(self, size):
        """The setter for my size field

        Args:
            the size of the created instance

        """
        """A condition for checking if it's an integer"""

        if type(size) is int:
            """Raising an exception if it's not"""
    
            raise TypeError("size must be an integer")

        """Checking the value of the size if it's bigger than 0"""
    
        if (size < 0):
            """Raising an exception if it's not"""
    
            raise ValueError("ValueError")
        """Putting the value in the end"""
    
        self.__size = size
