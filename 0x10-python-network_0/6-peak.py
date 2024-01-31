#!/usr/bin/python3
"""A file to find the peak"""


def find_peak(list_of_integers):
    """Here is the function btw

    list_of_integers: The list btw
    """
    tempPeak = -2147483648
    for myNum in list_of_integers:
        if myNum > tempPeak:
            tempPeak = myNum
    if tempPeak != -2147483648:
        return tempPeak
    else:
        return None
