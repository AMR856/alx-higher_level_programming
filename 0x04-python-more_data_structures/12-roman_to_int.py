#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    myDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        for key, value in myDic.items():
            if key == i:
                sum = sum + value
    return sum
