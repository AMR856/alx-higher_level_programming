#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = a_dictionary.copy()
    for key, value in newDic.items():
        newDic[key] = value * 2
    return newDic
