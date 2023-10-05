#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    counter = 1
    f = "arguments"
    s = "argument"
    length = len(argv)
    if (len(argv) == 1):
        print("0 arguments.")
    else:
        print("{} {}:".format(length - 1, f if length > 2 else s))
        for i in argv[1:]:
            print("{}: {}".format(counter, i))
            counter = counter + 1
