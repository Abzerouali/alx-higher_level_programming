#!/usr/bin/python3
"""Contains the "class_to_json" function"""


def class_to_json(obj):
    """
    Returns a dictionary description of a class instance with a simple data structure
    (list, dictionary, string, integer, and boolean) suitable for JSON serialization.
    """

    return obj.__dict__
