#!/usr/bin/python3
def islower(c):
    """A function to check if a char is lower or upper case"""
    if ord(c) >= 97 and ord(c) <= 123:
        return True
    else:
        return False
