#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    myFile = dir(hidden_4)
    for i in myFile:
        if (i[:2] != "__"):
            print(i)
