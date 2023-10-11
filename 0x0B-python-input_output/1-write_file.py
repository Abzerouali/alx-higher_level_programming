#!/usr/bin/python3
"""Module for writing to a text file"""


def write_file(filename="", text=""):
    """    Writes a string to a text file using UTF-8 encoding."""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
