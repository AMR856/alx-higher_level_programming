#!/usr/bin/python3
"""Making my square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Here is square that inherits from rectangle"""
    def __init__(self, size):
        """The init of my clas

        Args: The size of the square
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """A method to get the area"""
        return self.__size * self.__size
