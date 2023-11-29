#!/usr/bin/python3
"""Defines a function to divide a matrix by a scalar value."""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a scalar value.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The scalar value to divide the matrix by.

    Returns:
        list of lists: A new matrix with each element divided by the scalar value.

    Raises:
        TypeError: If the matrix is not a list of lists or the scalar value is not an integer or float.
        ZeroDivisionError: If the scalar value is zero.
    """
    import decimal
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
