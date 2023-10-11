#!/usr/bin/python3
"""Module for saving a Python object to a JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """ Saves a Python object to a JSON file. """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
