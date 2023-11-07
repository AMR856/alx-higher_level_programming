#!/usr/bin/python3
"""A script that reads from stdin"""
import sys


def printingMyInfo():
    print("File size: {:d}".format(myFinalSize))
    for i, j in sorted(myDic.items()):
        if j > 0:
            print("{:}: {:d}".format(i, j))


counter = 0
myDic = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

myFinalSize = 0
try:
    for myLine in sys.stdin:
        if counter != 0 and counter % 10 == 0:
            printingMyInfo()
        tryingToget = myLine.split()
        try:
            myStatus = tryingToget[-2]
            if myStatus in myDic.keys():
                myDic[myStatus] = myDic[myStatus] + 1
        except Exception as Everything:
            pass
        try:
            myFinalSize = int(tryingToget[-1]) + myFinalSize
        except Exception as Everything:
            pass
        counter = counter + 1
    printingMyInfo()
except KeyboardInterrupt:
    printingMyInfo()
    raise
