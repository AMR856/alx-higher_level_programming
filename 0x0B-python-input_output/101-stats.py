#!/usr/bin/python3
"""A script that reads from stdin"""
import sys


counter = 0
myDic = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
myFinalSize = 0
try:
    for line in sys.stdin:
        myList = line.split()
        myCode = int(myList[7])
        mySize = int(myList[8])
        myFinalSize = myFinalSize + mySize
        myDic[myCode] = myDic[myCode] + 1
        counter = counter + 1
        if counter == 10:
            print("File size: {:d}".format(myFinalSize))
            for i, j in myDic.items():
                if j != 0:
                    print("{:d}: {:d}".format(i, j))
            counter = 0
except KeyboardInterrupt:
    print("File size: {:d}".format(myFinalSize))
    for i, j in myDic.items():
        if j != 0:
            print("{:d}: {:d}".format(i, j))
