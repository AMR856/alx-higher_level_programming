#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    myNewList = []
    addedNum = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            addedNum = result
        except TypeError:
            print("wrong type")
            addedNum = 0
        except ZeroDivisionError:
            print("division by zero")
            addedNum = 0
        except IndexError:
            print("out of range")
            addedNum = 0
        finally:
            myNewList.append(addedNum)

