#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for i in argv[1:]:
        sum = sum + int(i)
    print(sum)
