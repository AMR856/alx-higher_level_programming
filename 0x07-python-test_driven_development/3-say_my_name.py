#!/usr/bin/python3
"""A function to print your first and last name"""
def say_my_name(first_name, last_name=""):
    """"Here is the function

    Args:
        first_name: Your first name
        last_name: Your last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is ", end= "")
    print(first_name + " " + last_name)
