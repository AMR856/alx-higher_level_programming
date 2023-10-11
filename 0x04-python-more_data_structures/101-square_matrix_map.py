#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda myP: list(map(lambda x: x ** 2, myP)), matrix)))
