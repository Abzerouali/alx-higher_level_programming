#!/usr/bin/python3
"""Defines a MyInt class that inherits from int and inverts comparison operators."""

class MyInt(int):
    """Invert the behavior of int comparison operators == and !=.

    This class overrides the equality and inequality operators to invert their behavior.
    """
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
