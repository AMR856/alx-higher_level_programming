#!/usr/bin/python3
"""A function to append text to my file"""


def append_after(filename="", search_string="", new_string=""):
    """Here is the function

    Args: The string we search for
    The string we put
    """
    with open(filename, 'r+', encoding='utf-8') as myFile:
        myLines = myFile.readlines()
        modified_lines = []
        for myLine in myLines:
            modified_lines.append(myLine)
            if search_string in myLine:
                modified_lines.append(new_string)
        myFile.seek(0)
        myFile.write("".join(modified_lines))
