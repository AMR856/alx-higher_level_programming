#!/usr/bin/python3
def add_attribute(myObj, TheAtt, TheValue):
    if hasattr(myObj, '__dict__') or \
            (hasattr(myObj, '__slots__') and attr_name in myObj.__slots__):
        setattr(myObj, TheAtt, TheValue)
    else:
        raise TypeError("can't add new attribute")
