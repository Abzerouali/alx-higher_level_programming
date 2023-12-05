#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.

This class modifies the behavior of == and != operators.
"""

class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
