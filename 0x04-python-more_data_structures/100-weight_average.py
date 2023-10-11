#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    theDiv = 0
    if my_list is None:
        return
    if not my_list:
        return 0
    for item in my_list:
        sum = sum + item[0] * item[1]
        theDiv = theDiv + item[1]
    return sum / theDiv
