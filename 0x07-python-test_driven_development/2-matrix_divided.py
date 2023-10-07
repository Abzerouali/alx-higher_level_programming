#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
    matrix (list): A list of lists containing integers or floats.
    div (int or float): The divisor.

    Raises:
    TypeError: If the matrix is not a list of lists containing numbers.
    TypeError: If the rows of the matrix have different sizes.
    TypeError: If the divisor (div) is not a number (int or float).
    ZeroDivisionError: If the divisor (div) is 0.

    Returns:
    list: A new matrix representing the result of the division, rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
        for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of ""integer /floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
