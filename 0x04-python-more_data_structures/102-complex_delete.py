#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, myValue in (a_dictionary.copy()).items():
        if value == myValue:
            a_dictionary.pop(key)
    return (a_dictionary)
