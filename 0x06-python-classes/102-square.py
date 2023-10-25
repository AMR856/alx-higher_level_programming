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

    def __eq__(self, other):
        """Adding == operator to my class

        Args:
            The other instance of the class

        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """Adding != operator to my class

        Args:
            The other instance of the class

        """
        return (self.area() != other.area())

    def __gt__(self, other):
        """Adding > operator to my class

        Args:
            The other instance of the class

        """
        return (self.area() > other.area())

    def __lt__(self, other):
        """Adding < operator to my class

        Args:
            The other instance of the class

        """
        return (self.area() < other.area())

    def __ge__(self, other):
        """Adding >= operator to my class

        Args:
            The other instance of the class

        """
        return (self.area() >= other.area())

    def __le__(self, other):
        """Adding <= operator to my class

        Args:
            The other instance of the class

        """
        return (self.area() <= other.area())

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
