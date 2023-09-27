#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    This function attempts to print the provided integer using the specified
    format specifier. If a ValueError or TypeError occurs during the printing,
    it catches the exception and prints an error message to standard error.

    Args:
    value (int): The int to print.

    Returns:
    True if the integer is printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
