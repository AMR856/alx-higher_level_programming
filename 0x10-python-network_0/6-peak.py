#!/usr/bin/python3
def find_peak(list_of_integers):
    tempPeak = -2147483648
    for myNum in list_of_integers:
        if myNum > tempPeak:
            tempPeak = myNum
    if tempPeak != -2147483648:
        return tempPeak
    else:
        return None
