#!/usr/bin/python3

"""A function to print some text"""
def text_indentation(text):
    """"This is the function btw

    Args: The text to be printed
    """
    flag = 0
    counter = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text.strip():
        if (flag and text[counter] != '\n'):
            flag = 0
            counter = counter + 1
            continue
        print(i, end='')
        if (i in ":?."):
            counter = counter + 1
            print()
            print()
            flag = 1
        if (i == '\n'):
            counter = counter + 1
            flag = 1
            print()