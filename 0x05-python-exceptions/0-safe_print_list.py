#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            except TypeError:
                break
        print()
        return count
    except IndexError:
        print()
        return i
