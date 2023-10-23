def list_division(my_list_1, my_list_2, list_length):
    myNewList = []
    try:
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
        while i < list_length:
            myNewList.append(0)
            i = i + 1
    finally:
        return myNewList
