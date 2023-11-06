#!/usr/bin/python3
"""A function to make you think about your life"""


def add_attribute(myObj, TheAtt, TheValue):
    """A weird function but handy sometimes

    Args:
        The attribute you want to set
        The value of the attribute
    """
    if hasattr(myObj, '__dict__') or \
            (hasattr(myObj, '__slots__') and attr_name in myObj.__slots__):
        setattr(myObj, TheAtt, TheValue)
    else:
        raise TypeError("can't add new attribute")
