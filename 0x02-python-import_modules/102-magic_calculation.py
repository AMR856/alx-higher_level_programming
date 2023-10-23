#!/usr/bin/python3
# print_list_integer = __import__
def magic_calculation(a, b):
    add, sub = __import__(('add', 'sub')).magic_calculation_102
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return (sub(a, b))
