#!/usr/bin/python3
"""Here we make a new module called rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Here is rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """The init of my clas

        Args:
            width:The width of the rec
            height:The height of the rec
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self__width = width
        self__height = height

    def area(self):
        """A method to get the area"""
        return self.__width * self.__height

    def __str__(self):
        """The str method to print the rec in a fancy way"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
