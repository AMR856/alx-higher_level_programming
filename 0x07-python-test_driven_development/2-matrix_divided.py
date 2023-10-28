#!/usr/bin/python3
""" This is a function that divides a list of integers or floats
and that's all actually
"""


def matrix_divided(matrix, div):
    """My function here

    Args:
        matrix: My function
        div: think about this one
    """
    mylen = 0
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    mylen = len(matrix[0])
    for i in range(len(matrix)):
        if (len(matrix[i]) != mylen):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if (type(element) is not int and type(element) is not float):
                raise TypeError(msg)
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
