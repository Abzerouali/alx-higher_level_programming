#!/usr/bin/python3
"""Module for converting a JSON string to a Python object"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON str"""
    return json.loads(my_str)
