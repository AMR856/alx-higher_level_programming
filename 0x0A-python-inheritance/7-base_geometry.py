#!/usr/bin/python3
"""Making my base geometry class"""


class BaseGeometry:
    """Here is the class"""
    def area(self):
        """A method to get the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method to the value
        Args: The name of the ...
        The value of the ...
        """

        if (type(value) is not int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
