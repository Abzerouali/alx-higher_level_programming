#!/usr/bin/python3
"""Module for converting a JSON string into a Python object"""
import json


def from_json_string(my_str):
    """ Converts a JSON-formatted string into a Python object (data structure)."""
    return json.loads(my_str)
