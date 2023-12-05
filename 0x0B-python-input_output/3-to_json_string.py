#!/usr/bin/python3
""" Module for converting an object to its JSON representation"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
