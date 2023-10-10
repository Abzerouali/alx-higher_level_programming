#!/usr/bin/python3
"""Defines a class-checking function that checks for inherited instances."""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or an inherited instance of a class.

    Args:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj to.

    Returns:
    bool: True if obj is an instance or inherited instance of a_class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
