#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except TypeError:
                break
        print()
        return i + 1
    except IndexError:
        print()
        return i
