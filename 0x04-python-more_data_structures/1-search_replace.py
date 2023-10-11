#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list.copy()
    for i in range(0, len(newList) - 1):
        if newList[i] == search:
            newList[i] = replace
    return (newList)
