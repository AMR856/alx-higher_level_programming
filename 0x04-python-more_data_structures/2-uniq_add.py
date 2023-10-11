#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    mySet = set(my_list)
    for i in mySet:
        sum = sum + i
    return sum
