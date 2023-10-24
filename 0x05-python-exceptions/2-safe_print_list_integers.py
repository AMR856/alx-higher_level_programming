#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    theSub = 0
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except Exception as Anything:
            theSub = theSub + 1
            pass
    print()
    return count - theSub
