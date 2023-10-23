#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    myNewList = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            myNewList.append(result)
        except TypeError:
            print("wrong type")
            myNewList.append(0)
        except ZeroDivisionError:
            print("division by zero")
            myNewList.append(0)
        except IndexError:
            print("out of range")
            myNewList.append(0)
    return myNewList
