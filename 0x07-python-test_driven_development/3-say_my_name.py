#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a person's name.

    Args:
    first_name (str): The first name of the person.
    last_name (str, optional): The last name of the person (default is an empty string).

    Raises:
    TypeError: If either first_name or last_name is not a string.
        """
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))
