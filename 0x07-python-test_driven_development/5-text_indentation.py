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
    for i in text:
        if i == ' ':
            counter = counter + 1
        else:
            break
    for counter in range(counter,len(text)):
        if (text[counter] in ":?."):
            print(text[counter], end="")
            print()
            print()
            flag = 1
            continue
        if text[counter] == '\n':
            print()
            flag = 1
            continue
        if text[counter] == ' ' and flag == 1:
            flag = 0
            continue
        print(text[counter], end="")
