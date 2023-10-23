def safe_print_list(my_list=[], x=0):
    printedChar = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printedChar = printedChar + 1
        except Exception as myError:
            break
    print()
    return printedChar