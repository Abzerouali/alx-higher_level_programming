#!/usr/bin/python3
"""Module for reading and printing the contents of a text file"""


def read_file(file=""):
    """ Reads a text file (UTF-8 encoded) and prints its content to the standard output (stdout)."""
    with open(file, encoding="utf-8") as f:
        print(f.read(), end="")
