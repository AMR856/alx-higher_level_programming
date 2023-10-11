#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    newList = list(map(lambda x : x ** 2, matrix[0], matrix[1], matrix[2]))
    return newList
