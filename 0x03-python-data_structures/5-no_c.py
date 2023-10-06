#!/usr/bin/python3
def no_c(my_string):
    newString = my_string
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            newString = newString[:i] + newString[i + 1:]
    return (newString)
