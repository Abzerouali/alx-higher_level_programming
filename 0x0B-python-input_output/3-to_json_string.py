#!/usr/bin/python3
"""Module for converting an object to its JSON representation (string)"""
import json


def to_json_string(my_obj):
    """Converts an object to its JSON representation in string format."""
    return json.dumps(my_obj)
