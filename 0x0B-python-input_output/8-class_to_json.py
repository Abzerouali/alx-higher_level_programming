#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object's attributes.

    :param obj: The object for which to generate the dictionary.

    :return: A dictionary containing the object's attributes.
    """

    return obj.__dict__
