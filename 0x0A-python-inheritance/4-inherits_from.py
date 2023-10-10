#!/usr/bin/python3
"""Defines a function for checking inheritance from a class."""


def inherits_from(obj, a_class):
    """Check if an object inherits from a specific class.

    Args:
    obj (any): The object to check.
    a_class (type): The class to check for inheritance.

    Returns:
    bool: True if obj is an inherited instance of a_class, False otherwise.
    """
        
        if issubclass(type(obj), a_class) and type(obj) != a_class:
            return True
        return False
