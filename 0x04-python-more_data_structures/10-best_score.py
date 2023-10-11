#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if not a_dictionary:
        return None
    myList = list(a_dictionary.values())
    myMax = max(myList)
    for key, value in a_dictionary.items():
        if value == myMax:
            return key
