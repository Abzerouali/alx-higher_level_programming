#!/usr/bin/python3
"""Defines a custom list class MyList that inherits from the built-in list class."""
class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
