#!/usr/bin/python3
"""
This module provides a function to print a square of specified size using the '#' character.

The `print_square` function takes an integer `size` as input and prints a square of size `size * size` using the '#' character.

Args:
    size (int): The size of the square to be printed.

Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than zero.
"""


def print_square(size):
    """prints a square with "#"'s that has a length of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
