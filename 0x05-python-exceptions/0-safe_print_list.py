#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except Exception as Anything:
            break
    print('')
    return i + 1
