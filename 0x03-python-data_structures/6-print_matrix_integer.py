#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    s = len(matrix)
    y = len(matrix[0])
    if matrix is None:
        return
    for i in range(s):
        for j in range(y):
            print("{:d}".format(matrix[i][j]), end=" " if j != y - 1 else "")
        print()
