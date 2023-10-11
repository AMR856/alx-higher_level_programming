#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    tryThisDic = dict(sorted(a_dictionary.items()))
    for key, value in tryThisDic.items():
        print("{}: {}".format(key, value))
