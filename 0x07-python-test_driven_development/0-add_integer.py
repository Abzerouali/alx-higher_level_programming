#!/usr/bin/python3
"""Defines a function for integer addition."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
    a (int, float): The first number.
    b (int, float, optional): The second number. Defaults to 98.

    Returns:
    int: The integer result of adding a and b after typecasting to integers.

    Raises:
    TypeError: If either a or b is neither an integer nor a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
