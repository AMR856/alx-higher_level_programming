#!/usr/bin/python3
def uppercase(str):
    h = 0
    k = len(str)
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            v = ord(i)
            print("{}".format(chr((v - 32))), end=""if h != k - 1 else '\n')
            h = h + 1
            continue
        elif i == "":
            continue
        print("{}".format(i), end="" if h != k - 1 else '\n')
        h = h + 1
